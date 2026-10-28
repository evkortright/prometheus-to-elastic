# Module 1, Video 2 — Run-sheet (screen capture)

**Video:** Build it up: a per-service error ratio, rung by rung (four ideas: label matchers, rate and sum, arithmetic with a scalar, a ratio of two aggregates)
**Status:** Draft v1, Oct 27, 2026. Written from narrative v2 (commit `a804543`), which the author accepted on Oct 27 as the working text for review and recording; changes are expected from the reviewers and from the take. The 17 main blocks and the 2 optional blocks below are copied by script from that narrative. If this sheet and the narrative differ, the narrative wins and this sheet is regenerated. The slide-shape versions of the hook and the recap are not here yet: they come with the slide narrations (contract, section 8, row 5). The decisions, results and evidence are in `module1-video2-log.md`.
**Commands:** at the end of this file (A-P to D-E, and E-P and E-E for the optional chart), from the query lab (R2, R5, R7, R8). They ran on Oct 21 on the previous dataset and run again in the rehearsal.
**Recording:** the laptop (macOS), with the built-in recorder (Command+Shift+5), settings below. Record without audio; the narration is generated afterwards, with the take's numbers.

---

## How to use this sheet

- **One machine.** The laptop runs the stack and records. Where this sheet is displayed during a take, and whether the narration plays in the background as a pacing guide, are the author's choice.
- **Browser.** Chrome, one window with two tabs in a group: **Tab 1** Prometheus (`http://localhost:9090`, **Table** view; the optional chart uses **Graph**), **Tab 2** Kibana Discover (ES|QL mode, date picker on **Last 1 hour**). Zoom is **125%** on both (Chrome keeps it per site). Full screen with **Control+Command+F**. Switch tabs with **Control+Tab**. Each switch briefly flashes the tab strip and toolbar; it is cut in DaVinci Resolve.
- **Controls.** Prometheus: **Execute**. Discover: **Search** or **Cmd+Enter** (the shortcut keeps the cursor in the editor). Never move the cursor to the very top edge: it reveals Chrome's toolbar. These names were observed on the author's screens on Oct 26 (Video 1's capture test); the practice runs re-observe them.
- **Recorder (decided Oct 26, carried over).** Command+Shift+5, then Options: save to `~/Movies/v2-capture` (a new folder for this video), microphone **None**, Show Mouse Clicks **off**, Timer **5 seconds**; choose **Record Entire Screen**, then **Record**. Stop with **Command+Control+Esc**. Keep "Include System Audio" off if your macOS offers it. The Oct 26 test clip was `.mov`, H.264, 3456 × 2234, with no audio; text was easy to read at 125%.
- **Highlights are added in post.** Parts of a query are highlighted in Resolve, so the cursor cues in the steps are optional. A slow cursor over a part is still a useful cue.
- **Method: PASTE.** Copy each command from the end of this file, off camera, before the take.
- **One continuous take per pair.** Record each pair (Prometheus, then Elastic) as one recording (Video 1's test clip of one pair was 47 seconds). There are six takes: the setup, then five pairs (idea 1 with the `!=` matcher, idea 1 without it, then ideas 2, 3 and 4). A seventh take exists only if the optional chart stays. The narration blocks stay separate; you cut the footage in Resolve. A continuous take keeps the gap between the two runs short (see "Timing").
- **The questions and answers have no footage of their own.** In Resolve, hold a frame from the end of the neighbouring take under each question and its answer (beats 3 and 5 say which). The 3-second pause after each question is placed in the edit.
- **No screenshots while recording.** The macOS floating thumbnail may appear on screen, and so in the video. Collect every number after you stop; the results stay on screen (see "After the take").

### Practice mode (from Oct 27, before any reset)

You can rehearse the mechanics on the stack as it is now: paste, run, switch tabs, rest the cursor, and keep a pair inside one scrape minute. Every command in this file only reads data. Two rules:
- **Do not switch the flag on** (Video 1's takes need it off) and **do not reset the stack**.
- **Don't read anything into the numbers.** They are not the take's numbers, idea 4's rows and values will differ on the reset stack, and the practice footage is never used in the video.

If you paste a few practice results with their clock times, they can be checked against the timing rule.

---

## Before every take (pre-roll)

**1. The stack.** `docs/reset-runbook.md` (v2.1): **Part B** (the reset and warm-up) then **Part C** (pre-roll). The commands live there. This video's state: a fresh reset, a warm-up of at least 45 minutes (contract, section 6), `paymentFailure` **on** (the variant and its effect measured in the rehearsal; register row 14), and the pre-roll checks passed, including C4. Notes:
- **Switching the flag on** is runbook B7 (`http://localhost:8080/feature`). Write down the time. The "90%" variant has the value 0.95, not 0.9: check what a variant does before any claim about it. Idea 4's narration says the payment service fails "some of its requests"; that sentence changes if the measurement says otherwise.
- **How long to wait after switching it on** before the ratio shows it is an inference (one rate window, five minutes). The rehearsal tests it. Record idea 4 only after that wait has passed.
- **C2's last number** counts warning and error lines. Prometheus's first compaction, about **3 hours** after the stack starts, logs one "Overlapping blocks found during reloadBlocks" warning. It does not affect remote write. A take within 3 hours of the start will not see it. **C2's "gap equals pending"** is a weak check: trust `failed 0`, `retried 0`, and `sent` growing.
- **Time zones.** Prometheus and Dev Tools show UTC; Discover shows the browser's zone. The author moves from CDT to CST on Nov 1 (runbook). Read timestamps with that in mind.

**2. Browser and screen** (this video):
1. One Chrome window, two tabs, as above, at 125%, in full screen. Do Not Disturb or a Focus on. Notifications off.
2. **Never show:** Prometheus Status, Configuration (it can show the remote-write URL); `.env.elastic`; any API key page; a terminal.
3. The frame includes Kibana's whole window (the left navigation, the project breadcrumb, the "AI Agent" button, your avatar, two small blue badges). Accepted in Video 1; crop or blur in post if you want.
4. Keep the laptop awake while the stack runs (runbook step A8).

**3. Staging before each pair** (proposed on Oct 26 for Video 1; judge it in practice):
- **Prometheus:** the ⋮ **Query options** menu, then **Remove query**, then **+ Add query**. That leaves an empty box and "No data queried yet".
- **Discover:** run a zero-row query, `FROM metrics-generic.prometheus-default | LIMIT 0`, with Cmd+Enter. Then clear the editor and paste the pair's Elastic line without running it. The results area shows "No results match your search criteria" until you run it. That panel can look like the line's own answer, so check it.

---

## Voice-over conventions

- Inside each block is **spoken text only**: no stage directions, no markdown.
- **Voice:** a professional trainer who is an SME speaking to peers (`docs/narration-voice-guide.md`): conversational authority, contractions, direct address, signposts, one idea per sentence, claims stated precisely and then shown. No hype, and no game language.
- **TTS spellings:** `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, symbols as words, `frontend proxy` for the service name with the hyphen.
- **Forbidden in this video** (contract, section 5): "runs unchanged" as an absolute; "all" as an absolute; any percentage, and the percent form altogether; any statement of seconds-free agreement; `increase()`; `topk`; claims about alerting, detection or "real time"; any statement about the feature's status; the sentence that Prometheus labels become Elastic dimensions (a Module 2 topic); and saying a service with no error series "has a ratio of zero": it is absent from the result.
- Say **expression**, not "query", when claiming sameness.
- **Numbers come only from the take.** Counts are whole numbers. Rates and per-minute values are spoken to three decimals. Seconds are whole numbers ("about 8"). The `{{DIGITS_...}}` values are computed from the full-precision values (see "After the take"). The spoken form of numbers is still open at the root, and payment's ratio may need another form (see "Still open").
- `{{LIKE_THIS}}` placeholders are all filled before the audio is generated. If a number disagrees with a sentence, **rewrite the sentence**; don't bend the number.

---

## Beat map

| Beat | What | Footage | Spoken (estimate) |
|---|---|---|---|
| 1 | Hook (slide) | none | about 84 s |
| 2 | Setup | one take, no query | about 40 s |
| 2b | OPTIONAL: what a series is (slide; decision 3) | none | about 15 s |
| 3 | Idea 1: narrow the field, pair 1 (with the `!=` matcher) | one take: Prometheus, then Elastic | about 53 s |
| 3 | Idea 1, pair 2 (matcher removed) | one take: Prometheus, then Elastic | about 28 s |
| 3 | Idea 1, question and answer | none (freeze frames) | about 19 s |
| 4 | Idea 2: how much, in total | one take: Prometheus, then Elastic | about 62 s |
| 5 | Idea 3: scale it with arithmetic, with question and answer | one take: Prometheus, then Elastic; the question and answer use freeze frames | about 52 s |
| 6 | Idea 4: divide one aggregate by another | one take: Prometheus, then Elastic | about 82 s |
| 7 | OPTIONAL: watch it over time (decision 5) | one take: Prometheus Graph tab, then Elastic range query | about 23 s |
| 8 | Recap (slide) | none | about 64 s |

The estimates are word counts at an assumed 150 words a minute, not measured audio. The 17 main blocks total 1207 words, about 8 minutes of speech. The optional beats are not counted. There is no hard limit.

---

## Beat 1 — Hook (slide, no capture)

The **spoken** text is what an instructor or the speech engine reads. The **slide version**, with an explicit shape for the slide toolkit, is a separate artifact derived from it; it comes with the recap's, in the next delivery. Nothing to capture.

**Narration: hook slide** (210 words)

<details><summary>Show voice-over</summary>

```
You can already pull a request rate out of prom-Q-L. The question people actually ask is harder: which of our services are failing, and how often? In prom-Q-L, that question has a name. It's an error ratio, one per service, and it looks like a lot to write.

So here's what this video is for. By the end, you'll be able to write and execute prom-Q-L against a live Elastic time series data stream. That means instant vectors, range vectors reduced by functions, aggregation, and arithmetic between aggregated results, getting results a Prometheus user would already expect.

To get there, we'll build the error ratio from four small ideas that stack. We'll pick out the series we care about with label matchers. Then we'll turn a counter into a rate and add it up, scale the result with a little arithmetic, and divide one aggregate by another. Each idea runs in Prometheus first, then in Elastic.

I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new in Elastic. And at the end, we'll be plain about the limits.

Now, don't take my word for the result. As each pair runs, watch two things: what the new idea adds to the expression, and whether the numbers agree.
```

</details>

Check:
- The objective is learning objective 2 in its own words, with "TSDS" spoken as "time series data stream"; it lands about 25 seconds in.
- "A live Elastic time series data stream": the current docs and the runbook's first-run record support it (log, section 3); the rehearsal shows the index mode again.
- No numbers, no percentages, no statement about the feature's status.

---

## Beat 2 — Setup (take v2-setup)

Staging: Tab 1 with an empty box and "No data queried yet"; Tab 2 with the empty-state panel (run the zero-row query first) and an empty editor, picker on Last 1 hour.

1. Tab 1 in view. Press Command+Shift+5, **Record**, and wait out the 5-second timer. Hold still for 4 seconds.
2. **Control+Tab** to Tab 2. Move the cursor slowly under the date picker (2 s). Hold for 4 seconds.
3. Stop with Command+Control+Esc.

The tab switch happens while recording, so the tab strip flashes here; cut it in post, or record Prometheus and Discover as two short takes.

**Voice-over: Setup** (99 words)

<details><summary>Show voice-over</summary>

```
Let's look at what we're working with. On one screen, Prometheus, on the Table tab. On the other, Kibana's Discover, in E-S-Q-L mode. E-S-Q-L is Elastic's query language, and it has a command for running prom-Q-L. Your expression goes inside the parentheses, and here a wrapper around it makes three choices: where it runs, when it's evaluated, and what to call the answer. The date picker stays on the last hour, because the command reads only the data inside that range. And our metric is traces span metrics calls total, a counter that the OpenTelemetry Collector builds from traces.
```

</details>

Check: "reads only the data inside that range" is register row 19 (the effect was seen in lab R4); the command page's wording is re-read, with the date recorded, before the take. The metric sentence is register row 45.

---

## Beat 2b — OPTIONAL: what a series is (slide, no capture; decision 3)

Deferred (Oct 27). Include only if the wording holds up: the current TSDS page does not contain the sentence "each document belongs to one time series" (log, section 3), so the block is reworded before any use.

**Voice-over: what a series is (optional)** (38 words)

<details><summary>Show voice-over</summary>

```
Underneath this is the series. You know it as one metric with one particular set of labels. In Elastic, a time series data stream stores each observation as a document, and each document belongs to one time series.
```

</details>


---

## Beat 3 — Idea 1: narrow the field (two takes, then the question and answer)

Expression, with the matcher: `count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"})`

### Take v2-A: Prometheus, then Elastic, with the `!=` matcher (A-P, then A-E)

**Staging (off camera).** Tab 1: Remove query, then Add query. Tab 2: run the zero-row query, clear the editor, paste **A-E**, don't run it. Copy **A-P**. Start the take so the Prometheus click lands in the window in "Timing".

1. Tab 1. Start recording; wait out the timer. Click the expression box and paste **A-P**. Optional cue: a slow cursor under the regex, then under the `!=` matcher, then under `count by`.
2. At "Let's run it" in the A1 narration, click **Execute**. Hold for 4 seconds with "Result series: N" in view. Rest the cursor on the **frontend** row for 3 seconds.
3. **Control+Tab** to Tab 2. Optional cue: a slow cursor under the expression inside the parentheses, then over `PROMQL`, `index=metrics-generic.prometheus-default`, `time=?_tend` and `series=`.
4. At "Let's run it" in the A2 narration, press **Cmd+Enter** (or click **Search**). Hold for 4 seconds with "N results" in view. Rest the cursor on the **frontend** row.
5. Stop with Command+Control+Esc. Then collect the numbers (see "After the take").

Notes:
- The result has one row per service and status code that survives. In the lab (Oct 21) it had two rows, checkout and frontend, both with status code unset. The narration's count is the frontend row's.
- Elastic's rows are not necessarily in the same order as Prometheus's (Video 1's rung 3 showed that). Point at the frontend row and its count, not at row order.

**Voice-over: A1 (Prometheus, with the matcher)** (64 words)

<details><summary>Show voice-over</summary>

```
Let's start with the first idea: narrowing the field. You usually want a subset of the series, and label matchers are how you choose. Here we use a regex, service name matches frontend or checkout, plus a negative, status code is not error. To see which series survive, we count them, by service name and status code. Let's run it. Frontend has {{A_FRONTEND_PROM}} series.
```

</details>

**Voice-over: A2 (Elastic, with the matcher)** (68 words)

<details><summary>Show voice-over</summary>

```
Now the same thing in Elastic. The text inside the parentheses is the expression. Around it is the wrapper. Index is where it runs. Time is when it's evaluated: once, at the end of the date picker's range. And the name out front is what we call the answer. Let's run it. Frontend has {{A_FRONTEND_ELASTIC}} series, against {{A_FRONTEND_PROM}} in Prometheus. The two runs were about {{SECONDS_A}} seconds apart.
```

</details>


### Take v2-A0: Prometheus, then Elastic, matcher removed (A-P0, then A-E0)

**Staging (off camera).** As for take v2-A, with **A-E0** staged in Tab 2 and **A-P0** on the clipboard. Window in "Timing".

1. Tab 1. Start recording; wait out the timer. Paste **A-P0**. Optional cue: the cursor on the place where the matcher used to be, then under `count by`.
2. At "Let's run it" in the A3 narration, click **Execute**. Hold for 4 seconds. Rows for status code error appear; rest the cursor on the **frontend** row with status code error for 3 seconds.
3. **Control+Tab** to Tab 2.
4. At "Let's run it" in the A4 narration, press **Cmd+Enter**. Hold for 4 seconds, then rest the cursor on the **frontend** row with status code error.
5. Stop with Command+Control+Esc. Then collect the numbers.

Notes: the baseline result has one row per status code for each service (in the lab, frontend 36 with status code unset and 14 with status code error). The frontend row with status code unset should keep the count it had in take v2-A; if it differs, write that in the take log.

**Voice-over: A3 (Prometheus, matcher removed)** (30 words)

<details><summary>Show voice-over</summary>

```
Now take the not-equals away, and run the same count again. Let's run it. The error series come back as new rows. Frontend, with status code error, has {{A_ERR_FRONTEND_PROM}} series.
```

</details>

**Voice-over: A4 (Elastic, matcher removed)** (39 words)

<details><summary>Show voice-over</summary>

```
And in Elastic, with the not-equals removed. Let's run it. Frontend with status code error has {{A_ERR_FRONTEND_ELASTIC}} series, against {{A_ERR_FRONTEND_PROM}} in Prometheus, about {{SECONDS_A_BASE}} seconds apart. So the series the not-equals removed were the error series, in both systems.
```

</details>


### The question and the answer (no footage)

In Resolve, hold a frame from the end of take v2-A0 (Elastic: the expression in the editor, and no frontend proxy row in the results) under both blocks. The 3-second pause after the question is placed in the edit.

**Voice-over: idea 1, question** (20 words)

<details><summary>Show voice-over</summary>

```
A question, before we continue. That regex says frontend or checkout. Will it also match frontend proxy? Take a second.
```

</details>

**Voice-over: idea 1, answer** (28 words)

<details><summary>Show voice-over</summary>

```
No. A regex matcher has to match the whole value, and frontend proxy is more than frontend, so there's no frontend proxy row in Prometheus or in Elastic.
```

</details>


Check: no frontend proxy row on either side (lab R2, Oct 21); confirm in the takes.

---

## Beat 4 — Idea 2: how much, in total (take v2-B: B-P, then B-E)

Expression: `sum(rate(traces_span_metrics_calls_total[5m]))`

**Staging (off camera).** As for idea 1, with **B-E** staged in Tab 2 and **B-P** on the clipboard. Window in "Timing".

1. Tab 1. Start recording; wait out the timer. Paste **B-P**. Optional cue: the cursor under `[5m]`, then under `sum(`.
2. At "Let's run it" in the B1 narration, click **Execute**. Hold for 4 seconds with the single value in view.
3. **Control+Tab** to Tab 2. Optional cue: the cursor on `total_rate=`.
4. At "Let's run it" in the B2 narration, press **Cmd+Enter**. Hold for 4 seconds with `total_rate` in view.
5. Stop with Command+Control+Esc. Then collect the numbers.

Notes: Prometheus shows `{}` for the empty label set; Elastic returns only `total_rate` and `step` (lab R5, Oct 21).

**Voice-over: B1 (Prometheus)** (94 words)

<details><summary>Show voice-over</summary>

```
Now the second idea: how much, in total. A counter keeps climbing, so on its own it says little about right now. What you want is its rate, calls per second averaged over a five minute window. Then we add the series up with sum. With nothing after the sum, they add up into a single number: the total calls per second across our services, as this metric counts them. Let's run it. {{B_PROM}} calls per second. Prometheus shows it with an empty set of curly braces, because there's no label left to show.
```

</details>

**Voice-over: B2 (Elastic)** (60 words)

<details><summary>Show voice-over</summary>

```
In Elastic, it's the same expression inside the same wrapper, with a new name for the answer: total rate. Let's run it. {{B_ELASTIC}} calls per second, against {{B_PROM}} in Prometheus. The runs were about {{SECONDS_B}} seconds apart, and the values agree to {{DIGITS_B}} digits. There are no curly braces here. Elastic shows the value and the time it was evaluated.
```

</details>


---

## Beat 5 — Idea 3: scale it with arithmetic (take v2-C: C-P, then C-E)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60`

**Staging (off camera).** As before, with **C-E** staged in Tab 2 and **C-P** on the clipboard. Window in "Timing".

1. Tab 1. Start recording; wait out the timer. Paste **C-P**. Optional cue: the cursor under `sum by (service_name)`, then under `* 60`.
2. At "Let's run it" in the C1 narration, click **Execute**. Hold for 4 seconds. The table has one row per service. Rest the cursor on the **frontend** row for 3 seconds.
3. **Control+Tab** to Tab 2.
4. At "Let's run it" in the C2 narration, press **Cmd+Enter**. Hold for 4 seconds, then rest the cursor on the **frontend** row for 3 seconds.
5. Stop with Command+Control+Esc. Then collect the numbers, **including the Elastic row count** ("N results"): the lab never recorded it.

Notes: point at **frontend**, not at a low-traffic service. Neither side sorts, so find the row on each side. In the lab, Prometheus returned 18 results, with a few services at 0.

**Voice-over: C1 (Prometheus)** (61 words)

<details><summary>Show voice-over</summary>

```
Third idea: arithmetic with a plain number. We put a by clause back, sum by service name, so we get one row per service, and then we multiply by sixty. That turns calls per second into calls per minute. Arithmetic with a plain number scales each value, and the labels stay attached. Let's run it. Frontend reads {{C_FRONTEND_PROM}} calls per minute.
```

</details>

**Voice-over: C2 (Elastic)** (33 words)

<details><summary>Show voice-over</summary>

```
In Elastic, the same expression inside the same wrapper. Let's run it. Frontend reads {{C_FRONTEND_ELASTIC}}, against {{C_FRONTEND_PROM}} in Prometheus. The runs were about {{SECONDS_C}} seconds apart, and the values agree to {{DIGITS_C}} digits.
```

</details>


### The question and the answer (no footage)

In Resolve, hold a frame from the end of take v2-C (the Elastic result with the frontend row visible) under both blocks. The 3-second pause is placed in the edit.

**Voice-over: idea 3, question** (17 words)

<details><summary>Show voice-over</summary>

```
Another question. What would the frontend row say if we multiplied by thirty-six hundred instead of sixty?
```

</details>

**Voice-over: idea 3, answer** (19 words)

<details><summary>Show voice-over</summary>

```
Sixty times as much, because thirty-six hundred is sixty times sixty. That's calls per hour, from changing one number.
```

</details>


---

## Beat 6 — Idea 4: divide one aggregate by another (take v2-D: D-P, then D-E)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`

**Staging (off camera).** As before, with **D-E** staged in Tab 2 and **D-P** on the clipboard. The flag is on and the wait after switching it on has passed (see "Before every take"). Window in "Timing".

1. Tab 1. Start recording; wait out the timer. Paste **D-P**. Optional cue: the cursor under the numerator, then the denominator, then the slash.
2. At "Let's run it" in the D1 narration, click **Execute**. Hold for 4 seconds with "Result series: N" in view. Rest the cursor on the **payment** row for 3 seconds.
3. **Control+Tab** to Tab 2.
4. At "Let's run it" in the D2 narration, press **Cmd+Enter**. Hold for 4 seconds, then rest the cursor on the **payment** row for 3 seconds. Then move the cursor slowly down the full list, so that "Now look at who's missing" has the whole list in view.
5. Stop with Command+Control+Esc. Then collect the numbers, **including the Elastic row count**.

Notes:
- The result has one row per service that has an error series. In the lab (Oct 21) six of the eight rows read exactly 0 and ten services were absent. If the take shows rows that read zero, write it in the take log: the narration says only that a service with no error series is absent, and whether a sentence is needed for the zero rows is an open question.
- Neither side sorts. Find the payment row on each side.

**Voice-over: D1 (Prometheus)** (120 words)

<details><summary>Show voice-over</summary>

```
Now the idea we came for: dividing one aggregate by another. On top, the rate of calls whose status code is error, summed by service name. On the bottom, the rate of all calls, summed by service name. Divide the first by the second, and each service that has error series gets its own error ratio.

The rule to remember: aggregate both sides the same way. Here, both sides are sum by service name, so each service on top finds its partner underneath.

To give the ratio something to show, we've switched on a feature flag in the demo that makes the payment service fail some of its requests. Let's run it. {{D_ROWS_PROM}} rows come back, and payment reads {{D_PAYMENT_PROM}}.
```

</details>

**Voice-over: D2 (Elastic)** (86 words)

<details><summary>Show voice-over</summary>

```
In Elastic, the same expression inside the same wrapper. Let's run it. {{D_ROWS_ELASTIC}} rows, against {{D_ROWS_PROM}} in Prometheus, and payment reads {{D_PAYMENT_ELASTIC}}, against {{D_PAYMENT_PROM}}. The runs were about {{SECONDS_D}} seconds apart, and the payment values agree to {{DIGITS_D}} digits.

Now look at who's missing. A service with no error series doesn't show up as a zero. It isn't in the result at all, in Prometheus or in Elastic. So a missing row means no error series was recorded for that service, not a ratio of zero.
```

</details>


---

## Beat 7 — OPTIONAL: watch it over time (take v2-E: E-P, then E-E; decision 5)

Deferred (Oct 27): the rehearsal shows both charts first. Provisional steps, not yet rehearsed.

1. Tab 1: switch from Table to **Graph**, range one hour. Paste **E-P**, click **Execute**.
2. Tab 2: paste **E-E** (no `time=` option, so it runs as a range query and Discover draws a chart), press **Cmd+Enter**.
3. Compare the shapes only after both charts are on screen.

**Voice-over: watch it over time (optional)** (58 words)

<details><summary>Show voice-over</summary>

```
One more look, if you want to see the ratio change. Take the time setting out of the wrapper, and Elastic evaluates the expression across the date picker's range instead of once, so Discover can chart it. Let's run it, first in Prometheus's Graph tab, then in Elastic. [Chart comparison sentence: written after the rehearsal shows both charts.]
```

</details>


---

## Beat 8 — Recap (slide, no capture)

The slide version is a separate artifact (the recap is four peer cards, shape C), in the next delivery. Nothing to capture.

**Narration: recap slide** (159 words)

<details><summary>Show voice-over</summary>

```
Let's come back to what we set out to do: write and execute prom-Q-L against a live Elastic time series data stream, getting results a Prometheus user would already expect. You've now built the error ratio one idea at a time. Label matchers picked out the series. A rate, summed, turned a counter into one number. Arithmetic with a plain number scaled it. And a ratio of two aggregates, aggregated the same way, answered the question you actually get asked: which of our services are failing, and how often. Each time, it was the same expression in Prometheus and in Elastic, and the numbers agreed.

There's one caution, because we said we'd be plain about the limits. Most of prom-Q-L works this way, though not all of it, and the edges are worth knowing before you rely on them. Elastic's documentation keeps the current list of what isn't supported, so check it before you move something you depend on.
```

</details>

Check:
- "Each time, it was the same expression in Prometheus and in Elastic, and the numbers agreed" depends on the takes. If a take disagrees, that sentence changes.
- "Elastic's documentation keeps the current list of what isn't supported": re-read the limitations page and record the retrieval date before the take (register row 40).

---

## Timing: keep each pair inside one scrape minute

Prometheus scrapes once a minute (`scrape_interval: 60s`); on Oct 26 the new samples landed at about :37 of each minute. Elastic receives each sample some time later (not measured; under about 28 s in one pair). A pair of runs agreed to better than 1e-9 on Oct 26 whenever both fell between a new sample and the next one. The Prometheus click should come after about **:40**, and the Elastic click before about **:35** of the next minute, so both use the same newest sample. This is a hypothesis that fitted all three of Video 1's timed pairs; this video's rehearsal re-measures the sample times on its own reset stack.

If the narration plays straight through as a pacing guide, the estimates (word counts at 150 words a minute, not measured; the offsets are from the start of the Prometheus block) are:

| Pair | Prometheus click | Elastic click | Gap | Prometheus click must land |
|---|---|---|---|---|
| A, with the matcher (A1, A2) | about 24 s into the take | about 46 s | about 22 s | from :40 until about :13 of the next minute |
| A0, matcher removed (A3, A4) | about 6 s into the take | about 16 s | about 10 s | from :40 until about :25 of the next minute |
| B (B1, B2) | about 29 s into the take | about 46 s | about 17 s | from :40 until about :18 of the next minute |
| C (C1, C2) | about 22 s into the take | about 29 s | about 7 s | from :40 until about :28 of the next minute |
| D (D1, D2) | about 45 s into the take | about 53 s | about 8 s | from :40 until about :27 of the next minute |

The window is the time from :40 until (95 minus the gap) seconds past the minute. A longer gap makes a shorter window. Replace these estimates with the real offsets of your rendered audio. Start each take so that its offset (the 5-second timer included) puts the Prometheus click in the window. Where the offset is short (pair A0 about 6 s, pair C about 22 s), paste first and start the narration afterwards, so the click can land in the window. Five pairs mean five separate windows; there is no need to record them in one sitting.

---

## After the take

Collect the numbers once you have stopped; the results stay on screen.

1. **Prometheus tab:** a screenshot of the result ("Result series: N", the value, or the row the narration names).
2. **Elastic tab:** a screenshot ("N results", the value) and the JSON of the result, as in Video 1's rehearsal, for full precision and the `step` time.
3. **The gap in seconds:** read it from the footage in Resolve, as the time between the Execute click and the Search click in the continuous take. Elastic's `step` gives the absolute time of the Elastic run as a check.
4. Run the counters command again (runbook Part C, command 2). `failed` and `retried` should still be 0.
5. Fill in the take log, then the placeholders (a Video 2 helper, named with the video, computes the `{{DIGITS_...}}` values and fills the narration; it is written when the takes exist).
6. Rename each take: `v2-setup`, `v2-A`, `v2-A0`, `v2-B`, `v2-C`, `v2-D` (and `v2-E`) plus the recorder's extension.

### Take log (fill in)

| Pair | Prometheus (value or count) | Elastic (value or count) | Gap (s) | Elastic step | Notes |
|---|---|---|---|---|---|
| A: frontend row, status code unset, with the matcher | | | | | |
| A0: frontend row, status code error, matcher removed | | | | | |
| B: total calls per second | | | | | |
| C: frontend calls per minute (and Elastic's row count) | | | | | |
| D: payment's ratio (and both row counts) | | | | | |

### Placeholders to fill

| Placeholder | Meaning | Source and form |
|---|---|---|
| `{{A_FRONTEND_PROM}}`, `{{A_FRONTEND_ELASTIC}}` | Series count of the frontend row in take v2-A | "Result series" and the frontend row; whole numbers |
| `{{SECONDS_A}}` | Seconds between the runs, take v2-A | The gap; whole seconds |
| `{{A_ERR_FRONTEND_PROM}}`, `{{A_ERR_FRONTEND_ELASTIC}}` | Series count of the row "frontend, status code error" in take v2-A0 | The row's count; whole numbers |
| `{{SECONDS_A_BASE}}` | Seconds between the runs, take v2-A0 | The gap; whole seconds |
| `{{B_PROM}}`, `{{B_ELASTIC}}` | Total calls per second | The values; three decimals |
| `{{SECONDS_B}}`, `{{DIGITS_B}}` | Seconds between the runs, and the leading significant digits the two values share | The gap; computed from the full-precision values |
| `{{C_FRONTEND_PROM}}`, `{{C_FRONTEND_ELASTIC}}` | Frontend calls per minute | The values; three decimals |
| `{{SECONDS_C}}`, `{{DIGITS_C}}` | Seconds between the runs, and the digits the two values share | The gap; computed |
| `{{D_ROWS_PROM}}`, `{{D_ROWS_ELASTIC}}` | Rows returned by the ratio | "Result series: N" and "N results"; whole numbers |
| `{{D_PAYMENT_PROM}}`, `{{D_PAYMENT_ELASTIC}}` | Payment's error ratio | The values; form still open |
| `{{SECONDS_D}}`, `{{DIGITS_D}}` | Seconds between the runs, and the digits the two payment values share | The gap; computed |

A digits sentence counts the leading significant digits the two full-precision values share (register row 64). If they share only a few (under about four), the sentence changes, not the number.

---

## Rehearsal (guided in chat; the video chat guides, the author runs)

Runs after Video 1's takes, on the reset stack, with the commands in this file. It records, in the video log:
- The values or counts and the times for all five pairs, with the seconds between the runs.
- The Elastic row counts for C and D, which the lab never recorded.
- The flag: which variant is used, the time it was switched on, payment's ratio before it and at intervals after it, so that we know how long the ratio takes to show. No claim about the size of the effect until it is measured.
- Whether idea 4 shows rows that read zero.
- The mapping check (read-only): the data stream's index mode, and, only if the optional series slide stays, how the labels are mapped. The exact requests are given in the session.
- If the optional chart stays: both charts on screen.

---

## Checked in this file (Oct 27, by script; text only)

- The 19 spoken blocks above (17 main, 2 optional) are identical to the 19 fenced blocks of narrative v2, in the same order (narrative sha256 `28694fa7c3281bb534f3b1b4e51c62e02dcd572b3d190b2296c3c6718da74c71`), and the word counts in the headings were computed from them (placeholders count as one word each).
- The 20 placeholders used in the 17 main blocks are exactly the 20 in the table above; the optional blocks use none.
- In each of the six pairs (A, A0, B, C, D and the optional E), the text between the parentheses of the Elastic line is character for character the text of the Prometheus line. The pairs differ only in the wrapper and the result name (`series`, `series`, `total_rate`, `per_minute`, `error_ratio`, `error_ratio`); E-E also drops the `time=` option.
- All twelve commands appear verbatim in the query lab (R2, R5, R7 and R8; E-E is the lab's R8 range form). None has a sort.
- Each of the ten executions in the main blocks says "Let's run it", and the steps point at those cues. The result names the narration uses ("total rate") match the commands.


This checks the text. It does not show that the commands run; they ran on Oct 21 on the previous dataset and run again in the rehearsal.

---

## If something goes wrong

- **An error in Elastic:** don't edit the command. Stop, copy the exact error text, and send it to me. Errors are findings.
- **Elastic shows the empty-state panel after a run:** check the picker says **Last 1 hour** and the stack uptime.
- **The two values differ at the third or fourth digit:** a new sample probably landed between your two runs. Retake the pair inside one scrape minute (see "Timing").
- **Prometheus shows no data:** check the stack is running, then the counters (runbook Part C).
- **Idea 4 returns no rows, or only zeros:** check the flag page and how long ago the flag was switched on (the wait is being measured), and the counters.

---

## Copy-paste commands

**A-P** — Prometheus, idea 1, with the matcher
```
count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"})
```

**A-E** — Elastic, idea 1, with the matcher
```
PROMQL index=metrics-generic.prometheus-default time=?_tend series=(count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"}))
```

**A-P0** — Prometheus, idea 1, matcher removed
```
count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout"})
```

**A-E0** — Elastic, idea 1, matcher removed
```
PROMQL index=metrics-generic.prometheus-default time=?_tend series=(count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout"}))
```

**B-P** — Prometheus, idea 2
```
sum(rate(traces_span_metrics_calls_total[5m]))
```

**B-E** — Elastic, idea 2
```
PROMQL index=metrics-generic.prometheus-default time=?_tend total_rate=(sum(rate(traces_span_metrics_calls_total[5m])))
```

**C-P** — Prometheus, idea 3
```
sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60
```

**C-E** — Elastic, idea 3
```
PROMQL index=metrics-generic.prometheus-default time=?_tend per_minute=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60)
```

**D-P** — Prometheus, idea 4
```
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

**D-E** — Elastic, idea 4
```
PROMQL index=metrics-generic.prometheus-default time=?_tend error_ratio=(sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```

**E-P** — Prometheus, the optional chart (Graph tab; the same expression as D-P)
```
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

**E-E** — Elastic, the optional chart (a range query: no `time=` option; the lab's R8 range form)
```
PROMQL index=metrics-generic.prometheus-default error_ratio=(sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```

---

## Still open

- **Where this sheet is displayed** during a take, and whether the narration plays in the background (the author's experiments).
- **The spoken form of numbers** (three decimals, whole counts, whole seconds): a proposal at the root. Payment's ratio may need another form; decide after the flag is measured.
- **The staging routine** (Remove query, the zero-row query): judge it in practice; the empty-state panel may look like an answer.
- **What Discover's grid shows for rates.** Video 1's rehearsal read full-precision values from the JSON; the grid may round them. If it does, say the values as shown and state the digits from the JSON.
- **The control names** (Execute, Search, Cmd+Enter, Remove query) come from Video 1; the practice runs re-observe them.
- **Rows that read zero in idea 4**, and whether a sentence is then needed.
- **The flag's variant and wording.** Which variant is used, and whether "some of its requests" still fits.
- **Footage against narration length:** the estimates above are not measured; a rendered guide measures them.
- **The slide versions** of the hook and the recap, and the shape of the hook, with the next delivery.
- **The optional beats** (decisions 3 and 5), deferred.
- **Grafana as a second data source** is untested, so nothing in this video may imply it.
