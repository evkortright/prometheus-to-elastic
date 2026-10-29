# Glossary and key technical facts

> Copied verbatim from docs/archive/handoff-module1-living.md, sections 10, on Oct 29, 2026, for path map v2 step 1. Numbers and wording are unchanged. The source is archived in step 3, with a one-line header only.

## 10. Glossary (running) and key technical facts

| Term | Plain meaning | Status and source |
|---|---|---|
| Metric | A named measurement, such as `traces_span_metrics_calls_total` | Standard |
| Label | A key and value on a series, such as `service_name="frontend"` | Standard |
| Series | One metric name plus one unique set of labels | Standard |
| Label matcher | A condition on a label inside `{}`; `=`, `!=`, `=~`, `!~` | Verified: https://next.prometheus.io/docs/querying/basics |
| Fully anchored regex | A regex must match the whole label value, so `frontend\|checkout` does not match `frontend-proxy` | Verified in Prometheus docs and in lab R2 on both sides |
| Instant vector | One sample per series at a single moment | Verified (Prometheus docs) |
| Range vector | A window of samples per series, written in square brackets such as `[5m]` | Standard; Elastic's functions page says range vector functions return an instant vector |
| Table tab and Graph tab | Prometheus runs an instant query on Table and a range query on Graph | Verified (Prometheus docs) |
| Counter | A cumulative metric that only increases or resets to zero on restart | Verified: https://prometheus.io/docs/concepts/metric_types/ |
| `rate()` | The per-second average rate of increase of a series over the range | Verified in Elastic's wording: https://www.elastic.co/docs/reference/query-languages/promql/functions/range-vector |
| Aggregation operator, `sum by` | Combines one instant vector into fewer elements; `by` keeps the named labels | Verified: https://prometheus.io/docs/prometheus/latest/querying/operators/ |
| `PROMQL` command | An ES\|QL source command: `PROMQL [option=value ...] [result_name=](expression)` | Lab setup section (from the command docs) |
| `index=` | The data stream to query: `metrics-generic.prometheus-default` | Lab |
| `time=?_tend` | Makes an instant query at the end of the date picker's range; leave it out for a range query with a chart | Lab (command docs) and Kibana docs for `?_tend`: https://www.elastic.co/docs/explore-analyze/query-filter/languages/esql-where |
| Wrapper | Our narration's word for everything around the expression in Elastic: the `PROMQL` command, its options (`index`, `time`) and the result name. It answers three questions: where this runs, when it is evaluated, and what the answer is called | Our term, not Elastic's; the pieces are from the command docs (see `PROMQL` command above) |
| Contract | The handoff for one video chat: the learning objective, audience, through-line, entry and exit sentences, entry knowledge, allowed and forbidden claims, the evidence and stack state needed, acceptance checks, deliverables and the files the chat owns | Our term (Oct 25) |
| Reset | The per-video procedure that clears all data and restarts the stack, so no video depends on another's data | Our term (Oct 25); the runbook is tracker row 26 |
| Date picker | PROMQL reads only data inside its range, so a window longer than the picker sees less data (lab R4: 9,391 versus 18,925 versus Prometheus 18,960 for `increase(...[30m])`) | Tested |
| ES\|QL | Elasticsearch Query Language | Verified (Kibana docs) |
| Remote write | How Prometheus sends its data to Elastic in this demo | Verified (register row 9) |
| `_timeseries` | The Elastic result column that holds a series' labels as JSON | Lab R1 |
| `step` | The evaluation time in an Elastic PROMQL result | Lab |
| Division of two aggregates | Both sides aggregated alike works; a series missing on one side drops out of the result | Lab R8 (both systems agree) and the limitations page |
| TSDS | Time series data stream: dimensions, series identity, metric types | **Not yet verified; check the TSDS docs before writing about it** |
