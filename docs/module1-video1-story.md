# Module 1, Video 1 — The story: Your PromQL, running in Elastic

**For:** reading aloud and peer review.
**Status:** draft, October 26, 2026, regenerated from the approved narrative and run-sheet v5.1. Numbers are placeholders until the take.
**Source of truth:** the narrative (`module1-video1-narrative.md`) for the seven demo blocks, and the run-sheet (`module1-video1-run-sheet.md`, beats 1 and 6) for the two slide narrations. This file is generated from them. If they differ, they win and this file is regenerated.

---

## About this video

- **Audience:** an SRE who uses PromQL and Grafana every day. A technical video for a technical audience, not a marketing video.
- **Objective (LO1):** recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
- **Length:** about 730 spoken words in nine blocks, which is roughly five minutes of speech at an assumed 150 words a minute (an estimate, not a measurement), plus the pauses on screen.
- **How to read it:** the quoted text is spoken. The italic lines say what is on screen. Anything in double curly braces is a number that will be filled in from the take log.

## The story in a paragraph

An SRE has spent years on scrape configs, dashboards and PromQL, and wonders whether moving to Elastic means rebuilding all of it. The video turns the question into a game: three expressions, each run twice, first in Prometheus and then in Elastic, while the viewer tries to catch the expression changing. It never changes. What changes is a wrapper around it, which here makes just three choices: where it runs, when it is evaluated, and what the answer is called. The video ends by saying plainly that most, though not all, of PromQL runs in Elastic, and that the edges come later.

---

## The script

*Opener slide (Shape D: a hook, a definition, a lead-in, three steps, a closing line).*

> You've spent years on your monitoring, and the real question about Elastic isn't whether it's powerful. It's whether you'd have to rebuild what you've already built.
>
> prom-Q-L is the language you use to ask Prometheus questions about your metrics, and an expression is one line of it.
>
> Three expressions, run twice. You probably know each one by heart, and we'll run each first in Prometheus, then in Elastic.
>
> First, a label matcher. It narrows a metric to the series you name, such as one service.
>
> Second, rate. It turns a counter that keeps climbing into a rate per second.
>
> Third, sum by. It adds those rates up and keeps one row for each service.
>
> Your job is simple: watch the expression, and try to catch it changing.

*Prometheus's Table tab with an empty box, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour.*

> Here's the board. On one screen, Prometheus, on the Table tab: where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode, which is Elastic's query language, and which has a command for running prom-Q-L. Both are looking at the same metrics, because in this demo Prometheus ships its data to Elastic with one remote-write block added to its config. Same data, two places to ask about it.
>
> One setting to notice. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.

*Prometheus: the selector is pasted, the cursor underlines the metric name and then the matcher, then Execute.*

> First move: choose which series you're looking at. Our metric is traces span metrics calls total, a counter of calls that the OpenTelemetry Collector builds from traces. Add curly braces and a label matcher, service name equals frontend, and we've picked out just that service. Run it. {{N_PROM}} series, each with its own set of labels.

*Elastic: the wrapper is already in the editor. The cursor underlines the expression, then the command, index, time and result name. Then Run.*

> Now, Elastic. Look inside the parentheses. That's the expression, the same text we just ran. Everything around it is a wrapper, and here it makes just three choices. Where does this run? That's index: the data stream that holds our metrics. When? That's time: the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.
>
> Run it. {{N_ELASTIC}} series, against {{N_PROM}}. The labels sit in a column instead of inline, but they're the same series. So, did you catch the expression changing? No. Only the wrapper is new.

*Prometheus: the rate expression is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears.*

> Now, a series on its own is only half the story. A counter just climbs. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast. That's what rate is for. Hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Run it. {{PROM_VALUE}}.

*Elastic: the same expression inside the wrapper, the result name highlighted, then Run.*

> In Elastic: same expression, same wrapper. The only thing we touch is the name of the answer, now frontend rate. Run it. {{ELASTIC_VALUE}}, against {{PROM_VALUE}}. The two runs were about {{SECONDS_C}} seconds apart, and the values are within {{PCT_C}} percent of each other.

*Prometheus: the sum-by expression is pasted, the cursor underlines the sum-by clause, then Execute. A table with one row per service appears, and the cursor rests on the frontend row.*

> One number for the whole frontend is useful, but it's rarely the question you actually have. The question is which service. So the third move keeps a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.

*Elastic: the same expression inside the wrapper, then Run. The cursor rests on the frontend row.*

> Elastic, same again. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}}, about {{SECONDS_D}} seconds apart.

