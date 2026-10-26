# Module 1, Video 1 — Run-sheet (screen capture)

**Video:** Your PromQL, running in Elastic (three rungs: label selector, `rate()`, `sum by`)
**Status:** Draft v5.1, Oct 26, 2026. v5 is commit `7edfc3f`; this revision adds the two slide narrations (opening: Shape D, decided by the author Oct 26; reveal: Shape C, proposed, awaiting approval). v5 was rewritten from the approved narrative (`module1-video1-narrative.md`, v1, commit `8f6f186`, with one phrase changed on Oct 25 after the docs check). It replaces v4 (`48717fa`), whose voice-over was iteration 1 and whose screen steps were written for the desktop, Game Bar and WSL. The seven clip voice-over blocks below are copied from the narrative by script, so they match it character for character. The two slide narrations are derived from the narrative's Opening and Reveal blocks, as the contract requires. **If this sheet and the narrative differ, the narrative wins; regenerate the sheet.**
**Commands:** C1 to C6 at the end of this file, taken from the query lab (R1, R3, R6). They were verified on Oct 20 on the previous dataset. **Run C1 to C6 once as a rehearsal on the freshly reset stack before the real take** (contract, deliverable 9).
**Recording:** the laptop (macOS), which also hosts the stack. The recorder is not decided yet (macOS's built-in recording or OBS); the capture test decides it. Narration is generated afterwards, so record without audio.
**Story version for reading and review:** `module1-video1-story.md`. It is stale until it is regenerated from the narrative (contract, deliverable 6).
**Slides:** the opening and the reveal are slides with their own narrations (beats 1 and 6), written to the shapes in the log (contract, deliverable 4). The slide generator reads those two blocks.

---

## How to use this sheet

- **One machine.** The laptop runs the stack and records, so this sheet cannot sit beside the recording. Where it is displayed (a phone, a tablet, a printout, or another screen) is a decision for the capture test (see "Still open").
- **Browser:** one window, full screen, two tabs. Tab 1 = Prometheus, Tab 2 = Kibana. Full screen hides the tab strip and the address bar, so switch tabs from the keyboard (the shortcut depends on the browser; confirm it in the capture test).
- **Markers:** **▶ START** and **■ STOP** start and stop the recorder (the shortcut is filled in after the capture test). **HOLD n s** means stay still, mouse included. **✂ CUT** means stop recording, copy the command, click back into the browser, start again. Each clip joins in DaVinci Resolve.
- **Commands** are at the end of this file (C1 to C6). Copy each one off camera, before **▶ START**, because the clipboard holds one command at a time.
- **Method: PASTE (default).** Reasons: the lines are long; pasting keeps the gap between the Prometheus run and the Elastic run short, and short gaps gave much tighter agreement in the lab (an inference, not a tested rule); and code editors can auto-close brackets and quotes while you type (not verified for this editor). Switch to typing only if you decide to after the capture test.
- **Timing rule:** run Prometheus first, then Elastic **within about 15 seconds**. To make that possible, **stage the Elastic line first**: paste it into Tab 2 and don't run it, then record the Prometheus clip, then run Elastic right away. Each rung says when.
- **Holds matter.** The narration is placed over them. Give every result a 4-second hold. Some clips' narration may run longer than their footage; see "Still open".

---

## Before every take (pre-roll)

**1. The stack.** Follow `docs/reset-runbook.md`: Part B (the reset and warm-up) before a rehearsal or a take, then Part C (pre-roll: uptime and clock, remote-write counters, the `paymentFailure` flag). The commands live there and are not copied here, so there is one place to fix them. This video's state, from its contract (section 6): warm-up of at least 45 minutes, `paymentFailure` **off**, pre-roll checks passed.

**2. Browser and screen** (this video only):

1. **One window**, full screen. **Tab 1:** `http://localhost:9090`, **Table** tab selected, query box empty. **Tab 2:** Kibana, Discover, **ES|QL** mode, date picker on **Last 1 hour**, editor empty.
2. Browser zoom at about 125 to 150% (set after the capture test). Bookmarks bar hidden.
3. Notifications off (Do Not Disturb or a Focus). The recorder ready, mic off.
4. **Never show:** Prometheus Status, Configuration (it can show the remote-write URL); `.env.elastic`; any API key page; a terminal.
5. **Decide before the real take:** whether the Kibana address bar (it contains the project ID) stays hidden by full screen, or is cropped or blurred in Resolve. Confirm in the capture test clip.
6. **Keep the laptop awake** while the stack runs (runbook step A10), charger in, lid open.

---

## Voice-over conventions

- Inside each voice-over block is **spoken text only**: no stage directions, no markdown.
- **TTS spellings** (as in the narrative): `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric and label names as plain words ("traces span metrics calls total", "service name equals frontend"), symbols as words ("equals", "square brackets"). How the speech engine reads them is a listening-test question.
- Say **expression**, not "query", when claiming sameness. Say **most** or **common**, never "all". No "preview", and no statement about the feature's status. No "no changes."
- Also forbidden for this video (contract, section 5): "runs unchanged" as an absolute; "single remote-write block" (say "one remote-write block added to its config"); "I want to show you"; any percentage without the seconds between the runs; "can't be done in PromQL"; `increase()`; `topk`; claims about alerting or "real time".
- **Numbers come only from the take log.** Every number is spoken next to what it is compared with. Every agreement statement carries the gap in seconds between the two runs. No bare percentages.
- `{{LIKE_THIS}}` placeholders must all be filled before the audio is generated. The table in "After the take" says where each one comes from.
- If a number disagrees with what a sentence claims, **rewrite the sentence**; don't bend the number.

---

## Beat map

| Beat | What | Capture | Target on screen |
|---|---|---|---|
| 1 | Opening (slide) | None (slide only) | n/a |
| 2 | Setup: the same data in both places | Clip A | about 25 s |
| 3 | Rung 1: pick out some series | Clips B1, B2 | about 45 s |
| 4 | Rung 2: how fast | Clips C1, C2 | about 45 s |
| 5 | Rung 3: which service | Clips D1, D2 | about 45 s |
| 6 | The reveal (slide) | None (slide only) | n/a |

---

## Beat 1 — Opening (slide, no capture)

The narration below is derived from the narrative's Opening block. **Shape D** (three parallel steps, with a lead-in), decided with the author on Oct 26. The slide generator reads this block. Nothing to capture.

**Narration: opener slide** (127 words)

<details><summary>Show narration</summary>

```
You've spent years on your monitoring, and the real question about Elastic isn't whether it's powerful. It's whether you'd have to rebuild what you've already built.

prom-Q-L is the language you use to ask Prometheus questions about your metrics, and an expression is one line of it.

Three expressions, run twice. You probably know each one by heart, and we'll run each first in Prometheus, then in Elastic.

First, a label matcher. It narrows a metric to the series you name, such as one service.

Second, rate. It turns a counter that keeps climbing into a rate per second.

Third, sum by. It adds those rates up and keeps one row for each service.

Your job is simple: watch the expression, and try to catch it changing.
```

Claims check:
- **Shape D:** a hook, one definition sentence, a lead-in of about 25 words that carries the planted title phrase ("Three expressions, run twice"), then exactly three steps in the demo's order ("First", "Second", "Third"), then one closing sentence. The title phrase does not give away the ending.
- **What changed from the narrative's Opening block:** the fear is kept ("years on your monitoring", "rebuild what you've already built"; "all of it" and "everything" were dropped so no absolute is used). The three expressions are now named, because Shape D needs countable items, and the narrative's block named none. Scrape configs and dashboards around S-L-Os were cut for length.
- "A counter that keeps climbing" is deliberately softer than "only goes up": a counter can reset when a service restarts (Prometheus's metric types page).
- Step 3: "adds those rates up and keeps one row for each service" is what `sum by (service_name)` does (Prometheus's operators page; register row 20 for the lab).
- No numbers, no placeholders, no status statement, no "unchanged", no visual references.

</details>

---

## Beat 2 — Setup (Clip A)

1. Tab 1 in view (Prometheus, Table tab, empty box). **▶ START.** HOLD 4 s.
2. Switch to Tab 2 (Kibana Discover, ES|QL mode, Last 1 hour, empty editor). Cursor slowly under the date picker (2 s). HOLD 4 s.
3. **■ STOP.**

Nothing to verify on screen here. That both systems hold the same metrics is shown at rung 1, by the series counts and the label sets.

**Voice-over: Clip A** (99 words)

<details><summary>Show voice-over</summary>

```
Here's the board. On one screen, Prometheus, on the Table tab: where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode, which is Elastic's query language, and which has a command for running prom-Q-L. Both are looking at the same metrics, because in this demo Prometheus ships its data to Elastic with one remote-write block added to its config. Same data, two places to ask about it.

One setting to notice. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.
```

Claims check:
- "Has a command for running prom-Q-L": the PROMQL command page; register row 3. Record the retrieval date when it is re-read.
- "One remote-write block added to its config": `config/prometheus-config.yaml` holds one `remote_write:` key with one entry (URL, name, API key, queue settings), read Oct 26. That the demo's own config lacks it is inferred (the demo is not in the repo archive). Keep the wording at "added to its config".
- "Elastic's query language" describes E-S-Q-L (the Elasticsearch Query Language, per the Kibana docs). It is not a sameness claim, so the "expression, not query" rule does not apply to it.
- "Both are looking at the same metrics": **open** until the series counts and the label sets agree at rung 1.
- "Reads only the data inside that range": register row 19 (the effect was verified in lab R4; the mechanism is consistent with the docs). **Open:** re-read the command page's wording and record the retrieval date. The consequences are left for Video 3.

</details>

---

## Beat 3 — Rung 1: pick out some series (R1)

Expression: `traces_span_metrics_calls_total{service_name="frontend"}`

**Before Clip B1 (off camera):** in Tab 2, paste **C2** into the editor and **do not run it**. Then copy **C1**.

**Clip B1 (Prometheus)**
1. Tab 1. Click into the expression box. **▶ START.**
2. Paste C1. Don't execute yet. Move the cursor slowly under the metric name (2 s), then under `{service_name="frontend"}` (2 s).
3. Click **Execute**. HOLD 4 s with the "N results" line in view. **Write down N and the clock time.**
4. **■ STOP.** Go straight to Clip B2.

**Clip B2 (Elastic), C2 already staged in Tab 2**
1. Tab 2. **▶ START.**
2. Cursor slowly under the expression, the part inside the parentheses. HOLD 3 s.
3. Cursor over the wrapper, in this order, 2 s on each: `PROMQL`, `index=metrics-generic.prometheus-default`, `time=?_tend`, `calls=`.
4. Run it. HOLD 4 s with the rows in view. **Write down the clock time.**
5. If Discover shows no row count: **✂ CUT**, copy **C2b**, paste, run, and HOLD 4 s on `series = N`. **Write down N.**
6. **■ STOP.**

Notes: the rows will not appear in the same order on the two sides, and Elastic holds the labels in a `_timeseries` column. Point at the count and at one label set, not at row order.

**Rehearsal check (not filmed):** the narration says "they're the same series", which needs the label sets to match, not only the counts. Pick two series on each side and compare every label name and value, and compare the full set of label names. Record the result in the take log.

**Voice-over: Clip B1** (56 words)

<details><summary>Show voice-over</summary>

```
First move: choose which series you're looking at. Our metric is traces span metrics calls total, a counter of calls that the OpenTelemetry Collector builds from traces. Add curly braces and a label matcher, service name equals frontend, and we've picked out just that service. Run it. {{N_PROM}} series, each with its own set of labels.
```

Claims check:
- "A counter": Prometheus's metric types page (a cumulative metric that only increases, or resets to zero on restart).
- "That the OpenTelemetry Collector builds from traces": register row 45 and `docs/otel-collector-reference.md` (the `spanmetrics` connector). The demo's own Collector config is not in the archive, so this is Docs (partly).
- `{{N_PROM}}`: from the take log.

</details>

**Voice-over: Clip B2** (108 words)

<details><summary>Show voice-over</summary>

```
Now, Elastic. Look inside the parentheses. That's the expression, the same text we just ran. Everything around it is a wrapper, and here it makes just three choices. Where does this run? That's index: the data stream that holds our metrics. When? That's time: the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.

Run it. {{N_ELASTIC}} series, against {{N_PROM}}. The labels sit in a column instead of inline, but they're the same series. So, did you catch the expression changing? No. Only the wrapper is new.
```

Claims check:
- "Here it makes just three choices": the command page lists more options (index, step, buckets, start, end, time, scrape_interval, and an optional result name); we set three. Register row 36 (retrieved Oct 25). "Just three choices" is true; "only three questions" was not.
- "Evaluated once, just like the Table tab", and `?_tend` as the end of the picker's range: register row 37 (command page, retrieved Oct 25).
- "The labels sit in a column": register row 38 (a result without a cross-series aggregation returns the labels in one `_timeseries` column). The "same series" part is the rehearsal check above.
- "Only the wrapper is new": the Elastic line's expression is character for character the Prometheus text. Checked in this file by script on Oct 26 (see "Checked in this file"). Confirm again in the take that what was pasted is what ran.

</details>

---

## Beat 4 — Rung 2: how fast (R3)

Expression: `sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))`

**Before Clip C1 (off camera):** in Tab 2, clear the editor, paste **C4**, and **do not run it**. Then copy **C3**. Clear Tab 1's box.

**Clip C1 (Prometheus)**
1. Tab 1. **▶ START.**
2. Paste C3. Don't execute yet. Cursor under `[5m]` (2 s), then under `sum(` (2 s).
3. Click **Execute.** HOLD 4 s with the single value in view. **Write down the value and the clock time.**
4. **■ STOP.** Go straight to Clip C2.

**Clip C2 (Elastic), C4 already staged in Tab 2** (within about 15 s of the Prometheus run)
1. Tab 2. **▶ START.**
2. Cursor on `frontend_rate=` (2 s). Run it. HOLD 4 s with `frontend_rate` in view. **Write down the value and the clock time.**
3. **■ STOP.**

Notes: Prometheus shows `{}` for the empty label set, and Elastic returns only `frontend_rate` and `step`. Don't point this out unless the narration needs it.

**Voice-over: Clip C1** (92 words)

<details><summary>Show voice-over</summary>

```
Now, a series on its own is only half the story. A counter just climbs. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast. That's what rate is for. Hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Run it. {{PROM_VALUE}}.
```

Claims check:
- Counter definition: Prometheus's metric types page. "What you want to know is how fast" is a judgment.
- "Returns the per-second average rate of increase": Prometheus's documentation for `rate()`; Elastic's range vector functions page uses the same wording (glossary).
- The number: from the take log.

</details>

**Voice-over: Clip C2** (43 words)

<details><summary>Show voice-over</summary>

```
In Elastic: same expression, same wrapper. The only thing we touch is the name of the answer, now frontend rate. Run it. {{ELASTIC_VALUE}}, against {{PROM_VALUE}}. The two runs were about {{SECONDS_C}} seconds apart, and the values are within {{PCT_C}} percent of each other.
```

Claims check:
- "The only thing we touch is the name of the answer": C2 and C4 differ only in the result name and the expression's own text. Checked in this file by script on Oct 26.
- Values and the gap in seconds: from the take log.
- "Within {{PCT_C}} percent" holds only if the difference is small (about 1 percent or less). **If it is larger, rewrite the sentence** instead of filling the template. Labs R3 and R6 saw gaps from about 2.5e-10 (relative) to a few percent, so the spoken form of a very small percent is also a decision (handoff section 8).
- Keeping `[5m]` is deliberate (register row 39). Say nothing that contradicts Elastic's advice to omit range selectors; Video 3 explains it.

</details>

---

## Beat 5 — Rung 3: which service (R6)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`

**Before Clip D1 (off camera):** in Tab 2, clear the editor, paste **C6**, and **do not run it**. Then copy **C5**. Clear Tab 1's box.

**Clip D1 (Prometheus)**
1. Tab 1. **▶ START.**
2. Paste C5. Don't execute yet. Cursor under `sum by (service_name)` (3 s).
3. Click **Execute.** HOLD 4 s. The table has one row per service. **Write down the row count and the clock time.**
4. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
5. **■ STOP.** Go straight to Clip D2.

**Clip D2 (Elastic), C6 already staged in Tab 2** (within about 15 s of the Prometheus run)
1. Tab 2. **▶ START.** Run it. HOLD 4 s. **Write down the row count and the clock time.**
2. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
3. **■ STOP.**

Notes:
- Point at **frontend** (or another busy service), not at a low-traffic one. In the lab, low-traffic services differed by up to about 13%, which looked like timing noise (an inference).
- Neither side's rows are guaranteed to be in the same order. Find the frontend row on each.
- Zero-traffic services show 0 on both sides.
- **C6 has no `| SORT service_name`.** The lab ran this line with the sort appended, and R7 and R8 ran without one, but this exact line has not been run. It is part of the rehearsal.

**Voice-over: Clip D1** (60 words)

<details><summary>Show voice-over</summary>

```
One number for the whole frontend is useful, but it's rarely the question you actually have. The question is which service. So the third move keeps a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.
```

Claims check:
- `sum by`: aggregation operators combine one instant vector into fewer elements, and the `by` clause preserves the named label (Prometheus's operators page).
- "It's rarely the question you actually have" is a judgment about the audience.
- `{{ROWS_PROM}}` and `{{PROM_FRONTEND}}`: from the take log.

</details>

**Voice-over: Clip D2** (15 words)

<details><summary>Show voice-over</summary>

```
Elastic, same again. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}}, about {{SECONDS_D}} seconds apart.
```

Claims check:
- "The same expression inside the wrapper": checked in this file by script on Oct 26 (C6 against C5).
- Values and the gap in seconds: from the take log. This block states no percentage, so `{{PCT_D}}` is retired.
- The lab's grouped `rate()` agreement is register row 20 (busy services within about 6%, small ones within about 13%). It is evidence, not script.
- C6 (without the sort) is still to be rehearsed.

</details>

---

## Beat 6 — The reveal (slide, no capture)

The narration below is derived from the narrative's Reveal block. **Shape C** (peer cards), **proposed** on Oct 26 and awaiting the author's approval, together with one wording change (see the claims check). The slide generator reads this block. Nothing to capture.

**Narration: recap slide** (130 words)

<details><summary>Show narration</summary>

```
Three expressions, and the expression never changed. What changed is the wrapper: everything around the expression when you run it in Elastic, which is the command, its options and a result name.

Here, the wrapper makes just three choices.

Where it runs. The index option names the data to read.

When it's evaluated. The time option sets the moment, here the end of the date picker's range.

What the answer is called. A result name labels the value that comes back.

There's also a catch. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges.

So take an expression you use every day, drop it between the parentheses, and most of the time, that's all it takes.
```

Claims check:
- **Shape C:** a hook, one definition sentence (the wrapper), a scoping sentence that carries the planted title phrase ("Here, the wrapper makes just three choices"), three peer cards (where it runs, when it's evaluated, what the answer is called), one signposted caveat ("There's also a catch"), then one closing sentence. No ordinals and no dependency language, as Shape C requires.
- **Proposed wording change, needs the author's approval:** the narrative says "now you know all of it". This block says "Here, the wrapper makes just three choices" instead. The command has more options than the three we set (register row 36), so "all of it" is an absolute; "here" and "just three" are scoped and match the Clip B2 voice-over. If approved, I update the narrative's line in a later delivery so the two agree; until then the narrative keeps its approved text.
- "The expression never changed": the same claim as the narrative. The text check in this file shows the Elastic line's expression is character for character the Prometheus text; confirm in the take.
- Cards: the `index` option names the data to read, and `?_tend` is the end of the date picker's range (register rows 36 and 37, retrieved Oct 25). The result name labels what comes back (the result column, as in C2 and C4).
- "Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges" keeps the narrative's strength and Elastic's own framing (register row 1 and the limitations rows). It states nothing about the feature's status. Re-read the limitations page and record the retrieval date before the take.
- The narrative's pointer to Video 2 ("which services are failing, and how often") is not in this block: it was a courtesy that could be cut without loss, and the slide holds one idea. It can go in the voice-over at assembly if you want it.

</details>

---

## After the take

1. Run the counters command again (runbook Part C, command 2). `failed` should be unchanged from before the take.
2. Fill in the take log below and paste it back to me.
3. Rename each clip right away, for example `v1-B1-r1-prometheus` plus the recorder's file extension.

### Take log (fill in)

| Beat | Prometheus (value or count, time) | Elastic (value or count, time) | Seconds between runs | Retakes and notes |
|---|---|---|---|---|
| 3 (R1) | | | | |
| 4 (R3) | | | | |
| 5 (R6, frontend row) | | | | |

### Placeholders to fill from the take log

| Placeholder | Meaning | Source |
|---|---|---|
| `{{N_PROM}}`, `{{N_ELASTIC}}` | Rung 1 series counts | Clips B1, B2 (Elastic: Discover's row count, or `series` from C2b) |
| `{{PROM_VALUE}}`, `{{ELASTIC_VALUE}}` | Frontend calls per second, rung 2 | Clips C1, C2 |
| `{{SECONDS_C}}`, `{{PCT_C}}` | Seconds between the runs, and the relative difference in percent, rung 2 | Take log; computed |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Row counts, rung 3 | Clips D1, D2 |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | Clips D1, D2 |
| `{{SECONDS_D}}` | Seconds between the runs, rung 3 | Take log |

`{{PCT_D}}` is retired: the narrative does not use it.

---

## Checked in this file (Oct 26, by script; text only, no stack)

- Each of the seven voice-over blocks above is identical to the matching block in the narrative, and the word counts in the headings were computed from them (placeholders count as one word each).
- The placeholders used in the seven blocks are exactly the eleven in the table above.
- In C2, C4 and C6, the text between the parentheses is character for character the text of C1, C3 and C5. C2 and C4 differ only in the result name and the expression.
- C1, C3 and C5 match the lab's R1, R3 and R6 Prometheus lines. C2, C4 and C6 match the lab's Elastic lines, except that C6 drops the lab's `| SORT service_name`.

- The two slide narrations were checked against the guidance by script on Oct 26: word counts (127 and 130, inside the 90 to 180 range), no sentence over 150 characters, no number or placeholder, and none of the forbidden words. The only watch-list hit is "never changed" in the recap, which is the narrative's own claim.

This checks the text of the commands and the narrations. It does not show that the commands run.

---

## If something goes wrong

- **An error in Elastic:** don't edit the command. Stop, copy the exact error text, and send it to me. Errors are findings.
- **Empty result in Elastic:** check the picker says **Last 1 hour** and the stack uptime. Try again.
- **Values differ more than a few percent:** rerun both sides within 15 s of each other, Prometheus first.
- **Prometheus shows no data:** check the stack is running, then the counters (runbook Part C).

---

## Copy-paste commands

**C1** — Prometheus, rung 1
```
traces_span_metrics_calls_total{service_name="frontend"}
```

**C2** — Elastic, rung 1
```
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name="frontend"})
```

**C2b** — Elastic, rung 1, only if Discover shows no row count
```
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name="frontend"}) | STATS series = COUNT(*)
```

**C3** — Prometheus, rung 2
```
sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))
```

**C4** — Elastic, rung 2
```
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_rate=(sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])))
```

**C5** — Prometheus, rung 3
```
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

**C6** — Elastic, rung 3 (rehearse: the lab's version had `| SORT service_name` appended)
```
PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```

---

## Still open

- **Recorder** (macOS's built-in recording or OBS), whether it captures the cursor, text legibility, resolution, and browser zoom: the capture test (contract, deliverable 8). The test clip also shows whether recording load affects the stack: re-check the counters afterwards.
- **Where this sheet is displayed during a take** (one machine).
- **Footage length against narration length.** At 150 spoken words a minute (an assumption, not a measurement of the speech engine), the clip blocks run about: Clip A 40 s (target on screen about 25 s), B1 plus B2 about 65 s (45 s), C1 plus C2 about 54 s (45 s), D1 plus D2 about 30 s (45 s). The spoken numbers add a little. So A and rung 1 could run longer than their footage unless holds are longer or the editor freezes a frame. A test render with the rehearsal's numbers would measure each clip before the take.
- **How to read the seconds between the runs:** a clock kept in view, or another source. Decide at the capture test.
- **Type or paste:** default is paste. Decide after the capture test.
- **Kibana address bar:** hidden by full screen, or crop or blur it. Confirm in the test clip.
- **The reveal's "now you know all of it"** (Beat 6): replaced in the recap narration by "Here, the wrapper makes just three choices". Waiting for the author's approval; the narrative line changes only if approved.
- **The reveal's shape** (Shape C): proposed, waiting for the author's approval with the narration.
- **Copy-across idea for rung 1** (copy the expression out of Prometheus's box and paste it between the parentheses of a staged Elastic skeleton, so the same text visibly moves across). Not adopted; it would change the rung 1 steps only.
- **Grafana as a second data source** is untested, so nothing in this video may imply it.
