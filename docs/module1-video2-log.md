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
| 3 | Narrative | Video chat and author | **v2 written Oct 27 (delivery 2):** the voice pass of the root's seed, structure kept, idea 1 in the approved order. 17 main blocks and 2 optional blocks; 1207 and 96 spoken words; 20 placeholders. The text checks passed (section 3). **Accepted by the author on Oct 27 as the working text** (it reads well in the speech engine); changes are expected from the reviewers and from the recording |
| 4 | Narrative approved | Author | Accepted Oct 27 as the working text for review and recording, not as final. Changes come from the reviewers and from the take |
| 5 | Slide narrations for the hook and the recap, with explicit shapes | Video chat | **Written Oct 27 (delivery 4)** as the slide versions in the run-sheet's beats 1 and 8: the hook is shape A (the author's choice), the recap is shape C. Not yet tried in the toolkit |
| 6 | Run-sheet written from the approved narrative | Video chat | **v1 written Oct 27 (delivery 3), v1.1 with the slide versions (delivery 4):** the 19 blocks copied from narrative v2, twelve commands, the timing windows, the take log and the 20 placeholders. Not yet used in practice |
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
| 10 | Oct 27 | **Narrative v2 stays as it is.** The author finds it good and says it reads well in the speech engine. It is the working text for the reviewers and the recording; changes come from the reviewers and from the author while recording. Meanwhile only edits that the numbers force: the flag sentence, a digits sentence if few digits agree, a sentence for zero-reading rows, the spoken form of payment's ratio, and the optional beats | **Decided** (the author) |
| 11 | Oct 27 | **Review script without placeholders.** The author leans toward running the measurements, filling the placeholders, and creating the narration document for the reviewers so that they do not deal with placeholders. This chat proposed two stages: a provisional review script after the rehearsal (rehearsal numbers, labelled), and the final one after the take (the take log's numbers) | **Proposed** (the author leans toward it) |
| 12 | Oct 27 | **The author does test recordings in practice mode** on the current stack while the measurements wait: read-only commands only, no flag change, no reset. Practice footage is never used in the video | **Decided** (the author) |
| 13 | Oct 28 | **The hook's slide shape is A**, a skills list ("what you will learn"), as in Video 1's opener. Shape D (a card grid) was the alternative; shape B was ruled out because idea 4 does not depend on idea 3. The recap stays shape C | **Decided** (the author) |
| 14 | Oct 28 | **Choices made in the slide versions, for the author to confirm:** (a) the objective is split into three short sentences so that each beat stays under 150 characters, with the data stream type defined in one sentence; (b) the planted title phrases are "Four small ideas, one error ratio" (hook) and "One question, four ideas" (recap); (c) the recap's closing sentence is the narrative's sentence about Elastic's documentation, and its caveat sentence is the contract's closing line | **Proposed** |

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
| The current TSDS page, read in full, says a TSDS needs an index template with `index.mode` set to `time_series`; that each document holds a timestamp, dimension fields and metric fields; that `_tsid` is derived from the dimensions; and that a counter accumulates and resets when a serving process restarts. https://www.elastic.co/docs/manage-data/data-store/data-streams/time-series-data-stream-tsds | Fetched and read | Docs | Oct 27 (retrieved) |
| The sentences "a document can only belong to one time series" and "a time series can't span multiple data streams" are in the 8.18 copy (https://www.elastic.co/guide/en/elasticsearch/reference/8.18/tsds.html). They are not on the current page, as far as the fetched text shows | Search result; full read of the current page | Docs (8.18 copy only) | Oct 27 |
| The Prometheus remote write page says the endpoint `/_prometheus/api/v1/write` stores data in time series data streams, defaults to `metrics-generic.prometheus-default`, maps Prometheus labels as time series dimensions, and infers counters from names ending in `_total`, `_sum`, `_count` or `_bucket`. https://www.elastic.co/docs/manage-data/data-store/data-streams/tsds-ingest-prometheus-remote-write | Fetched and read | Docs | Oct 27 (retrieved) |
| The runbook's step A7.3 (first run, Oct 26) expects `index_mode: time_series` and the template `metrics-prometheus@template` for `metrics-generic.prometheus-default`. The output itself was not seen by this chat | Read from `docs/reset-runbook.md` v2.1 | Observed (recorded by the root; not seen here) | Oct 27 |
| The objective's claim, that the demo's data stream is a time series data stream, is therefore supported by the docs and by the first run's record; the rehearsal's step B6.3 shows the index mode again. The narrative's claims table still lists it as Open; the log is ahead of it, and the table is refreshed at the next narrative edit | Reasoned from the rows above | Supported (final look at B6.3) | Oct 27 |
| Register row 41's caveat, that labels becoming dimensions is not supported yet, now has docs support (the remote write page). The contract still forbids the sentence in Video 2, as a Module 2 topic | Read | Docs | Oct 27 |
| `docs/reset-runbook.md` v2.1 read in full: Part B's destructive steps (B2, B4) are the author's; B7 sets the flag; the "90%" variant is 0.95; Part C is the pre-roll; UTC in Prometheus and Dev Tools against the browser's zone in Discover; CST from Nov 1 | Read | Read | Oct 27 |
| Run-sheet v1: the 19 spoken blocks are identical to narrative v2's; the 20 placeholders match the table; in each of the six pairs the Elastic expression equals the Prometheus text; the twelve commands appear verbatim in the lab | Checked by script | Verified (text) | Oct 27 |
| Run-sheet v1.1's two slide versions follow the toolkit's mechanical rules: 139 and 179 words (90 to 180), no sentence over 150 characters, the four hook items 32, 40, 31 and 32 characters (under 45), each planted title phrase said once, the objective's words in the hook, and no digit, percentage, visual reference or forbidden word. The one "all" is the contract's own "not all of it" | Checked by script | Verified (text) | Oct 28 |

## 4. Rehearsal and probe results

None yet. The rehearsal (contract, section 6) runs R2, R5, R7 and R8 on the fresh stack and must also record:
- the Elastic row counts for R7 and R8, which the lab never captured;
- what the `paymentFailure` flag does to payment's ratio, and how long after switching it on the ratio shows it (register row 14). No claim about the size of the effect until it is measured;
- only if the optional beats stay: the range-query chart on both sides (decision 5), and a mapping check of how the data stream marks dimensions (decision 3, register row 41).

## 5. Take log

None yet. Fields per pair (contract, section 6): the Prometheus value or count with its time, the Elastic value or count with its time, the seconds between the runs, retakes and notes. With the proposed order for idea 1 there are five pairs: idea 1 with the `!=` matcher, idea 1 without it, then ideas 2, 3 and 4.

## 6. Open items

- **Narrative v2** is the working text (section 2, row 10). Edits come from the reviewers and the recording; meanwhile only edits that the numbers force.
- **The review script.** Proposed (section 2, row 11): a provisional placeholder-free script after the rehearsal, a final one after the take. It needs a Video 2 review config (the author's title-slide narration is needed) and a Video 2 placeholder helper (17 main blocks and 20 placeholders; Video 1's helper expects nine blocks and ten keys). The example config's DEMO slide lists no optional headings, so they would have to be added if the optional beats stay.
- **Length, to raise with the author.** The main blocks grew from 784 to 1207 spoken words, about 8.0 minutes of speech at 150 words a minute before the demos and the pauses on screen. The contract's target is 7 to 10 minutes in all. The growth by section (seed to v2): hook 99 to 210, recap 80 to 159, idea 1 160 to 249, idea 2 98 to 154, idea 3 92 to 130, idea 4 178 to 206, setup 77 to 99. Decision 8 says length is flexible and the optional beats are cut first. Not decided; the practice recordings and the reviewers will show it.
- **The objective's claim** is supported (section 3): the docs, the remote write page and the runbook's first-run record. The rehearsal's B6.3 gives the final look.
- **The optional series block** (decision 3, deferred): the current TSDS page does not contain "each document belongs to one time series". If the block stays it is reworded to what the page supports (each document holds a timestamp, dimension fields that identify the series, and metric values), possibly with the labels-become-dimensions link from the remote write page. Its first sentence ("a series is one metric with one particular set of labels") still needs the Prometheus data model page, not read yet.
- **The flag.** Which variant is used, and whether idea 4's "some of its requests" still fits (the "90%" variant is 0.95). The wait after switching the flag on (one rate window, five minutes) is an inference to test.
- **Idea 4 on screen.** Whether the take shows rows that read zero (the lab's R8 run did: six of eight), and if so whether a sentence is needed on what a zero row means (inference to test: an error series with no increase in the window).
- **Spoken forms of numbers** are open at the root (counts whole, rates to three decimals, seconds whole). Payment's ratio may need another form; decide after the flag is measured.
- **Control names** in the run-sheet (Execute, Search, Cmd+Enter, Remove query) come from Video 1; the author's practice runs re-observe them.
- **Timing.** Five paired runs. The Prometheus click lands after about :40 and the Elastic click before about :35 of the next minute (register rows 58 and 59); the run-sheet computes a window per pair. The sample times are re-measured on the reset stack.
- **Clock change.** The author moves from CDT to CST on Nov 1; a rehearsal or take across that date shifts the timestamps that the gaps are read from.
- **Before the take:** re-read the limitations page and the command page and record the retrieval dates; the closing sentence about the documentation needs the limitations page.
- **The slide versions** are written (delivery 4). How the toolkit times its reveals against the audio is not known; the author tries them in the toolkit.
- **Next deliveries:** after Video 1's takes, the reset, the flag measurement and the rehearsal; the provisional review script after the rehearsal.

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
| S7 | The author applies delivery 2: base and base hashes, zip listing, unzip and status, after-apply hashes and stat, safety grep, commit and push, clean-tree check | Guided | Pass (Oct 27; commit `a804543`; entry 4) |
| S8 | Read `docs/reset-runbook.md` v2.1 in full | Read-only | Pass (section 3) |
| S9 | TSDS docs check: two searches, then fetches of the current TSDS page, its advanced-topics page and the Prometheus remote write page | Read-only | Pass (section 3) |
| S10 | Write run-sheet v1 by script from narrative v2 and the lab's commands; check it by script (blocks, placeholders, command pairs, lab verbatim) | Write (scratch); the checks are auto candidates | Pass (section 3) |
| S11 | Replay delivery 3 in a scratch repo | Write (scratch only) | Pass (entry 5) |
| S12 | The author applies delivery 3: base and base hash, zip listing, unzip and status, hashes and stat, safety grep, commit and push, clean-tree check | Guided | Pass (Oct 27; commit `7f417cf`; entry 6) |
| S13 | Draft the two slide versions and check them by script against the toolkit's rules (words, sentence length, item length, forbidden words, title phrases) | Write (scratch); the checks are auto candidates | Pass (section 3) |
| S14 | Rebuild the run-sheet as v1.1 by script, with all its checks, and replay delivery 4 in a scratch repo | Write (scratch only) | Pass (entry 7) |
| S15 | The author applies delivery 4 | Guided | Pending the author's paste |

## 9. Findings held for the root

Sent at a milestone, at most once per session, and only what a shared file needs (contract section 10).
- **Contract, section 8, row 2, and the outline:** decision 7 (a percent form) is settled as "not used" (Oct 27); decisions 3 and 5 are deferred. The contract lists 3, 5 and 7 as open. The outline is this chat's file; the contract is the root's.
- **Contract, section 5, claims-register rows used:** rows 59 (paired runs inside one scrape minute), 64 (digits, not percent) and 53 (no service count) now apply to Video 2 and are not on the list.
- **Contract, section 5, the no-errors wording:** the line "never say that a service with no errors 'has a ratio of zero': it is absent from the result (lab R8)" is imprecise. In the lab's R8 run six services appeared with a ratio of exactly 0, and ten were absent. The accurate statement is about error series: a service with no error series is absent. Narrative v2 says "no error series".
- **Register, row 41, and the learning objective:** learning objective 2 says "a live Elastic TSDS". The current TSDS page and the Prometheus remote write page (both retrieved Oct 27) support that the demo's data stream is one, and the runbook's A7.3 records `index_mode: time_series` from the first run. Row 41's wording came from an 8.x copy; two of its sentences (a document belongs to one series; a series can't span data streams) are not on the current page. A new or updated row is needed: the current pages with their retrieval date, and the lifted caveat that labels are mapped as dimensions (docs-supported; still out of Video 2 as a Module 2 topic). The rehearsal's B6.3 gives the final look.
- **Already handled by the root:** the stale line in the handoff header (the author says the root is fixing it). No request.

## 10. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 27, 2026 | Log created under contract section 10 (delivery 1: this file only, no shared file). **Base:** the repo archive's commit, `8ecede16a5679908b469a733bcd791fd96220567`, read from the archive's comment (an inference that it is the commit the archive was made from; the sandbox cannot run git). The log does not exist in the base. Base sha256 of the files this chat relies on: contract `98939264e55deb3e71d2343b464f1210596e7a010498a0b5e1823fb8cb0e263c`, narrative (seed v1) `2f0769f55b310fb66d18c23ac6fb164ef3b5027bae42493ceb9bb41a26ec7d6b`, outline `0ec9069f6cde1d7db2c47be5847a741268d83c5b088731c238d3da0eeada708d`, starter brief `b43bf84e19c0411dc8a352f8ba36e7a0cd4cebb716ee8a0aa7b859007a547b07`, voice guide `30ab52d4ebe3767fa083610559af0f4926efbc3c556e6e08f8b146449133bf69`. The author's decisions of Oct 27 are in section 2. The commit hash goes into entry 2, once the author's output is verified |
| 2 | Oct 27, 2026 | **Delivery 1 verified** from the author's pasted output: base HEAD `8ecede16a5679908b469a733bcd791fd96220567` (matches the archive's comment), tree clean (`## main...origin/main`); the zip listing matched (one file, 11702 bytes); the unzip created only `docs/module1-video2-log.md` and the status showed `??` for it; the sha256 matched (`c0998002…22508d`); the stat matched (98 insertions, one file); the safety grep printed nothing; commit `52e1bde` (1 file changed, 98 insertions, log created) and push `8ecede1..52e1bde main -> main`; afterwards HEAD is `52e1bdeb102987d81353af8baa49e8cc26da73e4`, equal to `origin/main`, and the tree is clean. The author approved the new order for idea 1 |
| 3 | Oct 27, 2026 | **Delivery 2** (narrative v2, the voice pass, and this log). **Base:** `52e1bdeb102987d81353af8baa49e8cc26da73e4`; base sha256: narrative (seed v1) `2f0769f55b310fb66d18c23ac6fb164ef3b5027bae42493ceb9bb41a26ec7d6b`, log `c0998002d6fd7eb91a2f7ff22be58f678a0337ae012119859ac78e93ec22508d`. **After apply:** narrative `28694fa7c3281bb534f3b1b4e51c62e02dcd572b3d190b2296c3c6718da74c71` (the log cannot list its own hash). No shared file is touched. The commit hash goes into entry 4, once the author's output is verified |
| 4 | Oct 27, 2026 | **Delivery 2 verified** from the author's pasted output: base HEAD `52e1bdeb102987d81353af8baa49e8cc26da73e4`, tree clean; the base sha256 matched (narrative `2f0769f5…`, log `c0998002…`); the zip listing matched (two files; 17336 and 24396 bytes); the unzip and status showed ` M` for both files; the after-apply sha256 matched (narrative `28694fa7…`, log `5c7b7cee…`); the stat matched (log 53, narrative 181; 145 insertions, 89 deletions); the safety grep printed nothing; commit `a804543` and push `52e1bde..a804543 main -> main`; afterwards HEAD `a804543d9435241c0e736b9c721c786c6ae43d71` equals `origin/main` and the tree is clean. The author accepted narrative v2 as the working text (row 10). The runbook read and the TSDS docs check are done (section 3) |
| 5 | Oct 27, 2026 | **Delivery 3** (run-sheet v1, a new file, and this log). **Base:** `a804543d9435241c0e736b9c721c786c6ae43d71`; the run-sheet does not exist in the base; base sha256: log `5c7b7cee64f3282dde7273fa714c9e94df0d23724b3003f95ffa0a877e70e2cf`, narrative `28694fa7c3281bb534f3b1b4e51c62e02dcd572b3d190b2296c3c6718da74c71` (not touched). **After apply:** run-sheet `acc5032c1fe1692a83d25bbcd47ecca4eccfb040d24f194ef66219f14b602981` (the log cannot list its own hash). The commit hash goes into entry 6, once the author's output is verified |
| 6 | Oct 27–28, 2026 | **Delivery 3 verified** from the author's pasted output: base HEAD `a804543d9435241c0e736b9c721c786c6ae43d71`, tree clean; the base sha256 of the log matched (`5c7b7cee…`); the zip listing matched (two files; 24977 and 41262 bytes); the unzip and status showed ` M` for the log and `??` for the run-sheet; the after-apply sha256 matched (run-sheet `b7b8ad43…`, log `b4cce8cd…`); the stat matched (log 48, run-sheet 612; 646 insertions, 14 deletions); the safety grep printed nothing; commit `7f417cf` (run-sheet created) and push `a804543..7f417cf main -> main`; afterwards HEAD `7f417cf1f8eeda6c5e09e23fed2fa1ab019eb097` equals `origin/main` and the tree is clean. The author chose shape A for the hook (row 13) |
| 7 | Oct 28, 2026 | **Delivery 4** (run-sheet v1.1 with the two slide versions, and this log). **Base:** `7f417cf1f8eeda6c5e09e23fed2fa1ab019eb097`; base sha256: run-sheet `b7b8ad4390d330805ec8fd67c9949f7cb772a561b2d4011bf714c4f8fa65a758`, log `b4cce8cd5a6dbca451454158c8e5928960bfbe864f0d5e55df645ef6a7d6e0ae`. **After apply:** run-sheet `421a0dec0d88219eb9bb8105842f4db54ea31a97886e0bab6e100e0b1b9414e4` (the log cannot list its own hash). No shared file is touched, and the narrative is not touched. The commit hash goes into entry 8, once the author's output is verified |
