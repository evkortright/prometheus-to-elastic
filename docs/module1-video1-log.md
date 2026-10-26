# Module 1, Video 1 — Log

**Owner:** the Video 1 chat (contract, section 10). **Created:** Oct 26, 2026.
**What this is:** the truth about this video's state, ahead of section 8 of the contract. The state table (1) and the decisions (2) are edited in place; the entry log (10) is append-only. Claim confirmations, rehearsal and probe results, and the take log are recorded here first; the root copies them into the claims register at a milestone (handoff section 9).
**Statuses:** Verified (seen or checked here), Docs, Observed, Open, Retired, Decision.

---

## 1. Checklist state (contract, section 8)

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline | Video chat | Done. v2 is `3e59f34`; v3 (delivery 6) follows narrative v2 and the capture test |
| 3 | Narrative approved | Author | Done. v1 approved Oct 25 (`8f6f186`); the reveal's "now you know all of it" changed Oct 26 (`5b21b4e`). **v2, the trainer-voice pass, approved by the author on Oct 26** and delivered in delivery 6: all nine spoken blocks are the normalized narration |
| 4 | Slide narrations for the opening and the reveal | Video chat | Done in delivery 6. The spoken text of both slides is in narrative v2; the slide-shape versions (the opener as Shape A, the recap as Shape C), derived for the slide toolkit, are in the run-sheet, beats 1 and 6. How the toolkit times its reveals against the audio is not known here |
| 5 | Run-sheet | Video chat | v6 (delivery 6): the nine blocks copied from narrative v2, the slide versions re-derived, the screen steps corrected from the guided session, `{{DIGITS_C}}` in place of `{{PCT_C}}`. Ready for the takes; the staging routine and where the sheet is displayed are for the author to judge |
| 6 | Story document regenerated from the narrative | Video chat | Done in delivery 6: regenerated from narrative v2 (909 words in nine blocks); every quoted paragraph checked against the narrative and the run-sheet |
| 7 | One-time setup and a stack reset | Root and author | Done Oct 26 (runbook v2, `f6cc7f2`). The stack has run since 11:10:56 CDT (T0 16:10:56 UTC) and was warm for the rehearsal |
| 8 | Capture test on the laptop | Author | **Closed Oct 26** (section 8, S6 to S25): the built-in recorder, settings and shortcuts settled; text easy to read at 125%; the cursor fine; the clip imports into Resolve; the stack unaffected |
| 9 | Rehearsal of R1, R3 and R6 on the fresh stack; claims confirmed | Video chat guides, author runs | The runs are done (Oct 26, S11 to S15): all three rungs agree between the systems (section 4). Claims are partly confirmed (section 3). Open: the label-value check, the docs re-reads with retrieval dates, and the straddle test |
| 10 | The take: footage and the take log | Author | Not started. The author's next step, together with generating the slides |
| 11 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 12 | The first-pass video assembled and exported | Author | Not started |
| 13 | Package submitted to the second editor | Author | Not started |

## 2. Decisions made with the author

