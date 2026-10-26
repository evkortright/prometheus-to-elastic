# Module 1, Video 1 — The story: Your PromQL, running in Elastic

**For:** reading aloud and peer review.
**Status:** draft, October 26, 2026, regenerated from narrative v2 (the trainer-voice pass the author approved on Oct 26). Numbers are placeholders until the take.
**Source of truth:** the narrative (`module1-video1-narrative.md`). This file is generated from it. If they differ, the narrative wins and this file is regenerated.

---

## About this video

- **Audience:** an SRE who uses PromQL and Grafana every day. A technical training video for a technical audience, spoken by a trainer who is a peer, not a presenter selling a feature.
- **Objective (LO1):** recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
- **Length:** about 909 spoken words in nine blocks, roughly six minutes of speech at an assumed 150 words a minute (an estimate, not a measurement), plus the pauses on screen. There is no hard limit.
- **How to read it:** the quoted text is spoken. The italic lines say what is on screen. Anything in double curly braces is a number that will be filled in from the take.

## The story in a paragraph

An SRE has spent years on a Prometheus setup, and the real question about Elastic is whether it would all have to be rebuilt. The video states its objective up front: recognize which everyday prom-Q-L expressions run in Elastic using the same expression. It tests three, each run twice, first in Prometheus and then in Elastic, against the same data, with two things for the viewer to watch: whether the expression changes, and whether the numbers agree. The expression does not change; what is new is a wrapper that here makes just three choices: where it runs, when it is evaluated, and what the answer is called. The recap closes the loop on the objective and says plainly that most, though not all, of prom-Q-L runs in Elastic.

---

## The script

*Slide: the opener. The slide-shape version, derived from this text for the slide toolkit, is in `module1-video1-run-sheet.md`, beat 1.*

> You've spent years on your Prometheus setup, so the real question about Elastic isn't whether it's capable. It's whether you'd have to rebuild what you've already built. You've got scrape configs tuned to your infrastructure, dashboards built around your S-L-Os, and prom-Q-L you could write in your sleep.
>
> So here's what this video is for. By the end, you'll be able to recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression.
>
> To get there, we'll take three expressions you probably use every day and run each one twice, first in Prometheus, then in Elastic, against the same data. Between them, we'll select series with a label matcher, take the rate of a counter, and aggregate with sum by.
>
> I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new. And at the end, we'll be plain about what doesn't carry over.
>
> Now, don't take my word for the result. As each pair runs, watch two things: whether the expression changes, and whether the numbers agree.

*Prometheus's Table tab with an empty box, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour.*

> Let's look at what we're working with. On one screen, we have Prometheus, on the Table tab, which is where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode. E-S-Q-L is Elastic's query language, and it has a command for running prom-Q-L.
>
> Both are looking at the same metrics. In this demo, Prometheus sends its data to Elastic with one remote-write block added to its config, so it's the same data, with two places to ask about it.
>
> One setting to notice before we start. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.

*Prometheus: the selector is pasted, the cursor underlines the metric name and then the matcher, then Execute.*

> Let's start with the first expression: choosing which series we're looking at. The metric is traces span metrics calls total. It's a counter of calls, and the OpenTelemetry Collector builds it from traces. To narrow it down, we add curly braces and a label matcher: service name equals frontend. That picks out just the frontend service. Let's run it. {{N_PROM}} series, each with its own set of labels.

*Elastic: the wrapper is already in the editor. The cursor underlines the expression, then the command, index, time and result name. Then Search (or Cmd+Enter).*

> Now, the same thing in Elastic. Look at what's inside the parentheses. That's the expression, the same text we just ran in Prometheus. Everything around it is a wrapper, and here the wrapper makes just three choices. Where does this run? That's index, the data stream that holds our metrics. When? That's time, the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.
>
> Let's run it. {{N_ELASTIC}} series, against {{N_PROM}} in Prometheus. The labels sit in a column here instead of inline, but they're the same series. So, did the expression change? No. What's new is the wrapper.

*Prometheus: the rate expression is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears.*

> Now for the second expression. A series on its own is only half the story, because a counter keeps climbing. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast, and that's what rate is for. You hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Let's run it. {{PROM_VALUE}}.

*Elastic: the same expression inside the wrapper, the result name highlighted, then Search.*

> In Elastic, it's the same expression inside the same wrapper. The one thing we change is the name of the answer, which is now frontend rate. Let's run it. {{ELASTIC_VALUE}} in Elastic, against {{PROM_VALUE}} in Prometheus. The two runs were about {{SECONDS_C}} seconds apart, and the values agree to {{DIGITS_C}} digits.

