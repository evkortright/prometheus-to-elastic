# Module 1, Video 2 — Narrative (seed draft v1)

**Working title:** Build it up: a per-service error ratio, rung by rung

**Status:** Seed draft v1 from the root chat, October 25, 2026. The Video 2 chat owns this file from now on and may use it, rewrite it or ignore it; the author decides at the start of that chat. It was written before that chat existed, and the author has not listened to it yet. For listening and reading aloud. Not the source of truth until the author approves a version. The Video 2 run-sheet does not exist yet; it is written from the approved version.

**Length:** about 784 spoken words in the main blocks, with the placeholders counted as one word each, plus 92 words in the two optional blocks. The target is 7 to 10 minutes with the demos and the pauses on screen (an estimate, not measured). No hard limit.

**The spine:** the viewer builds the answer to "which services are failing, and how often?" from four small ideas, one at a time, and checks each against Prometheus. The video is strictly standalone: the setup block restates what it needs, and nothing depends on another video.

## How to read this

- Each block in a code fence is **spoken text**. Copy it into the speech engine as is.
- The italic line above a block says what is on screen.
- `{{LIKE_THIS}}` is a number that comes from this video's take log. Nothing is final until the placeholders are filled.
- A block marked **OPTIONAL** depends on an open decision (3 or 5 in the outline) and is not counted in the main length.
- A question and its answer are separate blocks, so the silence between them is a 3-second pause placed in the edit, not something the speech engine has to produce.
- **Spellings** follow the Video 1 narrative: `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, `frontend proxy` for the service name with the hyphen.

---

## Hook

*Slide: a claim, not a transition. The question in large type, then the four ideas as a stack. The shape is chosen when the slide narration is derived from this block.*

```
Somebody asks, and it's the only question that matters: which services are failing, and how often?

In prom-Q-L, that question has a name. It's an error ratio, one per service, and it looks harder than it is, because it's built from four small ideas that stack. Pick out the series you care about. Turn a counter into a rate, and add it up. Scale the result with a little arithmetic. And divide one aggregate by another. We'll build it one idea at a time, run each step in Prometheus and then in Elastic, and check that the answers agree.
```

## Setup

*Prometheus on the Table tab, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour. About 30 seconds.*

```
Here's the setup. Prometheus, on the Table tab. Kibana Discover in E-S-Q-L mode, running Elastic's prom-Q-L command. Your expression sits inside the parentheses, and a wrapper around it makes three choices: where it runs, when it's evaluated, and what to call the answer. The date picker stays on the last hour, because the command only sees data inside that range. And our metric is traces span metrics calls total, a counter the OpenTelemetry Collector builds from traces.
```

## OPTIONAL: what a series is (decision 3)

*Slide, a short layered or card shape, decided after the docs check. Include only if the wording holds up against the TSDS pages (register row 41).*

```
Underneath all of this, a series is one metric with one particular set of labels. In Elastic, a time series data stream stores each observation as a document that belongs to exactly one time series.
```

## Idea 1: narrow the field

*Prometheus: the count expression with the regex and the not-equals matcher is pasted, the cursor underlines the regex and then the not-equals, then Execute. Then the same expression without the not-equals.*

```
First idea: narrow the field. You rarely want every series. You want some of them, and that's what label matchers are for. Here's a regex, service name matches frontend or checkout, plus a negative, status code is not error. To see which series survive, we count them, by service name and status code. Run it. Frontend has {{A_FRONTEND_PROM}} series. Now take the not-equals away and run it again, and the error series come back, so frontend jumps to {{A_BASE_FRONTEND_PROM}}. That's all the not-equals did: it removed the errors.
```

*Elastic: the same two expressions inside the wrapper, run with and without the not-equals.*

```
Same expression in Elastic, inside the wrapper. Frontend: {{A_FRONTEND_ELASTIC}} series with the matcher and {{A_BASE_FRONTEND_ELASTIC}} without it, against {{A_FRONTEND_PROM}} and {{A_BASE_FRONTEND_PROM}} in Prometheus. The runs were about {{SECONDS_A}} seconds apart.
```

*Question: the regex is on screen. Hold 3 seconds after the question.*

```
A question before we move on. That regex says frontend or checkout. Will it also match frontend proxy? Take a second.
```

*Answer: the result with no frontend proxy row stays on screen.*

```
No. A regex matcher has to match the whole value, so frontend proxy never shows up, in Prometheus or in Elastic.
```

## Idea 2: how much, in total

*Prometheus: the whole-system rate is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears with empty curly braces.*

```
Second idea: how much, in total. A counter on its own just climbs, so we ask for its rate, calls per second over a five minute window, and then add everything up with sum. Nothing after the sum means every series collapses into one number: the whole system's calls per second. Run it. {{B_PROM}}. Prometheus shows it with an empty set of curly braces, because there's no label left to show.
```

*Elastic: the same expression inside the wrapper, then Run. One value and its time.*

```
In Elastic, same expression, same wrapper. {{B_ELASTIC}}, about {{SECONDS_B}} seconds after the Prometheus run. No empty braces here, just the value and the time it was evaluated.
```

## Idea 3: scale it with arithmetic

*Prometheus: the sum-by expression times sixty is pasted, the cursor underlines the by clause and then the times sixty, then Execute. One row per service, the cursor rests on the frontend row.*

```
Third idea: arithmetic. Put a by clause back, sum by service name, so we get one row per service, and multiply the whole thing by sixty. Calls per second become calls per minute. Arithmetic with a plain number just works, and the labels come along for the ride. Frontend reads {{C_FRONTEND_PROM}} calls per minute.
```

*Elastic: the same expression inside the wrapper, then Run. The cursor rests on the frontend row.*

```
Elastic: {{C_FRONTEND_ELASTIC}}, about {{SECONDS_C}} seconds apart.
```

*Question on screen: the expression. Hold 3 seconds after the question.*

```
Another question. What would the frontend row say if we multiplied by thirty-six hundred instead of sixty?
```

*Answer: the frontend row stays on screen.*

```
About sixty times as much, because that's calls per hour. We only changed a number.
```

## Idea 4: divide one aggregate by another

*Prometheus: the error-ratio expression is pasted. The cursor underlines the numerator, then the denominator, then the slash, then Execute. A table of services appears, the cursor rests on the payment row.*

```
Now the idea we came for: divide one aggregate by another. On top, the rate of calls whose status code is error, summed by service name. On the bottom, the rate of all calls, summed by service name. Divide the first by the second, and each service gets its own error ratio.

