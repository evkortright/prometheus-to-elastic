# Module 1, Video 1 — Run-sheet (screen capture)

**Video:** Your PromQL, running in Elastic (three rungs: label selector, `rate()`, `sum by`)
**Status:** Draft v3, Oct 22, 2026. Follows the outline (`module1-video1-outline.md`, commit `edf75cf`). v3 carries voice-over iteration 1: reordered (selector, rate, `sum by`), the setup moved into Clip A, a ladder sentence added, and `SORT` dropped from the Elastic command for rung 3. Not yet heard through the speech engine.
**Commands:** taken from the query lab (R1, R3, R6). They were verified on Oct 20 and Oct 21 on the previous dataset. **Run C1 to C6 once as a rehearsal on the current stack before the real take.**
**Recording:** Windows Game Bar on the desktop. Narration is added afterwards, so record without audio.

---

## How to use this sheet

- **Laptop** shows this sheet. **Desktop** runs the capture.
- Game Bar: **Win + Alt + R** starts and stops. It records one app window at a time, so use **one browser window with two tabs**: Tab 1 = Prometheus, Tab 2 = Kibana.
- The commands are at the end of this file (C1 to C6). Open this same file on the desktop in a **second window** to copy from. Never record that window.
- Markers: **▶ START** and **■ STOP** are Win + Alt + R. **HOLD n s** means stay still, mouse included. **✂ CUT** means stop recording, copy the command, click back into the recorded window, start again. Each clip joins in DaVinci Resolve.
- **Method: PASTE (default).** Reasons: the lines are long; pasting keeps the gap between the Prometheus run and the Elastic run short, and short gaps gave much tighter agreement in the lab (an inference, not a tested rule); and code editors can auto-close brackets and quotes while you type (not verified for this editor). Switch to typing only if you decide to after the capture test.
- **Timing rule:** run Prometheus first, then Elastic **within about 15 seconds**. To make that possible, **stage the Elastic line first**: paste it into Tab 2 and don't run it, then record the Prometheus clip, then run Elastic right away. Each rung says when.
- Holds matter. The narration is placed over them. Give every result a 4-second hold.

---

## Before every take (pre-roll)

Desktop, in WSL:

1. Uptime and clock. The stack should have run at least 45 minutes.
```
date -u; docker ps --format '{{.Names}}: {{.Status}}' | grep -E 'prometheus|flagd'
```
2. Remote-write counters. Failed should be 0 (or unchanged from the last reading), and the last number should be 0.
```
date -u; curl -s http://localhost:9090/metrics | sed 's/{[^}]*}//' | awk '/^prometheus_remote_storage_samples_failed_total/{f=$2} /^prometheus_remote_storage_samples_retried_total/{r=$2} /^prometheus_remote_storage_samples_pending/{p=$2} /^prometheus_remote_storage_samples_in_total/{i=$2} /^prometheus_remote_storage_samples_total/{t=$2} END{printf "failed %s | retried %s | pending %s | in %.0f | sent %.0f | gap %.0f\n", f, r, p, i, t, i-t}'; docker logs prometheus 2>&1 | grep -cE 'level=(WARN|ERROR)'
```
3. Feature flags page: **paymentFailure is off.**

Browser and screen:

4. **One window**, maximized. **Tab 1:** `http://localhost:9090`, **Table** tab selected, query box empty. **Tab 2:** Kibana, Discover, **ES|QL** mode, date picker on **Last 1 hour**, editor empty.
5. Browser zoom at about 125 to 150% (set after the capture test). Bookmarks bar hidden.
6. Notifications off (Do Not Disturb). Game Bar enabled, mic off.
7. **Never show:** Prometheus Status, Configuration (it can show the remote-write URL); `.env.elastic`; any API key page; a terminal.
8. **Decide before the real take:** whether the Kibana address bar (it contains the project ID) stays visible or is cropped or blurred in Resolve.

---

## Voice-over conventions

- Inside each voice-over block is **spoken text only**: no stage directions, no markdown.
- **TTS spellings** (the audio engine reads these correctly): `prom-Q-L`, `E-S-Q-L`, metric and label names as plain words ("traces span metrics calls total", "service name equals frontend"), symbols as words ("equals", "square brackets"). The slide opener keeps the author's own spelling; test how the slide generator treats `promQL` and `ESQL`.
- Say **expression**, not "query", when claiming sameness. Say **most** or **common**, never "all". No "preview". No "no changes."
- **Numbers come only from the take log.** Every number is spoken next to what it is compared with. Every agreement statement carries the gap in seconds between the two runs. No bare percentages.
- `{{LIKE_THIS}}` placeholders must all be filled before the audio is generated. The table at the end of "After the take" says where each one comes from.
- If a number disagrees with what a sentence claims, **rewrite the sentence**; don't bend the number.

---

## Beat map

