# Module 1, Video 2 — Resume page

**Read this first in a new chat.** One page, written Oct 28, 2026 (delivery 9). The truth about the video's state is `docs/module1/video2/module1-video2-log.md`; read its sections 1, 2 and 6 only if you need detail. Update this page at milestones, not at every delivery.

## What this is
Video 2 of Module 1 of the Prometheus-to-Elastic training track: "Build it up: a per-service error ratio". The **Video 2 chat** owns this video's files (`docs/module1-video2-*`, plus `scripts/*video2*`). The **root chat** owns the shared files (`docs/handoff-module1-living.md`, the contract, the claims register, the runbook, `scripts/make_review_script.py`). The video chat never edits shared files; it sends the root a note at a milestone.

## Where we are
- **Done and pushed:** narrative v2.1 (accepted as the working text), outline, run-sheet v1.4 (steps, commands, timing windows, take log, the 20 placeholders, the approved rehearsal plan, and "Review script: how to build it"), the slide versions (hook shape A, recap shape C), the placeholder helpers and review config, and review versions of both narrations with dummy numbers (built outside the repo).
- **Next:** the rehearsal, in a fresh chat (prompt below), on a freshly reset stack. The reset in the runbook's Part B wipes the data stream, so check Video 1's takes first. Then the takes. A provisional review script follows the rehearsal; the final one follows the take.
- **Open:** decision 5 (the range chart); the flag variant and its wording; the spoken form of payment's ratio; zero-reading rows in idea 4; the closing sentence about Elastic's documentation (re-read and date the limitations page first); the form of the optional series beat on screen; length (about 8 minutes of speech).

## How we work
- Tiny steps, with the expected output before each; one question at a time; every command in a code block. The author runs commands and pastes the output; the author does the final commit and push.
- No "where we are" tracker or "parked" list in replies, unless something changed or the author asks.
- Claims discipline: numbers only from the take; no absolute words without a recorded result; every docs claim has a source and a retrieval date.
- Never paste the API key or `.env.elastic`. Never run a bare `git diff` in the demo folder. The gate steps (`docker compose down --volumes`, `DELETE _data_stream`) are always the author's.
- **Deliveries.** The chat builds a zip with `scripts/build_delivery.py` (baseline = the unzipped repo archive plus the deliveries already pushed; `--built-on` = the archive's comment, from `unzip -z`; the docstring has the rest). The author runs `python3 scripts/apply_delivery.py ~/Downloads/video2-delivery-N.zip` from the repo root and pastes its report; it checks everything, stages the files, and never commits. The message gives the manifest's sha256, and the author compares that one line. Fallback: the manual routine of handoff section 3, with `unzip -o <zip> -x MANIFEST.json`.

## Which file for what
Log (state and decisions) · run-sheet (steps, rehearsal, review-script how-to) · narrative (the words) · contract (the rules and deliverables) · runbook (the stack) · `docs/shared/narration-voice-guide.md` (the voice) · handoff sections 2, 3, 9 (the rules).

## Starter prompt: a new Video 2 chat
```
I'm the author of a Prometheus-to-Elastic training track, and this chat continues Video 2 of Module 1. Read docs/module1/video2/module1-video2-resume.md first, then only the files it names for the task at hand. Follow the working agreements in it. Tell me (a) your understanding of the state, (b) what you need from me, and (c) the one next step you'd take.
```

## Starter prompt: the rehearsal chat (upload the repo archive with it)
```
I'm the author of a Prometheus-to-Elastic training track. This chat guides me, step by step, through the rehearsal of Video 2 of Module 1 on a freshly reset stack. Read docs/module1/video2/module1-video2-resume.md first, then only these: docs/module1/video2/module1-video2-run-sheet.md (the sections "Before every take", "Rehearsal", "Timing", "After the take" and "Review script: how to build it", and the beats and commands), docs/shared/operations/reset-runbook.md (Parts B and C), and docs/module1/video2/module1-video2-log.md sections 1, 2 and 6. Follow the working agreements in the resume page: tiny steps, the expected output before each step, one question at a time, every command in a code block, no tracker. I run the commands and paste the output; you check it against what you expected. The destructive steps (docker compose down --volumes, DELETE _data_stream) are mine, and you say so before each one. Never ask me to paste the API key or .env.elastic. Status of Video 1's takes: [DONE or NOT DONE: fill in]. Keep a running record of times, values and decisions. At the end, give me the values file for the provisional review script and a delivery for the video log. First tell me (a) your understanding of the plan, (b) what you need from me, and (c) the one next step.
```
