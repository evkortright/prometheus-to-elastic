# Module 1 — Query Lab

**Purpose:** Run each query yourself, first in Prometheus, then in Elastic, and record what happens. The results are the evidence behind all three Module 1 videos, so record what you actually see, including surprises.

**Feeds:** Video 1 (R1, R3, R4, R6), Video 2 (R1 to R8), Video 3 (P1 to P8).

Every command below is complete and ready to copy. The Prometheus commands go in the Prometheus UI. The ES|QL commands go in Kibana Discover.

---

## Setup

- Stack running for **at least 45 minutes**, so a Last 30 minutes range is full and `rate()` windows have settled.
- Prometheus UI at `http://localhost:9090`: use the **Table** tab for values and the **Graph** tab for shape.
- Kibana → Discover → **ES|QL** mode, time picker on **Last 30 minutes**.
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
- Prometheus (series count, a sample value):
- Elastic (rows, columns shown):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R2 — Regex and negative matchers

Prometheus:
```promql
traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"}
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"})
```
- Prometheus:
- Elastic:
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R3 — rate() on a counter

Prometheus:
```promql
rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])
```
Elastic (instant):
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_rate=(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))
```
Elastic (range, for the chart):
```esql
PROMQL index=metrics-generic.prometheus-default frontend_rate=(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))
```
- Prometheus (value):
- Elastic (value):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R4 — increase() on a counter

Prometheus:
```promql
increase(traces_span_metrics_calls_total{service_name="frontend"}[30m])
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_increase=(increase(traces_span_metrics_calls_total{service_name="frontend"}[30m]))
```
Optional, Elastic only. The docs show a window that stretches over the whole date picker range, which Prometheus has no equivalent for. Compare it against the 30m version above:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_increase=(increase(traces_span_metrics_calls_total{service_name="frontend"}[?_tend - ?_tstart]))
```
- Prometheus (value):
- Elastic (value, both versions):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (how long has the stack been running?):

### R5 — Aggregation, whole system

Prometheus:
```promql
sum(rate(traces_span_metrics_calls_total[5m]))
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend total_rate=(sum(rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus (value):
- Elastic (value):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R6 — Aggregation by label

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
Elastic (instant):
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
Elastic (range, for the chart):
```esql
PROMQL index=metrics-generic.prometheus-default request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```
- Prometheus (number of series, frontend value; we saw 18 services earlier):
- Elastic (number of rows, frontend value):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R7 — Arithmetic with a scalar

Prometheus:
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60
```
Elastic:
```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend per_minute=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60)
```
- Prometheus (frontend value, per minute):
- Elastic (frontend value):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

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
- Prometheus (which services appear? frontend and payment values):
- Elastic (which services appear?):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (services with no error series: do they drop out in both?):

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
| R1 | | |
| R2 | | |
| R3 | | |
| R4 | | |
| R5 | | |
| R6 | | |
| R7 | | |
| R8 | | |
| P1 | | |
| P2 | | |
| P3 | | |
| P4 | | |
| P5 | | |
| P6 | | |
| P7 | | |
| P8 | | |

Screenshots worth keeping: R6 side by side, R8 in both, P1's error text, P6 in both, P7's three runs.
