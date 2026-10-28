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
| 3 | Narrative | Video chat and author | **v2 written Oct 27 (delivery 2):** the voice pass of the root's seed, structure kept, idea 1 in the approved order. 17 main blocks and 2 optional blocks; 1207 and 96 spoken words; 20 placeholders. The text checks passed (section 3). Not approved |
| 4 | Narrative approved | Author | Not started. Next: the author reads v2 and hears it through the speech engine; changes go into the narrative's listening notes |
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
| 7 | Oct 27 | **Idea 1 is reordered so that each Prometheus run is followed by its Elastic partner, back to back** (register row 59: paired runs agree when both fall inside one scrape minute). The seed ran both Prometheus expressions before either Elastic one. **Approved order:** Prometheus with the `!=` matcher, then Elastic with it; Prometheus without it, then Elastic without it; then the question and the answer. `{{SECONDS_A}}` splits into one gap per pair | **Decided** (the author, Oct 27: "I approve") |
| 8 | Oct 27 | **The setup block stays at the contract's about 30 seconds.** The listening test says whether it drags | **Decided** (the author) |
| 9 | Oct 27 | **Choices made in the v2 text, for the author to confirm when reading it:** (a) the objective's "TSDS" is spoken as "time series data stream", and the claim that the demo's data stream is one stays open until the mapping check; (b) one sentence in the first Elastic block says what index, time and the result name each do; (c) the second pair says the error series come back as new rows (the seed said frontend "jumps"), with the placeholders renamed `{{A_ERR_FRONTEND_*}}`; (d) agreement placeholders `{{DIGITS_B}}`, `{{DIGITS_C}}` and `{{DIGITS_D}}` are added for ideas 2, 3 and 4 (decision 4, register row 64); (e) "no errors" became "no error series"; (f) the closing adds one sentence about Elastic's documentation (decision 5), whose claim stays open until the limitations page is re-read and dated | **Proposed** |

## 3. Claim confirmations

The claims-to-confirm table lives in the narrative file (contract section 4) and stays the live table; confirmations are recorded here first, with their retrieval dates, as they happen. Docs to re-read before the take, with the date recorded: the limitations page and the PROMQL command page (handoff section 9).

