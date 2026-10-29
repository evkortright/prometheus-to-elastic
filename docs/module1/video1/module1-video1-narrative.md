# Module 1, Video 1 — Narrative (draft v2)

**Working title:** Your PromQL, running in Elastic

**Status:** Draft v2, October 26, 2026. **v2 is the trainer-voice pass, approved by the author on Oct 26.** All nine blocks are rewritten as a conversational instructor would say them; this is the *normalized narration*, the text an instructor or the speech engine reads, and it is the narrative of record. The slide-shape versions for the two slides (the opener and the recap) are separate, derived artifacts in the run-sheet (beats 1 and 6). The run-sheet's voice-over blocks and the story document are regenerated from this file.
**History:** v1 (Oct 22) was approved on Oct 25, with one phrase changed in rung 1 ("the wrapper only answers three questions" became "here it makes just three choices") after the docs check of the PROMQL command page, which lists more options than the three we set. On Oct 26 the reveal's "now you know all of it" became "here it makes just three choices", for the same reason. In v2, the game framing ("a little game", "find the seam", "did you catch it?", "first move") is gone; "only the wrapper is new" became "what's new is the wrapper", "a counter just climbs" became "keeps climbing" (a counter can reset when a service restarts), and "within {{PCT_C}} percent" became "agree to {{DIGITS_C}} digits", because the real difference (about 6e-8 percent) cannot be spoken as a percent.

**Length:** about 909 spoken words, with the placeholders counted as one word each, which is roughly six minutes of speech at an assumed 150 words a minute before the pauses on screen (an estimate, not measured). There is no hard limit on length.

**The spine:** a claim to verify. The viewer sets out to recognize which everyday prom-Q-L expressions run in Elastic using the same expression (the learning objective). Each pair of runs is a test with two things to watch: did the expression change, and do the numbers agree? The recap closes the loop on the objective, and says plainly that most, though not all, of prom-Q-L runs in Elastic.

## How to read this

- Each block in a code fence is **spoken text**. Copy it into the speech engine as is.
- The italic line above a block says what is on screen.
- `{{LIKE_THIS}}` is a number that comes from the take log. Nothing is final until the placeholders are filled.
- **Spellings** follow the voice-over conventions in the run-sheet: `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words. The wording is the v2 text approved in chat on Oct 26; only the spellings were applied. Whether Qwen3 needs these spellings is one of the things the listening test can answer: try `PromQL` and `ESQL` too, and note which reads better.

---

## Opening

*Slide: the opener. The slide-shape version, derived from this text for the slide toolkit, is in `module1-video1-run-sheet.md`, beat 1.*

```
You've spent years on your Prometheus setup, so the real question about Elastic isn't whether it's capable. It's whether you'd have to rebuild what you've already built. You've got scrape configs tuned to your infrastructure, dashboards built around your S-L-Os, and prom-Q-L you could write in your sleep.

So here's what this video is for. By the end, you'll be able to recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression.

To get there, we'll take three expressions you probably use every day and run each one twice, first in Prometheus, then in Elastic, against the same data. Between them, we'll select series with a label matcher, take the rate of a counter, and aggregate with sum by.

I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new. And at the end, we'll be plain about what doesn't carry over.

Now, don't take my word for the result. As each pair runs, watch two things: whether the expression changes, and whether the numbers agree.
```

## Setup

*Prometheus's Table tab with an empty box, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour.*

```
Let's look at what we're working with. On one screen, we have Prometheus, on the Table tab, which is where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode. E-S-Q-L is Elastic's query language, and it has a command for running prom-Q-L.

Both are looking at the same metrics. In this demo, Prometheus sends its data to Elastic with one remote-write block added to its config, so it's the same data, with two places to ask about it.

