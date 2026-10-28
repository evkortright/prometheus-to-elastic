# Module 1, Video 2 — Log

**Owner:** the Video 2 chat (contract, section 10). **Created:** Oct 27, 2026.
**What this is:** the truth about this video's state, ahead of section 8 of the contract. The state table (1) and the decisions (2) are edited in place; the entry log (10) is append-only. Claim confirmations, rehearsal and probe results, and the take log are recorded here first; the root copies them into the claims register at a milestone (handoff section 9).
**Statuses:** Verified (seen or checked here), Docs, Observed, Open, Retired, Decision.

---

## 1. Checklist state (contract, section 8)

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline, with decisions 1, 2, 4, 6, 8, 9 and 10 approved | Author | Done (decisions Oct 25). Since then, on Oct 27: decision 7 settled as "not used"; decisions 3 and 5 deferred (section 2). The outline file still lists 3, 5 and 7 as open; it is this chat's file and is updated in a later delivery |
| 3 | Narrative | Video chat and author | **Decided Oct 27: voice-pass the root's seed, keep its structure** (the four ideas, the two question-and-answer pairs as separate blocks, the optional beats). The v2 text is not written yet. First step: the author approves the new order for idea 1 (section 2, row 7) |
| 4 | Narrative approved | Author | Not started. The author has not listened to the seed and will listen to v2 |
| 5 | Slide narrations for the hook and the recap, with explicit shapes | Video chat | To do, after the narrative is approved. The recap is four peer cards (shape C, contract section 7). The hook's shape is not chosen |
| 6 | Run-sheet written from the approved narrative | Video chat | To do, after the narrative is approved |
| 7 | One-time setup and a stack reset (`docs/reset-runbook.md`, Parts A and B) | Root and author | Not started. Video 1's takes come first, with `paymentFailure` off; Video 2's stack is prepared after them (Parts B and C) |
| 8 | The flag measured (decision 4); decisions 3, 5 and 7 settled | Video chat guides, author runs | Not started. Decision 7 settled Oct 27 (not used). Decisions 3 and 5 deferred to the TSDS check and the rehearsal |
| 9 | Rehearsal of R2, R5, R7 and R8 on the fresh stack; claims confirmed | Video chat guides, author runs | Not started |
| 10 | The take: footage and the take log | Author | Not started |
| 11 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 12 | The first-pass video assembled and exported | Author | Not started |
| 13 | Package submitted to the second editor | Author | Not started |

## 2. Decisions made with the author

| # | Date | Decision | Status |
|---|---|---|---|
| 1 | Oct 27 | **The seed narrative is voice-passed, not rewritten and not ignored.** Keep its structure: the four ideas, the two question-and-answer pairs as separate blocks, and the optional beats. Apply `docs/narration-voice-guide.md`. The Video 1 starter brief is used as notes (its section 8, item 1, recommends the same) | **Decided** (the author) |
| 2 | Oct 27 | **The hook states the objective** in learning objective 2's own words, in the first minute (voice guide, section 3). The wording is written in the narrative pass | **Decided** (the author) |
| 3 | Oct 27 | **The optional beats stay as marked optional blocks.** Decision 3 (the series slide) waits for the TSDS wording check (register row 41) and a mapping check on the stack. Decision 5 (the range chart) waits for a rehearsal that shows both charts | **Deferred** (the author) |
| 4 | Oct 27 | **Decision 7, a percent form: not used.** When two values are too close to speak as a percent, the narration says how many leading digits agree (register row 64) | **Decided** (the author) |
| 5 | Oct 27 | **The closing line stands alone and makes no promise about Video 3** (under consideration for dropping, handoff section 8). A durable sentence is allowed if it follows the claims rules, for example that Elastic's documentation keeps the current list of limits, so the viewer should check it before moving something they depend on. The contract's closing line stays the base: "Most of prom-Q-L works this way, though not all of it, and the edges are worth knowing before you rely on them." Any added sentence about the documentation needs a docs source and a retrieval date before it is spoken | **Decided** (the principle; the wording comes in the narrative pass) |
| 6 | Oct 27 | **Flag-on stack plan: later.** Video 1's takes come first, with the flag off. Video 2's stack is prepared after them, using `docs/reset-runbook.md`, Parts B and C. How long to wait after switching the flag on is an inference (one rate window, five minutes) to test in the rehearsal | **Deferred** (the author) |
| 7 | Oct 27 | **Idea 1 is reordered so that each Prometheus run is followed by its Elastic partner, back to back** (register row 59: paired runs agree when both fall inside one scrape minute). The seed ran both Prometheus expressions before either Elastic one. This chat proposes the new order; the author approves it before any block is written | **Decided** (the principle); the order is **Proposed** |
| 8 | Oct 27 | **The setup block stays at the contract's about 30 seconds.** The listening test says whether it drags | **Decided** (the author) |

## 3. Claim confirmations

None yet in this chat. The claims-to-confirm table lives in the narrative file (contract section 4) and stays the live table; confirmations are recorded here first, with their retrieval dates, as they happen. Docs to re-read before the take, with the date recorded: the limitations page and the PROMQL command page (handoff section 9).

## 4. Rehearsal and probe results

