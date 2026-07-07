---
name: productivity-platforms
description: "Use when operating productivity SaaS and document workflows: Google Workspace, Notion, Airtable, PowerPoint, PDFs/OCR, Teams meeting pipelines, and maps."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [productivity, google-workspace, notion, airtable, powerpoint, pdf, teams, maps]
    related_skills: []
---

# Productivity Platforms

## Overview

This umbrella covers workplace data/document systems and adjacent utilities. The common workflow is authenticating to a platform, reading structured records or documents, applying bounded mutations, and verifying the remote/local artifact.

Former packages are preserved under `references/source-packages/<skill-name>/`.

## When to Use

- Gmail/Calendar/Drive/Docs/Sheets through Google Workspace tools.
- Notion pages/databases or Airtable bases/tables/records.
- PowerPoint deck creation, reading, or XML-level editing.
- PDF text extraction/OCR or small PDF text edits.
- Teams meeting summary pipeline operation.
- Geocoding, routes, POIs, or timezone lookups.

## Workflow Map

1. **Platform auth**: verify credentials and scopes before reads/writes.
2. **Read before write**: fetch current record/document/deck state.
3. **Bounded mutation**: change only requested fields/slides/pages/records.
4. **Artifact verification**: read back remote state, export result, or validate file structure.
5. **Privacy**: avoid exposing emails, docs, locations, or meeting content beyond the requested scope.

## Gmail / Email Drafting Notes

- When the user asks to reply within an existing email thread, do not create a fresh message. Use the existing Gmail `threadId` and set threading headers (`In-Reply-To`, `References`) from the last relevant message before sending.
- For formal Korean email drafts with requested documents or action items, keep list formatting clean and legible: use bullets with indented sub-bullets, or proper numbered sections with consistent numbering. Avoid messy mixed numbering where a numbered item contains a long, visually confusing nested list.
- If a payment/settlement email involves prior prepayment plus later institutional reimbursement, state the structure explicitly: the recipient should complete the institutional payment process, then transfer the reimbursed duplicate amount back to the specified settlement account.
- For sensitive institutional submissions (IDs, bank copies, resident registration numbers, evidence packages), draft before sending unless the user explicitly asks to send now; verify the draft by reading it back for correct thread, recipient, and attachment count/sizes. Keep chat summaries free of sensitive values.
- Korean provider large-file attachments may appear only as HTML links in Gmail raw bodies rather than MIME attachments. See `references/gmail-sensitive-document-submissions.md` for the direct-download, packaging, and verification workflow.


## Source Packages

- `references/source-packages/google-workspace/`
- `references/source-packages/notion/`
- `references/source-packages/airtable/`
- `references/source-packages/powerpoint/`
- `references/source-packages/ocr-and-documents/`
- `references/source-packages/nano-pdf/`
- `references/source-packages/teams-meeting-pipeline/`
- `references/source-packages/maps/`

## Verification Checklist

- [ ] Correct account/workspace/base/file identified.
- [ ] Mutations are scoped and reversible where possible.
- [ ] Remote writes or generated files are verified after creation/editing.
- [ ] Sensitive content is summarized only as needed.