| Claim | Result | Status | Date |
|---|---|---|---|
| Narrative v2 has 17 main blocks and 2 optional blocks, with 1207 and 96 spoken words. The same counting method gives the seed's own 784 and 92 | Counted by script | Verified (text) | Oct 27 |
| The 20 placeholders used in the main blocks are exactly the 20 in the narrative's placeholders table | Checked by script | Verified (text) | Oct 27 |
| The spoken blocks hold no retired word and none of the forbidden words (`increase(`, topk, alert, real time, percent, preview, another video, the word for a rung); every execution block says "Let's run it" (ten main blocks and the optional chart block); no sentence is over 30 words; the three phrases of learning objective 2 are in the hook, the first at word 62 | Checked by script | Verified (text) | Oct 27 |
| The absolute words that remain were reviewed: "all" in "the rate of all calls", "at all" and "not all of it" (the source's own framing); "only" in "reads only the data inside that range" (register row 19, re-read open); "the whole value" (the regex is anchored, row 29); "nothing after the sum" (syntax) | Reviewed by hand | Reviewed | Oct 27 |
| In the lab's R2 table the baseline run has one row per status code for each service (frontend 36 with status code unset and 14 with error; checkout 8 and 2), so removing the `!=` adds rows and does not change the unset row | Read from `docs/module1-query-lab.md` | Verified (lab record, previous dataset); confirm in the take | Oct 27 |
| The lab's R8 run returned eight services, six of them with a ratio of exactly 0, and ten absent | Read from the lab | Verified (lab record, previous dataset); the basis for "no error series" | Oct 27 |
| The review-script builder runs on v2 with the example config (nothing kept): four slides, 1221 spoken words with the example's 14-word title placeholder, 20 placeholders left in the script | Dry run in a scratch folder | Verified (text) | Oct 27 |

## 4. Rehearsal and probe results

None yet. The rehearsal (contract, section 6) runs R2, R5, R7 and R8 on the fresh stack and must also record:
- the Elastic row counts for R7 and R8, which the lab never captured;
- what the `paymentFailure` flag does to payment's ratio, and how long after switching it on the ratio shows it (register row 14). No claim about the size of the effect until it is measured;
- only if the optional beats stay: the range-query chart on both sides (decision 5), and a mapping check of how the data stream marks dimensions (decision 3, register row 41).

## 5. Take log

None yet. Fields per pair (contract, section 6): the Prometheus value or count with its time, the Elastic value or count with its time, the seconds between the runs, retakes and notes. With the proposed order for idea 1 there are five pairs: idea 1 with the `!=` matcher, idea 1 without it, then ideas 2, 3 and 4.

## 6. Open items

- **Narrative v2 is not approved.** The author reads it and hears it through the speech engine (Qwen3); changes go into the narrative's listening notes, then iteration 2.
- **Length, to raise with the author after reading v2.** The main blocks grew from 784 to 1207 spoken words, about 8.0 minutes of speech at 150 words a minute before the demos and the pauses on screen. The contract's target is 7 to 10 minutes in all, with the main blocks at about 780 words. The growth by section (seed to v2): hook 99 to 210, recap 80 to 159, idea 1 160 to 249 (the second pair and the wrapper sentence), idea 2 98 to 154, idea 3 92 to 130, idea 4 178 to 206, setup 77 to 99. Decision 8 says length is flexible and the optional beats are cut first. Not decided.
- **The objective's claim.** The hook and the recap say "a live Elastic time series data stream". Whether the demo's data stream is one is unverified (register row 41 covers the general pages only). The mapping check on the stack (the data stream's index mode) settles it; if it fails, the sentence changes.
- **Idea 4 on screen.** Whether the take shows rows that read zero (the lab's R8 run did: six of eight), and if so whether a sentence is needed on what a zero row means (inference to test: an error series with no increase in the window).
- **Spoken forms of numbers** are open at the root (counts whole, rates to three decimals, seconds whole). Payment's ratio may need another form; decide after the flag is measured.
- **Control names** in the screen notes (Execute, Search, Cmd+Enter) come from Video 1; re-observe them before the run-sheet.
- **Helpers.** Video 1's `fill_placeholders.py` expects nine fenced blocks and ten keys; Video 2 has 17 main blocks and 20 placeholders, so a Video 2 helper (named with the video) is adapted once the take is done. The review config for Video 2 is created when the narrative is approved; the example's DEMO slide lists no optional headings, so they would have to be added if the optional beats stay.
- **Timing.** Five paired runs. The Prometheus click lands after about :40 and the Elastic click before about :35 of the next minute (register rows 58 and 59). Planned per pair in the run-sheet.
- **The TSDS check** (register row 41): read the current TSDS pages in full, and check the mapping on the stack.
- **Before the stack work:** read `docs/reset-runbook.md` (the author's instruction, Oct 27).
- **Before the take:** re-read the limitations page and the command page and record the retrieval dates; the closing sentence about the documentation needs the limitations page.

## 7. Observed UI facts

None observed in this chat. Video 1's log (section 7) is a starting point, not a source: Execute, Search, Cmd+Enter, the recorder settings and the staging routine are re-observed before this video's run-sheet uses them (starter brief, sections 4 and 7).

## 8. Workflow notes: the step ledger

Classes: **read-only** (a script could run it), **write** (changes something local), **gate** (destructive, or touches a secret; always the author), **guided** (a human action with a visible check).

| Step | What | Class | Result |
|---|---|---|---|
| S1 | Read the contract, the files it lists, and handoff sections 1, 2, 3, 9, 10, 11 and 12 | Read-only | Pass (Oct 27) |
| S2 | Extract the archive into a scratch folder in the assistant's sandbox; nothing is written to the uploads folder | Read-only | Pass |
| S3 | Replay delivery 1 in a scratch repo and read the diff stat | Write (scratch only) | Pass (98 insertions) |
| S4 | The author applies delivery 1: base HEAD, zip listing, unzip and status, hash and stat, safety grep, commit and push, clean-tree check | Guided | Pass (Oct 27; commit `52e1bde`; entry 2) |
| S5 | Write narrative v2 in a scratch folder and check it by script (counts, placeholders, retired and absolute words, cues, sentence length, the objective's wording, tables); dry-run the review-script builder | Write (scratch); the checks are auto candidates | Pass (section 3) |
| S6 | Replay delivery 2 in a scratch repo | Write (scratch only) | Pass (entry 3) |
| S7 | The author applies delivery 2 | Guided | Pending the author's paste |

## 9. Findings held for the root

Sent at a milestone, at most once per session, and only what a shared file needs (contract section 10).
- **Contract, section 8, row 2, and the outline:** decision 7 (a percent form) is settled as "not used" (Oct 27); decisions 3 and 5 are deferred. The contract lists 3, 5 and 7 as open. The outline is this chat's file; the contract is the root's.
- **Contract, section 5, claims-register rows used:** rows 59 (paired runs inside one scrape minute), 64 (digits, not percent) and 53 (no service count) now apply to Video 2 and are not on the list.
- **Contract, section 5, the no-errors wording:** the line "never say that a service with no errors 'has a ratio of zero': it is absent from the result (lab R8)" is imprecise. In the lab's R8 run six services appeared with a ratio of exactly 0, and ten were absent. The accurate statement is about error series: a service with no error series is absent. Narrative v2 says "no error series".
- **Register, row 41 (and the learning objective):** learning objective 2 says "a live Elastic TSDS", and nothing recorded shows that the demo's data stream is one. A new row is needed after the mapping check.
- **Already handled by the root:** the stale line in the handoff header (the author says the root is fixing it). No request.

## 10. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 27, 2026 | Log created under contract section 10 (delivery 1: this file only, no shared file). **Base:** the repo archive's commit, `8ecede16a5679908b469a733bcd791fd96220567`, read from the archive's comment (an inference that it is the commit the archive was made from; the sandbox cannot run git). The log does not exist in the base. Base sha256 of the files this chat relies on: contract `98939264e55deb3e71d2343b464f1210596e7a010498a0b5e1823fb8cb0e263c`, narrative (seed v1) `2f0769f55b310fb66d18c23ac6fb164ef3b5027bae42493ceb9bb41a26ec7d6b`, outline `0ec9069f6cde1d7db2c47be5847a741268d83c5b088731c238d3da0eeada708d`, starter brief `b43bf84e19c0411dc8a352f8ba36e7a0cd4cebb716ee8a0aa7b859007a547b07`, voice guide `30ab52d4ebe3767fa083610559af0f4926efbc3c556e6e08f8b146449133bf69`. The author's decisions of Oct 27 are in section 2. The commit hash goes into entry 2, once the author's output is verified |
| 2 | Oct 27, 2026 | **Delivery 1 verified** from the author's pasted output: base HEAD `8ecede16a5679908b469a733bcd791fd96220567` (matches the archive's comment), tree clean (`## main...origin/main`); the zip listing matched (one file, 11702 bytes); the unzip created only `docs/module1-video2-log.md` and the status showed `??` for it; the sha256 matched (`c0998002…22508d`); the stat matched (98 insertions, one file); the safety grep printed nothing; commit `52e1bde` (1 file changed, 98 insertions, log created) and push `8ecede1..52e1bde main -> main`; afterwards HEAD is `52e1bdeb102987d81353af8baa49e8cc26da73e4`, equal to `origin/main`, and the tree is clean. The author approved the new order for idea 1 |
| 3 | Oct 27, 2026 | **Delivery 2** (narrative v2, the voice pass, and this log). **Base:** `52e1bdeb102987d81353af8baa49e8cc26da73e4`; base sha256: narrative (seed v1) `2f0769f55b310fb66d18c23ac6fb164ef3b5027bae42493ceb9bb41a26ec7d6b`, log `c0998002d6fd7eb91a2f7ff22be58f678a0337ae012119859ac78e93ec22508d`. **After apply:** narrative `28694fa7c3281bb534f3b1b4e51c62e02dcd572b3d190b2296c3c6718da74c71` (the log cannot list its own hash). No shared file is touched. The commit hash goes into entry 4, once the author's output is verified |
