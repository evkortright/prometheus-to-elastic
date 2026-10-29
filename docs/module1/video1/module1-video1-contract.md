# Module 1, Video 1 — Contract

**Status:** Draft v1, October 25, 2026. Filled in from `docs/shared/video-contract-template.md`. Owned by the root chat.
**If this contract and an older file disagree,** the contract wins for this video (older files: the outline, run-sheet and story document predate the narrative).

---

## 0. Header

| Field | Value |
|---|---|
| Video | 1, "Your PromQL, running in Elastic" (working title) |
| Contract version and date | v1, October 25, 2026 |
| Contract status | Active |
| Chat | The Video 1 chat, started after commit `dcbb48e`. Its first reply was checked by the root and passed |
| Shared files | `docs/shared/` (read-only for the video chat) |

## 1. The finish line

The contract is fulfilled when the author, as the first video editor, has assembled the complete video from the package in section 9 and can submit it to the second editor. The video chat's own work is complete at conditions 1 to 4 of the template's table (`docs/shared/video-contract-template.md`, section 1). Conditions 5 to 7 are the author's.

## 2. Identity

- **Learning objective (from `docs/shared/module-learning-objectives.md`):** **Recognize** which everyday PromQL patterns — label selectors, aggregation, `rate()` on counters — run in Elastic using the same PromQL expression. *(Remember)*
- **Module context (Module 01, PromQL Support; format: Feature Highlight):** the module aims at "PromQL syntax fluency on Elastic; TSDS conceptual grounding (series identity, dimensions, metric types); confidence that most everyday Prometheus expressions carry over, and the ability to check your own against the documented limits; an accurate, non-oversold picture of what's still incomplete."
- **Audience:** an SRE who uses PromQL and Grafana every day. Their question is "what do I have to change?"
- **Target length:** about five minutes. The narrative is about 670 spoken words; with the pauses on screen, five minutes is an estimate, not a measurement. No hard limit.

## 3. Standalone rule

| What the viewer needs to know | Where it comes from | Time on screen |
|---|---|---|
| PromQL, and Prometheus's expression browser (Table tab) | Assumed (the audience) | none |
| What Discover's E-S-Q-L mode is, and that it has a command for running PromQL | Setup beat | about 25 s |
| Which metric we query, and where it comes from | Setup beat and rung 1 (the metric is a counter built by the OpenTelemetry Collector from traces) | within the beats |
| What the wrapper around the expression is, and what it does | Taught in rung 1 | within the beat |
| The date picker's range matters for the PromQL command | Setup beat | one sentence |

- **Closing line:** "Next, we build the question you actually get paged about: which services are failing, and how often." This is a courtesy pointer to Video 2 and can be cut without loss. The honest limit before it ("Most, though, not all") stands on its own.

## 4. Story

- **Through-line:** "find the seam." The viewer watches the expression and tries to catch it changing. In three rungs it never does; only the wrapper is new.
- **Narrative file:** `docs/module1/video1/module1-video1-narrative.md`. v1 (`8f6f186`) was approved on Oct 25. **v2, the trainer-voice pass, was approved by the author on Oct 26 (`86f6c71`)** and is the narrative of record. The slide-shape versions of the opening (Shape A) and the recap (Shape C) are in the run-sheet. The video log (`docs/module1/video1/module1-video1-log.md`) holds the current state.

| Beat | What | Capture clips | Target on screen |
|---|---|---|---|
| 1 | Opening (slide) | none | n/a |
| 2 | Setup: the same data in both places | Clip A | about 25 s |
| 3 | Rung 1: pick out some series | B1, B2 | about 45 s |
| 4 | Rung 2: how fast (`sum(rate(...))`) | C1, C2 | about 45 s |
| 5 | Rung 3: which service (`sum by`) | D1, D2 | about 45 s |
| 6 | The reveal (recap slide) | none | n/a |

(Beats and clip names come from the run-sheet's beat map. The narrative's section names map to them one to one.)

## 5. Claims

