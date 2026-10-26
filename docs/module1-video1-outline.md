# Module 1, Video 1 — Outline (draft v2)

**Working title:** Your PromQL, running in Elastic
**Objective (LO1, as approved Oct 21):** Recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
**Level:** Remember. Slow, friendly, no tricks.
**Target length:** about five minutes (an estimate, not a measurement; no hard limit).
**Format:** slides plus a live demo, with TTS narration.

**Status:** Outline v2, Oct 25, 2026. Updated to match the approved narrative (`module1-video1-narrative.md`, v1, commit `8f6f186`, with one phrase changed on Oct 25 after the docs check) and the contract (`module1-video1-contract.md`). Where this outline and the contract disagree, the contract wins. v1 of this outline (Oct 21, commit `edf75cf`) assumed the narration would be written against the footage and that the desktop was the capture machine; both are superseded below. Oct 26: the pointer to the reset runbook was fixed (it now exists).

---

## The one idea

The expression you type in Prometheus is the same expression you type in Elastic. Elastic's PROMQL command runs it. The viewer plays "find the seam": watch the expression and try to catch it changing. In three rungs it never does. Only the wrapper is new.

The wrapper is everything around the expression on the Elastic line: the `PROMQL` command, its options, and a result name. Here it makes just three choices: where it runs (`index`), when it is evaluated (`time`), and what to call the answer (the result name).

Claim hygiene for this video (see the claims register in `module1-status-2026-10-19.md`, and the contract, section 5):
- Say **expression**, not "query", when claiming sameness.
- Say **most** or **everyday**, never "all" or "any". Absolute words ("only", "never", "always") are claims and each needs checking.
- Echo Elastic's own framing: most, but not all, of PromQL is supported (register rows 1 and 36). The recap says so plainly and points forward without promising what is there.
- **No statement about the feature's status** (Video 3 covers it). This replaces v1's plan to say once that PROMQL is available on Serverless and from 9.5; the contract's rule wins.
- Forbidden: "runs unchanged" as an absolute; "single remote-write block" (say "one remote-write block added to its config"); "I want to show you"; any percentage without the seconds between the runs; "can't be done in PromQL"; `increase()`; `topk`; claims about alerting or "real time".
- Keep `[5m]` on purpose in rung 2, and say nothing that contradicts Elastic's advice to omit range selectors when porting (register row 39). Video 3 explains the difference.
- Nothing may imply Grafana works as a data source (untested, register row 15).

---

## Beats

Beats and clip names follow the contract's beat table and the run-sheet's beat map. The narrative's section names map to them one to one.

| # | Beat | On screen | Capture clips | Target on screen |
|---|---|---|---|---|
| 1 | Opening | Slide (opener) | none | n/a |
| 2 | Setup: the same data in both places | Prometheus Table tab, then Discover | A | about 25 s |
| 3 | Rung 1: pick out some series | Prometheus, then Elastic | B1, B2 | about 45 s |
| 4 | Rung 2: how fast | Prometheus, then Elastic | C1, C2 | about 45 s |
| 5 | Rung 3: which service | Prometheus, then Elastic | D1, D2 | about 45 s |
| 6 | The reveal | Slide (recap) | none | n/a |

Rungs map to the lab: selector is R1, `rate()` is R3, `sum by` is R6. `increase()` (R4) belongs to Video 3 as the boundary-behavior example.

### Beat details

