# Module 1, Video 1 — Run-sheet (screen capture)

**Video:** Your PromQL, running in Elastic (three expressions: label selector, `rate()`, `sum by`)
**Status:** Draft v6, Oct 26, 2026. v5.1 is commit `2f2ceed`. This revision does four things. (1) The nine spoken blocks are copied by script from narrative v2, the trainer-voice pass the author approved on Oct 26 (`module1-video1-narrative.md`); if this sheet and the narrative differ, the narrative wins and this sheet is regenerated. (2) The slide-shape versions for beats 1 and 6 are re-derived from that text, as separate artifacts for the slide toolkit. (3) The screen steps are corrected from the rehearsal and the capture test of Oct 26 (the real control names, shortcuts, staging, the recorder and the timing). (4) `{{PCT_C}}` is replaced by `{{DIGITS_C}}`. The decisions, results and evidence are in `module1-video1-log.md`.
**Commands:** C1 to C6 at the end of this file, from the query lab (R1, R3, R6). All six ran on Oct 26 on the rehearsal stack.
**Recording:** the laptop (macOS), with the built-in recorder (Command+Shift+5), settings below. Record without audio; the narration is generated afterwards, with the take's numbers.
**Story document for reading and review:** `module1-video1-story.md`, generated from the narrative.

---

## How to use this sheet

