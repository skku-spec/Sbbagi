# Gmail watchdogs for token-efficient alerts

Use this pattern when the user wants Gmail replies monitored and posted to the current channel, but does **not** want an LLM to wake up on every poll.

## Pattern

1. Write a standalone Python script under the active profile's scripts directory (for profile `sbbagi`, `/data/profiles/sbbagi/scripts/<name>.py`).
2. The script uses Gmail API directly via `google_token.json` and keeps a small state file such as `state/gmail_watchdog_state.json`.
3. First run initializes state by marking current matching messages as seen and prints nothing.
4. Subsequent runs:
   - query the scope the user actually requested:
     - specific people/threads only when the user explicitly wants a narrow monitor, e.g. `from:person@example.com newer_than:30d`
     - all incoming mail when the user asks for a general inbox watcher, e.g. `in:anywhere newer_than:30d -in:sent -in:drafts -in:trash -in:spam`
   - if no new messages: print **nothing**
   - if a new message exists: print a short fixed-format alert to stdout
5. Register it as a script-only cron job with `no_agent=True`, e.g. schedule `every 5m`. This delivers non-empty stdout verbatim and uses no LLM tokens on empty polls.

## Privacy rules for alerts

- Do not upload or echo attachment contents to Discord/chat automatically.
- List attachment filenames only.
- Mask obvious sensitive numeric values in previews: resident registration numbers, bank/account-like long numbers, phone-like patterns.
- Include the Gmail message ID so the agent can fetch the full message later on explicit user request.

## Example alert shape

```text
[Gmail 회신 감지]

보낸 사람: 홍준 대표님 (홍준 <powerguy@naver.com>)
제목: Re: RISE 사업단 전문가활용비 지급 증빙서류 요청드립니다
시간: 2026-06-23 19:20 KST
본문 미리보기: 자료 첨부드립니다. 정산 가능합니다...
첨부파일: 강의자료.pdf, 통장사본.pdf
메일 ID: 19ef...

※ 개인정보 가능성이 있어 본문 숫자는 일부 자동 마스킹했고, 첨부 원문은 Discord에 올리지 않았습니다.
```

## Pitfalls

- Do not use an LLM-driven cron for simple polling; it wastes tokens. Use `no_agent=True` unless semantic summarization is required.
- Do not print heartbeat text on empty polls. Empty stdout means silent success for `no_agent=True` jobs.
- Do not silently hard-code a sender allowlist for a general inbox monitor. If the user says “reply from X/Y” or a task is clearly about two people, a narrow query is fine; if they ask to catch mail generally, monitor all incoming senders and exclude only outbound/drafts/trash/spam.
- If you change the query from narrow to broad after state initialization, the state may not contain older messages outside the original narrow scope, causing a flood of historical alerts. After broadening scope, re-bootstrap the state to mark current matching messages seen, or carefully preserve only deliberate test IDs for verification.
- Be careful with schedule strings: `5m` can create a one-shot job in some scheduler interfaces; use `every 5m` for recurring polling.
- If a job was accidentally created one-shot, remove and recreate it as recurring rather than assuming an update cleared the repeat count.
