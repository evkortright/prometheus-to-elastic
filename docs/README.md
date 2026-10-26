# Docs map

A one-page map of this repository: which file is which, who owns it, and when to open it. The root chat keeps it current and updates it in the same delivery whenever a file is added, renamed or retired.

**When two files disagree:** the living handoff wins, unless the claims register says otherwise; a video's contract wins for that video; the history files never win.

## Start here

- **To start a video chat:** open that video's contract (`module1-video1-contract.md`, `module1-video2-contract.md` or `module1-video3-contract.md`), go to section 11, and copy the prompt. Attach a fresh archive to the new chat (`handoff-module1-living.md`, section 15.3, has the command).
- **To see where the project stands:** `handoff-module1-living.md`, section 6 (the tracker) and section 7 (the decisions).
- **To apply, check and commit a delivery:** `handoff-module1-living.md`, section 3 (the repo routine).
- **To apply a video chat's delivery:** ask that chat for the steps; it verifies your pasted output. Run `unzip -l` on the zip first (handoff section 3). The root reviews only if you ask.

## Current working files (in `docs/`)

Owner key: **Root** = the root chat; **V1**, **V2**, **V3** = the chat for that video.

| File | What it is | Owner | Open it when |
|---|---|---|---|
| `handoff-module1-living.md` | The living handoff: working agreements, repo routine, environments, state, tracker, decisions, glossary, lessons, traps, starter prompts | Root | You want the state or a decision. Chats read parts of it |
| `video-contract-template.md` | The template every video contract is copied from | Root | You add a video or change the rules |
| `module1-video1-contract.md` | Video 1's job description and its starter prompt | Root | You start or check the Video 1 chat |
| `module1-video2-contract.md` | The same for Video 2 | Root | You start or check the Video 2 chat |
| `module1-video3-contract.md` | The same for Video 3 | Root | You start or check the Video 3 chat |
| `module1-video1-narrative.md` | Video 1's narrative of record (the demo clips). The opening and reveal slide narrations live in the run-sheet (v5.1) | V1 | You listen to it or change a claim |
| `module1-video1-outline.md` | Video 1's outline, v2 (matches the approved narrative and the contract) | V1 | The V1 chat works on it |
| `module1-video1-run-sheet.md` | Video 1's screen steps, voice-over blocks and slide narrations (v5.1, adapted to the laptop; the recorder-dependent steps wait for the capture test) | V1 | You prepare a take |
| `module1-video1-story.md` | The reading version of Video 1's spoken text, regenerated from the narrative and the run-sheet | V1 | You want to read the whole narration in order |
| `module1-video2-narrative.md` | A **seed** narrative for Video 2, written by the root. The V2 chat decides with you whether to use it | V2 | You listen to it, or the V2 chat starts |
| `module1-video2-outline.md` | Video 2's outline and its decisions | V2 | The V2 chat works on it |
| `module1-video1-log.md`, `module1-video2-log.md`, `module1-video3-log.md` | A video's working log: checklist state, claim confirmations with retrieval dates, probe results, the take log, and the decisions the author makes with that chat. Created by the chat with its first entry | V1, V2, V3 | You want the state of one video. The log is the truth about it, ahead of the contract's checklist |
| `module1-query-lab.md` | The tests (R1 to R8, P1 to P8) and the recorded results | Root | You run a rehearsal |
| `module1-status-2026-10-19.md` | The claims register (section 4) and an older status. The file name keeps its old date; do not rename it | Root | You check a claim |
| `module-learning-objectives.md` | The curriculum and the learning objectives. The author approves any change | Root | You check a learning objective |
| `slide-narrative-guidance.md` | The author's guidance for writing slide narrations | Root | You write or check a slide narration |
| `otel-collector-reference.md` | What the OpenTelemetry Collector does in the demo, and where the span metrics come from | Root | A claim concerns where a metric comes from |
| `reset-runbook.md` | The one-time setup (Part A), the per-video reset (Part B) and the pre-roll checks (Part C), each step with the output to expect | Root | You set up the stack, reset it for a video, or prepare a take |
| `retro-runbook-first-run.md` | The facts and the findings (81 entries) from the runbook's first run on Oct 26, and the grouped plan for revising the runbook | Root | You revise the runbook, or want the first run's numbers |
| `quickstart.md` | Daily stack launch and verification. Its closing paragraph was corrected; the full setup and reset procedures are in `reset-runbook.md` | Root | You start the stack |
| `environment-setup-guide.md` | The environment plan: the local stack with Elastic Serverless, and the Instruqt sandbox | Root | You want setup background |
| `diagrams/` | Environment diagrams: the source state, the bridge state, Module 4, and the optional EDOT path (SVG and PNG) | Root | You need a picture of the environment |

## History (not for current work)

| File or folder | What it is |
|---|---|
| `handoff-2026-10-19-module1-video.md` | The first handoff to a video chat. Superseded |
| `handoff-2026-10-20-module1-continuation.md` | The second handoff. Superseded by the living handoff, whose section 13 lists what in it is out of date |
| `../modules/module1-promql-compatibility/` | Three earlier Module 1 scripts from August and September 2026 (the demo script, the final recording script and a cheat sheet), written for the older environment. The final script's own status note says it was being re-validated. The current videos do not use them |

## Code and configuration (outside `docs/`)

| File | What it is |
|---|---|
| `../README.md` | Installation and local setup of the stack, service URLs, known issues |
| `../config/prometheus-config.yaml` | The Prometheus configuration template, with placeholders for the Elastic endpoint and key |
| `../config/compose.observability.yaml` | The Docker Compose layer that adds Prometheus, Grafana and the other observability services to the demo |
| `../config/.env.example` | The template for `.env.elastic`. The real file holds the key, stays on the laptop, and is blocked from commits by `.gitignore` |
| `../scripts/apply-config.sh` | Generates the Prometheus configuration from the template and `.env.elastic`. It has a known file-permission problem; the fix is pending (see the handoff's open decisions) |
| `../.gitignore` | Keeps credentials, macOS files and editor files out of the repository |