One rule makes this work, and it's worth saying plainly: aggregate both sides the same way. Here, both sides are sum by service name, so every row on top has a partner underneath.

To give the ratio something to show, we've switched on a feature flag in the demo that makes the payment service fail some of its requests. Run it in Prometheus. {{D_ROWS_PROM}} services come back, and payment reads {{D_PAYMENT_PROM}}.
```

*Elastic: the same expression inside the wrapper, then Run. The cursor rests on the payment row, then the full list.*

```
Elastic: {{D_ROWS_ELASTIC}} services, payment at {{D_PAYMENT_ELASTIC}}, about {{SECONDS_D}} seconds apart.

Now look at who's missing. A service with no error series doesn't show up as zero. It isn't in the result at all, in Prometheus or in Elastic, so a missing row means no errors were recorded for that service, not a ratio of zero.
```

## OPTIONAL: watch it over time (decision 5)

*Prometheus's Graph tab, then Discover's chart with the time setting removed from the wrapper. Include only if the rehearsal shows a clear chart on both sides.*

```
One more look. Take the time setting out of the wrapper, and Elastic runs the same expression across the whole date range instead of once, so Discover can chart it. Here's the ratio over the last hour in Prometheus's Graph tab, and here it is in Elastic. [Chart comparison sentence: written after the rehearsal shows both charts.]
```

## Recap

*Slide: four peer cards (shape C): matchers, a rate aggregated across series, arithmetic with a scalar, a ratio of two aggregates.*

```
That's the whole climb. Matchers pick the series. A rate, summed, turns a counter into one number. Arithmetic scales it. And a ratio of two aggregates, aggregated the same way, answers the question you actually get asked: which services are failing, and how often. Four small ideas, one expression, and the same text in Prometheus and in Elastic.

