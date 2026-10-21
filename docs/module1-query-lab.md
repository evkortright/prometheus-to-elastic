# Module 1 — Query Lab

**Purpose:** Run each query yourself, first in Prometheus, then in Elastic, and record what happens. The results are the evidence behind all three Module 1 videos, so record what you actually see, including surprises.

**Feeds:** Video 1 (R1, R3, R4, R6), Video 2 (R1 to R8), Video 3 (P1 to P8).

Every command below is complete and ready to copy. The Prometheus commands go in the Prometheus UI. The ES|QL commands go in Kibana Discover.

---

## Setup

- Stack running for **at least 45 minutes**, so a Last 30 minutes range is full and `rate()` windows have settled.
- Prometheus UI at `http://localhost:9090`: use the **Table** tab for values and the **Graph** tab for shape.
- Kibana → Discover → **ES|QL** mode, time picker on **Last 1 hour** (use Last 30 minutes until the stack has run that long). **The picker must cover the longest window in the query:** PROMQL only reads data inside the picker's range, so a 30-minute window under a 15-minute picker sees about 15 minutes (see R4).
- Feature flag `paymentFailure` **off** for the whole lab.
- Before you start: `curl -s http://localhost:9090/metrics | grep '^prometheus_remote_storage_samples'` should show `samples_failed_total` at 0.

**Elastic syntax** (from the PROMQL command docs):

```
PROMQL [ <option>=<value> ... ] [ <result_name>= ](<PromQL expression>)
```

- `index=` names the data stream. Here it is always `metrics-generic.prometheus-default`.
- `time=?_tend` makes an **instant query**: one row per series, evaluated at the end of the time picker's range. This is the form to compare against Prometheus's Table tab.
- Leave `time=?_tend` out for a **range query**: one row per series per step, plus a chart.
- The result name (`calls=`, `request_rate=`, and so on) is arbitrary. It becomes the column name.
- The ES|QL commands are single-line so they paste cleanly.

**How to compare.** Run the Prometheus and Elastic versions within a few seconds of each other. Expect values that are close, not identical, because the two systems evaluate at slightly different moments. Record both numbers and note any difference larger than a few percent.

**Verdict key:** **Same** (works, values agree) · **Differs** (works, but the result or behavior differs) · **Error** (the query is rejected) · **Empty** (runs but returns nothing).

---

## Part 1 — The ladder (expected to work)

Video 1 needs R1, R3, R4, and R6 first.

### R1 — Label selector

Prometheus:
```promql
traces_span_metrics_calls_total{service_name="frontend"}
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name="frontend"})
```
Count of series in Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name="frontend"}) | STATS series = COUNT(*)
```
- Prometheus: 50 series, labels listed inline.
- Elastic: 50 series. Columns: `calls`, `step`, and `_timeseries` (a JSON column holding the labels, including `__name__`).
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 20): series count and label names agree. Presentation differs: inline labels versus a `_timeseries` JSON column. `step` is the evaluation time.

### R2 — Regex and negative matchers

Prometheus:
```promql
traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"}
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"})
```

Count form used on Oct 21 (it shows which series matched without listing all of them). Run with the picker on Last 1 hour.

Prometheus (Table tab):
```promql
count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"})
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend series=(count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"}))
```
Baseline, the same expressions with the `status_code!=` matcher removed:
```promql
count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout"})
```
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend series=(count by (service_name, status_code) (traces_span_metrics_calls_total{service_name=~"frontend|checkout"}))
```

Recorded results (Oct 21, series counts):

| service_name | status_code | Prometheus with `!=` (11:10) | Elastic with `!=` (11:13) | Prometheus baseline | Elastic baseline (11:14) |
|---|---|---|---|---|---|
| checkout | STATUS_CODE_UNSET | 8 | 8 | 8 | 8 |
| frontend | STATUS_CODE_UNSET | 36 | 36 | 36 | 36 |
| checkout | STATUS_CODE_ERROR | not returned | not returned | 2 | 2 |
| frontend | STATUS_CODE_ERROR | not returned | not returned | 14 | 14 |

- Prometheus: checkout 8 and frontend 36 series, both STATUS_CODE_UNSET (11:10 CDT).
- Elastic: the same two rows, 8 and 36 (11:13 CDT).
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 21): `frontend-proxy` is absent on both sides, so the regex `frontend|checkout` is fully anchored in both systems. The `!=` matcher removed exactly the ERROR series on both sides (14 for frontend, 2 for checkout; 16 in total). Frontend has 36 + 14 = 50 series, equal to the 50 recorded in R1 on Oct 20. These two services have no STATUS_CODE_OK series in this data.

### R3 — rate() on a counter

Use the summed form so each side returns one number.

