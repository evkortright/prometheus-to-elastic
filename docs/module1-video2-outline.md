# Module 1, Video 2 — Outline (draft)

**Working title:** Build it up: a per-service error ratio, rung by rung
**Objective (LO2, as approved Oct 21):** Write and execute PromQL against a live Elastic TSDS — instant vectors, range vectors reduced by functions, aggregation, and arithmetic between aggregated results — getting results a Prometheus user would already expect. *(Apply)*
**Level:** Apply. The viewer builds one expression, one idea at a time, and checks each step against Prometheus.
**Target length:** flexible, about 7 to 10 minutes.
**Format:** slides plus a live demo, with TTS narration, recorded screen first (same workflow as Video 1).

**Status:** Outline only, drafted Oct 22, 2026. Nothing recorded. Narration and the run-sheet come after you approve this outline. Decisions 1, 2, 4, 6, 8 and 9 approved Oct 25, and a new decision 10 added and approved; 3, 5 and 7 are open.

---

## The one idea

An SRE's real question is "which services are failing, and how often?" In PromQL that is an error ratio per service. You can build it from four small ideas, each one rung: filter the series, take a rate and aggregate it, scale it with arithmetic, and divide two aggregates. Each rung runs in Prometheus and then in Elastic, and the viewer checks that the answers agree.

