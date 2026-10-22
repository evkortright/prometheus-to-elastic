# Module 1, Video 1 — Narrative (draft v1)

**Working title:** Your PromQL, running in Elastic
**Status:** Draft v1, October 22, 2026. For listening and reading aloud. Not yet the source of truth: until you approve a version, the voice-over in `module1-video1-run-sheet.md` stays authoritative. Once approved, the run-sheet's voice-over blocks and the story document are regenerated from this file.
**Length:** about 670 spoken words, with the placeholders counted as one word each. The target is around five minutes with the pauses on screen (an estimate, not measured).
**The spine:** the viewer plays "find the seam": watch the expression and try to catch it changing. Each rung is another look. The reveal is that the expression never changed; only the wrapper is new.

## How to read this

- Each block in a code fence is **spoken text**. Copy it into the speech engine as is.
- The italic line above a block says what is on screen.
- `{{LIKE_THIS}}` is a number that comes from the take log. Nothing is final until the placeholders are filled.
- **Spellings** follow the voice-over conventions in the run-sheet: `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words. The wording is exactly the text reviewed in chat on Oct 22; only the spellings were applied. Whether Qwen3 needs these spellings is one of the things the listening test can answer: try `PromQL` and `ESQL` too, and note which reads better.

---

## Opening

*Slide: the opener. Its own slide narration is derived from this block later, with an explicit shape for the generator.*

```
You've spent years on this. Scrape configs tuned to your infrastructure, dashboards built around your S-L-Os, and prom-Q-L you could write in your sleep. So when someone says "that runs in Elastic too," the question isn't whether Elastic is powerful. It's whether you'd have to rebuild everything you've already built.

Let's find out, with a little game. We'll take three expressions you probably know by heart, and run each one twice: first in Prometheus, then in Elastic. Your job is simple. Watch the expression, and try to catch it changing.
```

## Setup

*Prometheus's Table tab with an empty box, then Kibana Discover in E-S-Q-L mode with the date picker on the last hour.*

```
Here's the board. On one screen, Prometheus, on the Table tab: where you'd run an expression today. On the other, Kibana's Discover, in E-S-Q-L mode, which is Elastic's query language, and which has a command for running prom-Q-L. Both are looking at the same metrics, because in this demo Prometheus ships its data to Elastic with one remote-write block added to its config. Same data, two places to ask about it.

One setting to notice. The date picker is on the last hour, because Elastic's prom-Q-L command reads only the data inside that range. So we're keeping it wide.
```

## Rung 1: pick out some series

*Prometheus: the selector is pasted, the cursor underlines the metric name and then the matcher, then Execute.*

```
First move: choose which series you're looking at. Our metric is traces span metrics calls total, a counter of calls that the OpenTelemetry Collector builds from traces. Add curly braces and a label matcher, service name equals frontend, and we've picked out just that service. Run it. {{N_PROM}} series, each with its own set of labels.
```

*Elastic: the wrapper is already in the editor. The cursor underlines the expression, then the command, index, time and result name. Then Run.*

```
Now, Elastic. Look inside the parentheses. That's the expression, the same text we just ran. Everything around it is a wrapper, and the wrapper only answers three questions. Where does this run? That's index: the data stream that holds our metrics. When? That's time: the end of the date picker's range, so the expression is evaluated once, just like the Table tab. And what do we call the answer? That's the name out front: calls.