Prometheus:
```promql
sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))
```
Elastic (instant):
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_rate=(sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])))
```
Elastic (range, for the chart):
```esql
PROMQL index=metrics-generic.prometheus-default frontend_rate=(sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])))
```
Optional, the unaggregated form (50 rows per side):
```promql
rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])
```
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_rate=(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))
```
- Prometheus (value): 8.888018467743953
- Elastic (value): 8.888018465483446
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 20): relative difference about 2.5e-10. In the unaggregated Elastic rows, `_timeseries` still showed `__name__` after `rate()`, whereas Prometheus drops the metric name; unconfirmed whether that is a real difference or how the column is built. The aggregated Elastic result has no `_timeseries` column; Prometheus shows `{}`.

### R4 — increase() on a counter

Use the summed form.

Prometheus:
```promql
sum(increase(traces_span_metrics_calls_total{service_name="frontend"}[30m]))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_increase=(sum(increase(traces_span_metrics_calls_total{service_name="frontend"}[30m])))
```
Optional, Elastic only. The docs describe a window that spans the whole date picker range:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_increase=(sum(increase(traces_span_metrics_calls_total{service_name="frontend"}[?_tend - ?_tstart])))
```
**Picker-width test** (same expression, only the picker changes). Run in quick succession:
1. Picker **Last 15 minutes**: Elastic instant query above.
2. Prometheus query above.
3. Picker **Last 1 hour**: Elastic instant query above.

Recorded results (Oct 20, steady traffic of about 10 req/s):

| Run | Value | Versus Prometheus |
|---|---|---|
| Prometheus | 18,960.0 | |
| Elastic, picker 15 min | 9,391.1 | 49.5% |
| Elastic, picker 1 hour | 18,924.9 | 99.8% (evaluated about 80 s later) |
| Earlier run, picker 15 min | Elastic 9,729.1 | Prometheus 18,745.9 (51.9%) |

- Verdict: ☐ Same ☑ Differs ☐ Error ☐ Empty. **Differs when the picker is narrower than the window; Same when the picker covers it.**
- Notes: the expression is identical in every run, and only the picker width changes the answer. The about-50% result matches only 15 of 30 minutes being visible at steady load. The docs say the time range comes from the date picker and recommend omitting range selectors when porting queries. They do not spell out this specific effect in the parts I read, so it is recorded as measured. The same effect likely explains the chart ramp at the left edge of the picker (a 5-minute `rate()` window filling up).

### R5 — Aggregation, whole system

Prometheus:
```promql
sum(rate(traces_span_metrics_calls_total[5m]))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend total_rate=(sum(rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus (value): 46.37547088042138 (run immediately before the Elastic query; time not recorded)
- Elastic (value): 46.375470912857935 (step 11:16:55 CDT, Oct 21)
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 21, picker 1 hour): relative difference about 7.0e-10. Prometheus shows the empty label set `{}`; Elastic returns only `total_rate` and `step`.

### R6 — Aggregation by label

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
Elastic (instant, sorted so it lines up with Prometheus):
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))) | SORT service_name
```
Elastic (range, for the chart):
```esql
PROMQL index=metrics-generic.prometheus-default request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus: 18 series; labels shown inline as `{service_name="..."}`.
- Elastic: 18 results; `request_rate`, `step`, and `service_name` as separate columns, with the same `step` on every row.
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 20, picker 1 hour, run back to back): same 18 services. Busy services agree within about 1 to 6% (frontend 10.242 versus 10.338, frontend-proxy 9.801 versus 10.084, flagd 8.605 versus 8.467, product-catalog 4.167 versus 4.234, cart 2.038 versus 2.150). Low-traffic services differ by up to about 13% (payment 0.129 versus 0.113), consistent with a few calls' worth of timing noise in a 5-minute window; this is an inference, not tested at a fixed evaluation time. Zero-traffic services (frontend-web, flagd-ui, load-generator) are 0 on both sides.

