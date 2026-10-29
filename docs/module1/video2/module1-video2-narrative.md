# Module 1, Video 2 — Narrative (draft v2)

**Working title:** Build it up: a per-service error ratio, rung by rung

**Status:** Provisional, not yet approved by the author (October 29, 2026). Draft v2.1 (October 28) with the decision 25 changes: the five pairs are pinned to one evaluation instant, so the 'seconds apart' sentences now say "Both runs are evaluated at the same moment"; idea 2 says "about nine digits", the sweep's worst case (decision 28). The author approves it after the script review. Decision record: log, section 2 (decisions 25 to 29).

**History:** v1 (Oct 25) was the root's seed. In v2 the structure is kept: the four ideas, the two question-and-answer pairs as separate blocks, and the two optional beats. What changed:
- **The hook** now follows the guide's five parts: the viewer's stakes, the objective in learning objective 2's own words (with TSDS spelled out), the method, the level and scope, and a viewing task.
- **Idea 1 is reordered** (approved Oct 27): each Prometheus run is followed by its Elastic partner, so there are two pairs (with the `!=` matcher, then without it) and then the question. The placeholder `{{SECONDS_A}}` splits into `{{SECONDS_A}}` and `{{SECONDS_A_BASE}}`.
- **Idea 1's baseline sentence is corrected.** The seed said frontend "jumps" to a larger count once the not-equals is removed. The count by service name and status code returns one row per status code, so in the lab (R2, Oct 21) the frontend row with status code unset stayed at 36 and a new row appeared, frontend with status code error, at 14. v2 says that, and the placeholders `{{A_BASE_FRONTEND_PROM}}` and `{{A_BASE_FRONTEND_ELASTIC}}` become `{{A_ERR_FRONTEND_PROM}}` and `{{A_ERR_FRONTEND_ELASTIC}}`.
- **Absolutes removed or scoped:** "the only question that matters", "That's all the not-equals did", "never shows up", "every series collapses", "just works", "We only changed a number", "every row on top has a partner underneath", "That's the whole climb", and "exactly one time series" (optional block). "A counter on its own just climbs" became "keeps climbing" (a counter can reset when a service restarts, register row 48). "The whole system" became "the total across our services, as this metric counts them".
- **Control cues:** every execution now says "Let's run it." The screen notes use the control names Video 1 observed on the author's screens (Execute in Prometheus; Search or Cmd+Enter in Discover); they are re-observed before the run-sheet.
- **Agreement statements** carry the gap in seconds and, for values, the number of leading digits the two share (`{{DIGITS_C}}`, `{{DIGITS_D}}`; idea 2 says "about nine digits", the sweep's worst case, decision 28), as register row 64 decides. No percent form is used (decision 7, Oct 27).
- **"No errors" became "no error series"** in the missing-rows sentence: in the lab's R8 run, six services appeared with a ratio of exactly 0, so they have an error series with no increase in the window, while ten others had no error series and were absent.
- **One sentence added in idea 1** (Elastic, first pair): it says which part of the wrapper makes which choice, because the wrapper first appears on screen there and the setup block names the three choices without showing them. The author can strike it.
- **The closing** keeps the contract's line and adds one durable sentence about Elastic's documentation, with no pointer to another video (decision 5).
- **v2.1 (October 28, decision 3):** the optional series block is reworded so that every part of it is backed by the current TSDS page (the clause "each document belongs to one time series" is not on it). The claims table is refreshed for the objective and the optional rows, and this status line and the "Still open" list are brought up to date. The 17 main blocks are unchanged.

**Length:** 1207 spoken words in the main blocks, with the placeholders counted as one word each, plus 100 in the two optional blocks (counted by script). At an assumed 150 words a minute that is about 8.0 minutes of speech before the demos and the pauses on screen (an estimate, not measured). The contract's target is 7 to 10 minutes with the demos and pauses on screen; there is no hard limit on the narration's length.

**The spine:** the viewer builds the answer to "which of our services are failing, and how often?" from four small ideas, one at a time, and checks each against Prometheus. The objective is stated early, in learning objective 2's words. The video is strictly standalone: the setup block restates what it needs, and nothing depends on another video.

## How to read this

- Each block in a code fence is **spoken text**. Copy it into the speech engine as is.
- The italic line above a block says what is on screen.
- `{{LIKE_THIS}}` is a number that comes from this video's take log. Nothing is final until the placeholders are filled.
- A block marked **OPTIONAL** can be cut and is not counted in the main length. Decision 3 (the series block) was settled on Oct 28: kept, reworded. Decision 5 (the range chart) is deferred.
- A question and its answer are separate blocks, so the silence between them is a 3-second pause placed in the edit, not something the speech engine has to produce.
- **Spellings** follow the Video 1 narrative: `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, `frontend proxy` for the service name with the hyphen.
- **Spoken numbers** (a proposal, still open at the root): counts whole, rates to three decimals, seconds whole.

---

## Hook

*Slide: a claim, not a transition. The slide-shape version, with an explicit shape, is derived from this text (contract, section 8, row 5) and does not exist yet.*

```
You can already pull a request rate out of prom-Q-L. The question people actually ask is harder: which of our services are failing, and how often? In prom-Q-L, that question has a name. It's an error ratio, one per service, and it looks like a lot to write.

So here's what this video is for. By the end, you'll be able to write and execute prom-Q-L against a live Elastic time series data stream. That means instant vectors, range vectors reduced by functions, aggregation, and arithmetic between aggregated results, getting results a Prometheus user would already expect.

To get there, we'll build the error ratio from four small ideas that stack. We'll pick out the series we care about with label matchers. Then we'll turn a counter into a rate and add it up, scale the result with a little arithmetic, and divide one aggregate by another. Each idea runs in Prometheus first, then in Elastic.

I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new in Elastic. And at the end, we'll be plain about the limits.

Now, don't take my word for the result. As each pair runs, watch two things: what the new idea adds to the expression, and whether the numbers agree.
```

## Setup

*Prometheus on the Table tab, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour. About 30 seconds.*

```
Let's look at what we're working with. On one screen, Prometheus, on the Table tab. On the other, Kibana's Discover, in E-S-Q-L mode. E-S-Q-L is Elastic's query language, and it has a command for running prom-Q-L. Your expression goes inside the parentheses, and here a wrapper around it makes three choices: where it runs, when it's evaluated, and what to call the answer. The date picker stays on the last hour, because the command reads only the data inside that range. And our metric is traces span metrics calls total, a counter that the OpenTelemetry Collector builds from traces.
```

## OPTIONAL: what a series is (decision 3)

*Text or a slide on screen, about 17 seconds; its form is still open (a toolkit slide needs 90 to 180 spoken words, and this block has 42). Decision 3 settled Oct 28: kept, reworded, and cut-able.*

```
Underneath this is the series. You know it as one metric with one particular set of labels. In Elastic, a time series data stream stores each observation as a document: a timestamp, dimension fields that identify the series, and the metric values.
```

## Idea 1: narrow the field

*Prometheus: the count expression with the regex and the not-equals matcher is pasted, the cursor underlines the regex and then the not-equals, then Execute. The cursor rests on the frontend row.*

```
Let's start with the first idea: narrowing the field. You usually want a subset of the series, and label matchers are how you choose. Here we use a regex, service name matches frontend or checkout, plus a negative, status code is not error. To see which series survive, we count them, by service name and status code. Let's run it. Frontend has {{A_FRONTEND_PROM}} series. The number after the at sign is the moment both runs are evaluated, in seconds since 1970.
```

*Elastic: the same expression inside the wrapper, run right after the Prometheus one, in the same continuous take. The cursor underlines the expression in the parentheses, then index, time and the result name, then Search or Cmd+Enter.*

```
Now the same thing in Elastic. The text inside the parentheses is the expression. Around it is the wrapper. Index is where it runs. Time is the moment it's evaluated, and here that moment is fixed by the number. And the name out front is what we call the answer. Let's run it. Frontend has {{A_FRONTEND_ELASTIC}} series, against {{A_FRONTEND_PROM}} in Prometheus. Both runs are evaluated at the same moment.
```

*Prometheus: the same expression with the not-equals removed, then Execute. The error rows appear; the cursor rests on the frontend row with status code error.*

```
Now take the not-equals away, and run the same count again. Let's run it. The error series come back as new rows. Frontend, with status code error, has {{A_ERR_FRONTEND_PROM}} series.
```

*Elastic: the same expression with the not-equals removed, run right after, in the same continuous take. The cursor rests on the frontend row with status code error.*

```
And in Elastic, with the not-equals removed. Let's run it. Frontend with status code error has {{A_ERR_FRONTEND_ELASTIC}} series, against {{A_ERR_FRONTEND_PROM}} in Prometheus. Both runs are evaluated at the same moment. So the series the not-equals removed were the error series, in both systems.
```

*Question: the regex is on screen. Hold 3 seconds after the question.*

```
A question, before we continue. That regex says frontend or checkout. Will it also match frontend proxy? Take a second.
```

*Answer: the result with no frontend proxy row stays on screen.*

```
No. A regex matcher has to match the whole value, and frontend proxy is more than frontend, so there's no frontend proxy row in Prometheus or in Elastic.
```

## Idea 2: how much, in total

*Prometheus: the whole-system rate is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears with empty curly braces.*

```
Now the second idea: how much, in total. A counter keeps climbing, so on its own it says little about right now. What you want is its rate, calls per second averaged over a five minute window. Then we add the series up with sum. With nothing after the sum, they add up into a single number: the total calls per second across our services, as this metric counts them. Let's run it. {{B_PROM}} calls per second. Prometheus shows it with an empty set of curly braces, because there's no label left to show.
```

*Elastic: the same expression inside the wrapper, then Search or Cmd+Enter. One value and its time.*

```
In Elastic, it's the same expression inside the same wrapper, with a new name for the answer: total rate. Let's run it. {{B_ELASTIC}} calls per second, against {{B_PROM}} in Prometheus. Both runs are evaluated at the same moment, and the values agree to about nine digits. There are no curly braces here. Elastic shows the value and the time it was evaluated.
```

## Idea 3: scale it with arithmetic

*Prometheus: the sum-by expression times sixty is pasted, the cursor underlines the by clause and then the times sixty, then Execute. One row per service; the cursor rests on the frontend row.*

```
Third idea: arithmetic with a plain number. We put a by clause back, sum by service name, so we get one row per service, and then we multiply by sixty. That turns calls per second into calls per minute. Arithmetic with a plain number scales each value, and the labels stay attached. Let's run it. Frontend reads {{C_FRONTEND_PROM}} calls per minute.
```

*Elastic: the same expression inside the wrapper, then Search or Cmd+Enter. The cursor rests on the frontend row.*

```
In Elastic, the same expression inside the same wrapper. Let's run it. Frontend reads {{C_FRONTEND_ELASTIC}}, against {{C_FRONTEND_PROM}} in Prometheus. Both runs are evaluated at the same moment, and the values agree to {{DIGITS_C}} digits.
```

*Question: the expression is on screen. Hold 3 seconds after the question.*

```
Another question. What would the frontend row say if we multiplied by thirty-six hundred instead of sixty?
```

*Answer: the frontend row stays on screen.*

```
Sixty times as much, because thirty-six hundred is sixty times sixty. That's calls per hour, from changing one number.
```

## Idea 4: divide one aggregate by another

*Prometheus: the error-ratio expression is pasted. The cursor underlines the numerator, then the denominator, then the slash, then Execute. A table of services appears, and the cursor rests on the payment row.*

```
Now the idea we came for: dividing one aggregate by another. On top, the rate of calls whose status code is error, summed by service name. On the bottom, the rate of all calls, summed by service name. Divide the first by the second, and each service that has error series gets its own error ratio.

The rule to remember: aggregate both sides the same way. Here, both sides are sum by service name, so each service on top finds its partner underneath.

To give the ratio something to show, we've switched on a feature flag in the demo that makes the payment service fail some of its requests. Let's run it. {{D_ROWS_PROM}} rows come back, and payment reads {{D_PAYMENT_PROM}}.
```

*Elastic: the same expression inside the wrapper, then Search or Cmd+Enter. The cursor rests on the payment row, then on the full list.*

```
In Elastic, the same expression inside the same wrapper. Let's run it. {{D_ROWS_ELASTIC}} rows, against {{D_ROWS_PROM}} in Prometheus, and payment reads {{D_PAYMENT_ELASTIC}}, against {{D_PAYMENT_PROM}}. Both runs are evaluated at the same moment, and the payment values agree to {{DIGITS_D}} digits.

Now look at who's missing. A service with no error series doesn't show up as a zero. It isn't in the result at all, in Prometheus or in Elastic. So a missing row means no error series was recorded for that service, not a ratio of zero.
```

## OPTIONAL: watch it over time (decision 5)

*Prometheus's Graph tab, then Discover's chart with the time setting removed from the wrapper. Include only if the rehearsal shows a clear chart on both sides (decision 5, deferred Oct 27).*

```
One more look, if you want to see the ratio change. Take the time setting out of the wrapper, and Elastic evaluates the expression across the date picker's range instead of once, so Discover can chart it. Let's run it, first in Prometheus's Graph tab, then in Elastic. [Chart comparison sentence: written after the rehearsal shows both charts.]
```

## Recap

*Slide: four peer cards (shape C): matchers, a rate aggregated across series, arithmetic with a scalar, a ratio of two aggregates. The slide-shape version is derived from this text (contract, section 8, row 5) and does not exist yet.*

```
Let's come back to what we set out to do: write and execute prom-Q-L against a live Elastic time series data stream, getting results a Prometheus user would already expect. You've now built the error ratio one idea at a time. Label matchers picked out the series. A rate, summed, turned a counter into one number. Arithmetic with a plain number scaled it. And a ratio of two aggregates, aggregated the same way, answered the question you actually get asked: which of our services are failing, and how often. Each time, it was the same expression in Prometheus and in Elastic, and the numbers agreed.

There's one caution, because we said we'd be plain about the limits. Most of prom-Q-L works this way, though not all of it, and the edges are worth knowing before you rely on them. Elastic's documentation keeps the current list of what isn't supported, so check it before you move something you depend on.
```

---

## Placeholders

Every number is spoken, none is captioned. A Prometheus value and its Elastic partner come from the same take, with the seconds between the two runs. Twenty placeholders in the main blocks (the optional blocks add none).

| Placeholder | Meaning | Source and form |
|---|---|---|
| `{{A_FRONTEND_PROM}}`, `{{A_FRONTEND_ELASTIC}}` | Series count of the frontend row in the first pair (with the `!=` matcher) | Take log; whole numbers |
| `{{A_ERR_FRONTEND_PROM}}`, `{{A_ERR_FRONTEND_ELASTIC}}` | Series count of the row "frontend, status code error" in the second pair (without the `!=` matcher). Replace `{{A_BASE_FRONTEND_*}}` of the seed | Take log; whole numbers |
| `{{B_PROM}}`, `{{B_ELASTIC}}` | Total calls per second, idea 2 | Take log; three decimals |
| `{{C_FRONTEND_PROM}}`, `{{C_FRONTEND_ELASTIC}}` | Frontend calls per minute, idea 3 | Take log; three decimals |
| `{{DIGITS_C}}` | The leading significant digits the two values share, idea 3 | Take log; computed |
| `{{D_ROWS_PROM}}`, `{{D_ROWS_ELASTIC}}` | Rows returned by the error ratio, idea 4 ("Result series: N" and "N results"; the lab never recorded the Elastic count) | Take log; whole numbers |
| `{{D_PAYMENT_PROM}}`, `{{D_PAYMENT_ELASTIC}}` | Payment's error ratio, idea 4 | Take log; form still open (see "Still open") |
| `{{DIGITS_D}}` | The leading significant digits the two payment values share, idea 4 | Take log; computed |

Rule: if a number disagrees with a sentence, rewrite the sentence. A digits sentence ("agree to N digits") counts the leading significant digits the two full-precision values share (register row 64); if they share only a few (under about four), the sentence changes, not the number. Spoken forms (rounding, words) are tested with Qwen3 before the final audio, as for Video 1.

## Claims to confirm

| Sentence | Confirm against | Status |
|---|---|---|
| Idea 1, first pair: the frontend row with the `!=` matcher has N series on both sides | The take; lab R2 (Oct 21, previous dataset: frontend 36, checkout 8, both status code unset) | Open (the take) |
| Idea 1, second pair: "The error series come back as new rows" and "the series the not-equals removed were the error series, in both systems" | The baseline run's new rows are the status code error rows, and the first pair's rows are unchanged. Lab R2 (Oct 21): frontend 14 and checkout 2 error series appeared, and frontend 36 plus 14 equals the 50 of R1 | Open (the take) |
| "A regex matcher has to match the whole value ... no frontend proxy row in Prometheus or in Elastic" | Register row 29; lab R2; check both results in the take | Verified (lab, Oct 21); open (the take) |
| "Prometheus shows it with an empty set of curly braces ... Elastic shows the value and the time it was evaluated" | Register row 38 and lab R5 | Docs (Oct 25); observed in lab R5 (Oct 21) |
| "Arithmetic with a plain number scales each value, and the labels stay attached" | Register row 21 and lab R7 | Docs; verified (lab R7, Oct 21) |
| "Sixty times as much, because thirty-six hundred is sixty times sixty" | Arithmetic | Verified by arithmetic |
| "Aggregate both sides the same way ... each service on top finds its partner underneath" | Register row 21 (Elastic's limitations page) and lab R8 | Docs; verified (lab R8, Oct 21) |
| "A feature flag in the demo makes the payment service fail some of its requests" | The demo's flag configuration (register row 63: `paymentFailure` is off, its "90%" variant has the value 0.95) and a measurement of its effect (register row 14, open). Wait at least one rate window (five minutes) after switching it on, an inference to test in the rehearsal | Open |
| "A service with no error series ... isn't in the result at all, in Prometheus or in Elastic" | Register row 32; lab R8 (the same 10 services absent on both sides on Oct 21; six services were present with a ratio of 0) | Verified (previous dataset); re-check in the take |
| "The command reads only the data inside that range" | Register rows 19 and 51; lab R4. Re-read the command page and record the retrieval date | Verified (effect); open (the re-read) |
| "Traces span metrics calls total ... a counter that the OpenTelemetry Collector builds from traces" | Register row 45 and `docs/shared/otel-collector-reference.md` | Docs (partly) |
| "Here a wrapper around it makes three choices"; "index is where it runs, time is when it's evaluated, once, at the end of the date picker's range, and the name out front is what we call the answer" | Register rows 36 and 37 | Docs (Oct 25); lab R1, R3 and R6 used the options |
| "A counter keeps climbing" | Register row 48 (a counter can reset when a service restarts) | Docs |
| "A rate ... calls per second averaged over a five minute window" | Elastic's range-vector functions page, as quoted in `docs/shared/glossary.md` | Docs |
| "The values agree to N digits" (ideas 2, 3 and 4) | The take: computed from full-precision values; the sentence changes if few digits are shared (register row 64) | Open until the take |
| "The numbers agreed" and "the same expression in Prometheus and in Elastic" (recap) | The take's own numbers; the expression text is identical on both sides (checked in the run-sheet by script) | Open until the take |
| "Write and execute prom-Q-L against a live Elastic time series data stream" (the objective, in the hook and the recap): that the demo's data stream is a time series data stream | The current TSDS page and the Prometheus remote write page (both retrieved Oct 27); the runbook's A7.3 (`index_mode: time_series`, first run); the stack's mapping check (Oct 28, one field: `labels.service_name` is a dimension in both backing indices; the root records it as register row 65) | **Supported.** The rehearsal's step B6.3 shows the index mode again |
| "Most of prom-Q-L works this way, though not all of it" | Register row 1 and the command page | Docs (Oct 25); re-read before the take |
| "Elastic's documentation keeps the current list of what isn't supported" | The limitations page (register rows 1 and 40). Record the retrieval date | Open (the re-read) |
| OPTIONAL: "a series is one metric with one particular set of labels" | The Prometheus data model page (https://prometheus.io/docs/concepts/data_model/): a series is identified by its metric name and labels, and changing a label value creates a new series | Docs (an excerpt of the official page seen in search on Oct 28; not fetched in full) |
| OPTIONAL: "a time series data stream stores each observation as a document: a timestamp, dimension fields that identify the series, and the metric values" | The current TSDS page (read in full, Oct 27): each document holds a timestamp, dimension fields and metric fields, and metrics are identified by dimension fields; the stack's mapping check (Oct 28) shows a label as a dimension | Docs |
| OPTIONAL: "Take the time setting out of the wrapper, and Elastic evaluates the expression across the date picker's range instead of once" | Register rows 37 and 51; the lab's range-query forms | Docs |
| OPTIONAL: the chart comparison sentence | The rehearsal: both charts on screen | Open |

## Listening notes (fill in)

| Section | Timestamp | Drags, sings, or mispronounced | Suggested change |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Still open

- The author has heard v2 through the speech engine and finds that it reads well (Oct 27). Further changes come from the reviewers and from the recording.
- The setup block is at the contract's about 30 seconds on screen; the listening test says whether it drags.
- Decision 3 (the series block) is settled: kept, reworded (Oct 28). Decision 5 (the range chart) is deferred. Decision 7 (the percent form) is settled as not used.
- The form of the optional series beat on screen: a toolkit slide needs 90 to 180 spoken words and this block has 42, so it may be a short text on screen instead. To settle with the author.
- The spoken form of the ratio in idea 4 (`{{D_PAYMENT_PROM}}`): three decimals may lose too much of a small ratio. Decide after the flag's effect is measured.
- Whether the take's idea 4 table shows rows that read zero (as the lab's R8 run did), and whether a sentence is then needed to say what a zero row means.
- The control names in the screen notes (Execute, Search, Cmd+Enter) are from Video 1; the author's practice runs re-observe them.