*Prometheus: the sum-by expression is pasted, the cursor underlines the sum-by clause, then Execute. A table with one row per service appears, and the cursor rests on the frontend row.*

> One number for the whole frontend is useful, but it's rarely the question you actually have. Usually, you want to know which service. So for the third expression, we keep a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Let's run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.

*Elastic: the same expression inside the wrapper, then Search. The cursor rests on the frontend row.*

> And in Elastic, the same expression inside the same wrapper. Let's run it. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus. These two runs were about {{SECONDS_D}} seconds apart.

*Slide: the recap. The slide-shape version (Shape C, approved Oct 26), derived from this text, is in `module1-video1-run-sheet.md`, beat 6.*

> Let's come back to what we set out to do: recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression. For these three, you've seen it. The label matcher, the rate over a counter, and the sum by all ran as the same text in Prometheus and in Elastic, and the numbers agreed.
>
> What changed is the wrapper, which is everything around the expression when you run it in Elastic: the command, its options, and a result name. Here, it made just three choices. Where it runs: the index option names the data to read. When it's evaluated: the time option sets the moment, here the end of the date picker's range. And what the answer is called: a result name labels the value that comes back.
>
> There's one caution, because we said we'd be plain about it. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges. So take an expression you use every day, drop it between the parentheses, and try it. Most of the time, that's all it takes.

---

## For reviewers: what to look at

1. Does the opening sound like a trainer talking to a peer? Does the objective say what the viewer will be able to do?
2. Is the wrapper explained clearly at the first pair, and does the recap's "three choices" match what you saw?
3. Are the reasons for `rate` and for `sum by` stated well enough for someone who already knows them, or do they over-explain?
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
| `time` is the end of the date picker's range, so the expression is evaluated once | Docs and observed | The command page (register row 37, retrieved Oct 25); Elastic's `step` was the run time in three readings on Oct 26 |
| The command reads only data inside the date picker's range | Observed (effect), Docs (mechanism) | Lab R4 (about half the Prometheus value when the picker was narrower than the window); register row 19. The docs wording is to be re-read and dated |
| Prometheus sends its data to Elastic with one remote-write block added to its config | Docs (partly) | `config/prometheus-config.yaml` holds one `remote_write` entry (read Oct 26); that the demo's own config lacks it is inferred |
| Both systems hold the same metrics | Observed (counts and label names) | Oct 26 rehearsal: 41 series in each, and the same ten label names on a sampled row; label values are not yet compared |
| The metric is a counter of calls that the OpenTelemetry Collector builds from traces | Docs (partly) | Register row 45 (the upstream `spanmetrics` connector README) and `docs/otel-collector-reference.md`; the demo's own Collector config is not in the repo |
| A counter keeps climbing (it is cumulative, and resets when a service restarts) | Docs | Prometheus metric types: https://prometheus.io/docs/concepts/metric_types/ |
| `rate` gives the per-second average rate of increase over the window | Docs | Prometheus's documentation and Elastic's range vector functions page: https://www.elastic.co/docs/reference/query-languages/promql/functions/range-vector |
| `sum by` keeps the named label and aggregates the rest | Docs | Prometheus operators page: https://prometheus.io/docs/prometheus/latest/querying/operators/ |
| The labels come back in one column, not inline | Observed | Register row 38; on Oct 26 the grid cut the JSON off, and the whole list showed in the expanded row |
| The expression did not change (the Elastic line's expression is the Prometheus text) | Verified (text), to confirm in the take | Checked by script in the run-sheet on Oct 26 (C2, C4, C6 against C1, C3, C5) |
| The two systems' values agree | Observed, to be redone in the take | Oct 26 rehearsal: rung 2 differed by 6.0e-10 relative; rung 3 by 2.543e-10 on every one of the 14 comparable rows. The take gives the final numbers |
| Paired runs agree when both fall inside one scrape minute | Hypothesis | Prometheus scrapes once a minute (about :37 on Oct 26); both timed pairs agreed to better than 1e-9. A deliberate straddle would test it |

## Still open before recording

- Hear the nine blocks through the speech engine, then revise. The two slide versions also go through the slide toolkit.
- Every `{{placeholder}}` is filled from the take (the run-sheet's "After the take").
- Confirm in the take that the label sets match, that the pasted line is the line that ran, and that each rung ran in both places.
- Re-read the limitations page and the command page, and record the retrieval dates, before the take.
- The recap has no pointer to Video 2. Add it at assembly only if wanted, and only once Video 2's through-line is approved.
- Narration may run longer than the footage for the setup and rung 1; a rendered guide would measure it.