| Beat | What | Capture | Target on screen |
|---|---|---|---|
| 1 | Opener slide | None (slide only) | n/a |
| 2 | Setup: same data in both places | Clip A | about 25 s |
| 3 | Rung 1: label selector | Clips B1, B2 | about 45 s |
| 4 | Rung 2: `rate()` on a counter | Clips C1, C2 | about 45 s |
| 5 | Rung 3: `sum by` | Clips D1, D2 | about 45 s |
| 6 | Recap slide | None (slide only) | n/a |

---

## Beat 1 — Opener slide (no capture)

Narration iteration 1 (Oct 22), built on the author's draft. The slide generator reads this block.

**Narration: opener slide** (96 words)

<details><summary>Show narration</summary>

```
Most common promQL expressions run unchanged in Elastic.

Elastic's promQL command, part of the Elasticsearch Query Language, evaluates a promQL expression against metrics stored in Elastic. The expression is the same text you'd run in Prometheus. What you add is a wrapper: the ESQL command and a few parameters.

We'll test that with three expressions you likely use already, first in Prometheus, then in Elastic.

First, select series with a label selector.

Second, take the rate of a counter.

Third, aggregate with sum by.

Then we compare the output, and you can judge the match yourself.
```

Claims check:
- Changes from the author's draft: (1) items reordered to match the demo (selector, rate, `sum by`), because `sum by` builds on `rate`; (2) "run unchanged" and "stays the same" merged into "The expression is the same text you'd run in Prometheus"; (3) the remote-write sentence moved to Clip A; (4) the closing line is "you can judge the match yourself". The author's original closing, "observe essentially the same results", is the alternative if the take supports it.
- "Most common ... run unchanged": Elastic's limitations page says the majority of expressions run unchanged (register row 1). The next paragraph explains the wrapper, so "unchanged" refers to the expression.
- "Part of the Elasticsearch Query Language": verified in the Kibana docs.
- Test the speech-engine spelling of `promQL` and `ESQL`. If misread, use `prom-Q-L` and `E-S-Q-L`.

</details>

---

## Beat 2 — Setup (Clip A)

1. Tab 1 in view (Prometheus, Table tab, empty box). **▶ START.** HOLD 4 s.
2. Click Tab 2 (Kibana Discover, ES|QL mode, Last 1 hour, empty editor). HOLD 4 s.
3. **■ STOP.**

Nothing to verify here. The claim that both systems hold the same metrics is shown at rung 1.

**Voice-over: Clip A** (80 words)

<details><summary>Show voice-over</summary>

```
Two tabs. In one, Prometheus, on the Table tab, with an empty expression box: the place you'd run an expression today. In the other, Kibana's Discover, in E-S-Q-L mode, pointed at the same metrics. In this demo, Prometheus sends them to Elastic through remote write, so both systems hold the same data. One setting to notice: the date picker is set to the last hour. The prom-Q-L command reads only the data inside that range, so we're keeping it wide.
```

Claims check:
- "Prometheus sends them through remote write": verified (register row 9).
- "Reads only the data inside that range": the lab's setup section, and tested in lab R4 (about half the Prometheus value when the picker was narrower than the window). The consequences are left for Video 3.

</details>

---

## Beat 3 — Rung 1: label selector (R1)

Expression: `traces_span_metrics_calls_total{service_name="frontend"}`

**Before Clip B1 (off camera):** in Tab 2, paste **C2** into the editor and **do not run it**. Then copy **C1**.

**Clip B1 (Prometheus)**
1. Tab 1. Click into the expression box. **▶ START.**
2. Paste C1. Don't execute yet. Move the cursor slowly under the metric name (2 s), then under `{service_name="frontend"}` (2 s).
3. Click **Execute**. HOLD 4 s with the "N results" line in view. **Write down N.**
4. **■ STOP.** Go straight to Clip B2.

**Clip B2 (Elastic), C2 already staged in Tab 2**
1. Tab 2. **▶ START.**
2. Cursor slowly under the expression, the part inside the parentheses. HOLD 3 s.
3. Cursor over the wrapper, in this order, 2 s on each: `PROMQL`, `index=metrics-generic.prometheus-default`, `time=?_tend`, `calls=`.
4. Run it. HOLD 4 s with the rows in view.
5. If Discover shows no row count: **✂ CUT**, copy **C2b**, paste, run, and HOLD 4 s on `series = N`. **Write down N.**
6. **■ STOP.**

Notes: the rows will not appear in the same order on the two sides, and Elastic holds the labels in a `_timeseries` column. Point at the count and at one label set, not at row order.

**Voice-over: Clip B1** (67 words)

<details><summary>Show voice-over</summary>

