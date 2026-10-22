# Module 1, Video 1 — Outline (draft)

**Working title:** Your PromQL, running in Elastic
**Objective (LO1, as approved Oct 21):** Recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
**Level:** Remember. Slow, friendly, no tricks.
**Target length:** about 4 to 5 minutes.
**Format:** slides plus a live demo, with TTS narration.

**Status:** Outline updated Oct 21, after the query lab (R1 to R8, all confirmed) and the decisions below. Recording comes first; narration is written against the footage.

---

## The one idea

The expression you type in Prometheus is the same expression you type in Elastic. Elastic's PROMQL command runs it. The viewer watches that be true three times.

Claim hygiene for this video (see the claims register in `module1-status-2026-10-19.md`):
- Say **expression**, not "query", when claiming sameness.
- Say **most** or **everyday**, never "all" or "any".
- Don't say "preview". Say once, plainly, that PROMQL is available on Elastic Cloud Serverless and in the Elastic Stack from 9.5 (claims register row 3).
- Echo Elastic's own framing: most, but not all, of PromQL is supported (claims register rows 1 and 4 to 6).
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
| 6 | Recap and what comes next | Slide (recap) | 0:40 |

Rungs map to the lab: selector is R1, `rate()` is R3, `sum by` is R6. `increase()` (R4) moved to Video 3 as the boundary-behavior example. The recording is a fresh live run; the lab numbers are evidence, not script.

### Beat details

1. **Hook and slide.** A claim, not a transition, for example that the PromQL you write today has a new place to run. Plant one short title phrase (3 to 8 words). List the patterns the viewer will recognize (Shape A, verb-first, three items: label selectors, aggregation, `rate()` on counters).
2. **Setup.** One sentence on how the data got there (Prometheus remote-writes to Elastic) and that both screens show the same metrics. Show the Prometheus Table tab and Discover in ES|QL mode. Say once that PROMQL is available on Elastic Cloud Serverless and in the Elastic Stack from 9.5.
3. **Each rung, the same four moves:**
   1. Type the expression in Prometheus and run it.
   2. Type it in Discover inside the PROMQL command.
   3. Point at the expression, which is the same on both screens.
   4. Point at the values, which are close.
   On the first rung only, say what the extra words around the expression are: the PROMQL command and a result name. Don't call it "no changes."
6. **Recap slide.** Name the patterns that carried over (Shape C cards, 3: label selectors, aggregation with `sum by`, `rate()` on counters). Close with one honest sentence: most, but not all, of PromQL is supported, some constructs behave differently or aren't supported yet, and Video 3 covers them.

---

## Slides (shapes to confirm when narrations are written)

- **Opener:** Shape A, "what you will recognize." Not a course opener, so no "Welcome to:" line.
- **Recap:** Shape C, peer cards for the patterns, each with a name and one short definition.
- No screenshot references on slides unless we supply the screenshot.

---

## Decisions

1. **Recording workflow. Decided Oct 21:** record the screen first, then write or time the narration to it.
2. **Capture machine. Decided Oct 21:** the desktop, using `localhost`. **Still open:** which recorder. Before the real take, record a 30-second test clip while the stack is running, then re-check `samples_failed_total` and `pending` to see whether recording load affects the stack. Keep Prometheus's Status, Configuration page off camera (it can show the remote-write URL).
3. **Grafana as a second data source. Open.** Elastic's docs describe using Elasticsearch as a Prometheus data source in Grafana; it is untested here. Not required for Video 1. Until it is tested, say "the same expression," never "the same query."
4. **Wording of "same". Decided:** "the same expression."
5. **Where `increase()` goes. Decided Oct 21:** Video 3, as the boundary-behavior example (R4 gives about half the Prometheus value when the date picker is narrower than the window). LO1 was updated to match.

## Dependencies

- Query lab verdicts: R1, R3 and R6 Same (Oct 20); R2, R5, R7 and R8 Same (Oct 21). R4 belongs to Video 3.
- The stack was wiped and restarted on Oct 22 at 00:41:00 UTC for a clean dataset. Confirm the Last 30 minutes chart looks right once there is enough data, and re-run R1, R3 and R6 live before recording.
- Before every recording: check uptime, confirm `paymentFailure` is off, and confirm `samples_failed_total` is 0 (or explained).
