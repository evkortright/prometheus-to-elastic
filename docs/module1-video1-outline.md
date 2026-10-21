# Module 1, Video 1 — Outline (draft)

**Working title:** Your PromQL, running in Elastic
**Objective (LO1, proposed wording):** Recognize which everyday PromQL query patterns (label selectors, aggregation, `rate()` and `increase()` on counters) run in Elastic using the same PromQL expression.
**Level:** Remember. Slow, friendly, no tricks.
**Target length:** about 5 minutes.
**Format:** slides plus a live demo, with TTS narration.

**Status:** Outline only. Narration is written after the query lab confirms R1 to R6.

---

## The one idea

The expression you type in Prometheus is the same expression you type in Elastic. Elastic's PROMQL command runs it. The viewer watches that be true four times.

Claim hygiene for this video (see the claims register in `module1-status-2026-10-19.md`):
- Say **expression**, not "query", when claiming sameness.
- Say **most** or **everyday**, never "all" or "any".
- Mention **technical preview** once, plainly.
- Point forward to Video 3 for the edges, without promising what is there.
- No "pure PromQL can't" claims, and no "didn't change a single character."

---

## Beats

| # | Beat | On screen | Approx. |
|---|---|---|---|
| 1 | Hook and what you'll recognize | Slide (opener) | 0:30 |
| 2 | Setup: same data in both places | Prometheus graph, then Discover | 0:30 |
| 3 | Rung 1: label selector | Type in Prometheus, then in Discover | 0:50 |
| 4 | Rung 2: `rate()` on a counter | Both | 0:50 |
| 5 | Rung 3: aggregation with `sum by` | Both | 0:50 |
| 6 | Rung 4: `increase()` | Both | 0:40 |
| 7 | Recap and what comes next | Slide (recap) | 0:40 |

Rungs map to the lab: selector is R1, `rate()` is R3, `sum by` is R6, `increase()` is R4. Dropping any rung that doesn't hold up in the lab is fine.

### Beat details

1. **Hook and slide.** A claim, not a transition, for example that the PromQL you write today has a new place to run. Plant one short title phrase (3 to 8 words). List the patterns the viewer will recognize (Shape A, verb-first, three items: label selectors, aggregation, `rate()` and `increase()`).
2. **Setup.** One sentence on how the data got there (Prometheus remote-writes to Elastic) and that both screens show the same metrics. Show the Prometheus Table tab and Discover in ES|QL mode.
3. **Each rung, the same four moves:**
   1. Type the expression in Prometheus and run it.
   2. Type it in Discover inside the PROMQL command.
   3. Point at the expression, which is the same on both screens.
   4. Point at the values, which are close.
   On the first rung only, say what the extra words around the expression are: the PROMQL command and a result name. Don't call it "no changes."
7. **Recap slide.** Name the patterns that carried over (Shape C cards, 3 to 4). Close with one honest sentence: some constructs behave differently or aren't supported yet, and Video 3 covers them.

---

## Slides (shapes to confirm when narrations are written)

- **Opener:** Shape A, "what you will recognize." Not a course opener, so no "Welcome to:" line.
- **Recap:** Shape C, peer cards for the patterns, each with a name and one short definition.
- No screenshot references on slides unless we supply the screenshot.

---

## Open decisions

1. **Recording workflow.** Typing time varies, so I'd record the screen first and write or time the narration to it, instead of fitting live typing to fixed-length TTS audio. Confirm.
2. **Capture on the desktop.** Which recorder, and does the Windows browser reach WSL's `localhost:9090`?
3. **Grafana as a second data source.** If Elastic can be added as a Prometheus data source in Grafana, rung 1 could show a literally identical query. Needs reading the docs page and a test. Not required for Video 1.
4. **Wording of "same".** "The same expression" versus "the same query." Use "expression" until we confirm what the Grafana route shows.
5. **Where `increase()` goes.** R4 gives about half the Prometheus value when the date picker is narrower than the window. Recommendation: keep Video 1 to selector, `rate()`, and `sum by`, and show `increase()` in Video 3 as the boundary-behavior example. The alternative is to keep it here with the picker set to Last 1 hour and say nothing about windows, which sets Video 3 up as a reveal. LO1 currently names `increase()`, so this also touches the LO wording. Needs your call.

## Dependencies

- Query lab verdicts for R1, R3, R4, R6: **done Oct 20.** R1, R3, and R6 are Same. R4 matches only when the date picker covers the window (see decision 5).
- Confirm the Last 30 minutes chart looks right after 45 minutes of data.
