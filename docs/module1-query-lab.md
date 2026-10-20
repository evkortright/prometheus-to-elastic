# Module 1 — Query Lab

**Purpose:** Type each query yourself, first in Prometheus, then in Elastic, and record what happens. The results are the evidence behind all three Module 1 videos, so record what you actually see, including surprises.

**Feeds:** Video 1 (rungs R1 to R4, R6), Video 2 (rungs R1 to R8), Video 3 (probes P1 to P8).

---

## Setup

- Stack running for **at least 45 minutes**, so a Last 30 minutes range is full and `rate()` windows have settled.
- Prometheus UI at `http://localhost:9090` (use the **Table** tab for values, **Graph** for shape).
- Kibana → Discover → **ES|QL** mode, time picker on **Last 30 minutes**.
- Keep `paymentFailure` **off** for the whole lab unless a rung says otherwise.

**The Elastic wrapper.** Everything in the PromQL box goes between the parentheses:

```esql
PROMQL index=metrics-generic.prometheus-default result=( <PromQL expression> )
```

Type the same expression in Prometheus without the wrapper.

**How to compare values.** Prometheus's Table tab shows one value at the moment you click Execute. A Kibana range query returns one row per step. For a like-for-like number, add `time=?_tend` to evaluate once at the end of the date picker's range:

```esql
PROMQL index=metrics-generic.prometheus-default time=?_tend result=( <PromQL expression> )
```

Run both within a few seconds of each other. Expect values that are close, not identical, because the two systems evaluate at slightly different moments. Record both numbers, and note any difference larger than a few percent.

**Verdict key:** **Same** (works, values agree) · **Differs** (works, but the result or behavior differs) · **Error** (the query is rejected) · **Empty** (runs but returns nothing).

---

## Part 1 — The ladder (expected to work)

### R1 — Label selector
```promql
traces_span_metrics_calls_total{service_name="frontend"}
```
- Prometheus (series count, a sample value):
- Elastic (rows, columns shown, the `_timeseries` column?):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R2 — Regex and negative matchers
```promql
traces_span_metrics_calls_total{service_name=~"frontend|checkout", status_code!="STATUS_CODE_ERROR"}
```
- Prometheus:
- Elastic:
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R3 — rate() on a counter
```promql
rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])
```
- Prometheus (value):
- Elastic (value, with `time=?_tend`):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R4 — increase() on a counter
```promql
increase(traces_span_metrics_calls_total{service_name="frontend"}[1h])
```
- Prometheus (value):
- Elastic (value, with `time=?_tend`):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (data only covers the time the stack has run; say how long that is):

### R5 — Aggregation, whole system
```promql
sum(rate(traces_span_metrics_calls_total[5m]))
```
- Prometheus (value):
- Elastic (value, with `time=?_tend`):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R6 — Aggregation by label
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
- Prometheus (number of series, frontend value):
- Elastic (rows, frontend value, with `time=?_tend`):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (count the services in each; we saw 18 in Prometheus):

### R7 — Arithmetic with a scalar
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) * 60
```
- Prometheus (frontend value, per minute):
- Elastic (frontend value):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes:

### R8 — Error ratio (arithmetic between two aggregated results)
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m]))
  / sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
- Prometheus (which services appear? frontend and payment values):
- Elastic (which services appear?):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (services with no error series: do they drop out in both?):

---

## Part 2 — Probes (documented limits and behaviors to observe)

The docs list P1 to P4 as unsupported and say they return a client error. Confirm each by running it. Run each in Prometheus first; if Prometheus rejects it, note that too.

### P1 — Explicit vector matching with on()
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m]))
  / on(service_name) sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P2 — Subquery
```promql
max_over_time(sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))[30m:1m])
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P3 — The @ modifier
```promql
traces_span_metrics_calls_total{service_name="frontend"} @ end()
```
- Prometheus (may need a feature flag; note what you see):
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P4 — Set operator: and
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
  and sum by (service_name) (rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m]))
```
- Prometheus:
- Elastic (exact error text):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P5 — Division between two different unaggregated metrics
Pick two raw metrics with matching labels from Prometheus's autocomplete. A likely pair is the span-metrics duration sum and count (names unverified):
```promql
traces_span_metrics_duration_milliseconds_sum / traces_span_metrics_duration_milliseconds_count
```
- Prometheus (rows returned):
- Elastic (rows returned; the docs say this returns no results, not an error):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty
- Notes (metric names you used):

### P6 — No range selector
```promql
rate(traces_span_metrics_calls_total{service_name="frontend"})
```
- Prometheus (expected to reject it):
- Elastic (accepted? what window is used?):
- Verdict: ☐ Same ☐ Differs ☐ Error ☐ Empty

### P7 — Step control
Run the same expression three times in Elastic with different steps:
```esql
PROMQL index=metrics-generic.prometheus-default step=10s result=( sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) )
PROMQL index=metrics-generic.prometheus-default step=1m  result=( sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) )
PROMQL index=metrics-generic.prometheus-default          result=( sum by (service_name) (rate(traces_span_metrics_calls_total[5m])) )
```
- Row counts and gap between steps for each:
- Does the automatic step match what the time picker implies?
- Notes (earlier we saw one-minute steps once and ten-second steps elsewhere):

### P8 — Ranking with topk (untested)
```promql
topk(3, sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
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
