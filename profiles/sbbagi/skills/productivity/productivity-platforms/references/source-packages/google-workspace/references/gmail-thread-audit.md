# Gmail thread audit: bulk-read conversations and attachments

Use this when the user asks to review an entire Gmail conversation history, identify obligations, and read/download every document in the thread.

## Why not only `google_api.py gmail get`

The high-level `google_api.py gmail search/get` commands are good for quick search/read, but they do **not** expose attachments and can return an empty `body` for some MIME layouts. For full audits, use the Gmail API directly with the same Hermes OAuth token.

## Workflow

1. Search broadly first with `google_api.py gmail search` to identify likely sender/recipient/thread IDs.
2. Use the raw Gmail API to expand matching messages to **full threads** (`users().threads().get(..., format='full')`).
3. Traverse MIME parts recursively:
   - collect `text/plain`, fallback to stripped `text/html`
   - collect links from body/snippet
   - download each part with `body.attachmentId` via `users().messages().attachments().get(...)`
4. Save:
   - `records.json` with message metadata/body/links/attachment paths
   - `messages.md` chronological human-readable transcript
   - `attachments/` containing every downloaded file
5. Extract text from downloaded documents when possible:
   - `.docx`: `python-docx`
   - `.pdf`: `pypdf`
   - `.hwpx`: unzip and parse XML text
   - `.hwp`: best-effort OLE stream extraction; expect noisy text for some forms
6. Summarize only after reading both the email bodies and extracted attachment text.

## Minimal raw Gmail API skeleton

```python
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64, re, pathlib, json

HOME = '/data/profiles/sbbagi'  # or active Hermes profile home
creds = Credentials.from_authorized_user_file(f'{HOME}/google_token.json')
svc = build('gmail', 'v1', credentials=creds)

def decode(data):
    return base64.urlsafe_b64decode(data.encode()).decode('utf-8', 'replace') if data else ''

def walk(payload):
    yield payload
    for p in payload.get('parts', []) or []:
        yield from walk(p)

resp = svc.users().messages().list(userId='me', q='from:person@example.com OR to:person@example.com', maxResults=50).execute()
thread_ids = {m['threadId'] for m in resp.get('messages', [])}

out = pathlib.Path('/tmp/gmail_audit'); att_dir = out / 'attachments'
out.mkdir(exist_ok=True); att_dir.mkdir(exist_ok=True)
records = []
for tid in thread_ids:
    thread = svc.users().threads().get(userId='me', id=tid, format='full').execute()
    for msg in thread.get('messages', []):
        payload = msg['payload']
        headers = {h['name'].lower(): h['value'] for h in payload.get('headers', [])}
        texts, htmls, attachments = [], [], []
        for part in walk(payload):
            mt = part.get('mimeType', '')
            body = part.get('body', {})
            if body.get('data') and mt == 'text/plain':
                texts.append(decode(body['data']))
            elif body.get('data') and mt == 'text/html':
                htmls.append(decode(body['data']))
            if part.get('filename') and body.get('attachmentId'):
                att = svc.users().messages().attachments().get(userId='me', messageId=msg['id'], id=body['attachmentId']).execute()
                data = base64.urlsafe_b64decode(att['data'].encode())
                path = att_dir / f"{msg['id']}_{part['filename']}"
                path.write_bytes(data)
                attachments.append(str(path))
        body = '\n'.join(texts) or re.sub('<[^>]+>', ' ', '\n'.join(htmls))
        records.append({'id': msg['id'], 'threadId': tid, 'from': headers.get('from',''), 'to': headers.get('to',''), 'date': headers.get('date',''), 'subject': headers.get('subject',''), 'body': body, 'attachments': attachments})
(out / 'records.json').write_text(json.dumps(records, ensure_ascii=False, indent=2))
```

## Pitfalls

- Expand full threads after the first search; obligations often appear in replies that do not match the exact search query.
- Do not claim a document was reviewed just because it was attached. Download it and extract/read text, or state that extraction was only best-effort.
- For privacy-heavy attachment sets, summarize required actions without exposing unnecessary personal data in the final response.
