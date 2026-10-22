# Module 1, Video 1 — Run-sheet (screen capture)

**Video:** Your PromQL, running in Elastic (three rungs: label selector, `rate()`, `sum by`)
**Status:** Draft v1, Oct 22, 2026. Follows the outline (`module1-video1-outline.md`, commit `edf75cf`).
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

## Beat 2 — Setup (Clip A)

1. Tab 1 in view (Prometheus, Table tab, empty box). **▶ START.** HOLD 4 s.
2. Click Tab 2 (Kibana Discover, ES|QL mode, Last 1 hour, empty editor). HOLD 4 s.
3. **■ STOP.**

Nothing to verify here. The claim that both systems hold the same metrics is shown at rung 1.

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
