# Module 1, Video 1 — Log

**Owner:** the Video 1 chat (contract, section 10). **Created:** Oct 26, 2026.
**What this is:** the truth about this video's state, ahead of section 8 of the contract. The state table (1) and the decisions (2) are edited in place; the entry log (7) is append-only. Claim confirmations, rehearsal and probe results, and the take log are recorded here first; the root copies them into the claims register at a milestone (handoff section 9).
**Statuses:** Verified (seen or checked here), Docs, Observed, Open, Retired, Decision.

---

## 1. Checklist state (contract, section 8)

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline | Video chat | Done. v2 is `3e59f34`; the two reference fixes (the runbook pointer and the narrative reference) are in the commit that adds this log |
| 3 | Narrative approved | Author | Done (v1 stands, Oct 25; one phrase changed and approved the same day; `8f6f186`) |
| 4 | Slide narrations for the opening and the reveal | Video chat | To do. Waiting on the author's decision on the shapes (see 2) |
| 5 | Run-sheet | Video chat | v5 is in the commit that adds this log: voice-over copied from the narrative, screen steps adapted to the laptop, pre-roll moved to the runbook. Not closed: the recorder-dependent steps wait for the capture test (row 8), and C6 waits for the rehearsal (row 9) |
| 6 | Story document regenerated from the narrative | Video chat | To do, after row 4 (it needs the slide narrations) |
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
| Oct 26 | **Slide shapes for the opener and the reveal.** The guidance allows one shape per slide. My recommendation: the opener as Shape D (three parallel steps in the demo's order, a short lead-in about the game, closing on "watch the expression and try to catch it changing"), and the reveal as Shape C (three peer cards for the wrapper's choices: where it runs, when it is evaluated, what the answer is called; "most, though, not all" as the closing sentence). Alternative for the opener: Shape A, a verb-first "what you will recognize" list. The reveal follows the opener's choice | **Open.** Question asked Oct 26; waiting for the author |
| Oct 26 | **The reveal's "now you know all of it"** (the wrapper). The command has more options than the three we set (register row 36), so "all of it" is an absolute of the same kind as the phrase fixed on Oct 25. The narrative is approved, so a change needs the author. To be proposed together with the recap narration | **Open** |

## 3. Claim confirmations

| Claim | Result | Status | Date |
|---|---|---|---|
| The seven clip voice-over blocks in the run-sheet are identical to the narrative's, and their word counts are right (99, 56, 108, 92, 43, 60, 15; 670 in all with the opening and the reveal) | Checked by script | Verified (text) | Oct 26 |
| The placeholders used in the seven blocks are exactly the contract's eleven (`{{PCT_D}}` is retired) | Checked by script | Verified (text) | Oct 26 |
| In C2, C4 and C6 the text inside the parentheses is character for character the text of C1, C3 and C5; C2 and C4 differ only in the result name and the expression | Checked by script. Confirm again in the take that what was pasted is what ran | Verified (text only) | Oct 26 |
| C1, C3 and C5 and C2, C2b and C4 appear verbatim in the lab; C6 is the lab's R6 line without `| SORT service_name` | Checked by script. This shows the text, not that the lines run | Verified (text only) | Oct 26 |
| "Prometheus ships its data to Elastic with one remote-write block added to its config" | `config/prometheus-config.yaml` holds one `remote_write:` key with one entry (URL, name, API key, queue settings). That the demo's own config lacks it is inferred: the demo is not in the repo archive | Docs (partly) | Oct 26 |
| "Elastic's query language" (Clip A) | Describes E-S-Q-L, not sameness, so the "expression, not query" rule does not apply | Decision | Oct 26 |
| "Now you know all of it" (the reveal) | See 2 | Open | Oct 26 |

**Not done yet in this chat (no retrieval dates exist):** re-read the PROMQL command page for the wording behind "reads only the data inside that range" (register row 19) and "has a command for running prom-Q-L" (row 3), and record the date; re-read the limitations page before the take; confirm in the rehearsal that the label sets match, not only the counts; confirm the series counts agree ("the same metrics"); check that nothing said about `[5m]` contradicts Elastic's advice to omit range selectors (row 39).

## 4. Rehearsal and probe results

None yet. They wait for the one-time setup and a reset (`docs/reset-runbook.md`, Parts A and B). Items: R1, R3 and R6 on the fresh stack, with C6 (no sort) run exactly as it will be filmed.

## 5. Take log

None yet. Fields per rung (run-sheet, "After the take"): Prometheus value or count and time, Elastic value or count and time, seconds between the runs, retakes and notes.

## 6. Open items

The recorder, cursor, legibility, resolution, zoom, where the run-sheet is displayed, how to read the seconds between runs, the Kibana address bar, and type or paste are all listed in the run-sheet's "Still open". One more is recorded only here and there: narration may run longer than footage for Clip A and rung 1 (estimates at 150 words a minute, not measured); a test render with the rehearsal's numbers would measure it.

## 7. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 26, 2026 | Log created under contract section 10. Deliveries so far: (1) outline v2, committed as `3e59f34` and reviewed by the root before the authority rules; (2) run-sheet v5, the two outline reference fixes and this log, delivered as one commit. **Base of delivery 2:** the repo after the authority-rules commit, whose hash is recorded from the author's paste (entry 2). Base files: outline sha256 `0ee9ee1912f5d544ca82dc59ccb98a43bfefd946cbf2626ab342e16a3fe853b4`, run-sheet (v4) sha256 `4937bc6042a91d09083ba663e632821a7b5ee666b262955c5cca32164914c333`. **After delivery 2 is applied:** outline sha256 `e452157324cde0babdcabf206638b2c291e91f05aaab2fa785a1a2592682e4ad`, run-sheet sha256 `acbd5af85ae7394aba20b72d1a1e8f47d67dcf3a60d4fb5a51699dc859ec3215`. The commit hash of delivery 2 goes into entry 2, once the author's output is verified |