*Recap slide (Shape C: three cards for the wrapper's choices, one caveat, a closing line).*

> Three expressions, and the expression never changed. What changed is the wrapper: everything around the expression when you run it in Elastic, which is the command, its options and a result name.
>
> Here, the wrapper makes just three choices.
>
> Where it runs. The index option names the data to read.
>
> When it's evaluated. The time option sets the moment, here the end of the date picker's range.
>
> What the answer is called. A result name labels the value that comes back.
>
> There's also a catch. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges.
>
> So take an expression you use every day, drop it between the parentheses, and most of the time, that's all it takes.

---

## For reviewers: what to look at

1. Does the opening question (would you have to rebuild what you've already built?) feel like the viewer's real question, or a manufactured one?
2. Is the wrapper explained clearly at rung 1, and does the recap's "three choices" match what you saw?
3. Are the reasons for `rate` and for `sum by` stated well enough for someone who already knows them?
4. Does "most, though not all" feel honest, or does the video promise too much?
5. Is anything missing that you would want answered before trusting this?
6. Is the pace right for a viewer who is checking each claim against the screen?

## Claims and evidence

Statuses are the register's: Verified (seen or checked here), Docs, Observed, Open. The claims register and the Video 1 log (`module1-video1-log.md`) hold the detail and the dates.

| Claim in the script | Status | Source |
|---|---|---|
| Most, though not all, of PromQL runs in Elastic; a few things don't run yet and a few behave differently at the edges | Docs | Elastic's PromQL limitations page: https://www.elastic.co/docs/reference/query-languages/promql/promql-limitations (retrieved Oct 21, 2026; register row 1). To be re-read, with the date recorded, before the take |
| E-S-Q-L is the Elasticsearch Query Language | Verified | Kibana docs: https://www.elastic.co/guide/en/kibana/current/try-esql.html |
| Here the wrapper makes just three choices, because the command has more options (the register lists index, step, buckets, start, end, time, scrape_interval and a result name) | Docs | The PROMQL command page (register row 36, retrieved Oct 25) |
| `time` is set to the end of the date picker's range, so the expression is evaluated once | Docs and observed | The command page (register row 37, retrieved Oct 25); each lab result row carried one evaluation time |
| The command reads only data inside the date picker's range | Observed (effect), Docs (mechanism) | Lab R4 (about half the Prometheus value when the picker was narrower than the window); register row 19. The docs wording is to be re-read and dated |
| Prometheus ships its data to Elastic with one remote-write block added to its config | Docs (partly) | `config/prometheus-config.yaml` holds one `remote_write` entry (read Oct 26); that the demo's own config lacks it is inferred |
| Both systems hold the same metrics | Open | Lab R1 saw the same series and labels on Oct 20 (previous dataset); to be confirmed on the fresh stack by the rung 1 counts and label sets |
| The metric is a counter of calls that the OpenTelemetry Collector builds from traces | Docs (partly) | Register row 45 (the upstream `spanmetrics` connector README) and `docs/otel-collector-reference.md`; the demo's own Collector config is not in the repo |
| A counter keeps climbing (it is cumulative, and resets when a service restarts) | Docs | Prometheus metric types: https://prometheus.io/docs/concepts/metric_types/ |
| `rate` gives the per-second average rate of increase over the window | Docs | Prometheus's documentation and Elastic's range vector functions page: https://www.elastic.co/docs/reference/query-languages/promql/functions/range-vector |
| `sum by` keeps the named label and aggregates the rest | Docs | Prometheus operators page: https://prometheus.io/docs/prometheus/latest/querying/operators/ |
| The labels come back in one column, not inline | Docs | Register row 38 |
| The expression never changed (the Elastic line's expression is the Prometheus text) | Verified (text), to confirm in the take | Checked by script in the run-sheet on Oct 26 (C2, C4, C6 against C1, C3, C5) |
| The two systems' values agree at each rung | Observed, to be redone | Labs R1, R3 and R6 (Oct 20) and R5, R7 and R8 (Oct 21), on the previous dataset; the take log gives the final numbers and the seconds between the runs |

## Still open before recording

- Hear the nine blocks through the speech engine, then revise. The slide narrations also go through the slide generator.
- Every `{{placeholder}}` is filled from the take log.
- Confirm in the take that the label sets match, that the expression is the only thing pasted unchanged, and that each rung ran in both places.
- Re-read the limitations page and the command page, and record the retrieval dates, before the take.
- The recap narration has no pointer to Video 2 (the narrative's reveal block still has one). Add it in the voice-over at assembly only if you want it, and only once Video 2's through-line is approved.
- Narration may run longer than the footage for the setup and rung 1 (estimates at 150 words a minute); the rehearsal can measure it.
