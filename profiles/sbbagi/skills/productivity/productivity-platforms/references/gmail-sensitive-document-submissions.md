# Gmail Sensitive Document Submission Workflow

Use this when preparing institutional submission emails from Gmail threads with sensitive personal documents (IDs, bank copies, resident registration numbers, etc.).

## Pattern

1. **Read the relevant Gmail message in full/raw form**
   - Metadata/snippet may omit large-file download links or MIME structure.
   - Save the raw `.eml` locally for audit/debugging when handling external large-file links.

2. **Extract large-file links from HTML body when attachments are not MIME attachments**
   - Some Korean mail providers (e.g. Naver 대용량 첨부) expose files as `https://bigfile.mail.naver.com/download?...` links inside the HTML body rather than as Gmail MIME attachments.
   - Parse both `text/html` anchor tags and regex URLs; prefer `bigfile.mail.naver.com/download` links over `mybox.naver.com/saveFile` links for direct download.
   - Download with redirects enabled and a browser-like user agent, then verify exact file sizes and expected formats.

3. **Separate working package from user-facing summary**
   - Keep downloaded documents under a dedicated working directory.
   - Do not paste sensitive field values (resident registration number, account number, address, ID images) into chat summaries.
   - Summaries should say what was received/created, not expose the values.

4. **Build a submission package plus an email draft**
   - Include the completed institutional form, received evidence files, prior result/evidence documents if needed, checklist, and draft body.
   - If a required artifact is missing (e.g. no lecture material original), create a clearly labeled substitute only when appropriate and flag it in the draft as “대체 검토용 / 원본 필요 시 추가 확보”. Do not imply it is the original.
   - For Gmail replies to an existing thread, set `threadId`, `In-Reply-To`, and `References` from the relevant prior message.

5. **Draft before sending when sensitive documents are involved**
   - Create a Gmail draft with attachments and verify attachment count/sizes by reading the draft back.
   - Do not send without explicit user confirmation unless the user explicitly requested immediate sending.

## Verification checklist

- [ ] All external large-file downloads succeeded and file sizes match the provider listing.
- [ ] Generated forms open/save successfully and contain required fields.
- [ ] Missing/non-original materials are clearly labeled in filenames and email body.
- [ ] Gmail draft is in the correct existing thread with the intended recipient.
- [ ] Draft read-back confirms all intended attachments are present.
- [ ] Chat response avoids exposing sensitive personal data.
