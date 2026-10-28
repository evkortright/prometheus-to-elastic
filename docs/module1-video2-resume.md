# Module 1, Video 2 — Resume page

**Read this first in a new chat.** One page, written Oct 28, 2026 (delivery 8). The truth about the video's state is `docs/module1-video2-log.md`; read its sections 1, 2 and 6 only if you need detail. Update this page at milestones, not at every delivery.

## What this is
Video 2 of Module 1 of the Prometheus-to-Elastic training track: "Build it up: a per-service error ratio". The **Video 2 chat** owns this video's files (`docs/module1-video2-*`, plus `scripts/*video2*`). The **root chat** owns the shared files (`docs/handoff-module1-living.md`, the contract, the claims register, the runbook, `scripts/make_review_script.py`). The video chat never edits shared files; it sends the root a note at a milestone.

## Where we are
- **Done and pushed:** narrative v2.1 (accepted as the working text), outline, run-sheet v1.4 (steps, commands, timing windows, take log, the 20 placeholders, the approved rehearsal plan, and "Review script: how to build it"), the slide versions (hook shape A, recap shape C), the placeholder helpers and review config, and review versions of both narrations with dummy numbers (built outside the repo).
- **Waiting:** Video 1's takes (the reset in the runbook's Part B wipes the data stream). Then the rehearsal (plan in the run-sheet), then the takes. A provisional review script follows the rehearsal; the final one follows the take.
- **Open:** decision 5 (the range chart); the flag variant and its wording; the spoken form of payment's ratio; zero-reading rows in idea 4; the closing sentence about Elastic's documentation (re-read and date the limitations page first); the form of the optional series beat on screen; length (about 8 minutes of speech).

## How we work
- Tiny steps, with the expected output before each; one question at a time; every command in a code block. The author runs commands and pastes the output; the author does the final commit and push.
- No "where we are" tracker or "parked" list in replies, unless something changed or the author asks.
- Claims discipline: numbers only from the take; no absolute words without a recorded result; every docs claim has a source and a retrieval date.
- Never paste the API key or `.env.elastic`. Never run a bare `git diff` in the demo folder. The gate steps (`docker compose down --volumes`, `DELETE _data_stream`) are always the author's.
- **Deliveries:** the chat builds a zip with a `MANIFEST.json`. The author runs `python3 scripts/apply_delivery.py ~/Downloads/video2-delivery-N.zip` from the repo root and pastes its report; it checks everything, stages the files, and never commits. The message gives the manifest's sha256, and the author compares that one line. Fallback: the manual routine of handoff section 3, with `unzip -o <zip> -x MANIFEST.json`.

## Which file for what
Log (state and decisions) · run-sheet (steps, rehearsal, review-script how-to) · narrative (the words) · contract (the rules and deliverables) · runbook (the stack) · `docs/narration-voice-guide.md` (the voice) · handoff sections 2, 3, 9 (the rules).

## Starter prompt for a new chat
```
I'm the author of a Prometheus-to-Elastic training track, and this chat continues Video 2 of Module 1. Read docs/module1-video2-resume.md first, then only the files it names for the task at hand. Follow the working agreements in it. Tell me (a) your understanding of the state, (b) what you need from me, and (c) the one next step you'd take.
```