Run it. {{N_ELASTIC}} series, against {{N_PROM}}. The labels sit in a column instead of inline, but they're the same series. So, did you catch the expression changing? No. Only the wrapper is new.
```

## Rung 2: how fast

*Prometheus: the rate expression is pasted, the cursor underlines the five-minute window and then the sum, then Execute. A single value appears.*

```
Now, a series on its own is only half the story. A counter just climbs. It counts every call since the start, which tells you almost nothing about right now. What you want to know is how fast. That's what rate is for. Hand it a counter and a window, here five minutes in square brackets, and it returns the per-second average rate of increase. This metric has many series, so we wrap it in sum to get one number: how many calls per second the frontend is handling. Run it. {{PROM_VALUE}}.
```

*Elastic: the same expression inside the wrapper, the result name highlighted, then Run.*

```
In Elastic: same expression, same wrapper. The only thing we touch is the name of the answer, now frontend rate. Run it. {{ELASTIC_VALUE}}, against {{PROM_VALUE}}. The two runs were about {{SECONDS_C}} seconds apart, and the values are within {{PCT_C}} percent of each other.
```

## Rung 3: which service?

*Prometheus: the sum-by expression is pasted, the cursor underlines the sum-by clause, then Execute. A table with one row per service appears, and the cursor rests on the frontend row.*

```
One number for the whole frontend is useful, but it's rarely the question you actually have. The question is which service. So the third move keeps a label. Sum by service name adds up everything else and holds on to that label, so we get one row per service. Run it. {{ROWS_PROM}} rows, and frontend reads {{PROM_FRONTEND}} calls per second.
```

*Elastic: the same expression inside the wrapper, then Run. The cursor rests on the frontend row.*

```
Elastic, same again. {{ROWS_ELASTIC}} rows, and frontend reads {{ELASTIC_FRONTEND}}, against {{PROM_FRONTEND}}, about {{SECONDS_D}} seconds apart.
```

## The reveal

*Slide: the recap. Its own slide narration is derived from this block later.*

```
So, did you catch it? Three expressions, and the expression never changed. What changed is the wrapper, and now you know all of it: where it runs, when it's evaluated, and what to call the answer. Take an expression you use every day, drop it between the parentheses, and most of the time, that's all it takes.

Most, though, not all. A few things in prom-Q-L don't run in Elastic yet, and a few behave differently at the edges. We'll get to those. First, let's put these pieces to work. Next, we build the question you actually get paged about: which services are failing, and how often.
```

---

## Placeholders

Decision (Oct 22): every number is spoken, not captioned. That keeps the narration the only place a number lives, so a re-capture means refilling this table and regenerating the audio.

| Placeholder | Meaning | Source |
|---|---|---|
| `{{N_PROM}}` | Series count, rung 1, Prometheus | "N results" in the Prometheus clip |
| `{{N_ELASTIC}}` | Series count, rung 1, Elastic | Discover's row count, or `series` from the count form |
| `{{PROM_VALUE}}`, `{{ELASTIC_VALUE}}` | Frontend calls per second, rung 2 | Take log |
| `{{SECONDS_C}}`, `{{PCT_C}}` | Seconds between the two runs, and the relative difference in percent, rung 2 | Take log; computed |
| `{{ROWS_PROM}}`, `{{ROWS_ELASTIC}}` | Row counts, rung 3 | Take log |
| `{{PROM_FRONTEND}}`, `{{ELASTIC_FRONTEND}}` | Frontend row values, rung 3 | Take log |
| `{{SECONDS_D}}` | Seconds between the two runs, rung 3 | Take log |

Rule: if a number disagrees with a sentence, rewrite the sentence. Rung 2 says "within {{PCT_C}} percent", which only holds if the difference is small (about 1 percent or less). Otherwise the sentence changes, not the number.

## Claims to confirm in the take

| Sentence | Confirm against |
|---|---|
| "They're the same series" (rung 1) | The label sets on both sides match, not just the counts |
| "Only the wrapper is new" (rung 1) | The Elastic line's expression is character-for-character the Prometheus text |
| "The only thing we touch is the name of the answer" (rung 2) | The two commands differ only in the result name and the expression's own text |
| "Elastic's prom-Q-L command reads only the data inside that range" | Lab R4; re-read the limitations page and record the retrieval date |
| "One remote-write block added to its config" | `remote_write` block in `config/prometheus-config.yaml` (URL, name, API key and queue settings in one block). The repo also patches the compose file, so keep the wording at "added to its config" |
| "Most, though, not all" | The limitations page: the majority of expressions run unchanged |
| "Next, we build ... which services are failing" | Video 2's through-line, which is not yet approved |

## Listening notes (fill in)

| Section | Timestamp | Drags, sings, or mispronounced | Suggested change |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

## Still open

- Hear it through the speech engine (Qwen3), then revise (iteration 2).
- Whether Qwen3 needs the hyphenated spellings (`prom-Q-L`, `E-S-Q-L`, `S-L-Os`).
- Slide narrations for the opener and the recap, derived from this piece with an explicit shape for the generator.
- Update the run-sheet voice-over and the story document once this is approved.
- The reveal's pointer to an error ratio depends on Video 2's through-line.
