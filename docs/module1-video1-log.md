# Module 1, Video 1 — Log

**Owner:** the Video 1 chat (contract, section 10). **Created:** Oct 26, 2026.
**What this is:** the truth about this video's state, ahead of section 8 of the contract. The state table (1) and the decisions (2) are edited in place; the entry log (7) is append-only. Claim confirmations, rehearsal and probe results, and the take log are recorded here first; the root copies them into the claims register at a milestone (handoff section 9).
**Statuses:** Verified (seen or checked here), Docs, Observed, Open, Retired, Decision.

---

## 1. Checklist state (contract, section 8)

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline | Video chat | Done. v2 is `3e59f34`; the two reference fixes are in `7edfc3f`; delivery 3 (`2f2ceed`) records the slide shapes in its Slides section |
| 3 | Narrative approved | Author | Done (v1 stands, Oct 25; one phrase changed and approved the same day; `8f6f186`). A second phrase changed in the reveal on Oct 26, approved by the author, in delivery 4 |
| 4 | Slide narrations for the opening and the reveal | Video chat | Written (run-sheet v5.1, `2f2ceed`, beats 1 and 6). **Reveal: Shape C and the wording approved by the author on Oct 26.** Opener: Shape D decided Oct 26; its wording has no explicit approval yet and goes through the author's reading or listening test |
| 5 | Run-sheet | Video chat | v5 is `7edfc3f`; v5.1 (`2f2ceed`) adds the slide narrations. v5 had: voice-over copied from the narrative, screen steps adapted to the laptop, pre-roll moved to the runbook. Not closed: the recorder-dependent steps wait for the capture test (row 8), and C6 waits for the rehearsal (row 9) |
| 6 | Story document regenerated from the narrative | Video chat | Done in delivery 4: nine spoken blocks (730 words), generated from the narrative and run-sheet v5.1; every quoted line checked against the run-sheet |
| 7 | One-time setup and a stack reset | Root and author | Not started, as far as this chat knows (the runbook is written; its first run is the author's) |
| 8 | Capture test on the laptop | Author | Not started |
| 9 | Rehearsal of R1, R3 and R6 on the fresh stack; claims confirmed | Video chat guides, author runs | Not started; waits on rows 7 and 8 |
| 10 | The take: footage and the take log | Author | Not started |
| 11 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 12 | The first-pass video assembled and exported | Author | Not started |
| 13 | Package submitted to the second editor | Author | Not started |

## 2. Decisions made with the author

| Date | Decision | Status |
|---|---|---|
| Oct 26 | **Opening slide: Shape D** (three parallel steps in the demo's order, with a lead-in; the three patterns are named; closes on "watch the expression, and try to catch it changing"). The author: "Shape D is fine for the opening slide" | **Decided** |
| Oct 26 | **Reveal slide: Shape C** (peer cards for the wrapper's three choices: where it runs, when it is evaluated, what the answer is called; one signposted caveat, "most, though not all"; one closing sentence). I proposed it with D and the author has not yet answered for the reveal | **Decided** (the author, Oct 26: "I approve your proposal for the reveal wording"; read as covering the shape and the wording) |
| Oct 26 | **The reveal's "now you know all of it".** The command has more options than the three we set (register row 36), so "all of it" was an absolute. Both the recap narration and the narrative's reveal block now say "here it makes just three choices", which matches Clip B2. The reveal block keeps its 107 words | **Decided** (the author, Oct 26); the narrative was updated in delivery 4 |

## 3. Claim confirmations

| Claim | Result | Status | Date |
|---|---|---|---|
| The seven clip voice-over blocks in the run-sheet are identical to the narrative's, and their word counts are right (99, 56, 108, 92, 43, 60, 15; 670 in all with the opening and the reveal) | Checked by script | Verified (text) | Oct 26 |
| The placeholders used in the seven blocks are exactly the contract's eleven (`{{PCT_D}}` is retired) | Checked by script | Verified (text) | Oct 26 |
| In C2, C4 and C6 the text inside the parentheses is character for character the text of C1, C3 and C5; C2 and C4 differ only in the result name and the expression | Checked by script. Confirm again in the take that what was pasted is what ran | Verified (text only) | Oct 26 |
| C1, C3 and C5 and C2, C2b and C4 appear verbatim in the lab; C6 is the lab's R6 line without `| SORT service_name` | Checked by script. This shows the text, not that the lines run | Verified (text only) | Oct 26 |
| "Prometheus ships its data to Elastic with one remote-write block added to its config" | `config/prometheus-config.yaml` holds one `remote_write:` key with one entry (URL, name, API key, queue settings). That the demo's own config lacks it is inferred: the demo is not in the repo archive | Docs (partly) | Oct 26 |
| "Elastic's query language" (Clip A) | Describes E-S-Q-L, not sameness, so the "expression, not query" rule does not apply | Decision | Oct 26 |
| "Now you know all of it" (the reveal) | Replaced in the recap narration and in the narrative's reveal block (see 2); only that phrase changed in the nine spoken blocks, checked by script | Decision | Oct 26 |
| The two slide narrations meet the guidance's mechanical rules: 127 and 130 words (90 to 180), no sentence over 150 characters, no number, placeholder or forbidden word; the items are counted (opener: three steps; recap: three cards and one signposted caveat). The only watch-list hit is "never changed" in the recap, the narrative's own claim | Checked by script | Verified (text) | Oct 26 |
| "A counter that keeps climbing" (opener) is deliberately softer than "only goes up": a counter can reset when a service restarts | Prometheus's metric types page, as known; no retrieval date yet | Docs | Oct 26 |

| Every quoted paragraph in the regenerated story document (23, in nine blocks) appears verbatim in the run-sheet, and the seven demo blocks equal the narrative's | Checked by script | Verified (text) | Oct 26 |

**Not done yet in this chat (no retrieval dates exist):** re-read the PROMQL command page for the wording behind "reads only the data inside that range" (register row 19) and "has a command for running prom-Q-L" (row 3), and record the date; re-read the limitations page before the take; confirm in the rehearsal that the label sets match, not only the counts; confirm the series counts agree ("the same metrics"); check that nothing said about `[5m]` contradicts Elastic's advice to omit range selectors (row 39).

## 4. Rehearsal and probe results

None yet. They wait for the one-time setup and a reset (`docs/reset-runbook.md`, Parts A and B). Items: R1, R3 and R6 on the fresh stack, with C6 (no sort) run exactly as it will be filmed.

## 5. Take log

None yet. Fields per rung (run-sheet, "After the take"): Prometheus value or count and time, Elastic value or count and time, seconds between the runs, retakes and notes.

## 6. Open items

The recorder, cursor, legibility, resolution, zoom, where the run-sheet is displayed, how to read the seconds between runs, the Kibana address bar, and type or paste are all listed in the run-sheet's "Still open". One more is recorded only here and there: narration may run longer than footage for Clip A and rung 1 (estimates at 150 words a minute, not measured); a test render with the rehearsal's numbers would measure it. Also: the nine spoken blocks total 730 words against the narrative's 670, because the slide narrations follow the guidance (90 to 180 words each); at 150 words a minute that is about five minutes of speech before the pauses on screen. The contract's five minutes is an estimate with no hard limit.

## 7. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 26, 2026 | Log created under contract section 10. Deliveries so far: (1) outline v2, committed as `3e59f34` and reviewed by the root before the authority rules; (2) run-sheet v5, the two outline reference fixes and this log, delivered as one commit. **Base of delivery 2:** the repo after the authority-rules commit, whose hash is recorded from the author's paste (entry 2). Base files: outline sha256 `0ee9ee1912f5d544ca82dc59ccb98a43bfefd946cbf2626ab342e16a3fe853b4`, run-sheet (v4) sha256 `4937bc6042a91d09083ba663e632821a7b5ee666b262955c5cca32164914c333`. **After delivery 2 is applied:** outline sha256 `e452157324cde0babdcabf206638b2c291e91f05aaab2fa785a1a2592682e4ad`, run-sheet sha256 `acbd5af85ae7394aba20b72d1a1e8f47d67dcf3a60d4fb5a51699dc859ec3215`. The commit hash of delivery 2 goes into entry 2, once the author's output is verified |
| 2 | Oct 26, 2026 | **Delivery 2 verified** from the author's pasted output: base HEAD `2890132`, tree clean (`## main...origin/main`); the base sha256 of the outline and the run-sheet matched; the zip listing matched (three files; lengths 7122, 24287, 9311); the post-apply sha256 matched; the stats matched (outline 6, run-sheet 268, 119 insertions and 155 deletions; the log 64 insertions); the safety grep printed nothing; commit `7edfc3f` (3 files changed, 183 insertions, 155 deletions, log created) and push `2890132..7edfc3f main -> main`; afterwards HEAD equals `origin/main` and the tree is clean. The author decided the opener's shape: Shape D |
| 3 | Oct 26, 2026 | **Delivery 3** (outline Slides section, run-sheet v5.1 with the two slide narrations, this log). **Base:** `7edfc3f`; base sha256: run-sheet `acbd5af85ae7394aba20b72d1a1e8f47d67dcf3a60d4fb5a51699dc859ec3215`, outline `e452157324cde0babdcabf206638b2c291e91f05aaab2fa785a1a2592682e4ad`, log `5f58a380b0563519dd176056d5392d637c5bdb16be4acae094347df800702ec8`. **After apply:** run-sheet `5024bc4fd79ed3dd2b3927f6f12632cf77029a13d2c76fe01ca8589c64734ca5`, outline `455a32b8710c4bd6efab7bedbb84f6a6c6118761c6ca2e925298ff98a0c77956` (the log cannot list its own hash). The commit hash goes into entry 4, once the author's output is verified |
| 4 | Oct 26, 2026 | **Delivery 3 verified** from the author's pasted output: base HEAD `7edfc3f`, tree clean; the base sha256 of the log, the outline and the run-sheet matched; the zip listing matched (three files; lengths 9318, 29558, 9464); the post-apply sha256 of the outline and the run-sheet matched; the stat matched (log 19, outline 4, run-sheet 74; 81 insertions, 16 deletions); the safety grep printed nothing; commit `2f2ceed` and push `7edfc3f..2f2ceed main -> main`; afterwards HEAD equals `origin/main` and the tree is clean. The author's glob also showed the contract, narrative and story hashes (`c1f1a122…`, `08b94f49…`, `91aaf262…`), identical to the copies in the earlier archive. The author approved the reveal's shape and wording |
| 5 | Oct 26, 2026 | **Delivery 4** (narrative: the approved reveal phrase, plus the stale status line and two stale on-screen notes corrected; story document regenerated; this log). **Base:** `2f2ceed`; base sha256: narrative `08b94f49a69f663b51b656d95fa8c4b13d824f324c2403d3254e10ad48e8fc00`, story `91aaf26242a5294f1e02e1c0b3aad8594b2833e17f6a730fef83485dfddb6b10`, log `e1fbb97fb7b527f00594ea5e4a43e8416f9e8cbc1d731c6fd354d914bfb03df4`. **After apply:** narrative `b364b1a488aa9750dc9f7a2bfab247c9826707c861cd17148a8607365fe98b61`, story `b5da1ab63eb50d6d3aeb413ba89fc4ebb200af9b24a4538661d47b412314e80d`. The run-sheet and the outline are not touched. The commit hash goes into entry 6, once the author's output is verified |
