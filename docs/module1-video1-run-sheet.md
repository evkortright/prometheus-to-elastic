# Module 1, Video 1 — Run-sheet (screen capture)

**Video:** Your PromQL, running in Elastic (three rungs: label selector, `rate()`, `sum by`)
**Status:** Draft v2, Oct 22, 2026. Follows the outline (`module1-video1-outline.md`, commit `edf75cf`). v2 adds the voice-over: the opener is the author's draft, kept verbatim; the demo-beat voice-over is a first draft in the same style.
**Commands:** taken from the query lab (R1, R3, R6). They were verified on Oct 20 and Oct 21 on the previous dataset. **Run C1 to C6 once as a rehearsal on the current stack before the real take.**
**Recording:** Windows Game Bar on the desktop. Narration is added afterwards, so record without audio.

---

## How to use this sheet

- **Laptop** shows this sheet. **Desktop** runs the capture.
- Game Bar: **Win + Alt + R** starts and stops. It records one app window at a time, so use **one browser window with two tabs**: Tab 1 = Prometheus, Tab 2 = Kibana.
- The commands are at the end of this file (C1 to C6). Open this same file on the desktop in a **second window** to copy from. Never record that window.
- Markers: **▶ START** and **■ STOP** are Win + Alt + R. **HOLD n s** means stay still, mouse included. **✂ CUT** means stop recording, copy the command, click back into the recorded window, start again. Each clip joins in DaVinci Resolve.
- **Method: PASTE (default).** Reasons: the lines are long; pasting keeps the gap between the Prometheus run and the Elastic run short, and short gaps gave much tighter agreement in the lab (an inference, not a tested rule); and code editors can auto-close brackets and quotes while you type (not verified for this editor). Switch to typing only if you decide to after the capture test.
- **Timing rule:** run Prometheus first, then Elastic **within about 15 seconds**.
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

Author's draft of Oct 22, kept verbatim (a double space was removed). The slide generator reads this block.

<details><summary>Show narration</summary>

```
Most common promQL expressions run unchanged in Elastic.

Elastic's promQL command, part of the Elasticsearch Query Language, evaluates a promQL expression against metrics stored in Elastic. The expression stays the same. What you add is an ESQL command wrapper and parameters, such as the index to query.

In this demo, Prometheus sends its data to Elastic through remote write, so both systems hold the same metrics. We'll run three expressions you likely use already, first in Prometheus, then in Elastic.

First, select series with a label selector.

Second, aggregate with sum by.

Third, take the rate of a counter. Then we compare the output and observe essentially the same results.
```

Notes:
- "Most common ... run unchanged" follows Elastic's limitations page (the majority of expressions run unchanged; claims register row 1). The next paragraph explains the wrapper, so "unchanged" refers to the expression.
- "Part of the Elasticsearch Query Language": verified in the Kibana docs (Elasticsearch Query Language, ES|QL).
- "Observe essentially the same results" is a claim about the footage. **Confirm it against the take log; if a rung differs, change the sentence.**
- Test the TTS spelling of `promQL` and `ESQL`. If they are misread, use `prom-Q-L` and `E-S-Q-L`.

</details>

---

## Beat 2 — Setup (Clip A)

1. Tab 1 in view (Prometheus, Table tab, empty box). **▶ START.** HOLD 4 s.
2. Click Tab 2 (Kibana Discover, ES|QL mode, Last 1 hour, empty editor). HOLD 4 s.
3. **■ STOP.**

Nothing to verify here. The claim that both systems hold the same metrics is shown at rung 1.

**Voice-over: Clip A** (62 words)

<details><summary>Show voice-over</summary>

```
Here's the setup. This is Prometheus, on the Table tab, with an empty expression box: the same place you'd run an expression today. And this is Kibana's Discover, in E-S-Q-L mode, looking at the metrics Prometheus sent over. One thing to notice: the date picker is set to the last hour. Keep it wide like this. Video 3 explains why it matters.
```