None yet. The rehearsal (contract, section 6) runs R2, R5, R7 and R8 on the fresh stack and must also record:
- the Elastic row counts for R7 and R8, which the lab never captured;
- what the `paymentFailure` flag does to payment's ratio, and how long after switching it on the ratio shows it (register row 14). No claim about the size of the effect until it is measured;
- only if the optional beats stay: the range-query chart on both sides (decision 5), and a mapping check of how the data stream marks dimensions (decision 3, register row 41).

## 5. Take log

None yet. Fields per pair (contract, section 6): the Prometheus value or count with its time, the Elastic value or count with its time, the seconds between the runs, retakes and notes. With the proposed order for idea 1 there are five pairs: idea 1 with the `!=` matcher, idea 1 without it, then ideas 2, 3 and 4.

## 6. Open items

- **Idea 1 order:** the proposal waits for the author's approval. If approved, the placeholder `{{SECONDS_A}}` splits into two gaps, one per pair, and the contract's clip names stay as they are (A-P and A-E, then A-P0 and A-E0).
- **Wording found in the seed on the first read** (to fix in the voice pass; each absolute is a claim that needs a recorded result or a docs link, or a softer word):
  - The hook has no objective.
  - Absolutes: "the only question that matters" (hook); "That's all the not-equals did" and "never shows up" (idea 1); "every series collapses" (idea 2); "just works" (idea 3); "We only changed a number" (idea 3, answer); "every row on top has a partner underneath" (idea 4); "That's the whole climb" (recap); "exactly one time series" (the optional series block, which needs the TSDS check anyway).
  - "A counter on its own just climbs" needs "keeps climbing" (a counter can reset when a service restarts, register row 48).
  - Retired word "just" as a minimizer: "just the value and the time" (idea 2, Elastic).
  - Every execution says "Run it." The guide asks for "Let's run it." at each one (section 4).
  - The screen notes say "then Run". The real controls, observed in Video 1, are Execute in Prometheus and Search or Cmd+Enter in Discover; they are re-observed for this video before the run-sheet uses them.
  - "{{D_ROWS_PROM}} services come back": decide in the pass how to say a rows-returned count without implying a total service count (register row 53: no video states a service count).
- **The spoken form of numbers** is still open at the root (a proposal: counts whole, rates to three decimals, seconds whole).
- **Before the stack work:** read `docs/reset-runbook.md` (the author's instruction, Oct 27).
- **Timing:** five paired runs. The Prometheus click lands after about :40 and the Elastic click before about :35 of the next minute (register rows 58 and 59). Planned per pair in the run-sheet.
- **The TSDS check** (register row 41): read the current TSDS pages in full, and check the mapping on the stack.
- **Narrative claims table:** the seed's table is kept current by this chat; it also needs rows for the digits form (row 64) and for the closing sentence about the documentation, once written.

## 7. Observed UI facts

None observed in this chat. Video 1's log (section 7) is a starting point, not a source: Execute, Search, Cmd+Enter, the recorder settings and the staging routine are re-observed before this video's run-sheet uses them (starter brief, sections 4 and 7).

## 8. Workflow notes: the step ledger

Classes: **read-only** (a script could run it), **write** (changes something local), **gate** (destructive, or touches a secret; always the author), **guided** (a human action with a visible check).

| Step | What | Class | Result |
|---|---|---|---|
| S1 | Read the contract, the files it lists, and handoff sections 1, 2, 3, 9, 10, 11 and 12 | Read-only | Pass (Oct 27) |
| S2 | Extract the archive into a scratch folder in the assistant's sandbox; nothing is written to the uploads folder | Read-only | Pass |
| S3 | Replay delivery 1 in a scratch repo and read the diff stat | Write (scratch only) | Pass (entry 1 states the stat) |
| S4 | The author applies delivery 1 and checks the stat | Guided | Pending the author's paste |

## 9. Findings held for the root

Sent at a milestone, at most once per session, and only what a shared file needs (contract section 10).
- **Contract, section 8, row 2, and the outline:** decision 7 (a percent form) is settled as "not used" (Oct 27); decisions 3 and 5 are deferred. The contract lists 3, 5 and 7 as open. The outline is this chat's file; the contract is the root's.
- **Contract, section 5, claims-register rows used:** rows 59 (paired runs inside one scrape minute), 64 (digits, not percent) and 53 (no service count) now apply to Video 2 and are not on the list.
- **Already handled by the root:** the stale line in the handoff header (the author says the root is fixing it). No request.

## 10. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 27, 2026 | Log created under contract section 10 (delivery 1: this file only, no shared file). **Base:** the repo archive's commit, `8ecede16a5679908b469a733bcd791fd96220567`, read from the archive's comment (an inference that it is the commit the archive was made from; the sandbox cannot run git). The log does not exist in the base. Base sha256 of the files this chat relies on: contract `98939264e55deb3e71d2343b464f1210596e7a010498a0b5e1823fb8cb0e263c`, narrative (seed v1) `2f0769f55b310fb66d18c23ac6fb164ef3b5027bae42493ceb9bb41a26ec7d6b`, outline `0ec9069f6cde1d7db2c47be5847a741268d83c5b088731c238d3da0eeada708d`, starter brief `b43bf84e19c0411dc8a352f8ba36e7a0cd4cebb716ee8a0aa7b859007a547b07`, voice guide `30ab52d4ebe3767fa083610559af0f4926efbc3c556e6e08f8b146449133bf69`. The author's decisions of Oct 27 are in section 2. The commit hash goes into entry 2, once the author's output is verified |