- **One machine.** The laptop runs the stack and records. Where this sheet is displayed during a take, and whether the narration plays in the background as a pacing guide, are the author's choice; the author is experimenting.
- **Browser.** Chrome, one window with two tabs in a group: **Tab 1** Prometheus (`http://localhost:9090`, **Table** view), **Tab 2** Kibana Discover (ES|QL mode, date picker on **Last 1 hour**). Zoom is **125%** on both (Chrome keeps it per site). Full screen with **Control+Command+F**. Switch tabs with **Control+Tab**. Each switch briefly flashes the tab strip and toolbar; it is cut in DaVinci Resolve (author's decision, Oct 26).
- **Controls.** Prometheus: **Execute**. Discover: **Search** or **Cmd+Enter** (the shortcut keeps the cursor in the editor). Never move the cursor to the very top edge: it reveals Chrome's toolbar.
- **Recorder (decided Oct 26).** Command+Shift+5, then Options: save to `~/Movies/v1-capture`, microphone **None**, Show Mouse Clicks **off**, Timer **5 seconds**; choose **Record Entire Screen**, then **Record**. Stop with **Command+Control+Esc**. Keep "Include System Audio" off if your macOS offers it. The test clip: `.mov`, H.264, 3456 × 2234, about 6 Mbit/s, with no audio. Text was easy to read at 125%.
- **Highlights are added in post.** Parts of a query will be highlighted in Resolve, so the cursor underlines in the steps are optional. A slow cursor over a part is still a useful cue.
- **Method: PASTE.** Copy each command from the end of this file, off camera, before the take.
- **One continuous take per rung.** Record each pair (Prometheus, then Elastic) as one recording, like the Oct 26 test clip (about 25 to 35 seconds for a whole rung). The narration blocks stay separate; you cut the footage in Resolve. This keeps the gap between the two runs short (see "Timing"). It is the recommended default; adjust it after your own experiments.
- **No screenshots while recording.** The macOS floating thumbnail may appear on screen, and so in the video. Collect every number after you stop; the results stay on screen (see "After the take").

---

## Before every take (pre-roll)

**1. The stack.** `docs/shared/operations/reset-runbook.md`: **Part B** (the reset and warm-up; a fresh reset and at least 45 minutes of warm-up) then **Part C** (pre-roll). The commands live there. This video's state: warm-up of at least 45 minutes, `paymentFailure` **off**, pre-roll checks passed. Two notes from the Oct 26 session:
- C2's last number counts warning and error lines. Prometheus's first compaction, about **3 hours** after the stack starts, logs one "Overlapping blocks found during reloadBlocks" warning (seen at T+3.0 h; probably caused by the 30-minute out-of-order window, which was not verified). It does not affect remote write. A take within 3 hours of the start will not see it.
- C2's "gap equals pending" is a weak check: it failed on three of four readings with `failed` and `retried` at 0. Trust `failed 0`, `retried 0`, and `sent` growing.

**2. Browser and screen** (this video only):
1. One Chrome window, two tabs, as above, at 125%, in full screen. Do Not Disturb or a Focus on. Notifications off.
2. **Never show:** Prometheus Status, Configuration (it can show the remote-write URL); `.env.elastic`; any API key page; a terminal.
3. The frame includes Kibana's whole window: the left navigation, the "My Observability project" breadcrumb, the "AI Agent" button, your avatar, and two small blue badges. Accepted; crop or blur in post if you want.
4. Keep the laptop awake while the stack runs (runbook step A10).

**3. Staging before each rung** (proposed on Oct 26; judge it on the first take):
- **Prometheus:** the ⋮ **Query options** menu, then **Remove query**, then **+ Add query**. That leaves an empty box and "No data queried yet".
- **Discover:** run a zero-row query, `FROM metrics-generic.prometheus-default | LIMIT 0`, with Cmd+Enter. Then clear the editor and paste the rung's Elastic line without running it. The results area shows "No results match your search criteria" until you run it. That panel can look like the line's own answer, so check it in the first take.

---

## Voice-over conventions

- Inside each block is **spoken text only**: no stage directions, no markdown.
- **Voice:** a professional trainer who is an SME speaking to peers: conversational authority, contractions, direct address, signposts, one idea per sentence, claims stated precisely and then shown. No hype, and no game language.
- **TTS spellings:** `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, symbols as words. How the speech engine reads them is a listening-test question.
- Say **expression**, not "query", when claiming sameness. Say **most** or **everyday**, never "all". No statement about the feature's status. Also forbidden: "runs unchanged" as an absolute; "single remote-write block" (say "one remote-write block added to its config"); any bare percentage; "can't be done in PromQL"; `increase()`; `topk`; claims about alerting or "real time".
- **Numbers come only from the take.** Counts are whole numbers. Rates are spoken to three decimals. Seconds are whole numbers ("about 8"). `{{DIGITS_C}}` is computed from the full-precision values (see "After the take"). The spoken form of numbers is still open (`docs/shared/decisions.md`, section 8); this is a proposal.
- `{{LIKE_THIS}}` placeholders are all filled before the audio is generated.
- If a number disagrees with a sentence, **rewrite the sentence**; don't bend the number.

---

## Beat map

| Beat | What | Footage | Spoken (estimate) |
|---|---|---|---|
| 1 | Opening (slide) | none | about 69 s |
| 2 | Setup | one take, no query | about 45 s |
| 3 | Rung 1: select series | one take: Prometheus, then Elastic | about 75 s |
| 4 | Rung 2: how fast | one take: Prometheus, then Elastic | about 60 s |
| 5 | Rung 3: which service | one take: Prometheus, then Elastic | about 38 s |
| 6 | The reveal (slide) | none | about 76 s |

The estimates are word counts at an assumed 150 words a minute, not measured audio. The nine blocks total about 6 minutes of speech. There is no hard limit.

---

## Beat 1 — Opening (slide, no capture)

Two versions of the same idea. The **spoken** text is what an instructor or the speech engine reads. The **slide version** is a separate artifact for the slide toolkit (Shape A, the toolkit's own rules), derived from the spoken text. Nothing to capture.

**Narration: opener slide** (173 words)

<details><summary>Show narration</summary>

```
You've spent years on your Prometheus setup, so the real question about Elastic isn't whether it's capable. It's whether you'd have to rebuild what you've already built. You've got scrape configs tuned to your infrastructure, dashboards built around your S-L-Os, and prom-Q-L you could write in your sleep.

So here's what this video is for. By the end, you'll be able to recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression.

To get there, we'll take three expressions you probably use every day and run each one twice, first in Prometheus, then in Elastic, against the same data. Between them, we'll select series with a label matcher, take the rate of a counter, and aggregate with sum by.

I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new. And at the end, we'll be plain about what doesn't carry over.

Now, don't take my word for the result. As each pair runs, watch two things: whether the expression changes, and whether the numbers agree.
```

Claims check:
- The objective echoes the learning objective (LO1) in its own words: recognize which everyday prom-Q-L expressions run in Elastic using the same expression.
- "Most" and "everyday" scope the claim; the closing "plain about what doesn't carry over" matches the recap and Elastic's own "most, not all" framing (register row 1).
- No definition of prom-Q-L, on purpose: this audience writes it daily.
- No numbers, no percentages, no feature-status statement.

</details>

**Slide version: opener** (92 words)

<details><summary>Show slide version</summary>

```
You've spent years on your Prometheus setup, so the real question about Elastic isn't whether it's capable. It's whether you'd have to rebuild what you've already built.

Three expressions, run twice: first in Prometheus, then in Elastic, against the same data.

By the end, you'll be able to recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression.

Select series with a label matcher. Take the rate of a counter. Aggregate with sum by.

Don't take my word for the result: watch the expression, and watch the numbers.
```

Notes: Shape A (a skills list). A hook with a contrast, the title phrase "Three expressions, run twice", the objective, three verb-first items (34, 26 and 21 characters), one closing sentence; no sentence over 150 characters (checked by script). It is the staccato version on purpose: the toolkit needs short beats. No "Welcome to:" line, because the outline treats this as the opening of Module 1; if it opens the whole course, the guidance wants that line first. How the toolkit times its reveals against the audio is not known here.

</details>

---

## Beat 2 — Setup (take A)

Staging: Tab 1 with an empty box and "No data queried yet"; Tab 2 with the empty-state panel (run the zero-row query first) and an empty editor, picker on Last 1 hour.

1. Tab 1 in view. Press Command+Shift+5, **Record**, and wait out the 5-second timer. Hold still for 4 seconds.
2. **Control+Tab** to Tab 2. Move the cursor slowly under the date picker (2 s). Hold for 4 seconds.
3. Stop with Command+Control+Esc.

The tab switch happens while recording, so the tab strip flashes here; cut it in post, or record Prometheus and Discover as two short takes.

**Voice-over: Clip A** (113 words)

<details><summary>Show voice-over</summary>

```
Let's look at what we're working with. On one screen, we have Prometheus, on the Table tab, which is where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode. E-S-Q-L is Elastic's query language, and it has a command for running prom-Q-L.

Both are looking at the same metrics. In this demo, Prometheus sends its data to Elastic with one remote-write block added to its config, so it's the same data, with two places to ask about it.

One setting to notice before we start. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.
```

Claims check:
- "Elastic's query language" describes E-S-Q-L, not sameness, so the "expression, not query" rule does not apply to it. "Has a command for running prom-Q-L": the PROMQL command page (register row 3); record the retrieval date when it is re-read.
- "One remote-write block added to its config": `config/prometheus-config.yaml` holds one `remote_write:` key with one entry (read Oct 26). That the demo's own config lacks it is inferred. Keep the wording at "added to its config".
- "Both are looking at the same metrics": the rung 1 counts agreed (41 and 41) and the label names matched on one sampled row (Oct 26); label values are not yet compared.
- "Reads only the data inside that range": register row 19 (the effect was seen in lab R4; the mechanism is consistent with the docs). **Open:** re-read the command page's wording and record the retrieval date.

</details>

---

## Beat 3 — Rung 1: select series (one take: B1, then B2)

Expression: `traces_span_metrics_calls_total{service_name="frontend"}`

**Staging (off camera).** Tab 1: Remove query, then Add query. Tab 2: run the zero-row query, clear the editor, paste **C2**, don't run it. Copy **C1**. Start the take so the Prometheus click lands in the window in "Timing" (rung 1: between :40 and :56 of a minute).

1. Tab 1. Start recording; wait out the timer. Click the expression box and paste **C1**. Optional cue: a slow cursor under the metric name, then under the matcher.
2. At "Let's run it" in the B1 narration, click **Execute**. Hold for 4 seconds with "Result series: N" in view.
3. **Control+Tab** to Tab 2. Optional cue: a slow cursor under the expression inside the parentheses, then over `PROMQL`, `index=metrics-generic.prometheus-default`, `time=?_tend` and `calls=`.
4. At "Let's run it" in the B2 narration, press **Cmd+Enter** (or click **Search**). Hold for 4 seconds with "N results" in view.
5. Stop with Command+Control+Esc. Then collect the numbers (see "After the take").

Notes: Elastic's rows are not in the same order as Prometheus's, and the labels sit in a `_timeseries` column that the grid cuts off after `collector_instance_id`; the whole label list shows in the expanded row. Point at the count and at one label set, not at row order.

**Voice-over: Clip B1** (68 words)

<details><summary>Show voice-over</summary>

```
Let's start with the first expression: choosing which series we're looking at. The metric is traces span metrics calls total. It's a counter of calls, and the OpenTelemetry Collector builds it from traces. To narrow it down, we add curly braces and a label matcher: service name equals frontend. That picks out just the frontend service. Let's run it. {{N_PROM}} series, each with its own set of labels.
```

Claims check:
- "A counter": Prometheus's metric types page. "Builds it from traces": register row 45 and `docs/shared/otel-collector-reference.md` (the `spanmetrics` connector). The demo's own Collector config is not in the archive, so this is Docs, partly.
- `{{N_PROM}}`: from "Result series: N" in the take.

</details>

**Voice-over: Clip B2** (119 words)

<details><summary>Show voice-over</summary>

```
Now, the same thing in Elastic. Look at what's inside the parentheses. That's the expression, the same text we just ran in Prometheus. Everything around it is a wrapper, and here the wrapper makes just three choices. Where does this run? That's index, the data stream that holds our metrics. When? That's time, the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.

Let's run it. {{N_ELASTIC}} series, against {{N_PROM}} in Prometheus. The labels sit in a column here instead of inline, but they're the same series. So, did the expression change? No. What's new is the wrapper.
```

Claims check:
- "Here the wrapper makes just three choices": the command page lists more options (index, step, buckets, start, end, time, scrape_interval, and an optional result name); we set three. Register row 36, retrieved Oct 25. "Just three choices" is true; "only three questions" was not.
- "Evaluated once, just like the Table tab", and `?_tend` as the end of the picker's range: register row 37, retrieved Oct 25. Elastic's `step` is the run time (three readings on Oct 26).
- "The labels sit in a column": register row 38; the grid shows `_timeseries` as JSON, cut off. "The same series": counts and label names agree (Oct 26); values are not yet compared.
- "What's new is the wrapper": the Elastic line's expression is character for character the Prometheus text (checked in this file by script on Oct 26). Confirm in the take that what was pasted is what ran.
- `{{N_ELASTIC}}`: from "N results" in the take.

</details>

---

## Beat 4 — Rung 2: how fast (one take: C1, then C2)

Expression: `sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))`

**Staging (off camera).** As for rung 1, with **C4** staged in Tab 2 and **C3** on the clipboard. Window in "Timing" (rung 2: from :40 of a minute until about :20 of the next).

1. Tab 1. Start recording; wait out the timer. Paste **C3**. Optional cue: the cursor under `[5m]`, then under `sum(`.
2. At "Let's run it" in the C1 narration, click **Execute**. Hold for 4 seconds with the single value in view.
3. **Control+Tab** to Tab 2. Optional cue: the cursor on `frontend_rate=`.
4. At "Let's run it" in the C2 narration, press **Cmd+Enter**. Hold for 4 seconds with `frontend_rate` in view.
5. Stop with Command+Control+Esc. Then collect the numbers.

Notes: Prometheus shows `{}` for the empty label set; Elastic returns only `frontend_rate` and `step`.

**Voice-over: Clip C1** (100 words)

<details><summary>Show voice-over</summary>

```
Now for the second expression. A series on its own is only half the story, because a counter keeps climbing. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast, and that's what rate is for. You hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Let's run it. {{PROM_VALUE}}.
```

Claims check:
- "A counter keeps climbing": a counter is cumulative and resets to zero on restart (Prometheus's metric types page), which is why the wording is "keeps", not "only goes up".
- "Returns the per-second average rate of increase": Prometheus's documentation for `rate()`; Elastic's range vector functions page uses the same wording.
- `{{PROM_VALUE}}`: from the take.

</details>

**Voice-over: Clip C2** (51 words)

<details><summary>Show voice-over</summary>

```
In Elastic, it's the same expression inside the same wrapper. The one thing we change is the name of the answer, which is now frontend rate. Let's run it. {{ELASTIC_VALUE}} in Elastic, against {{PROM_VALUE}} in Prometheus. The two runs were about {{SECONDS_C}} seconds apart, and the values agree to {{DIGITS_C}} digits.
```

Claims check:
- "The one thing we change is the name of the answer": C2 and C4 differ only in the result name and the expression's own text (checked in this file by script on Oct 26).
- "Agree to `{{DIGITS_C}}` digits": the leading significant digits the two full-precision values share. In the rehearsal, 14.995958299652495 against 14.995958290594942 share ten, a relative difference of 6.0e-10. If the take shares few digits (under about four), rewrite the sentence.
- The values and the gap come from the take. Keeping `[5m]` is deliberate (register row 39): say nothing that contradicts Elastic's advice to omit range selectors; Video 3 explains it.

</details>

---

## Beat 5 — Rung 3: which service (one take: D1, then D2)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`

**Staging (off camera).** As before, with **C6** staged in Tab 2 and **C5** on the clipboard. Window in "Timing" (rung 3: from :40 of a minute until about :25 of the next).

1. Tab 1. Start recording; wait out the timer. Paste **C5**. Optional cue: the cursor under `sum by (service_name)`.
2. At "Let's run it" in the D1 narration, click **Execute**. Hold for 4 seconds. The table has one row per service. Rest the cursor on the **frontend** row for 3 seconds.
3. **Control+Tab** to Tab 2.
4. At "Let's run it" in the D2 narration, press **Cmd+Enter**. Hold for 4 seconds, then rest the cursor on the **frontend** row for 3 seconds.
5. Stop with Command+Control+Esc. Then collect the numbers.

Notes:
- Point at **frontend**, not at a low-traffic service. Neither side sorts: on Oct 26 frontend was the ninth row in Prometheus and the eleventh in Elastic, so find it on each side.
- **C6 has no `| SORT service_name`.** It ran as written on Oct 26 and returned all 18 rows.

**Voice-over: Clip D1** (65 words)

<details><summary>Show voice-over</summary>

```
One number for the whole frontend is useful, but it's rarely the question you actually have. Usually, you want to know which service. So for the third expression, we keep a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Let's run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.
```

Claims check:
- `sum by` adds up the rest and keeps the named label (Prometheus's operators page). "Rarely the question you actually have" is a judgment about the audience.
- `{{ROWS_PROM}}` and `{{PROM_FRONTEND}}`: from the take. "Result series: N" gives the rows.

</details>

**Voice-over: Clip D2** (31 words)

<details><summary>Show voice-over</summary>

```
And in Elastic, the same expression inside the same wrapper. Let's run it. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus. These two runs were about {{SECONDS_D}} seconds apart.
```

Claims check:
- "The same expression inside the same wrapper": checked in this file by script on Oct 26 (C6 against C5).
- The values and the gap come from the take. This block states no agreement and no percentage. On Oct 26 the 14 comparable rows all differed by 2.543e-10 relative.

</details>

---

## Beat 6 — The reveal (slide, no capture)

The same two versions. Nothing to capture.

**Narration: recap slide** (189 words)

<details><summary>Show narration</summary>

```
Let's come back to what we set out to do: recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression. For these three, you've seen it. The label matcher, the rate over a counter, and the sum by all ran as the same text in Prometheus and in Elastic, and the numbers agreed.

What changed is the wrapper, which is everything around the expression when you run it in Elastic: the command, its options, and a result name. Here, it made just three choices. Where it runs: the index option names the data to read. When it's evaluated: the time option sets the moment, here the end of the date picker's range. And what the answer is called: a result name labels the value that comes back.

There's one caution, because we said we'd be plain about it. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges. So take an expression you use every day, drop it between the parentheses, and try it. Most of the time, that's all it takes.
```

Claims check:
- The recap closes the loop on the objective in its own words. "The numbers agreed" depends on the take: if a take disagrees, that sentence changes.
- "Here, it made just three choices" matches Clip B2 (register row 36). The `index` option names the data to read, and `?_tend` is the end of the picker's range (register rows 36 and 37).
- "Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges" keeps the narrative's strength and Elastic's own framing (register row 1). It states nothing about the feature's status. Re-read the limitations page and record the retrieval date before the take.
- No pointer to Video 2 in this block. Add it at assembly only if wanted, and only once Video 2's through-line is approved.

</details>

**Slide version: recap** (131 words)

<details><summary>Show slide version</summary>

```
In all three pairs, the expression didn't change. What changed is the wrapper: everything around the expression when you run it in Elastic, which is the command, its options and a result name. Here, the wrapper makes just three choices.

Where it runs. The index option names the data to read.

When it's evaluated. The time option sets the moment, here the end of the date picker's range.

What the answer is called. A result name labels the value that comes back.

There's also a catch. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges.

So take an expression you use every day, drop it between the parentheses, and most of the time, that's all it takes.
```

Notes: Shape C (peer cards): a hook, a one-sentence definition of the wrapper, the planted title phrase ("Here, the wrapper makes just three choices"), three cards (where it runs, when it's evaluated, what the answer is called), one signposted caveat, one closing sentence. No ordinals and no dependency language. It says "the expression didn't change" about these three runs; confirm in the take.

</details>

---

## Timing: keep each pair inside one scrape minute

Prometheus scrapes once a minute (`scrape_interval: 60s`); on Oct 26 the new samples landed at about :37 of each minute. Elastic receives each sample some time later (not measured; under about 28 s in rung 3). A pair of runs agreed to better than 1e-9 on Oct 26 whenever both fell between a new sample and the next one. The Prometheus click should come after about **:40**, and the Elastic click before about **:35** of the next minute, so both use the same newest sample. This is a hypothesis that fits all three timed pairs; a deliberate straddle would test it.

If the narration plays straight through as a pacing guide, the estimates (word counts at 150 words a minute, not measured) are:

| Rung | Prometheus click | Elastic click | Gap | Prometheus click must land |
|---|---|---|---|---|
| 1 (B1, B2) | about 22 s into the take | about 61 s | about 38 s | between :40 and :56 of a minute |
| 2 (C1, C2) | about 38 s | about 50 s | about 12 s | from :40 until about :23 of the next minute |
| 3 (D1, D2) | about 21 s | about 30 s | about 9 s | from :40 until about :26 of the next minute |

Rung 1 is the tight one (a window of about 17 seconds). Replace these estimates with the real offsets of your rendered audio. Start the take so that its offset (the 5-second timer included) puts the Prometheus click in the window.

---

## After the take

Collect the numbers once you have stopped; the results stay on screen.

1. **Prometheus tab:** a screenshot of the result (Result series, the value, or the frontend row).
2. **Elastic tab:** a screenshot (the "N results" line, the value) and the JSON of the result, as in the rehearsal, for full precision and the `step` time.
3. **The gap in seconds:** read it from the footage in Resolve, as the time between the Execute click and the Search click in the continuous take. Elastic's `step` gives the absolute time of the Elastic run as a check.
4. Run the counters command again (runbook Part C, command 2). `failed` and `retried` should still be 0.
5. Fill in the take log, then the placeholders (the helper `fill_placeholders.py`, outside the repo, computes `{{DIGITS_C}}` and fills the nine blocks from a small values file).
6. Rename each take: `v1-A`, `v1-rung1`, `v1-rung2`, `v1-rung3` plus the recorder's extension.

### Take log (fill in)

| Beat | Prometheus (value or count) | Elastic (value or count) | Gap (s) | Elastic step | Notes |
|---|---|---|---|---|---|
| 3 (rung 1) | | | | | |
| 4 (rung 2) | | | | | |
| 5 (rung 3, frontend row) | | | | | |

### Placeholders to fill

| Placeholder | Meaning | Source and form |
|---|---|---|
| `{{N_PROM}}` | Rung 1 series count, Prometheus | "Result series: N"; whole number |
| `{{N_ELASTIC}}` | Rung 1 series count, Elastic | "N results"; whole number |
| `{{PROM_VALUE}}`, `{{ELASTIC_VALUE}}` | Frontend calls per second, rung 2 | The values; three decimals |
| `{{SECONDS_C}}` | Seconds between the rung 2 runs | The gap; whole seconds |
| `{{DIGITS_C}}` | Leading significant digits the two rung 2 values share | Computed from the full-precision values |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Rung 3 row counts | "Result series: N", "N results" |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | The values; three decimals |
| `{{SECONDS_D}}` | Seconds between the rung 3 runs | The gap; whole seconds |

`{{PCT_C}}` is retired.

---

## Checked in this file (Oct 26, by script; text only)

- The seven clip blocks and the two spoken slide blocks above are identical to the nine blocks of narrative v2, and the word counts in the headings were computed from them (placeholders count as one word each).
- The placeholders used are exactly the eleven in the table above.
- In C2, C4 and C6, the text between the parentheses is character for character the text of C1, C3 and C5. C2 and C4 differ only in the result name and the expression.
- C1 to C6 appear verbatim in the query lab, except that C6 drops the lab's sort.
- The two slide versions were checked against the toolkit's mechanical rules: no sentence over 150 characters, the items' lengths, no number or placeholder, and none of the forbidden words.

This checks the text. It does not show that the commands run; they ran on Oct 26 on the rehearsal stack.

---

## If something goes wrong

- **An error in Elastic:** don't edit the command. Stop, copy the exact error text, and send it to me. Errors are findings.
- **Elastic shows the empty-state panel after a run:** check the picker says **Last 1 hour** and the stack uptime.
- **The two values differ at the third or fourth digit:** a new sample probably landed between your two runs. Retake the pair inside one scrape minute (see "Timing").
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

**C6** — Elastic, rung 3 (no sort; ran as written on Oct 26)
```
PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```

---

## Still open

- **Where this sheet is displayed** during a take, and whether the narration plays in the background (the author's experiments).
- **The spoken form of numbers** (three decimals, whole counts, whole seconds): a proposal; `docs/shared/decisions.md`, section 8, lists it as open.
- **The staging routine** (Remove query, the zero-row query): judge it on the first take; the empty-state panel may look like an answer.
- **What Discover's grid shows for rates.** The rehearsal read full-precision values from the JSON; the grid may round them. If it does, say the values as shown and state the digits from the JSON.
- **How the slide toolkit times its reveals** against audio read from the spoken version.
- **Footage against narration length:** the estimates above are not measured; a rendered guide will measure them.
- **The recap's pointer to Video 2:** not included; add it at assembly only if wanted.
- **Grafana as a second data source** is untested, so nothing in this video may imply it.