- **Wording rules:** as in the template. In addition: no `increase()`, no `topk`, no statement about the feature's status (Video 3 covers status), no claims about alerting or "real time".
- **Forbidden for this video:** "runs unchanged" as an absolute; "single remote-write block" (say "one remote-write block added to its config"); "I want to show you"; any percentage without the seconds between the runs; "can't be done in PromQL".
- **Claims-register rows used** (status doc, section 4): 1 (most, not all), 2 (the expression body is identical), 18 (`rate()` values agree back to back), 19 (the date picker's range), 20 (grouped `rate()` agrees), 29 (`=~` and `!=` behavior, if the matcher is mentioned), 30 (our wording is "most everyday expressions").
- **Known edge (Oct 25):** Elastic's porting advice is to omit range selectors so the window adapts to the time range, and to use a fixed window only when you need exactly that window (register row 39). Video 1 keeps `[5m]` on purpose: with `time=?_tend` it is the rate over the last five minutes, and it makes the "same expression" point. Video 3 explains the difference. Do not say anything in Video 1 that contradicts Elastic's advice.

The status of each claim below is kept in the video log (section 3), which is the truth. This table lists what must be confirmed.

| Sentence | Confirm against | Status |
|---|---|---|
| "The labels sit in a column instead of inline, but they're the same series" (rung 1) | Docs support the column claim: a result without a cross-series aggregation returns the labels in one `_timeseries` column as JSON (register row 38). The "same series" part needs the label sets on both sides to match (take) | Open (the take) |
| "Only the wrapper is new" (rung 1) | The Elastic line's expression is character for character the Prometheus text (take) | Open |
| "The only thing we touch is the name of the answer" (rung 2) | The two commands differ only in the result name and the expression text (take) | Open |
| "Everything around it is a wrapper, and here it makes just three choices" (index, time, result name) | The `PROMQL` command page lists more options (index, step, buckets, start, end, time, scrape_interval, and an optional result name), so "three choices" is true and "only three questions" was not. Register row 36, retrieved Oct 25 | Docs (Oct 25) |
| "evaluated once, just like the Table tab" (time = the end of the picker's range) | The command page: `time` evaluates the expression once, and `?_tend` is the end of the date picker's range. Register row 37, retrieved Oct 25 | Docs (Oct 25) |
| "Elastic's prom-Q-L command reads only the data inside that range" | Register row 19 (effect verified in lab R4; mechanism consistent with the docs). Re-read the docs wording and record the retrieval date | Open |
| "Kibana's Discover, in E-S-Q-L mode ... has a command for running prom-Q-L" | The command page; register row 3. Record the retrieval date | Docs |
| "traces span metrics calls total is a counter ... the OpenTelemetry Collector builds from traces" | `docs/shared/otel-collector-reference.md` and the upstream spanmetrics connector README (register row 45, Oct 26). The demo's own Collector config is not in the repo archive | Docs (partly) |
| "Prometheus ships its data to Elastic with one remote-write block added to its config" | The `remote_write` block in `config/prometheus-config.yaml`; the pre-roll counters (failed is 0 or unchanged) | Docs |
| "Both are looking at the same metrics" | The pre-roll counters, and the agreement of the series counts in rung 1 | Open |
| "rate ... returns the per-second average rate of increase" | Prometheus's documentation for `rate()` | Docs |
| "Most, though, not all" | Register row 1; the command page says the command supports most, but not all, of PromQL (register row 36 notes, retrieved Oct 25) | Docs (Oct 25) |

## 6. Evidence plan

- **Lab items this video runs:** R1 (rung 1), R3 (rung 2), R6 (rung 3). They were verified on the old dataset; they are rerun on the fresh stack as the rehearsal. R4 belongs to Video 3.
- **Stack state required:** a freshly reset stack (`docs/shared/operations/reset-runbook.md`, Part B); warm-up of at least 45 minutes (the run-sheet's existing rule, which the author may raise); `paymentFailure` off; the pre-roll checks passed (uptime, the remote-write counters, the flags page, browser and screen).
- **Take log fields:** per rung, the Prometheus value or count and time, the Elastic value or count and time, the seconds between the runs, and retakes and notes (as in the run-sheet's take log).

| Placeholder | Meaning | Source |
|---|---|---|
| `{{N_PROM}}`, `{{N_ELASTIC}}` | Rung 1 series counts | Clip B1, B2 |
| `{{PROM_VALUE}}`, `{{ELASTIC_VALUE}}` | Frontend calls per second, rung 2 | Clip C1, C2 |
| `{{SECONDS_C}}`, `{{DIGITS_C}}` | Seconds between the runs, and how many leading digits the two rung 2 values share (the relative difference, about 6e-8 percent, cannot be spoken), rung 2 | Take log; computed (`scripts/fill_placeholders.py`) |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Row counts, rung 3 | Clip D1, D2 |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | Clip D1, D2 |
| `{{SECONDS_D}}` | Seconds between the runs, rung 3 | Take log |

`{{PCT_D}}` (the run-sheet) and `{{PCT_C}}` (the percent form) are retired: the narration says the two rung 2 values agree to `{{DIGITS_C}}` digits.

## 7. Narration rules

As in the template. Two decisions for Video 1 specifically:
- The spellings `prom-Q-L`, `E-S-Q-L` and `S-L-Os` are the current default; the author's listening test asked for no changes.
- The slide narrations exist: the spoken text of the opening and the reveal is in narrative v2, and the slide-shape versions (opener Shape A, recap Shape C) are in the run-sheet.
- The voice is the trainer voice (objective first), and the three-version model applies: see `docs/shared/narration-voice-guide.md`.

## 8. Deliverables and acceptance checklist

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline, updated to match the narrative | Video chat | Done (v2, `3e59f34`). One stale line (the runbook "not yet written") is for the chat to fix in its next round |
| 3 | Narrative approved | Author | Done (v1 stands, Oct 25; one phrase changed and approved the same day) |
| 4 | Slide narrations for the opening and the reveal, with explicit shapes | Video chat | To do |
| 5 | Run-sheet final: the voice-over regenerated from the narrative, and the screen steps adapted to the laptop (the recorder is a decision; the pre-roll commands drop WSL) | Video chat | To do |
| 6 | Story document regenerated from the narrative | Video chat | To do |
| 7 | One-time setup and a stack reset (`docs/shared/operations/reset-runbook.md`, Parts A and B) | Root and author | Not started |
| 8 | Capture test on the laptop (recorder, cursor, readable text, resolution) | Author | Not started |
| 9 | Rehearsal of R1, R3 and R6 on the fresh stack; claims in section 5 confirmed | Video chat guides, author runs | Not started |
| 10 | The take: footage and the take log | Author | Not started |
| 11 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 12 | The first-pass video assembled and exported | Author | Not started |
| 13 | Package submitted to the second editor | Author | Not started |

## 9. Package for the second editor

- The exported first-pass video.
- The slide files: the slide generator produces a `.pptx`; the author uploads it to Google Drive, opens it as Google Slides, and gives the second editor the link.

The second editor took the author's DaVinci Resolve export plus the slides on an earlier project, animated the slides, and used the demo and audio straight from the video. Everything else stays in the repo. **This section changes only if something changes on the author's side.**

## 10. Ownership and change rules

- **The Video 1 chat owns:** `docs/module1/video1/module1-video1-outline.md`, `docs/module1/video1/module1-video1-run-sheet.md`, `docs/module1/video1/module1-video1-story.md`, `docs/module1/video1/module1-video1-narrative.md`, `docs/module1/video1/module1-video1-log.md` (created with its first entry), and its helper files `scripts/fill_placeholders.py`, `docs/module1/video1/take-values.example.json` and `docs/module1/video1/review-config.video1.json`.
- **Material written before this chat:** the Video 1 narrative (v1) was written by the root before this chat existed, and the author approved it on Oct 25. It is approved material, not a seed: this chat changes it only to fix a claim (section 5) or with the author's approval.
- **Shared files belong to the root** (see the template, section 10). Send the root a request only when a shared file truly needs a change, when a decision crosses videos, or at a milestone (a checklist row changes state); most turns say nothing about the root. Already handled: the claims-register rows for the wrapper wording, the `time` option and the labels column (rows 36 to 39, Oct 25) and the spanmetrics origin (row 45, Oct 26).
- **Authority and the video log (Oct 26):** this chat is the source of truth for this video's files and for the video's state. It verifies the author's pasted output for its own deliveries (the base hash, the expected stat, the commit result) and does not route them through the root. It keeps `docs/module1/video1/module1-video1-log.md`, which it creates with its first entry: the checklist state, claim confirmations with their retrieval dates, probe results, the take log, and the decisions the author makes with this chat (for example the slide shapes). Once the log exists, it is the truth about the video's state, ahead of section 8 of this contract. The root reviews a delivery only if the author asks. This applies while the chat is the active chat: only one chat at a time delivers changes to the repo (`docs/shared/working-agreements.md`, section 2, agreement 15), and a chat the author has not named active is advisory.

## 11. Video chat routine and starter prompt

As in the template (sections 11 and 12). The starter prompt, with this file's name filled in:

```
I'm the author of a Prometheus-to-Elastic training track, and this chat produces Video 1 of Module 1. Please read docs/module1/video1/module1-video1-contract.md first, then the files it lists, then docs/shared/working-agreements.md (sections 1, 2, 3 and 9), docs/shared/glossary.md and docs/shared/lessons-and-traps.md (read-only). Follow the working agreements in section 2 of docs/shared/working-agreements.md: tiny steps, expected output before each step, one question at a time, and the repo routine in its section 3. I'm not a PromQL specialist; explain everything. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Don't edit shared files. You are the source of truth for this video's files and state: verify my pasted output for your own deliveries, keep a video log, and send requests to the root chat only when the contract says to (a shared file that truly needs a change, a decision that crosses videos, or a milestone). You are the active chat only when I say so; until then you are advisory: answer and review, but do not deliver files. Do not end replies with status lists unless something changed materially or I ask.
```

Files to read, in order: this contract; `docs/module1/video1/module1-video1-narrative.md`; `docs/module1/video1/module1-video1-run-sheet.md`; `docs/module1/video1/module1-video1-outline.md`; `docs/module1/module1-query-lab.md` (R1, R3, R6); `docs/shared/claims-register.md` (the claims register); `docs/shared/otel-collector-reference.md`; `docs/shared/slide-narrative-guidance.md`.


Work that can start before the one-time setup (no stack needed): checklist rows 2, 4, 5 and 6 of section 8.