1. **Opening (slide).** Open with the viewer's fear: the years invested in scrape configs, dashboards and PromQL, and the question of whether they would have to rebuild it all. Then hand over to the game: three expressions you probably know by heart, each run twice, first in Prometheus, then in Elastic; watch the expression and try to catch it changing. The slide narration is derived from this block later, with an explicit shape for the slide generator (see Slides).
2. **Setup (Clip A).** Two screens: Prometheus on the Table tab, where you run an expression today, and Kibana Discover in E-S-Q-L mode, which has a command for running prom-Q-L. Both look at the same metrics, because in this demo Prometheus ships its data to Elastic with one remote-write block added to its config. One setting to notice: the date picker is on the last hour, because the command reads only the data inside that range.
3. **Rung 1 (B1, B2): pick out some series.** The metric is `traces_span_metrics_calls_total`, a counter of calls that the OpenTelemetry Collector builds from traces. A label matcher (`service_name="frontend"`) picks out one service. Run it in Prometheus, then in Elastic. This is the one rung that teaches the wrapper: look inside the parentheses, the expression is the same text; around it, the wrapper makes three choices. The labels sit in a column instead of inline but are the same series. Did you catch the expression changing? No.
4. **Rung 2 (C1, C2): how fast.** A counter only climbs, which says little about right now, so `rate()` over `[5m]` gives the per-second average rate of increase, and `sum` makes one number: the frontend's calls per second. In Elastic: same expression, same wrapper; only the result name changes. Values and the seconds between the runs are spoken.
5. **Rung 3 (D1, D2): which service.** One number is rarely the question; the question is which service, so `sum by (service_name)` keeps one row per service. Row counts and the frontend row's value, side by side, with the seconds between the runs.
6. **The reveal (slide).** Three expressions, and the expression never changed. What changed is the wrapper: where it runs, when it is evaluated, and what to call the answer. Take an expression you use every day, drop it between the parentheses, and most of the time that is all it takes. Most, though, not all: a few things don't run in Elastic yet and a few behave differently at the edges. The closing pointer to Video 2 (the question you get paged about: which services are failing, and how often) is a courtesy that can be cut without loss.

Each rung repeats the same rhythm: say why the move is wanted, show it in Prometheus, show it in Elastic inside the same wrapper, then state the values side by side with the gap in seconds. Every number is spoken, not captioned, and comes from the take log.

---

## Slides

- **Shapes are not decided yet.** The slide guidance (`slide-narrative-guidance.md`) requires one shape per slide. v1 of this outline named Shape A for the opener and Shape C for the recap, but the approved narrative's opening block names no items, so the opener's shape has to be chosen when its narration is written. Decide the opener and recap shapes together with the author at that point.
- Not a course opener, so no "Welcome to:" line.
- No screenshot references on slides unless we supply the screenshot.
- Spellings: `prom-Q-L`, `E-S-Q-L` and `S-L-Os` in voice-over; the slide generator turns them back into the written forms. How the speech engine reads them is still a listening-test question.

---

## Decisions

1. **Narration source. Decided Oct 25:** the approved narrative file is the source of truth. The run-sheet's voice-over blocks and the story document are regenerated from it. Numbers stay `{{placeholders}}` until the take log is filled; the audio is generated after the take with the real numbers.
2. **Recording workflow:** record the screen first (no audio), then generate the narration with the real numbers. The narrative is written and approved before the take; only its numbers wait for the footage.
3. **Capture machine. Decided Oct 22:** the laptop (macOS), using `localhost`. The desktop is out. **Still open:** which recorder (macOS built-in recording or OBS), whether the cursor is captured, text legibility, resolution, browser zoom, and where the run-sheet is displayed during a take. All are settled by the capture test (contract, deliverable 8). Keep Prometheus's Status, Configuration page off camera (it can show the remote-write URL).
4. **Grafana as a second data source. Open.** Elastic's docs describe it; it is untested here. Not required for Video 1. Until it is tested, say "the same expression," never "the same query."
5. **Wording of "same". Decided:** "the same expression."
6. **Where `increase()` goes. Decided Oct 21:** Video 3, as the boundary-behavior example (R4). LO1 was updated to match.

## Dependencies

- Query lab verdicts: R1, R3 and R6 Same (Oct 20), recorded on the old dataset. They are rerun on a freshly reset stack as the rehearsal. R4 belongs to Video 3.
- **Stack state required (contract, section 6):** a freshly reset stack (`docs/reset-runbook.md`, Part B); a warm-up of at least 45 minutes (the run-sheet's existing rule, which the author may raise); `paymentFailure` off; the pre-roll checks passed (Part C of the runbook: uptime, the remote-write counters, the flags page; plus the browser and screen steps in the run-sheet).
- The one-time setup (new Serverless project and key, laptop readiness check, first start) comes first (`docs/reset-runbook.md`, Part A).
- Re-read the limitations page and record the retrieval date before the take; docs change often.