One setting to notice before we start. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.
```

## Rung 1: pick out some series

*Prometheus: the selector is pasted, the cursor underlines the metric name and then the matcher, then Execute.*

*On screen, not read aloud (Prometheus, Table tab): `traces_span_metrics_calls_total{service_name="frontend"}`*

```
Let's start with the first expression: choosing which series we're looking at. The metric is traces span metrics calls total. It's a counter of calls, and the OpenTelemetry Collector builds it from traces. To narrow it down, we add curly braces and a label matcher: service name equals frontend. That picks out just the frontend service. Let's run it. {{N_PROM}} series, each with its own set of labels.
```

*Elastic: the wrapper is already in the editor. The cursor underlines the expression, then the command, index, time and result name. Then Search (or Cmd+Enter).*

*On screen, not read aloud (Kibana Discover, ES|QL editor): `PROMQL index=metrics-generic.prometheus-default time=?_tend calls=(traces_span_metrics_calls_total{service_name="frontend"})`*

```
Now, the same thing in Elastic. Look at what's inside the parentheses. That's the expression, the same text we just ran in Prometheus. Everything around it is a wrapper, and here the wrapper makes just three choices. Where does this run? That's index, the data stream that holds our metrics. When? That's time, the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.

Let's run it. {{N_ELASTIC}} series, against {{N_PROM}} in Prometheus. The labels sit in a column here instead of inline, but they're the same series. So, did the expression change? No. What's new is the wrapper.
```

## Rung 2: how fast

*Prometheus: the rate expression is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears.*

*On screen, not read aloud (Prometheus, Table tab): `sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m]))`*

```
Now for the second expression. A series on its own is only half the story, because a counter keeps climbing. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast, and that's what rate is for. You hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Let's run it. {{PROM_VALUE}}.
```

*Elastic: the same expression inside the wrapper, the result name highlighted, then Search.*

*On screen, not read aloud (Kibana Discover, ES|QL editor): `PROMQL index=metrics-generic.prometheus-default time=?_tend frontend_rate=(sum(rate(traces_span_metrics_calls_total{service_name="frontend"}[5m])))`*

```
In Elastic, it's the same expression inside the same wrapper. The one thing we change is the name of the answer, which is now frontend rate. Let's run it. {{ELASTIC_VALUE}} in Elastic, against {{PROM_VALUE}} in Prometheus. The two runs were about {{SECONDS_C}} seconds apart, and the values agree to {{DIGITS_C}} digits.
```

## Rung 3: which service?

*Prometheus: the sum-by expression is pasted, the cursor underlines the sum-by clause, then Execute. A table with one row per service appears, and the cursor rests on the frontend row.*

*On screen, not read aloud (Prometheus, Table tab): `sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))`*

```
One number for the whole frontend is useful, but it's rarely the question you actually have. Usually, you want to know which service. So for the third expression, we keep a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Let's run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.
```

*Elastic: the same expression inside the wrapper, then Search. The cursor rests on the frontend row.*

*On screen, not read aloud (Kibana Discover, ES|QL editor): `PROMQL index=metrics-generic.prometheus-default time=?_tend request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))`*

```
And in Elastic, the same expression inside the same wrapper. Let's run it. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}} in Prometheus. These two runs were about {{SECONDS_D}} seconds apart.
```

## The reveal

*Slide: the recap. The slide-shape version (Shape C, approved Oct 26), derived from this text, is in `module1-video1-run-sheet.md`, beat 6.*

```
Let's come back to what we set out to do: recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression. For these three, you've seen it. The label matcher, the rate over a counter, and the sum by all ran as the same text in Prometheus and in Elastic, and the numbers agreed.

What changed is the wrapper, which is everything around the expression when you run it in Elastic: the command, its options, and a result name. Here, it made just three choices. Where it runs: the index option names the data to read. When it's evaluated: the time option sets the moment, here the end of the date picker's range. And what the answer is called: a result name labels the value that comes back.