Claims check:
- "Metrics Prometheus sent over": remote write, verified (register row 9).
- "Keep it wide ... Video 3 explains why it matters": the picker effect was tested (lab R4); the mechanism is deliberately left for Video 3. **Decision: keep this line or cut it.**

</details>

---

## Beat 3 — Rung 1: label selector (R1)

Expression: `traces_span_metrics_calls_total{service_name="frontend"}`

**Clip B1 (Prometheus)**
1. Tab 1. **✂ CUT:** copy **C1**. Click into the query box. **▶ START.**
2. Paste C1. Click **Execute**. Wait for the rows.
3. HOLD 4 s with the "N results" line in view. **Write down N.**
4. Move the cursor slowly under the expression. HOLD 3 s.
5. **■ STOP.**

**Clip B2 (Elastic)**
1. Tab 2. **✂ CUT:** copy **C2**. Click into the editor. **▶ START.**
2. Paste C2. Run it. HOLD 4 s with the rows in view.
3. Move the cursor slowly under the expression, which is the part inside the parentheses. HOLD 3 s.
4. **First rung only.** Move the cursor over the extra words, in this order, 2 s on each: `PROMQL`, `index=metrics-generic.prometheus-default`, `time=?_tend`, `calls=(` and the closing `)`.
5. If Discover shows no row count: **✂ CUT**, copy **C2b**, paste, run, and HOLD 4 s on `series = N`. **Write down N.**
6. **■ STOP.**

Notes: the rows will not appear in the same order on the two sides, and Elastic holds the labels in a `_timeseries` column. Point at the count and at one label set, not at row order.

**Voice-over: Clip B1** (53 words)

<details><summary>Show voice-over</summary>

```
Rung one: a label selector. We start with the metric name, traces span metrics calls total. It's a counter of calls, generated from traces by the OpenTelemetry Collector. Then, in curly braces, we filter by label: service name equals frontend. Run it. Prometheus returns {{N_PROM}} series, each with its own set of labels.
```

Claims check:
- Metric derived from traces by the Collector: `docs/otel-collector-reference.md`.
- `{{N_PROM}}`: from the take log.

</details>

**Voice-over: Clip B2** (86 words)

<details><summary>Show voice-over</summary>

```
Now the same expression in Elastic. Run it: {{N_ELASTIC}} series. Prometheus gave {{N_PROM}}. Look inside the parentheses. That's exactly the expression we ran in Prometheus. Around it is what you add. The prom-Q-L command. Index, which names the data stream that holds the metrics. Time, the end of the date picker's range, so the expression is evaluated once, at that moment, just like the Table tab. And calls, a name for the result. One difference in presentation: the labels sit in a column instead of inline.
```

