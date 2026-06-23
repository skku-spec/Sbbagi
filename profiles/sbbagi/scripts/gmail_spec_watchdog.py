#!/usr/bin/env python3
"""Script-only Gmail watchdog for SPEC / 스빡이.

Checks Gmail for new incoming messages and prints a Discord-safe alert only when
new mail is detected. It prints nothing when there is no new mail, making it
suitable for Hermes cron jobs with no_agent=true.

Required per machine/profile:
- A Google OAuth token at $HERMES_PROFILE_HOME/google_token.json with Gmail scope.
- Python packages: google-auth, google-api-python-client.

Privacy:
- Does not download or print attachment contents.
- Masks obvious resident-registration numbers, account-like numbers, and long
  numeric identifiers in the preview before sending to Discord.
"""
from __future__ import annotations

import base64
import json
import os
import re
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

PROFILE = Path(os.environ.get("HERMES_PROFILE_HOME") or os.environ.get("HERMES_HOME") or Path.home() / ".hermes")
TOKEN = PROFILE / "google_token.json"
STATE_DIR = PROFILE / "state"
STATE = STATE_DIR / "gmail_spec_watchdog_state.json"

# Monitor every incoming sender. Existing messages are tracked in STATE so only
# newly-arrived mail after initialization produces an alert.
# Exclude sent/drafts/trash/spam to avoid alerting on our own outbound mail.
QUERY = os.environ.get(
    "SPAKKI_GMAIL_QUERY",
    "in:anywhere newer_than:30d -in:sent -in:drafts -in:trash -in:spam",
)
MAX_RESULTS = int(os.environ.get("SPAKKI_GMAIL_MAX_RESULTS", "20"))
PREVIEW_LIMIT = int(os.environ.get("SPAKKI_GMAIL_PREVIEW_LIMIT", "500"))


def load_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"initialized": False, "seen_ids": []}


def save_state(state: dict) -> None:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    tmp = STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(STATE)


def get_header(payload: dict, name: str) -> str:
    lname = name.lower()
    for h in payload.get("headers", []):
        if h.get("name", "").lower() == lname:
            return h.get("value", "")
    return ""


def walk_parts(part: dict):
    yield part
    for child in part.get("parts", []) or []:
        yield from walk_parts(child)


def decode_body(data: str) -> str:
    try:
        return base64.urlsafe_b64decode(data.encode()).decode("utf-8", "replace")
    except Exception:
        return ""


def extract_text(payload: dict, snippet: str) -> str:
    texts = []
    htmls = []
    for part in walk_parts(payload):
        mime = part.get("mimeType", "")
        data = part.get("body", {}).get("data")
        if not data:
            continue
        if mime == "text/plain":
            texts.append(decode_body(data))
        elif mime == "text/html":
            htmls.append(decode_body(data))
    text = "\n".join(t.strip() for t in texts if t.strip()).strip()
    if not text and htmls:
        html = "\n".join(htmls)
        html = re.sub(r"<br\s*/?>", "\n", html, flags=re.I)
        html = re.sub(r"</p\s*>", "\n", html, flags=re.I)
        html = re.sub(r"<[^>]+>", " ", html)
        html = (
            html.replace("&nbsp;", " ")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&amp;", "&")
        )
        text = re.sub(r"[ \t]+", " ", html)
        text = re.sub(r"\n\s*\n+", "\n\n", text).strip()
    return text or snippet or ""


def sender_addr(from_header: str) -> str:
    m = re.search(r"<([^>]+)>", from_header)
    addr = m.group(1) if m else from_header
    return addr.strip().lower()


def safe_preview(text: str, limit: int = PREVIEW_LIMIT) -> str:
    text = re.sub(r"\b\d{6}-?\d{7}\b", "[주민등록번호 마스킹]", text)
    text = re.sub(r"\b\d{2,6}-\d{2,6}-\d{2,8}\b", "[번호 마스킹]", text)
    text = re.sub(r"\b\d{10,16}\b", "[긴 숫자 마스킹]", text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        return text[:limit].rstrip() + "..."
    return text


def main() -> None:
    if not TOKEN.exists():
        raise SystemExit(f"Missing Gmail OAuth token: {TOKEN}")

    state = load_state()
    seen = set(state.get("seen_ids", []))

    creds = Credentials.from_authorized_user_file(str(TOKEN))
    svc = build("gmail", "v1", credentials=creds, cache_discovery=False)

    ids = []
    req = svc.users().messages().list(userId="me", q=QUERY, maxResults=MAX_RESULTS)
    while req:
        resp = req.execute()
        ids.extend(m["id"] for m in resp.get("messages", []))
        req = svc.users().messages().list_next(req, resp)

    # First run: mark current matching messages as already seen and stay silent.
    if not state.get("initialized"):
        state["initialized"] = True
        state["seen_ids"] = sorted(set(ids))[-500:]
        state["initialized_at"] = datetime.now(timezone.utc).isoformat()
        save_state(state)
        return

    new_ids = [mid for mid in ids if mid not in seen]
    if not new_ids:
        return

    messages = []
    for mid in new_ids:
        msg = svc.users().messages().get(userId="me", id=mid, format="full").execute()
        payload = msg.get("payload", {})
        from_h = get_header(payload, "From")
        addr = sender_addr(from_h)
        subject = get_header(payload, "Subject") or "(제목 없음)"
        date_h = get_header(payload, "Date")
        try:
            dt = parsedate_to_datetime(date_h)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            date_s = dt.astimezone(timezone(timedelta(hours=9))).strftime("%Y-%m-%d %H:%M KST")
        except Exception:
            date_s = date_h or "시간 확인 불가"
        attachments = []
        for part in walk_parts(payload):
            fn = part.get("filename")
            if fn and part.get("body", {}).get("attachmentId"):
                attachments.append(fn)
        body = extract_text(payload, msg.get("snippet", ""))
        messages.append({
            "who": addr or "알 수 없음",
            "from": from_h,
            "subject": subject,
            "date": date_s,
            "preview": safe_preview(body),
            "attachments": attachments,
            "id": mid,
        })
        seen.add(mid)

    state["seen_ids"] = sorted(seen)[-500:]
    state["last_checked_at"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    if not messages:
        return

    chunks = ["[Gmail 회신 감지]"]
    for m in messages:
        chunks.append(
            f"\n보낸 사람: {m['who']} ({m['from']})\n"
            f"제목: {m['subject']}\n"
            f"시간: {m['date']}\n"
            f"본문 미리보기: {m['preview'] or '(본문 없음)'}\n"
            f"첨부파일: {', '.join(m['attachments']) if m['attachments'] else '없음'}\n"
            f"메일 ID: {m['id']}"
        )
    chunks.append("\n※ 개인정보 가능성이 있어 본문 숫자는 일부 자동 마스킹했고, 첨부 원문은 Discord에 올리지 않았습니다.")
    print("\n".join(chunks))


if __name__ == "__main__":
    main()