| Date | Decision | Status |
|---|---|---|
| Oct 26 | **Opening slide: Shape D** (three parallel steps; closes on "watch the expression, and try to catch it changing"). The author: "Shape D is fine for the opening slide". Superseded later the same day, when the voice changed to objective-first training, by the Shape A slide version below | **Superseded** |
| Oct 26 | **Reveal slide: Shape C** (peer cards for the wrapper's three choices: where it runs, when it is evaluated, what the answer is called; one signposted caveat, "most, though not all"; one closing sentence). I proposed it with D and the author has not yet answered for the reveal | **Decided** (the author, Oct 26: "I approve your proposal for the reveal wording"; read as covering the shape and the wording) |
| Oct 26 | **The reveal's "now you know all of it".** The command has more options than the three we set (register row 36), so "all of it" was an absolute. Both the recap narration and the narrative's reveal block now say "here it makes just three choices", which matches Clip B2. The reveal block keeps its 107 words | **Decided** (the author, Oct 26); the narrative was updated in delivery 4 |
| Oct 26 | **The brief flash of the tab strip and toolbar on Control+Tab in full screen** is cut in DaVinci Resolve or the final polish, not prevented at capture. It matters only where a tab switch happens while recording (Clip A) | **Decided** (the author) |
| Oct 26 | **Staging routine between clips.** Prometheus: the ⋮ Query options menu, then Remove query, then Add query, which leaves an empty box and "No data queried yet". Discover: run a zero-row query (a `FROM metrics-generic.prometheus-default` query ending in `LIMIT 0`), clear the editor, paste the clip's line without running it. The empty-state panel reads "No results match your search criteria", which could look like the line's own answer | **Proposed**, to be judged on the test clip |
| Oct 26 | **The rung 2 agreement sentence.** "Within {{PCT_C}} percent" would be about 6e-8 percent, which cannot be spoken. Clip C2 now says the values "agree to {{DIGITS_C}} digits" (the leading significant digits the two full-precision values share; ten in the rehearsal). The author approved the pass that contains it | **Decided** (a new placeholder; the contract's placeholder table needs a line, held for the root) |
| Oct 26 | **The narrative's opening and reveal blocks against the slide narrations.** Resolved by the three-version model below: the narrative holds the normalized narration for all nine blocks, and the slide-shape versions are separate, derived artifacts in the run-sheet | **Decided** |
| Oct 26 | **The trainer voice.** The narration is spoken by a professional SME trainer to peers: objective first, conversational authority (connectors, direct address, short sentences), claims stated and then shown, no hype and no game language ("a little game", "find the seam", "did you catch it?", "first move" are gone). The author: "Yes. This is very good!" (the opener) and "I think it works very well" (the whole pass) | **Decided** |
| Oct 26 | **Three versions of each narration (the author's model).** An informal outline; the normalized narration (what an instructor or the speech engine reads); and the slide-shape version that triggers the slide toolkit. The toolkit's shape and beat-length rules bind only the third; length restrictions are relaxed. For this video: narrative v2 is the second, the run-sheet's beats 1 and 6 hold the third | **Decided** (the author) |
| Oct 26 | **Edits to approved text in the pass:** "only the wrapper is new" became "what's new is the wrapper" (drops an absolute; the label column is also new on screen); "a counter just climbs" became "keeps climbing" (a counter can reset on restart); the opener and reveal rewritten; "first move" and "third move" became "first expression" and "third expression"; Clip D2 gained a "Let's run it" cue; the recap closes the loop on the objective and has no pointer to Video 2 | **Decided** (the author approved the pass) |
| Oct 26 | **The slide-shape versions.** Opener: Shape A (a hook with a contrast, the title phrase "Three expressions, run twice", the objective, three verb-first items, one closing sentence). Recap: Shape C (three peer cards and one signposted caveat). No "Welcome to:" line, because the outline treats this as the opening of Module 1, not of the course | **Proposed**, to be used when the author generates the slides |
| Oct 26 | **One continuous take per rung** (the pair recorded together; the narration blocks stay separate), recommended because it keeps the gap between the two runs short. The author said they will experiment | **Proposed** |
| Oct 26 | **Takes without screenshots.** The macOS floating thumbnail may appear on screen during a recording; the numbers are collected after the take stops, and the gap between the two runs is read from the footage. The helper `fill_placeholders.py` (outside the repo) computes `{{DIGITS_C}}` and fills the blocks | **Proposed** |

## 3. Claim confirmations

| Claim | Result | Status | Date |
|---|---|---|---|
| The seven clip voice-over blocks in the run-sheet are identical to the narrative's, and their word counts are right (99, 56, 108, 92, 43, 60, 15; 670 in all with the opening and the reveal) | Checked by script | Verified (text) | Oct 26 |
| The placeholders used in the seven blocks are exactly the contract's eleven (`{{PCT_D}}` is retired) | Checked by script | Verified (text) | Oct 26 |
| In C2, C4 and C6 the text inside the parentheses is character for character the text of C1, C3 and C5; C2 and C4 differ only in the result name and the expression | Checked by script. Confirm again in the take that what was pasted is what ran | Verified (text only) | Oct 26 |
| C1, C3 and C5 and C2, C2b and C4 appear verbatim in the lab; C6 is the lab's R6 line without `\| SORT service_name` | Checked by script. This shows the text, not that the lines run | Verified (text only) | Oct 26 |
| "Prometheus ships its data to Elastic with one remote-write block added to its config" | `config/prometheus-config.yaml` holds one `remote_write:` key with one entry (URL, name, API key, queue settings). That the demo's own config lacks it is inferred: the demo is not in the repo archive | Docs (partly) | Oct 26 |
| "Elastic's query language" (Clip A) | Describes E-S-Q-L, not sameness, so the "expression, not query" rule does not apply | Decision | Oct 26 |
| "Now you know all of it" (the reveal) | Replaced in the recap narration and in the narrative's reveal block (see 2); only that phrase changed in the nine spoken blocks, checked by script | Decision | Oct 26 |
| The two slide narrations meet the guidance's mechanical rules: 127 and 130 words (90 to 180), no sentence over 150 characters, no number, placeholder or forbidden word; the items are counted (opener: three steps; recap: three cards and one signposted caveat). The only watch-list hit is "never changed" in the recap, the narrative's own claim | Checked by script | Verified (text) | Oct 26 |
| "A counter that keeps climbing" (opener) is deliberately softer than "only goes up": a counter can reset when a service restarts | Prometheus's metric types page, as known; no retrieval date yet | Docs | Oct 26 |

| Every quoted paragraph in the regenerated story document (23, in nine blocks) appears verbatim in the run-sheet, and the seven demo blocks equal the narrative's | Checked by script | Verified (text) | Oct 26 |
| Rung 1 series counts agree: Prometheus "Result series: 41", Discover "41 results" (the lab saw 50 on the previous dataset) | Seen in screenshots, Oct 26 13:12 CDT | Observed | Oct 26 |
| "They're the same series" (rung 1), on label names: one sampled row on each side has the same ten label names (`collector_instance_id`, `host_name`, `job`, `service_criticality`, `service_name`, `service_namespace`, `service_version`, `span_kind`, `span_name`, `status_code`); Elastic's `_timeseries` adds `__name__`. The rows are not in the same order and the sampled rows differ, so label values are not yet compared | The count-by check on `status_code` was planned and not run | Observed (names), Open (values) | Oct 26 |
| "The labels sit in a column" (rung 1) | Elastic returns `calls`, `step` and a `_timeseries` JSON column; the grid cuts the JSON off after `collector_instance_id`, and the full list shows only in the expanded row | Observed | Oct 26 |
| Rung 2: Prometheus 14.995958299652495, Elastic 14.995958290594942, relative difference 6.0e-10; Prometheus screenshot 13:18:57 CDT, Elastic `step` 13:19:03.567, so the gap was at least 6.6 s | Seen in a screenshot and a JSON export | Observed | Oct 26 |
| Rung 3, C6 exactly as filmed (no sort): both sides return 18 rows. Elastic has `request_rate`, `step` and `service_name`, with one `step` (13:26:05.485 CDT) on every row. For the 14 rows visible in the Prometheus screenshot, the relative difference is 2.543e-10 on every one (spread 2.5e-15); frontend is 13.921645429316712 against 13.921645425776056. The gap was about 7.5 to 15.5 s | Seen in a screenshot and a JSON export | Observed | Oct 26 |
| Prometheus scrapes once a minute (`scrape_interval: 60s`, config line 6), and at one reading the newest sample of the frontend `GET /` series was stamped 13:21:37.131 CDT, so the phase is about :37 | One query of `timestamp(...)`; the phase holds only if scrapes stay on schedule | Observed (one reading) | Oct 26 |
| Elastic's `step` is the time of the run (inference): three readings were :03.185, :03.567 and :05.485, and the newest samples were stamped :37, so `step` is not a sample time | Inference from three readings | Open | Oct 26 |
| Paired runs agreed to better than 1e-9 (6.0e-10 and 2.5e-10) when both fell inside one scrape minute, after the new sample has reached Elastic and before the next one. Both timed pairs did. My reading of Prometheus's rate extrapolation says the result does not depend on where in the window it is evaluated. The lab's 1 to 6 percent differences on busy services (Oct 20) may have been pairs that straddled a sample; this is a hypothesis, and a deliberate straddle would test it | Hypothesis, consistent with rungs 2 and 3 | Open | Oct 26 |
| The service count: Prometheus reported 17 in the runbook's snapshot and 18 here (rung 3); the lab saw 18. No video states a count | Seen | Observed | Oct 26 |
| `paymentFailure` is off and enabled (`defaultVariant` `off`, `state` `ENABLED`); its 90% variant has the value 0.95 | The flag page and its JSON, `/feature/advanced` | Observed | Oct 26 |
| Remote write on Oct 26 at 17:50 to 17:53 UTC (uptime about 1 h 40 min): `failed 0`, `retried 0`, 0 warning or error lines; `sent` 22,220,532, then 22,578,173 in 74 s (about 4,800 a second). The runbook's "gap equals pending" did not hold (gap 9,176 against pending 14,176, then gap 0 against 3,852), so it is a weak check, not an invariant | Two readings of runbook C2 | Observed | Oct 26 |
| Restarts: `product-catalog` at 16:11:11 UTC (15 s after T0, the accepted startup race) and `checkout` at 16:16:40 UTC (5 min 44 s after T0, mid-run, more than an hour before the rehearsal, so accepted) | Runbook C3 | Observed | Oct 26 |
| Capture test, Oct 26 (the test clip `Screen Recording 2026-10-26 at 2.47.38 PM.mov`, about 47.3 s, 37 MB): 3456 × 2234, H.264, no audio; the Search click was at 14:48:06 CDT, about 23 s after the recording started; the author judged the cursor fine, the text easy to read at 125%, and the clip fine in Resolve | `mdls` on the file; the author's report | Observed | Oct 26 |
| Prometheus's first compaction logged one WARN at 19:10:39 UTC, 3.0 h after the first sample (16:10:38 UTC): "Overlapping blocks found during reloadBlocks", two blocks that both end at 18:00:00 UTC (one 16:00 to 18:00, one 16:10:38 to 18:00). `failed` and `retried` stayed 0, so remote write was unaffected. Hypothesis, not verified: the 30-minute out-of-order window makes Prometheus write an extra block that overlaps the in-order one. The desktop stack's earlier warnings are probably the same pattern (not investigated) | One log line | Observed (the cause is a hypothesis) | Oct 26 |
| Remote write at 19:58 UTC (about 3 h 47 min up): `failed 0`, `retried 0`, `sent` 60,049,606, `pending` and `gap` both 3,863. So "gap equals pending" held on one of four readings: a weak check | Runbook C2, fourth reading | Observed | Oct 26 |
| Rung 2 values share ten leading significant digits (14.995958299652495 and 14.995958290594942) | Computed from the rehearsal values | Observed | Oct 26 |

**Not done yet in this chat (no retrieval dates exist):** re-read the PROMQL command page for the wording behind "reads only the data inside that range" (register row 19) and "has a command for running prom-Q-L" (row 3), and record the date; re-read the limitations page before the take; confirm in the rehearsal that the label sets match, not only the counts; confirm the series counts agree ("the same metrics"); check that nothing said about `[5m]` contradicts Elastic's advice to omit range selectors (row 39).

## 4. Rehearsal and probe results

Rehearsal runs on Oct 26, 2026, on the stack that started at 11:10:56 CDT. Times are CDT; the author's screenshots carry the times (file names) and Elastic's `step` is the evaluation time. These are provisional numbers for a test render of the narration; the take's own numbers replace them.

| Rung | Prometheus | Elastic | Gap | Notes |
|---|---|---|---|---|
| 1 (R1, C1 and C2) | 41 series | 41 series (205 documents processed, 245 ms) | not measured | The same ten label names on the sampled row each side. The Elastic `step` was 13:11:03.185, earlier than both screenshots (13:12:02 and 13:12:24), so Elastic was probably run first |
| 2 (R3, C3 and C4) | 14.995958299652495 | 14.995958290594942 | at least 6.6 s | Relative difference 6.0e-10. The Prometheus result shows `{}`; Elastic shows only `frontend_rate` and `step` |
| 3 (R6, C5 and C6) | 18 rows; frontend 13.921645429316712 | 18 rows; frontend 13.921645425776056 | about 7.5 to 15.5 s | Relative difference 2.543e-10 on all 14 comparable rows. Not sorted on either side: frontend is the ninth row in Prometheus and the eleventh in Elastic. C6 without the sort ran as written |

**Not run:** the rung 1 label-value check (`count by (status_code)` on both sides, planned as a new form adapted from the lab's R2) and a deliberate straddle test of the timing hypothesis.

**Capture test (Oct 26, 14:47 to 14:48 CDT):** one continuous recording of the rung 1 pair, 47.3 s, 3456 × 2234, H.264. Search was clicked at 14:48:06, about 23 s after the start. Afterwards `failed 0`, `retried 0`. The author: the cursor looks fine; the text is easy to read at 125%; the clip is fine in DaVinci Resolve; parts of a query can be highlighted in post; the narration may play in the background while the author experiments.

## 5. Take log

None yet. Fields per rung (run-sheet, "After the take"): Prometheus value or count and time, Elastic value or count and time, seconds between the runs, retakes and notes.

## 6. Open items

The recorder, cursor, legibility, resolution, zoom, where the run-sheet is displayed, how to read the seconds between runs, the Kibana address bar, and type or paste are all listed in the run-sheet's "Still open". One more is recorded only here and there: narration may run longer than footage for Clip A and rung 1 (estimates at 150 words a minute, not measured); a test render with the rehearsal's numbers would measure it. Also: the nine spoken blocks total 730 words against the narrative's 670, because the slide narrations follow the guidance (90 to 180 words each); at 150 words a minute that is about five minutes of speech before the pauses on screen. The contract's five minutes is an estimate with no hard limit.

**Run-sheet corrections:** delivered in run-sheet v6 (delivery 6): the real control names, Control+Tab, the staging routine, the timing rule, one continuous take per rung, the clock replaced by the footage and Elastic's `step`, the percent sentence replaced by digits, and the label column's truncation.

**Open after delivery 6:** where the run-sheet is displayed during a take; the spoken form of numbers (a proposal: counts whole, rates to three decimals, seconds whole); the staging routine (judge it on the first take); what Discover's grid shows for rates (the rehearsal read full precision from the JSON); how the slide toolkit times its reveals against audio read from the spoken version; the footage-against-narration estimates (a rendered guide would measure them).

## 7. Observed UI facts (Oct 26, from the author's screens)

| Where | Fact |
|---|---|
| Chrome | Zoom is kept per site (125% on both). Control+Tab switches between the two tabs. In full screen (Control+Command+F) a tab switch flashes the tab strip and toolbar; the author cuts that in post. The two recording tabs sit in a tab group |
| Prometheus (v3.13.1) | The Query page has Table, Graph and Explain; Table is used. The result line reads "Load time: Nms" and "Result series: N". The button is **Execute**. The query and its results survive a reload. The ⋮ **Query options** menu has Explore metrics, Format expression, Show tree view, Duplicate query and Remove query. After Remove query the page shows a "+ Add query" button; clicking it gives an empty box ("Enter expression (press Shift+Enter for newlines)") and "No data queried yet" |
| Discover (Serverless) | The ES\|QL editor sits under a natural-language bar and a top row ("New session", "Untitled", "Switch to Classic", "Save"). The date picker reads "Last 1 hour". The run button is **Search** (grey while the editor is empty, blue when it holds a query); **Cmd+Enter** runs the query. A new session starts with a query already in the editor and runs it. Clearing the editor leaves the old results in place. A zero-row query shows "No results match your search criteria". The status line reads "Nms, N documents processed" and the table header reads "N results". The `PROMQL` line is highlighted without any error marks, and fits on one line at 125% |
| Elastic result shape | Rung 1: `calls`, `step`, `_timeseries` (JSON labels, cut off in the grid, whole in the expanded row). Rung 2: `frontend_rate`, `step`. Rung 3: `request_rate`, `step`, `service_name`, one `step` on every row |
| macOS recorder | Command+Shift+5. Options set and kept: save to `~/Movies/v1-capture`, microphone none, mouse clicks off, 5-second timer. Stop with Command+Control+Esc. Files are `Screen Recording <date> at <time>.mov`, H.264. Apple's instructions list no pause (a third-party site claims one; not relied on). Apple's page says macOS 27 and later has an "Include System Audio" option; keep it off |

## 8. Workflow notes: the step ledger

Each step of the guided session is classed as **read-only** (a script could run it without asking), **write** (changes something local; needs the author's OK), **gate** (destructive, or touches a secret; always the author) or **guided** (a human action with a visible check). "Auto candidate" means a script could print PASS or FAIL.

| Step | What | Class | Result |
|---|---|---|---|
| S1 | Runbook C1: uptime and the flag service | Read-only, auto candidate | Pass (all `Up 2 hours`) |
| S2 | Runbook C2: remote-write counters | Read-only, auto candidate | Pass on failed 0, retried 0, warnings 0; gap and pending differed |
| S3 | C2 again | Read-only, auto candidate | Pass; gap 0, pending 3,852, `sent` growing |
| S4 | Runbook C3: restarts | Read-only, auto candidate (needs an allowlist of known restarts relative to T0) | Pass; two known early restarts |
| S5 | Runbook C4: the `paymentFailure` flag | Guided; auto candidate through `/feature/advanced` (untried by command line) | Pass; off, ENABLED |
| S6 | Open the two tabs | Guided | Pass; Chrome |
| S7 | Clear the Kibana editor, check the picker | Guided | Pass |
| S8 | Browser zoom | Guided | Pass; 125% on both. Found: the button is Search, not Run |
| S9 | How Discover runs a query | Guided | Pass; Search button, Cmd+Enter |
| S10 | Paste the Elastic line, unrun | Guided | Pass; no error marks |
| S11 | Rung 1, both sides | Guided | Pass; 41 and 41 |
| S12 | Open one Elastic row, compare label names | Guided | Pass |
| S13 | Rung 2, both sides | Guided | Pass; 6.0e-10 |
| S14 | Newest-sample timestamp of one series | Read-only, auto candidate | Pass; phase about :37 |
| S15 | Rung 3, both sides, timed | Guided | Pass; 18 and 18 rows |
| S16 | Full screen, tab shortcut | Guided | Pass; Control+Tab |
| S17 | A clean recording window | Guided | Pass; my "third tab" reading was a tab group |
| S18 | Create `~/Movies/v1-capture` | Write (one empty folder); auto candidate | Pass |
| S19 | Set the recorder's options | Guided | Pass |
| S20 | Stage the tabs, see what a recording would show | Guided | Pass, with findings (stale results in both tools) |
| S21 | Test an empty state in Discover | Read-only | Pass |
| S22 | Stage both tabs as for Clip B1 and B2 | Guided | Pass |
| S23 | Record the test clip | Guided; writes one video file | Pass; 37 MB, 47.3 s, one continuous take, stop worked |
| S24 | Clip's resolution and codec; C2 after recording | Read-only, auto candidate | Pass; 3456 × 2234, H.264; warning count 1 |
| S25 | Read the warning line; close the capture test | Read-only plus the author's judgment | Pass; first compaction at T+3.0 h; capture test closed |

**What the session taught about a workflow system:**
- **UI facts are data.** Labels and shortcuts must be observed once and kept (section 7). I wrote "Run" in the run-sheet without having seen the screen.
- **Preconditions are checks, not assumptions.** The editor's old query, the stale results in both tools, the window's tabs, and the picker all need a visible check before a clip.
- **Tolerances and allowlists.** Runbook C2's "gap equals pending" failed twice and is a weak check; a script should test `failed` and `retried` at 0 and `sent` growing between two readings. C3 needs an allowlist of known restarts relative to T0.
- **Do not predict numbers.** My estimate of `sent` was low because the rate keeps ramping. A step should give an expected relationship, or a documented baseline.
- **Time sources.** Screenshot file names (to the second), Elastic's `step` (to the millisecond) and Prometheus's `timestamp()` replaced the phone clock. A script could read them and compute the gaps and relative differences, which I did by hand.
- **A check must not change what it checks.** A screenshot taken during a recording may put its own thumbnail in the video, so the numbers are collected after the take stops. Where a script can compute (the digits, the gap, the relative difference), it should.
- **Claude Code.** Read-only steps could run with the author's approval. How its permissions work was not checked (to read in the docs before relying on anything). Writes and gates stay with the author.

## 9. Findings held for the root (the note is prepared in delivery 6; sent when the author pastes it)

- **Contract placeholder table (Video 1):** `{{DIGITS_C}}` replaces `{{PCT_C}}` (the percent cannot be spoken).
- **Runbook C2:** "gap equal to pending" is a weak check (it held on one of four readings while `failed` and `retried` stayed 0); the "0 warnings" expectation needs an allowance for Prometheus's first compaction at about 3 h after the start, which logs one "Overlapping blocks found during reloadBlocks" warning (the desktop stack's nine warnings are probably the same pattern; the cause is a hypothesis).
- The first-run notes say `checkout` restarted 5 min 40 s after T0; T0 11:10:56 and 11:16:40 make it 5 min 44 s.
- `/feature/advanced` returns the flag JSON and is a candidate for a scripted check.
- Register row 53's service count (17) was a snapshot; the count was 18 during the rehearsal.
- **Across videos:** Prometheus scrapes once a minute (phase about :37) and Elastic receives each sample some time later. Any paired comparison in Video 2 or 3 should run both sides inside one scrape minute.
- **Across videos:** the three-version model (outline, normalized narration, slide-shape version) and the trainer voice, as the author set them for Video 1. The slide guidance says to use it for every slide narration; the new model says the shape rules bind only the slide-shape version.
- **Where scripts live:** the helpers `fill_placeholders.py` and the guide script are outside the repo; the root decides if a `scripts/` home is wanted.

## 10. Entry log

| Entry | Date | What |
|---|---|---|
| 1 | Oct 26, 2026 | Log created under contract section 10. Deliveries so far: (1) outline v2, committed as `3e59f34` and reviewed by the root before the authority rules; (2) run-sheet v5, the two outline reference fixes and this log, delivered as one commit. **Base of delivery 2:** the repo after the authority-rules commit, whose hash is recorded from the author's paste (entry 2). Base files: outline sha256 `0ee9ee1912f5d544ca82dc59ccb98a43bfefd946cbf2626ab342e16a3fe853b4`, run-sheet (v4) sha256 `4937bc6042a91d09083ba663e632821a7b5ee666b262955c5cca32164914c333`. **After delivery 2 is applied:** outline sha256 `e452157324cde0babdcabf206638b2c291e91f05aaab2fa785a1a2592682e4ad`, run-sheet sha256 `acbd5af85ae7394aba20b72d1a1e8f47d67dcf3a60d4fb5a51699dc859ec3215`. The commit hash of delivery 2 goes into entry 2, once the author's output is verified |
| 2 | Oct 26, 2026 | **Delivery 2 verified** from the author's pasted output: base HEAD `2890132`, tree clean (`## main...origin/main`); the base sha256 of the outline and the run-sheet matched; the zip listing matched (three files; lengths 7122, 24287, 9311); the post-apply sha256 matched; the stats matched (outline 6, run-sheet 268, 119 insertions and 155 deletions; the log 64 insertions); the safety grep printed nothing; commit `7edfc3f` (3 files changed, 183 insertions, 155 deletions, log created) and push `2890132..7edfc3f main -> main`; afterwards HEAD equals `origin/main` and the tree is clean. The author decided the opener's shape: Shape D |
| 3 | Oct 26, 2026 | **Delivery 3** (outline Slides section, run-sheet v5.1 with the two slide narrations, this log). **Base:** `7edfc3f`; base sha256: run-sheet `acbd5af85ae7394aba20b72d1a1e8f47d67dcf3a60d4fb5a51699dc859ec3215`, outline `e452157324cde0babdcabf206638b2c291e91f05aaab2fa785a1a2592682e4ad`, log `5f58a380b0563519dd176056d5392d637c5bdb16be4acae094347df800702ec8`. **After apply:** run-sheet `5024bc4fd79ed3dd2b3927f6f12632cf77029a13d2c76fe01ca8589c64734ca5`, outline `455a32b8710c4bd6efab7bedbb84f6a6c6118761c6ca2e925298ff98a0c77956` (the log cannot list its own hash). The commit hash goes into entry 4, once the author's output is verified |
| 4 | Oct 26, 2026 | **Delivery 3 verified** from the author's pasted output: base HEAD `7edfc3f`, tree clean; the base sha256 of the log, the outline and the run-sheet matched; the zip listing matched (three files; lengths 9318, 29558, 9464); the post-apply sha256 of the outline and the run-sheet matched; the stat matched (log 19, outline 4, run-sheet 74; 81 insertions, 16 deletions); the safety grep printed nothing; commit `2f2ceed` and push `7edfc3f..2f2ceed main -> main`; afterwards HEAD equals `origin/main` and the tree is clean. The author's glob also showed the contract, narrative and story hashes (`c1f1a122…`, `08b94f49…`, `91aaf262…`), identical to the copies in the earlier archive. The author approved the reveal's shape and wording |
| 5 | Oct 26, 2026 | **Delivery 4** (narrative: the approved reveal phrase, plus the stale status line and two stale on-screen notes corrected; story document regenerated; this log). **Base:** `2f2ceed`; base sha256: narrative `08b94f49a69f663b51b656d95fa8c4b13d824f324c2403d3254e10ad48e8fc00`, story `91aaf26242a5294f1e02e1c0b3aad8594b2833e17f6a730fef83485dfddb6b10`, log `e1fbb97fb7b527f00594ea5e4a43e8416f9e8cbc1d731c6fd354d914bfb03df4`. **After apply:** narrative `b364b1a488aa9750dc9f7a2bfab247c9826707c861cd17148a8607365fe98b61`, story `b5da1ab63eb50d6d3aeb413ba89fc4ebb200af9b24a4538661d47b412314e80d`. The run-sheet and the outline are not touched. The commit hash goes into entry 6, once the author's output is verified |
| 6 | Oct 26, 2026 | **Delivery 4 verified** from the author's pasted output: base HEAD `2f2ceed`, tree clean; base sha256 of the log, narrative and story matched; the zip listing matched (lengths 11692, 11876, 10716); the post-apply sha256 of the narrative and the story matched; the stat matched (log 22, narrative 13, story 119; 87 insertions, 67 deletions); the safety grep printed nothing; commit `5b21b4e` and push `2f2ceed..5b21b4e main -> main`; afterwards HEAD equals `origin/main` and the tree is clean. Confirmed again from the author's later archive: the narrative, story, outline, run-sheet and log in it are byte-identical to the delivered files |
| 7 | Oct 26, 2026 | **Guided session** (about 12:50 to 13:55 CDT): runbook Part C, the rehearsal of R1, R3 and R6, and the capture test up to S22 (sections 3, 4, 7, 8 and 9 hold the results). An unescaped pipe in one claims row of this log's table is fixed in this delivery. **Delivery 5** (the log only; the run-sheet corrections wait for the capture test). **Base:** the repo after the author's later commits, whose HEAD hash is recorded from the author's paste; base log sha256 `af82c331ac0cf286582cd7358491c11e6d47523115a3c2728318916a6f3ccd4a`. The commit hash goes into entry 8, once the author's output is verified |
| 8 | Oct 26, 2026 | **Delivery 5 verified** from the author's pasted output: base HEAD `f6cc7f2`, tree clean; the base sha256 matched (`af82c331…`); the zip listing matched (one file, 26949); the post-apply sha256 matched (`55cbf62f…`); the stat matched (98 changed lines; 91 insertions, 7 deletions); the safety grep printed nothing; commit `839a5a5` and push `f6cc7f2..839a5a5 main -> main`; afterwards HEAD equals `origin/main` and the tree is clean |
| 9 | Oct 26, 2026 | **Capture test closed and the voice settled.** The test clip, `mdls` and runbook C2 (S23 to S25); the first-compaction warning decoded. Then the trainer-voice pass: the author chose a blend, asked for more connectors and a conversational voice, said the shape restrictions apply only to the slide-shape version, and approved the full pass. The author's next step is to generate the slides and record the demos |
| 10 | Oct 26, 2026 | **Delivery 6** (narrative v2, run-sheet v6, outline v3, story, this log). **Base:** `839a5a5`; base sha256: narrative `b364b1a488aa9750dc9f7a2bfab247c9826707c861cd17148a8607365fe98b61`, run-sheet `5024bc4fd79ed3dd2b3927f6f12632cf77029a13d2c76fe01ca8589c64734ca5`, outline `455a32b8710c4bd6efab7bedbb84f6a6c6118761c6ca2e925298ff98a0c77956`, story `b5da1ab63eb50d6d3aeb413ba89fc4ebb200af9b24a4538661d47b412314e80d`, log `55cbf62fbd5a663a0aa0efacb0870db11369f4cc70fac0c9369cb4659ed2974b`. **After apply:** narrative `50eacdf5a462225e0b1a4f1c6a67765a0f07e4a3faf6d0cd972984484f1b87f7`, run-sheet `844e5d5807e6c156d3ea04a0b38333a0bc046b0a943497c460d8c82f7415e4ca`, outline `0175fc2a6e43ef884e4a2a235babc7e1c33b5ee93605e4ca76a93a7b74eca5a3`, story `25046cbbb636114bafd991a908ec7ef08c7d234f55de17b8bd2b5d443ac83dd1` (the log cannot list its own hash). The commit hash goes into entry 11, once the author's output is verified |