Most of prom-Q-L works this way, though not all of it, and the edges are worth knowing before you rely on them.
```

---

## Placeholders

Every number is spoken, none is captioned. A Prometheus value and its Elastic partner come from the same take, with the seconds between the two runs.

| Placeholder | Meaning | Source |
|---|---|---|
| `{{A_FRONTEND_PROM}}`, `{{A_FRONTEND_ELASTIC}}` | Frontend series count with the `!=` matcher, idea 1 | Take log |
| `{{A_BASE_FRONTEND_PROM}}`, `{{A_BASE_FRONTEND_ELASTIC}}` | Frontend series count without the `!=` matcher (baseline), idea 1 | Take log |
| `{{SECONDS_A}}` | Seconds between the Prometheus and Elastic runs, idea 1 | Take log |
| `{{B_PROM}}`, `{{B_ELASTIC}}` | Whole-system calls per second, idea 2 | Take log |
| `{{SECONDS_B}}` | Seconds between the runs, idea 2 | Take log |
| `{{C_FRONTEND_PROM}}`, `{{C_FRONTEND_ELASTIC}}` | Frontend calls per minute, idea 3 | Take log |
| `{{SECONDS_C}}` | Seconds between the runs, idea 3 | Take log |
| `{{D_ROWS_PROM}}`, `{{D_ROWS_ELASTIC}}` | Services returned by the error ratio, idea 4 (read the Elastic count from Discover; the lab never recorded it) | Take log |
| `{{D_PAYMENT_PROM}}`, `{{D_PAYMENT_ELASTIC}}` | Payment's error ratio, idea 4 | Take log |
| `{{SECONDS_D}}` | Seconds between the runs, idea 4 | Take log |

Rule: if a number disagrees with a sentence, rewrite the sentence. Spoken forms (rounding, words) are tested with Qwen3 before the final audio, as for Video 1.

## Claims to confirm

| Sentence | Confirm against | Status |
|---|---|---|
| "That's all the not-equals did: it removed the errors" | The baseline count minus the count with `!=` equals the error-series count (lab R2, Oct 21: 14 for frontend; verify in the take) | Open (the take) |
| "A regex matcher has to match the whole value, so frontend proxy never shows up" | Register row 29; lab R2; check on both sides in the take | Open (the take) |
| "Prometheus shows empty curly braces ... Elastic: just the value and the time it was evaluated" | Register row 38 and lab R5 | Docs (Oct 25) |
| "Arithmetic with a plain number just works, and the labels come along" | Register row 21 and lab R7 | Docs, verified |
| "About sixty times as much, because that's calls per hour" | Arithmetic: 3600 divided by 60 | Verified by arithmetic |
| "Aggregate both sides the same way" | Register row 21 (Elastic's limitations page) and lab R8 | Docs, verified |
| "A feature flag in the demo makes the payment service fail some of its requests" | The demo's flag configuration and a measurement of its effect (register row 14, open). Wait at least one rate window (five minutes) after switching it on, an inference to test in the rehearsal | Open |
| "A service with no error series ... isn't in the result at all, in Prometheus or in Elastic" | Register row 32; lab R8 (the same 10 services were absent on both sides on Oct 21) | Verified (old dataset); re-check |
| "The command only sees data inside that range" | Register row 19 | Verified (effect) |
| "traces span metrics calls total ... the OpenTelemetry Collector builds from traces" | `docs/otel-collector-reference.md` | Docs |
| "A wrapper around it makes three choices" | Register row 36 | Docs (Oct 25) |
| "Most of prom-Q-L works this way, though not all of it" | Register row 1 and the command page | Docs (Oct 25) |
| OPTIONAL: "a series is one metric with one particular set of labels" | The Prometheus data model page (to read) | Open |
| OPTIONAL: "each observation is a document that belongs to exactly one time series" | Register row 41 (TSDS page, read in part) | Docs (partly) |
| OPTIONAL: the chart comparison sentence | The rehearsal: both charts on screen | Open |

## Listening notes (fill in)

| Section | Timestamp | Drags, sings, or mispronounced | Suggested change |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Still open

- Hear it through the speech engine (Qwen3), then revise (iteration 2).
- The setup block is about 30 seconds against a target of about 20; trim it if the listening test says it drags.
- Outline decisions 3 (series slide), 5 (range chart) and 7 (percent form, not used here) are open.
- The size of the payment flag's effect is unmeasured, so `{{D_PAYMENT_PROM}}` and `{{D_PAYMENT_ELASTIC}}` stay placeholders until the rehearsal.
- Slide narrations for the hook and the recap, derived from this piece with an explicit shape for the slide generator.
- The Video 2 run-sheet, written after this narrative is approved.
