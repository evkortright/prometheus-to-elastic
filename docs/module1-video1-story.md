# Module 1, Video 1 — The story: Your PromQL, running in Elastic

**For:** reading aloud and peer review.
**Status:** draft, October 22, 2026. Numbers are placeholders until the recording.
**Source of truth:** the voice-over in `module1-video1-run-sheet.md`. This file is generated from it. If they differ, the run-sheet wins and this file is regenerated.

---

## About this video

- **Audience:** an SRE who uses PromQL and Grafana every day. A technical video for a technical audience, not a marketing video.
- **Objective (LO1):** recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
- **Length:** about 621 spoken words, roughly four minutes of speech, plus pauses on screen.
- **How to read it:** the quoted text is spoken. The italic lines say what is on screen. Anything in double curly braces is a number that will be filled in from the recording.

## The story in a paragraph

An SRE who runs PromQL every day wonders what they would have to change to run it on Elastic. The video makes a measured claim: most common expressions carry over, and what is new is a wrapper around the expression. It then tests the claim live, with three expressions of increasing difficulty, each run in Prometheus and then in Elastic, so the viewer can compare the output and judge. It ends by naming what carried over, saying plainly that not everything does, and pointing at what comes next.

---

## The script

*Opener slide.*

> Most common promQL expressions run unchanged in Elastic.
>
> Elastic's promQL command, part of the Elasticsearch Query Language, evaluates a promQL expression against metrics stored in Elastic. The expression is the same text you'd run in Prometheus. What you add is a wrapper: the ESQL command and a few parameters.
>
> We'll test that with three expressions you likely use already, first in Prometheus, then in Elastic.
>
> First, select series with a label selector.
>
> Second, take the rate of a counter.
>
> Third, aggregate with sum by.
>
> Then we compare the output, and you can judge the match yourself.

*Setup: Prometheus's Table tab with an empty expression box, then Kibana's Discover in ES\|QL mode with the date picker on the last hour.*

> Two screens. In one, Prometheus, on the Table tab, with an empty expression box: the place you'd run an expression today. In the other, Kibana's Discover, in E-S-Q-L mode, pointed at the same metrics. In this demo, Prometheus sends them to Elastic through remote write, so both systems hold the same data. One setting to notice: the date picker is set to the last hour. The prom-Q-L command reads only the data inside that range, so we're keeping it wide.

*Rung 1, Prometheus: the selector is pasted, the cursor underlines the metric name and then the matcher, then Execute.*

> We'll climb a short ladder: three expressions, simplest first, each checked in both places. Rung one: a label selector. Our metric is traces span metrics calls total, a counter of calls that the OpenTelemetry Collector generates from traces. Add curly braces and a label matcher, service name equals frontend, and we've selected just that service's series. Run it. {{N_PROM}} series, each with its own set of labels.

*Rung 1, Elastic: the wrapper is already in the editor. The cursor underlines the expression, then the command, index, time and result name. Then Run.*

> Now Elastic. Look inside the parentheses: that's the expression we just ran in Prometheus. The rest is the wrapper. The line starts with the prom-Q-L command, and three parameters answer three questions. Where should this run? That's index, the data stream that holds the metrics. When? That's time: the end of the date picker's range, so the expression is evaluated once, like the Table tab. And what do we call the answer? That's calls, the name of the result. Run it. {{N_ELASTIC}} series, against {{N_PROM}} in Prometheus. The labels appear in a column instead of inline, but that's only display. The only thing we changed is the wrapper.

*Rung 2, Prometheus: the rate expression is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears.*

> Rung two: the rate of a counter. On its own, a counter just climbs: it counts every call since the start. What you usually want is how fast. Rate takes the counter over a window, here five minutes in square brackets, and returns its per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: the frontend's calls per second. Run it. {{PROM_VALUE}}.

*Rung 2, Elastic: the same expression inside the wrapper, the result name highlighted, then Run.*

> Same expression in Elastic, same wrapper. Only the result name changes, now frontend rate. {{ELASTIC_VALUE}}, against {{PROM_VALUE}} in Prometheus. The two runs were about {{SECONDS_C}} seconds apart, and the values differ by about {{PCT_C}} percent.