```
We'll climb a short ladder: three expressions, simplest first, each checked in both places. Rung one: a label selector. Our metric is traces span metrics calls total, a counter of calls that the OpenTelemetry Collector generates from traces. Add curly braces and a label matcher, service name equals frontend, and we've selected just that service's series. Run it. {{N_PROM}} series, each with its own set of labels.
```

Claims check:
- The ladder sentence is new: it introduces "rung" once, and it sets up Video 2.
- Metric derived from traces by the Collector: `docs/otel-collector-reference.md`. "Counter": Prometheus's metric types page (a cumulative metric that only increases or resets to zero on restart).
- `{{N_PROM}}`: from the take log.

</details>

**Voice-over: Clip B2** (106 words)

<details><summary>Show voice-over</summary>

```
Now Elastic. Look inside the parentheses: that's the expression we just ran in Prometheus. The rest is the wrapper. The line starts with the prom-Q-L command, and three parameters answer three questions. Where should this run? That's index, the data stream that holds the metrics. When? That's time: the end of the date picker's range, so the expression is evaluated once, like the Table tab. And what do we call the answer? That's calls, the name of the result. Run it. {{N_ELASTIC}} series, against {{N_PROM}} in Prometheus. The labels sit in a column instead of inline, but for this expression, the wrapper is everything that's new.
```

Claims check:
- Where, when, what to call it: the lab's syntax section (`index=`, `time=`, result name). `?_tend` is the end of the date picker's range: Kibana docs.
- "Evaluated once, like the Table tab": the lab's setup section (from the PROMQL command docs) and tested (one `step` value per row, equal to the run time).
- "Labels in a column": lab R1 (`_timeseries`). **Confirm in the take that the label sets match** before keeping the sentence.
- "For this expression, the wrapper is everything that's new": every expression in the lab ran inside the same wrapper. Confirm against the take.

</details>

---

## Beat 4 — Rung 2: `rate()` on a counter (R3)

Expression: `sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))`

**Before Clip C1 (off camera):** in Tab 2, clear the editor, paste **C4**, and **do not run it**. Then copy **C3**. Clear Tab 1's box.

**Clip C1 (Prometheus)**
1. Tab 1. **▶ START.**
2. Paste C3. Don't execute yet. Cursor under `[5m]` (2 s), then under `sum(` (2 s).
3. Click **Execute.** HOLD 4 s with the single value in view. **Write down the value and the time.**
4. **■ STOP.** Go straight to Clip C2.

**Clip C2 (Elastic), C4 already staged in Tab 2** (within about 15 s of the Prometheus run)
1. Tab 2. **▶ START.**
2. Cursor on `frontend_rate=` (2 s). Run it. HOLD 4 s with `frontend_rate` in view. **Write down the value.**
3. **■ STOP.**

Notes: Prometheus shows `{}` for the empty label set, and Elastic returns only `frontend_rate` and `step`. Don't point this out unless the narration needs it.

**Voice-over: Clip C1** (72 words)

<details><summary>Show voice-over</summary>

```
Rung two: the rate of a counter. On its own, a counter just climbs: it counts every call since the start. What you usually want is how fast. Rate takes the counter over a window, here five minutes in square brackets, and returns its per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: the frontend's calls per second. Run it. {{PROM_VALUE}}.
```