There's one caution, because we said we'd be plain about it. Most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet, and a few behave differently at the edges. So take an expression you use every day, drop it between the parentheses, and try it. Most of the time, that's all it takes.
```

---

## Placeholders

Decision (Oct 22): every number is spoken, not captioned. That keeps the narration the only place a number lives, so a re-capture means refilling this table and regenerating the audio.

| Placeholder | Meaning | Source |
|---|---|---|
| `{{N_PROM}}` | Series count, rung 1, Prometheus | "Result series: N" in the Prometheus result |
| `{{N_ELASTIC}}` | Series count, rung 1, Elastic | "N results" above Discover's table |
| `{{PROM_VALUE}}`, `{{ELASTIC_VALUE}}` | Frontend calls per second, rung 2 | Take log |
| `{{SECONDS_C}}`, `{{DIGITS_C}}` | Seconds between the two runs, and how many leading significant digits the two values share, rung 2 | Take log; computed (`{{PCT_C}}` is retired) |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Row counts, rung 3 | Take log |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | Take log |
| `{{SECONDS_D}}` | Seconds between the two runs, rung 3 | Take log |

Rule: if a number disagrees with a sentence, rewrite the sentence. Rung 2 says the values "agree to {{DIGITS_C}} digits", where the digits are the leading significant digits the two full-precision values share (14.995958299… and 14.995958290… share ten). If they share only a few (under about four), the sentence changes, not the number.

## Claims to confirm in the take

| Sentence | Confirm against | Status |
|---|---|---|
| "They're the same series" (rung 1) | The label sets on both sides match, not just the counts | Observed for names and counts (Oct 26); label values not yet compared |
| "What's new is the wrapper" (rung 1) | The Elastic line's expression is character-for-character the Prometheus text | Verified in the file (Oct 26); confirm in the take |
| "The one thing we change is the name of the answer" (rung 2) | The two commands differ only in the result name and the expression's own text | Verified in the file (Oct 26) |
| "The values agree to {{DIGITS_C}} digits" (rung 2) | The digits computed from full-precision values; the sentence changes if few digits are shared | Open until the take |
| "Elastic's prom-Q-L command reads only the data inside that range" | Lab R4; re-read the limitations page and record the retrieval date | Open |
| "One remote-write block added to its config" | `remote_write` block in `config/prometheus-config.yaml` (URL, name, API key and queue settings in one block). The repo also patches the compose file, so keep the wording at "added to its config" | Docs, partly (Oct 26) |
| "Most, though not all" | The limitations page: the majority of expressions run unchanged | Docs (Oct 21); re-read before the take |
| "Here the wrapper makes just three choices" (rung 1 and the recap) | The command page lists more options (index, step, buckets, start, end, time, scrape_interval, and an optional result name); we set three. Register row 36 | Docs (Oct 25) |
| "A counter keeps climbing" (rung 2) | Prometheus's metric types page: a counter is cumulative and resets to zero on restart | Docs |
| "The numbers agreed" (recap) | The take's own numbers | Open until the take |

## Listening notes (fill in)

| Section | Timestamp | Drags, sings, or mispronounced | Suggested change |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Still open

- **On-screen commands in the review text.** The italic 'On screen, not read aloud' lines above the demo blocks carry the commands. `make_review_script.py` does not print them yet, so the review snapshot (`module1-video1-review-provisional.txt`) carries them by hand. To decide later: have the generator print these lines as ON SCREEN boxes, and put the rule in the contract.

- Hear it through the speech engine, then revise (iteration 2).
- Whether the speech engine needs the hyphenated spellings (`prom-Q-L`, `E-S-Q-L`, `S-L-Os`).
- The recap has no pointer to Video 2. Add it at assembly only if wanted, and only once Video 2's through-line is approved.
- The slide-shape versions (run-sheet beats 1 and 6) are derived from this text; how the slide toolkit times its reveals against the audio is not known here.
- The placeholders are filled from the take log (the run-sheet's "After the take").
