# Module 1, Video 2 — Contract

**Status:** Draft v1, October 25, 2026. Filled in from `docs/video-contract-template.md`. Owned by the root chat.
**If this contract and an older file disagree,** the contract wins for this video. The Video 2 outline (`docs/module1-video2-outline.md`) holds the beats and the decision history.

---

## 0. Header

| Field | Value |
|---|---|
| Video | 2, "Build it up: a per-service error ratio, rung by rung" (working title from the outline) |
| Contract version and date | v1, October 25, 2026 |
| Contract status | Draft |
| Chat | Not started yet |
| Root handoff | `docs/handoff-module1-living.md` (read-only for the video chat) |

## 1. The finish line

The contract is fulfilled when the author, as the first video editor, has assembled the complete video from the package in section 9 and can submit it to the second editor. The video chat's own work is complete at conditions 1 to 4 of the template's table (`docs/video-contract-template.md`, section 1). Conditions 5 to 7 are the author's.

## 2. Identity

- **Learning objective (from `docs/module-learning-objectives.md`):** **Write and execute** PromQL against a live Elastic TSDS — instant vectors, range vectors reduced by functions, aggregation, and arithmetic between aggregated results — getting results a Prometheus user would already expect. *(Apply)*
- **Module context (Module 01, PromQL Support; format: Feature Highlight):** the module aims at "PromQL syntax fluency on Elastic; TSDS conceptual grounding (series identity, dimensions, metric types); confidence that most everyday Prometheus expressions carry over, and the ability to check your own against the documented limits; an accurate, non-oversold picture of what's still incomplete."
- **Audience:** an SRE who uses PromQL and Grafana every day. Their question is "what do I have to change?" Here it becomes "can I build the question I actually get asked?"
- **Target length:** 7 to 10 minutes, flexible. The main narrative blocks are about 780 spoken words; the demos and the pauses on screen make up the rest. Cut the optional beats first if it runs long.

## 3. Standalone rule

| What the viewer needs to know | Where it comes from | Time on screen |
|---|---|---|
| PromQL, and Prometheus's expression browser (Table tab) | Assumed (the audience) | none |
| What Discover's E-S-Q-L mode and Elastic's PROMQL command are, and what the wrapper does (where it runs, when it is evaluated, what the answer is called) | Setup block, restated in full | about 30 s |
| That the date picker's range limits what the command sees | Setup block | one sentence |
| Which metric we query and where it comes from | Setup block | one sentence |

- **Closing line:** "Most of prom-Q-L works this way, though not all of it, and the edges are worth knowing before you rely on them." It stands on its own. Any pointer to Video 3 is a courtesy that can be cut without loss.

## 4. Story