Claim hygiene for this video (see the claims register in `module1-status-2026-10-19.md`):
- Say **expression**, not "query", when claiming sameness. Say **most** or **everyday**, never "all". No "preview".
- Every number comes from the take log, next to what it is compared with. Agreement statements carry the gap in seconds between the two runs.
- State the ratio rule positively: aggregate both sides the same way (Elastic's docs; lab R8). Leave the failures to Video 3.
- No claims about alerting, detection or "real time". No `increase()` and no `topk` (Video 3 and untested).
- Don't say a service with no errors "has a ratio of zero". It is absent from the result (lab R8).

---

## Beats

| # | Beat | On screen | Approx. |
|---|---|---|---|
| 1 | Hook: the question you actually ask | Slide | 0:40 |
| 2 | What a series is in Elastic (optional) | Slide | 1:00 |
| 3 | Rung A: narrow the series with matchers (R2) | Prometheus, then Discover | 1:30 |
| 4 | Rung B: one rate for the whole system (R5) | Both | 1:00 |
| 5 | Rung C: scale it with arithmetic (R7) | Both | 1:00 |
| 6 | Rung D: divide two aggregates, the error ratio (R8) | Both | 2:00 |
| 7 | Payoff: watch it over time (optional) | Both | 1:30 |
| 8 | Recap and what comes next | Slide | 0:40 |

Rungs map to the lab: R2, R5, R7 and R8 are the new ones. R1, R3 and R6 from Video 1 get one sentence each as the starting point. All four new rungs were verified Same on Oct 21 on the previous dataset.

### Beat details

1. **Hook slide.** The question, then the plan: four small ideas that stack into one expression. Shape to decide when the narration is written.
2. **What a series is (optional slide).** Metric name plus labels identifies a series; Elastic stores the labels as dimensions in a time series data stream. This supports the module's stated skill of TSDS grounding. **Needs verification against the TSDS docs before any wording is written.**
3. **Rung A: matchers (R2).** Show `=~` and `!=` on the same metric, using the count form so the viewer sees which series matched.
   - Run `count by (service_name, status_code)` with and without the `status_code!=` matcher. The difference is the error series that `!=` removes (Oct 21: 14 for frontend and 2 for checkout, live numbers will differ).
   - Teaching point: a regex matcher is fully anchored, so `frontend|checkout` does not match `frontend-proxy` (verified on both sides).
   - **Pause-and-try prompt:** "Will `frontend-proxy` match?" Answer: no.
4. **Rung B: whole-system rate (R5).** `sum(rate(...[5m]))` with no `by` collapses every series into one number. Prometheus shows `{}` for the empty label set; Elastic returns just the value and the evaluation time.
5. **Rung C: arithmetic with a scalar (R7).** `sum by (service_name) (rate(...)) * 60` turns calls per second into calls per minute, one row per service, labels kept.
   - **Pause-and-try prompt:** "What does the frontend row say if we multiply by 3600 instead?" (calls per hour, by arithmetic only).
6. **Rung D: the error ratio (R8).** Error rate by service divided by total rate by service.
   - The rule in plain words: aggregate both sides the same way. Both sides here use `sum by (service_name)`.
   - Services with no error series drop out of the result on both sides. Say so, because an SRE will read the missing rows.
   - Values depend on what is happening at record time. See the dependency on nonzero values below.
7. **Payoff (optional).** Run the ratio as a range query (leave out `time=?_tend`) and show it over time in Discover next to Prometheus's Graph tab. **Needs a rehearsal to see how the chart looks.** If the `paymentFailure` flag is used to make the ratio move, it needs the incident-demo measurements first (claims register row 13, section 3 of the status doc).
8. **Recap slide.** Four ideas, peer cards (Shape C): matchers, a rate aggregated across series, arithmetic with a scalar, and a ratio of two aggregates. Close with the honest sentence: most, but not all, of PromQL works this way, and Video 3 looks at the edges.

---

## Slides (shapes to confirm when narrations are written)

- **Hook:** a claim, not a transition. Not a course opener.
- **What a series is (optional):** a short layered or card shape, decided after the docs check.
- **Recap:** Shape C, four peer cards.
- No screenshot references on slides unless we supply the screenshot.

---

## Open decisions

1. **Through-line.** Build toward the per-service error ratio (R8). Recommended: it is the question an SRE asks, and every earlier rung contributes a piece. **Approved Oct 25.**
2. **Which rungs to show.** Recommended: R2, R5, R7, R8 in full, and R1, R3, R6 as one-sentence reminders from Video 1. **Approved Oct 25.**
3. **Series slide (beat 2).** Include only if the TSDS docs support the wording. Otherwise it moves to a later module or a short slide in Video 3.
4. **Nonzero values.** In the Oct 21 R8 run, six of eight services showed a ratio of exactly 0, so agreement is trivial for those rows. Options: wait for a natural error episode, or turn `paymentFailure` on for a controlled one. Recommended: measure the flag's effect first. **Decided Oct 25:** use the controlled `paymentFailure` flag, after measuring its effect on a fresh stack. Every video starts from a reset, so we cannot wait for a natural error episode.
5. **Range query and chart (beat 7).** Include if the rehearsal shows a clear chart on both sides.
6. **Pause-and-try prompts.** Recommended: two (beats 3 and 5), matching the Apply level. They cost a few seconds each. **Approved Oct 25.**
7. **A percent form.** `* 100` on the ratio is untested. Test in the rehearsal, or keep `* 60` from R7.
8. **Length.** Flexible. Cut the optional beats first if it runs long. **Approved Oct 25.**
9. **Same recording workflow as Video 1.** The run-sheet is drafted after you approve this outline. **Approved Oct 25.**
10. **Strictly standalone (Oct 25).** The video restates what it needs in about 20 seconds before the first rung: how Elastic's `PROMQL` command wraps an expression, and which metric we query. Any pointer to Video 1 or Video 3 is a courtesy that can be cut without loss. The contract lists this as the video's entry knowledge. **Approved Oct 25.**

## Dependencies

- Query lab verdicts for R2, R5, R7 and R8: **done Oct 21**, on the previous dataset. Re-run them on the fresh stack in a rehearsal.
- The Elastic row counts for R7 and R8 were not recorded in the lab; record them in the rehearsal.
- Nonzero values at record time (decision 4): the controlled flag, with its effect measured first.
- TSDS docs check, if beat 2 stays.
- Before every recording: uptime, `paymentFailure` state, and `samples_failed_total`.
- A reset before the rehearsal and before the take (the reset runbook, handoff tracker row 26).