Claims check:
- `?_tend` is the end of the date picker's range: Kibana docs (the `?_tstart` and `?_tend` parameters sync with the time filter).
- "Evaluated once, at that moment, like the Table tab": tested (one `step` value per row, equal to the run time; Prometheus's Table tab is an instant query per its docs). The PROMQL command's own wording for `time` is not yet read.
- "Labels in a column": lab R1 (`_timeseries`).
- **Confirm in the take that the label sets match** before keeping the sentence about the presentation difference.

</details>

---

## Beat 4 — Rung 2: `rate()` on a counter (R3)

Expression: `sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))`

**Clip C1 (Prometheus)**
1. Tab 1. **✂ CUT:** copy **C3**. Click into the query box (clear it first). **▶ START.**
2. Paste C3. **Execute.** HOLD 4 s with the single value in view. **Write down the value and the time.**
3. Cursor under the expression. HOLD 3 s.
4. **■ STOP.** Then go straight to Clip C2.

**Clip C2 (Elastic), within about 15 s of the Prometheus run**
1. Tab 2. **✂ CUT:** copy **C4**. **▶ START.**
2. Clear the editor, paste C4, run. HOLD 4 s with `frontend_rate` in view. **Write down the value.**
3. Cursor under the expression. HOLD 3 s.
4. **■ STOP.**

Notes: Prometheus shows `{}` for the empty label set, and Elastic returns only `frontend_rate` and `step`. Don't point this out unless the narration needs it.

**Voice-over: Clip C1** (51 words)

<details><summary>Show voice-over</summary>

```
Rung two: the rate of a counter. Rate takes a counter and returns its per-second average rate of increase over the range in square brackets, here five minutes. This metric has many series, so we wrap it in sum to get one number: the frontend's calls per second. Run it. {{PROM_VALUE}}.
```

Claims check:
- `rate`: per-second average rate of increase of the series in the range vector (Elastic's range vector functions page).
- "Counter" is used but not defined; the official Prometheus definition is still to be fetched.

</details>

**Voice-over: Clip C2** (34 words)

<details><summary>Show voice-over</summary>

```
Same expression in Elastic, same wrapper. Only the result name changes, now frontend rate. {{ELASTIC_VALUE}}. Prometheus said {{PROM_VALUE}}. They agree to within about {{PCT_C}} percent, and the two runs were about {{SECONDS_C}} seconds apart.
```

Claims check:
- Values and gap: from the take log.
- If the relative difference is larger than about 1 percent, **rewrite this sentence** instead of filling the template.

</details>

---

## Beat 5 — Rung 3: `sum by` (R6)

Expression: `sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`

**Clip D1 (Prometheus)**
1. Tab 1. **✂ CUT:** copy **C5**. Clear the box. **▶ START.**
2. Paste C5. **Execute.** HOLD 4 s. The table has one row per service. **Write down the row count.**
3. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
4. **■ STOP.** Then go straight to Clip D2.

**Clip D2 (Elastic), within about 15 s of the Prometheus run**
1. Tab 2. **✂ CUT:** copy **C6**. **▶ START.**
2. Clear the editor, paste C6, run. HOLD 4 s. **Write down the row count.**
3. Cursor on the **frontend** row. HOLD 3 s. **Write down its value.**
4. **■ STOP.**

Notes:
- Point at **frontend** (or another busy service), not at a low-traffic one. In the lab, low-traffic services differed by up to about 13%, which looked like timing noise (an inference).
- Zero-traffic services show 0 on both sides.

**Voice-over: Clip D1** (38 words)

<details><summary>Show voice-over</summary>

```
Rung three: aggregate by a label. Sum by service name adds up the rates for each service, so instead of one number we get one row per service. Prometheus returns {{ROWS_PROM}} rows. Here's frontend: {{PROM_FRONTEND}} calls per second.
```

Claims check:
- `sum by`: aggregation operators combine one instant vector into fewer elements; the `by` clause preserves the named label (Prometheus operators page).

</details>

**Voice-over: Clip D2** (44 words)

<details><summary>Show voice-over</summary>

```
Same expression in Elastic. After the pipe, the sort is plain E-S-Q-L. It just puts the services in a readable order. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus. That's within about {{PCT_D}} percent, with the two runs about {{SECONDS_D}} seconds apart.
```

Claims check:
- The pipe and `SORT` are ES|QL, not PromQL: ES|QL commands can continue after the PROMQL command (register row 11).
- Prometheus's table order is not alphabetical, so the narration does not say the rows line up.
- Values and gap: from the take log.

</details>

---

## Beat 6 — Recap slide (no capture)

Pending. The earlier recap draft was written in the old style. It will be rewritten in the author's style after the demo voice-over is approved. It must keep the honest sentence (most, but not all; Video 3 looks at the edges) and the claim about the values, which depends on the take log.

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

**C6** — Elastic, rung 3 (sorted so it lines up with Prometheus)
```
PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))) | SORT service_name
```

---

## Still open

- Type or paste: default is paste. Decide after the capture test.
- Kibana address bar: show, crop, or blur.
- Browser zoom level.
- Whether Game Bar records the mouse cursor (check in the test clip).
- Grafana as a second data source is untested, so nothing in this video may imply it.
- Clip A: keep or cut the "keep the date picker wide, Video 3 explains why" line.
- Narration style: first draft; expect rewrites after the first take.
- Recap slide narration: rewrite in the author's style after the demo voice-over is approved.