- **Through-line:** build the per-service error ratio from four small ideas, one at a time, and check each step against Prometheus.
- **Narrative file:** `docs/module1-video2-narrative.md` (the root's seed draft v1; see section 10). It becomes the source of truth once the author approves a version.

| Beat | What | Capture clips | Target on screen |
|---|---|---|---|
| 1 | Hook (slide) | none | n/a |
| 2 | Setup, restated | A-setup | about 30 s |
| 2b | OPTIONAL: what a series is (slide; decision 3) | none | about 15 s |
| 3 | Idea 1: matchers (lab R2), with a pause-and-try question | A-P, A-P0, A-E, A-E0 | about 1:30 |
| 4 | Idea 2: whole-system rate (R5) | B-P, B-E | about 1:00 |
| 5 | Idea 3: arithmetic with a scalar (R7), with a pause-and-try question | C-P, C-E | about 1:00 |
| 6 | Idea 4: the error ratio (R8) | D-P, D-E | about 2:00 |
| 7 | OPTIONAL: watch it over time (decision 5) | E-P, E-E | about 1:30 |
| 8 | Recap (slide) | none | n/a |

(Clip names are proposals: P for Prometheus, E for Elastic, P0 and E0 for the baseline without the `!=` matcher.)

## 5. Claims

- **Wording rules:** as in the template. In addition: no `increase()`, no `topk`, no alerting, detection or "real time" claims, no percent form (`* 100` is untested; decision 7), no statement about the feature's status, and never say that a service with no errors "has a ratio of zero": it is absent from the result (lab R8).
- **Forbidden for this video:** "runs unchanged" as an absolute; "all"; any percentage without the seconds between the runs; the sentence that Prometheus labels become Elastic dimensions (unverified; Module 2 topic, register row 41).
- **Claims-register rows used** (status doc, section 4): 1 (most, not all), 19 (the date picker's range), 21 (binary expressions need both sides aggregated alike; operations with a number are supported), 29 (`=~` is anchored; `!=` behaves as in Prometheus), 32 (a division drops services with no series on the left), 33 (R5, R7 and R8 agree), 36 (the command's options), 38 (the label columns), 14 (the flag's effect, open) and, if the optional beats stay, 41.
- **Known edge:** Video 2 keeps `[5m]` in the expressions, as in Video 1 (register row 39). Do not say anything that contradicts Elastic's advice to omit range selectors; Video 3 explains it.

The claims-to-confirm table lives in the narrative file (section "Claims to confirm"). The video chat keeps it current and does not duplicate it here.

## 6. Evidence plan

- **Lab items this video runs:** R2, R5, R7 and R8 (verified Same on Oct 21 on the old dataset); rerun on the fresh stack as the rehearsal. The rehearsal must also record the Elastic row counts for R7 and R8, which the lab never captured.
- **The flag (decision 4):** before the take, measure what the `paymentFailure` flag does to payment's ratio on the fresh stack, and how long after switching it on the ratio shows it (register row 14). Do not write any claim about the size of the effect until that is measured.
- **Stack state required:** a freshly reset stack (`docs/reset-runbook.md`, Part B); warm-up of at least 45 minutes (the Video 1 rule, which the author may raise); the flag state as measured; the pre-roll checks passed (uptime, remote-write counters, flags page, browser and screen).
- **Rehearsal extras, only if the optional beats stay:** the range-query chart on both sides (decision 5), and a mapping check that shows how the data stream marks dimensions (decision 3, register row 41).
- **Take log fields:** per idea, the Prometheus value or count with its time, the Elastic value or count with its time, the seconds between the runs, and retakes and notes.

The placeholder table lives in the narrative file (section "Placeholders").

## 7. Narration rules

As in the template. For Video 2 specifically:
- A question and its answer are separate clips; the 3-second pause is placed in the edit.
- The slide narrations (the hook and the recap) are derived from the narrative file with an explicit shape for the slide generator. The recap is four peer cards (shape C). They do not exist yet.

## 8. Deliverables and acceptance checklist

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline, with decisions 1, 2, 4, 6, 8, 9 and 10 approved (3, 5 and 7 open) | Author | Done (decisions Oct 25) |
| 3 | Narrative: the root's seed draft v1 exists; this chat decides with the author whether to use it, rewrite it or ignore it | Video chat and author | Seed delivered; the author has not listened yet |
| 4 | Narrative approved | Author | Not started |
| 5 | Slide narrations for the hook and the recap, with explicit shapes | Video chat | To do |
| 6 | Run-sheet written from the approved narrative | Video chat | To do |
| 7 | One-time setup and a stack reset (`docs/reset-runbook.md`, Parts A and B) | Root and author | Not started |
| 8 | The flag measured (decision 4); decisions 3, 5 and 7 settled | Video chat guides, author runs | Not started |
| 9 | Rehearsal of R2, R5, R7 and R8 on the fresh stack; claims confirmed | Video chat guides, author runs | Not started |
| 10 | The take: footage and the take log | Author | Not started |
| 11 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 12 | The first-pass video assembled and exported | Author | Not started |
| 13 | Package submitted to the second editor | Author | Not started |

## 9. Package for the second editor

- The exported first-pass video.
- The slide files: the slide generator produces a `.pptx`; the author uploads it to Google Drive, opens it as Google Slides, and gives the second editor the link.

Everything else stays in the repo. **This section changes only if something changes on the author's side.**

## 10. Ownership and change rules

- **The Video 2 chat owns:** `docs/module1-video2-outline.md`, `docs/module1-video2-narrative.md`, `docs/module1-video2-log.md` (created with its first entry), and the Video 2 run-sheet and story document when they exist.
- **Seed material:** `docs/module1-video2-narrative.md` (draft v1, about 780 spoken words in the main blocks) was written by the root on Oct 25, before this chat existed, together with the claims-to-confirm table and the placeholder table inside it. It is a proposal, not a decision. This chat asks the author at the start whether to use it, rewrite it or ignore it, and owns the file from then on.
- **Shared files belong to the root** (see the template, section 10). Known needs (record them in the video log first and send them at a milestone): the register needs a row for the flag's measured effect once it exists, and the lab needs the Elastic row counts for R7 and R8 once recorded.
- **Authority and the video log (Oct 26):** this chat is the source of truth for this video's files and for the video's state. It verifies the author's pasted output for its own deliveries (the base hash, the expected stat, the commit result) and does not route them through the root. It keeps `docs/module1-video2-log.md`, which it creates with its first entry: the checklist state, claim confirmations with their retrieval dates, probe results, the take log, and the decisions the author makes with this chat (for example the slide shapes). Once the log exists, it is the truth about the video's state, ahead of section 8 of this contract. The root reviews a delivery only if the author asks.

## 11. Video chat routine and starter prompt

As in the template (sections 11 and 12). The starter prompt, with this file's name filled in:

```
I'm the author of a Prometheus-to-Elastic training track, and this chat produces Video 2 of Module 1. Please read docs/module1-video2-contract.md first, then the files it lists, then sections 1, 2, 3, 9, 10, 11 and 12 of docs/handoff-module1-living.md (read-only). Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Don't edit shared files. You are the source of truth for this video's files and state: verify my pasted output for your own deliveries, keep a video log, and send requests to the root chat only when the contract says to (a shared file that truly needs a change, a decision that crosses videos, or a milestone). If the contract lists seed material, ask me first whether to use it, rewrite it, or ignore it.
```

Files to read, in order: this contract; `docs/module1-video2-narrative.md`; `docs/module1-video2-outline.md`; `docs/module1-query-lab.md` (R2, R5, R7, R8); `docs/module1-status-2026-10-19.md` (the claims register, section 4); `docs/otel-collector-reference.md`; `docs/slide-narrative-guidance.md`; `docs/module1-video1-narrative.md` (for the voice only; Video 2 must not depend on it).


Work that can start before the one-time setup (no stack needed): checklist rows 3 to 6 of section 8.