### R7 — Arithmetic with a scalar

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend per_minute=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60)
```
- Prometheus (frontend value, per minute): 767.3139428285692 (frontend-proxy 775.5646303858657). 18 results, 11:19 CDT, Oct 21.
- Elastic (frontend value): 767.3139427675849 (frontend-proxy 775.5646303242174). Step 11:19:05 CDT.
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 21, picker 1 hour): relative differences about 7.9e-11 on both compared rows, with the same sign. The cause of the near-identical gaps is unexplained. Prometheus returned 18 results, with frontend-web, flagd-ui and load-generator at 0, as in R6. The Elastic row count was not recorded.

### R8 — Error ratio (arithmetic between two aggregated results)

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
Elastic (instant):
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend error_ratio=(sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
Elastic (range, for the chart):
```esql
PROMQL index=metrics-generic.prometheus-default error_ratio=(sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus (which services appear? frontend and payment values): 8 services (as pasted). payment 0.03125, flagd 0.0008347245409015025, and ad, recommendation, frontend-proxy, frontend, shipping and checkout all 0. Run 11:26 CDT, Oct 21.
- Elastic (which services appear?): the same 8 services. payment 0.0312500000000003, flagd 0.0008347245409015352, the other six 0. Step 11:26:21 CDT.
- Verdict: ☑ Same ☐ Differs ☐ Error ☐ Empty
- Notes (Oct 21, picker 1 hour): yes, services with no matching error series drop out in both systems. The same 10 services are absent on both sides: frontend-web, flagd-ui, load-generator, telemetry-docs, quote, email, currency, cart, product-catalog, image-provider. The nonzero values agree to about 1e-14 (payment) and 4e-14 (flagd), relative. The row counts were assumed from the pasted rows, not read from Discover. A first attempt at 11:22 was discarded because the Prometheus paste was the R7 table, not the R8 result. Payment's ratio was 0 at 11:22:53 and 0.03125 at 11:26 with `paymentFailure` off.

---

## Part 2 — Probes (documented limits and behaviors to observe)

The docs list P1 to P4 as unsupported and say they return a client error. Confirm each by running it. Run each in Prometheus first. If Prometheus rejects it, note that too. Copy the **exact error text** from Elastic.

### P1 — Explicit vector matching with on()

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / on(service_name) sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend matched=(sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) / on(service_name) sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P2 — Subquery

Prometheus:
```promql
max_over_time(sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))[30m:1m])
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend peak=(max_over_time(sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))[30m:1m]))
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P3 — The @ modifier

Prometheus (may need a feature flag; note what you see):
```promql
traces_span_metrics_calls_total{service_name="frontend"} @ end()
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend at_end=(traces_span_metrics_calls_total{service_name="frontend"} @ end())
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P4 — Set operator: and

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) and sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m]))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend both=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) and sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])))
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P5 — Division between two different unaggregated metrics

First find the metric names. Run this in Prometheus only (selecting by metric name pattern is itself a documented limit in Elastic):
```promql
count by (__name__) ({__name__=~"traces_span_metrics.*"})
```
Then try this pair, which assumes the span-metrics duration sum and count exist (names unverified; swap in what you found):

Prometheus:
```promql
traces_span_metrics_duration_milliseconds_sum / traces_span_metrics_duration_milliseconds_count
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend avg_duration=(traces_span_metrics_duration_milliseconds_sum / traces_span_metrics_duration_milliseconds_count)
```
- Metric names used:
- Prometheus (rows returned):
- Elastic (rows returned; the docs say this returns no results, not an error):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P6 — No range selector

Prometheus (expected to reject it):
```promql
rate(traces_span_metrics_calls_total{service_name="frontend"})
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend implicit_rate=(rate(traces_span_metrics_calls_total{service_name="frontend"}))
```
- Prometheus:
- Elastic (accepted? compare the value to R3):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P7 — Step control

Run all three in Elastic and compare. No Prometheus command; this is an Elastic-only option.
```esql
PROMQL index=metrics-generic.prometheus-default step=10s request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
```esql
PROMQL index=metrics-generic.prometheus-default step=1m request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
```esql
PROMQL index=metrics-generic.prometheus-default request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
- Row counts and the gap between steps for each:
- Does the automatic step match what the time picker implies?
- Notes (earlier we saw one-minute steps once and ten-second steps elsewhere):

### P8 — Ranking with topk (untested)

Prometheus:
```promql
topk(3, sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend top3=(topk(3, sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))))
```
- Prometheus (which three, in what order):
- Elastic:
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

---

## Summary (fill in last)

| ID | Verdict | One line |
|---|---|---|
| R1 | Same | 50 series, same labels; presentation differs (`_timeseries` column) |
| R2 | Same | Regex anchored and `!=` agree: frontend 36 and checkout 8 UNSET series; baseline adds 14 and 2 ERROR series on both sides |
| R3 | Same | 8.888018468 versus 8.888018465 (summed, instant) |
| R4 | Differs / Same | Half the value when the picker is narrower than the window; matches when the picker covers it |
| R5 | Same | 46.375470881 versus 46.375470913 (summed, instant) |
| R6 | Same | 18 services; busy ones within about 6%, small ones within about 13% (timing) |
| R7 | Same | frontend 767.31394283 versus 767.31394277 per minute; `* 60` works |
| R8 | Same | Same 8 services; 10 without error series drop out on both sides; nonzero values agree to about 1e-14 |
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |
| P5 | | |
| P6 | | |
| P7 | | |
| P8 | | |

Screenshots worth keeping: R6 side by side, R8 in both, P1's error text, P6 in both, P7's three runs.