Claims check:
- Counter definition: Prometheus's metric types page. "What you usually want is how fast" is a judgment.
- `rate`: per-second average rate of increase of the series in the range vector (Elastic's range vector functions page).
- The number: from the take log.

</details>

**Voice-over: Clip C2** (35 words)

<details><summary>Show voice-over</summary>

```
Same expression in Elastic, same wrapper. Only the result name changes, now frontend rate. {{ELASTIC_VALUE}}, against {{PROM_VALUE}} in Prometheus. The two runs were about {{SECONDS_C}} seconds apart, and the values differ by about {{PCT_C}} percent.
```

Claims check:
- Values and gap: from the take log.
- If the relative difference is larger than about 1 percent, **rewrite this sentence** instead of filling the template.

</details>

---

## Beat 5 — Rung 3: `sum by` (R6)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`

**Before Clip D1 (off camera):** in Tab 2, clear the editor, paste **C6**, and **do not run it**. Then copy **C5**. Clear Tab 1's box.

**Clip D1 (Prometheus)**
1. Tab 1. **▶ START.**
2. Paste C5. Don't execute yet. Cursor under `sum by (service_name)` (3 s).
3. Click **Execute.** HOLD 4 s. The table has one row per service. **Write down the row count.**
4. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
5. **■ STOP.** Go straight to Clip D2.

**Clip D2 (Elastic), C6 already staged in Tab 2** (within about 15 s of the Prometheus run)
1. Tab 2. **▶ START.** Run it. HOLD 4 s. **Write down the row count.**
2. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
3. **■ STOP.**

Notes:
- Point at **frontend** (or another busy service), not at a low-traffic one. In the lab, low-traffic services differed by up to about 13%, which looked like timing noise (an inference).
- Neither side's rows are guaranteed to be in the same order. Find the frontend row on each.
- Zero-traffic services show 0 on both sides.
- **C6 no longer has `| SORT service_name`.** The lab ran this line with the sort appended, and R7 and R8 ran without one, but this exact line has not been run. It is part of the rehearsal.

**Voice-over: Clip D1** (53 words)

<details><summary>Show voice-over</summary>

```
Rung three: aggregate by a label. So far we have one number for the whole frontend, but the question you ask is usually per service. Sum by service name keeps that label and adds up the rest, so we get one row per service. Run it. {{ROWS_PROM}} rows. Frontend: {{PROM_FRONTEND}} calls per second.
```

Claims check:
- `sum by`: aggregation operators combine one instant vector into fewer elements; the `by` clause preserves the named label (Prometheus operators page).
- "The question you ask is usually per service" is a judgment about the audience.

</details>

**Voice-over: Clip D2** (27 words)

<details><summary>Show voice-over</summary>

```
Same expression in Elastic, same wrapper. {{ROWS_ELASTIC}} rows. Frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus: within about {{PCT_D}} percent, with the two runs about {{SECONDS_D}} seconds apart.
```

Claims check:
- Values and gap: from the take log.
- C6 (without the sort) is still to be rehearsed.

</details>

---

## Beat 6 — Recap slide (no capture)

Narration iteration 1 (Oct 22). The slide generator reads this block.

**Narration: recap slide** (83 words)

<details><summary>Show narration</summary>

```
Three everyday promQL expressions, and each one ran in both places.

A label selector chooses which series you look at.

The rate of a counter tells you how fast it's climbing.

Sum by collapses the series into one row per label value, such as one per service.

Most, but not all, of promQL runs this way. Next, we build a real expression from these pieces: an error ratio for each service. And later in the module, we look at where the edges are.
```

Claims check:
- "Each one ran in both places": confirm against the take log.
- "Most, but not all": Elastic's limitations page and the PROMQL command page.
- "Next, we build ... an error ratio for each service": depends on the Video 2 outline being approved (`module1-video2-outline.md`, not yet committed). Change this line if Video 2's through-line changes.
- "Later in the module, we look at where the edges are": the Video 3 plan.

</details>

---

## After the take

1. Run the counters command (pre-roll step 2) again. `failed` should be unchanged.
2. Fill in the take log below and paste it back to me.
3. Rename each clip right away, for example `v1-B1-r1-prometheus.mp4`.

### Take log (fill in)

| Beat | Prometheus (value or count, time) | Elastic (value or count, time) | Seconds between runs | Retakes and notes |
|---|---|---|---|---|
| 3 (R1) | | | | |
| 4 (R3) | | | | |
| 5 (R6, frontend row) | | | | |


### Placeholders to fill from the take log

| Placeholder | Meaning | Source |
|---|---|---|
| `{{N_PROM}}` | Rung 1 series count, Prometheus | "N results" in clip B1 |
| `{{N_ELASTIC}}` | Rung 1 series count, Elastic | Discover's row count, or `series` from C2b |
| `{{PROM_VALUE}}` | Frontend calls per second, Prometheus (2 or 3 decimals) | Clip C1 |
| `{{ELASTIC_VALUE}}` | Same, Elastic | Clip C2 |
| `{{PCT_C}}` | Relative difference of the two values, in percent | Computed from the two values above |
| `{{SECONDS_C}}` | Seconds between the two runs | Take log |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Row counts, rung 3 | Clips D1, D2 |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | Clips D1, D2 |
| `{{PCT_D}}`, `{{SECONDS_D}}` | Difference in percent and seconds between runs, rung 3 | Computed and take log |

---

## If something goes wrong

- **An error in Elastic:** don't edit the command. Stop, copy the exact error text, and send it to me. Errors are findings.
- **Empty result in Elastic:** check the picker says **Last 1 hour** and the stack uptime. Try again.
- **Values differ more than a few percent:** rerun both sides within 15 s of each other, Prometheus first.
- **Prometheus shows no data:** check the stack is running, and the counters command.

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

- Type or paste: default is paste. Decide after the capture test.
- Kibana address bar: show, crop, or blur.
- Browser zoom level.
- Whether Game Bar records the mouse cursor (check in the test clip).
- Grafana as a second data source is untested, so nothing in this video may imply it.
- Copy-across idea for rung 1: copy the expression out of Prometheus's box and paste it between the parentheses of a staged Elastic skeleton, so the same text visibly moves across. Not adopted; it would change the rung 1 steps only.
- Opener closing: "judge the match yourself" (iteration 1) or the author's "observe essentially the same results".
- Narration: iteration 1 is awaiting the speech-engine test; expect iteration 2.
- Video 2's through-line (the error ratio) is referenced in the recap and is not yet approved.
