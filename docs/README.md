# Docs index

This folder holds the documents for the Prometheus-to-Elastic training track. Each file's stage (provisional, approved or final) is in its header, not in its name.

**When two files disagree:** `shared/working-agreements.md` wins on how we work, `shared/claims-register.md` on facts, and a video's contract wins for that video. The archive never wins.

## Start here

- **To start a video chat:** open that video's contract (`module1/video1/`, `module1/video2/` or `module1/video3/`), go to section 11, and copy the prompt. The archive command is in `shared/working-agreements.md`, section 15.
- **To see where the project stands:** `shared/decisions.md` (the dated decisions and open items) and the video's log.
- **To apply, check and commit a delivery:** `shared/working-agreements.md`, section 3 (the repo routine), and `scripts/apply_delivery.py`.

## shared/ (root-owned; read-only for the video chats)

| File | Owner | Open it when |
|---|---|---|
| `shared/working-agreements.md` | Root | You need how we work, the repo routine, or the starter prompts |
| `shared/decisions.md` | Root | You want a dated decision, the open items, or the update log |
| `shared/glossary.md` | Root | A term or a key technical fact is unclear |
| `shared/lessons-and-traps.md` | Root | Before a take or a rehearsal: what went wrong before |
| `shared/claims-register.md` | Root | You check a claim (rows are cited by number) |
| `shared/narration-voice-guide.md` | Root | You write or review narration |
| `shared/slide-narrative-guidance.md` | Root | You write slide narration |
| `shared/video-contract-template.md` | Root | A new video chat is starting (copy it once per video) |
| `shared/module-learning-objectives.md` | Root | You check what a module must teach |
| `shared/otel-collector-reference.md` | Root | You need the Collector's role in the demo |
| `shared/quickstart.md` | Root | Daily launch and verification of the stack |
| `shared/environment-setup-guide.md` | Root | Setting up the environment (history notes point to the archive) |
| `shared/operations/reset-runbook.md` | Root | Before every take: the reset (Part B), warm-up and pre-roll (Part C); section 0 holds the facts about this laptop and the Elastic project |
| `shared/operations/retro-runbook-first-run.md` | Root | A retrospective on the first run (dated; history) |
| `shared/diagrams/` | Root | The four architecture diagrams, each as SVG and PNG: `01_source_state`, `02_bridge_state`, `03_module4_esql`, `04_edot_optional` (`.svg` and `.png`) |

## module1/ (per video, in one folder each)

| File | Owner | Open it when |
|---|---|---|
| `module1/module1-query-lab.md` | Root | You run or check a lab probe (P1 to P8, R1 to R8) |
| `module1/video1/module1-video1-contract.md` | Root (the Video 1 chat owns its files) | You start or check Video 1 |
| `module1/video1/module1-video1-outline.md` | Video 1 chat | Video 1's structure |
| `module1/video1/module1-video1-narrative.md` | Video 1 chat | Video 1's narration (approved draft) |
| `module1/video1/module1-video1-run-sheet.md` | Video 1 chat | Video 1's steps and commands |
| `module1/video1/module1-video1-log.md` | Video 1 chat | Video 1's state and dated decisions |
| `module1/video1/module1-video1-story.md` | Video 1 chat | Video 1's story and claims |
| `module1/video1/review-config.video1.json` | Video 1 chat | The review script's settings for Video 1 |
| `module1/video1/take-values.example.json` | Video 1 chat | An example values file for Video 1 (its rehearsal numbers) |
| `module1/video2/module1-video2-contract.md` | Root (the Video 2 chat owns its files) | You start or check Video 2 |
| `module1/video2/module1-video2-outline.md` | Video 2 chat | Video 2's structure |
| `module1/video2/module1-video2-narrative.md` | Video 2 chat | Video 2's narration (provisional) |
| `module1/video2/module1-video2-run-sheet.md` | Video 2 chat | Video 2's steps, commands and placeholders |
| `module1/video2/module1-video2-log.md` | Video 2 chat | Video 2's state, decisions and measured records |
| `module1/video2/module1-video2-resume.md` | Video 2 chat | Opening a new Video 2 chat |
| `module1/video2/module1-video2-starter-brief.md` | Video 2 chat | The brief the Video 2 chat starts from |
| `module1/video2/review-config.video2.json` | Video 2 chat | The review script's settings for Video 2 |
| `module1/video2/review-config.video2.example.json` | Video 2 chat | An example of the review settings |
| `module1/video2/take-values.video2.template.json` | Video 2 chat | The template for the take's values (filled copies stay outside the repo) |
| `module1/video3/module1-video3-contract.md` | Root | Video 3 is under consideration; its outline, narrative and log are created if Video 3 is kept |

Video 3's outline, narrative and log are created if Video 3 is kept.

## archive/ (history only; never the target of a live pointer)

| File | Owner | Open it when |
|---|---|---|
| `archive/handoff-2026-10-19-module1-video.md` | History | The first handoff to a video chat (superseded) |
| `archive/handoff-2026-10-20-module1-continuation.md` | History | The second handoff (superseded) |
| `archive/module1-status-2026-10-19.md` | History | Sections 1 to 3: the environment change and open findings of Oct 19 (its claims register is in docs/shared/claims-register.md) |
| `archive/handoff-module1-living.md` | History | The living handoff, retired: its content lives in docs/shared/ |
| `archive/modules-aug-sep-2026/module1-demo-script.md` | History | The Aug-Sep single-video demo script (superseded) |
| `archive/modules-aug-sep-2026/module1-promql-cheatsheet.md` | History | The Aug-Sep cheat sheet (superseded) |
| `archive/modules-aug-sep-2026/module1-recording-script-final.md` | History | The Aug-Sep single-video recording script (not Video 1's final) |

## scripts/ and config/ (tools and settings)

| File | Owner | Open it when |
|---|---|---|
| `../scripts/apply_delivery.py` | Root | Applying a delivery (checked, staged, never committed) |
| `../scripts/build_delivery.py` | Root | Building a delivery with a manifest |
| `../scripts/apply-config.sh` | Root | Generating the Prometheus configuration (see the runbook for its permission note) |
| `../scripts/fill_placeholders.py` | Video 1 chat | Filling Video 1's narration and building its review script |
| `../scripts/fill_placeholders.video2.py` | Video 2 chat | Filling Video 2's narration and building its review script |
| `../scripts/make_review_script.py` | Root | Building the review script from a narrative and a config |
| `../config/.env.example` | Root | The template for the Elastic settings (copy to `.env.elastic`; never commit the filled copy) |
| `../config/compose.observability.yaml` | Root | The Compose file for the demo's observability services |
| `../config/prometheus-config.yaml` | Root | The Prometheus configuration (generated from the template) |

## This file

| `README.md` | Root | You need the index |