*Rung 3, Prometheus: the sum-by expression is pasted, the cursor underlines the sum-by clause, then Execute. A table with one row per service appears, and the cursor rests on the frontend row.*

> Rung three: aggregate by a label. So far we have one number for the whole frontend, but the question you ask is usually per service. Sum by service name keeps that label and adds up the rest, so we get one row per service. Run it. {{ROWS_PROM}} rows. Frontend: {{PROM_FRONTEND}} calls per second.

*Rung 3, Elastic: the same expression inside the wrapper, then Run. The cursor rests on the frontend row.*

> Same expression in Elastic, same wrapper. {{ROWS_ELASTIC}} rows. Frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus: within about {{PCT_D}} percent, with the two runs about {{SECONDS_D}} seconds apart.

*Recap slide.*

> Three everyday promQL expressions, and each one ran in both places.
>
> A label selector chooses which series you look at.
>
> The rate of a counter tells you how fast it's climbing.
>
> Sum by collapses the series into one row per label value, such as one per service.
>
> Most, but not all, of promQL runs this way. Next, we build a real expression from these pieces: an error ratio for each service. And later in the module, we look at where the edges are.

---

## For reviewers: what to look at

1. Does the opening claim ("most common expressions run unchanged") feel honest, or does it promise too much?
2. Is the wrapper explained clearly enough (where it runs, when it is evaluated, what the result is called)?
3. Are the reasons for `rate` and for `sum by` stated well enough for someone who already knows them?
4. Is anything missing that you would want answered before trusting this?
5. Is the pace right for a viewer who is checking each claim against the screen?

## Claims and evidence

| Claim in the script | Status | Source |
|---|---|---|
| Most common PromQL expressions run unchanged in Elastic, but not all | Docs | Elastic's PromQL limitations page: https://www.elastic.co/docs/reference/query-languages/promql/promql-limitations (retrieved Oct 21, 2026), and the note on the PROMQL command page |
| ES\|QL is the Elasticsearch Query Language | Verified | Kibana docs: https://www.elastic.co/guide/en/kibana/current/try-esql.html |
| The wrapper is the command plus parameters: index, time, and a result name | Tested | The query lab (`module1-query-lab.md`), syntax section, taken from the command docs |
| `time` set to the end of the date picker's range, so the expression is evaluated once | Docs and tested | Kibana docs for the time-filter parameters: https://www.elastic.co/docs/explore-analyze/query-filter/languages/esql-where. Each result row carried one evaluation time. |
| PROMQL reads only data inside the date picker's range | Tested | Lab R4 (about half the Prometheus value when the picker was narrower than the window) |
| Prometheus sends its data to Elastic by remote write, so both systems hold the same data | Verified | Claims register row 9; lab R1 (same series and labels on both sides, Oct 20) |
| The metric is a counter of calls generated from traces by the OpenTelemetry Collector | Verified | `docs/otel-collector-reference.md` |
| A counter is cumulative and only increases (or resets on restart) | Verified | Prometheus metric types: https://prometheus.io/docs/concepts/metric_types/ |
| `rate` gives the per-second average rate of increase over the window | Verified | Elastic's range vector functions page: https://www.elastic.co/docs/reference/query-languages/promql/functions/range-vector |
| `sum by` keeps the named label and aggregates the rest | Verified | Prometheus operators page: https://prometheus.io/docs/prometheus/latest/querying/operators/ |
| Each rung gives agreeing values in both systems | Tested, to be re-confirmed | Lab R1, R3, R6 (Oct 20) and R5, R7, R8 (Oct 21); the recording's take log gives the final numbers |

## Still open before recording

- Hear it through the speech engine, then revise (iteration 2).
- Every `{{placeholder}}` is filled from the take log.
- Confirm in the take that the label sets match, that the wrapper really is the only change, and that each rung ran in both places.
- The recap's pointer to an error ratio depends on Video 2's through-line, which is not yet approved.
- The opener's closing line has an alternative: "observe essentially the same results".
