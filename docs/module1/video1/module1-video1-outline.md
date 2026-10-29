# Module 1, Video 1 — Outline (draft v3)

**Working title:** Your PromQL, running in Elastic
**Objective (LO1, as approved Oct 21):** Recognize which everyday PromQL patterns (label selectors, aggregation, `rate()` on counters) run in Elastic using the same PromQL expression.
**Level:** Remember. Slow, friendly, no tricks.
**Target length:** about five minutes (an estimate, not a measurement; no hard limit).
**Format:** slides plus a live demo, with TTS narration.

**Status:** Outline v3, Oct 26, 2026. Updated to match narrative v2 (`module1-video1-narrative.md`, the trainer-voice pass the author approved on Oct 26), the contract (`module1-video1-contract.md`), and the guided rehearsal and capture test of Oct 26 (`module1-video1-log.md`). Where this outline and the contract disagree, the contract wins. v1 of this outline (Oct 21, commit `edf75cf`) assumed the narration would be written against the footage and that the desktop was the capture machine; both are superseded. v2 is commit `3e59f34`.

---

## The one idea

The expression you type in Prometheus is the same expression you type in Elastic, and Elastic's PROMQL command runs it. The video is training, spoken by a trainer who is a peer: it states its objective up front (recognize which everyday prom-Q-L expressions run in Elastic using the same expression), tests it three times, and gives the viewer two things to watch each time: does the expression change, and do the numbers agree? It never changes. What's new is the wrapper.

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

1. **Opening (slide).** Open with the viewer's stakes: the years invested in scrape configs, dashboards and PromQL, and the question of whether they would have to rebuild it all. Then state the objective in the learning objective's own words, name the method (three expressions, each run twice, first in Prometheus, then in Elastic, against the same data) and the three patterns, set the level (this audience writes prom-Q-L daily), promise plainness about what doesn't carry over, and give the viewing task. The spoken text is in narrative v2; the slide-shape version (Shape A) is derived from it (run-sheet, beat 1).
2. **Setup (Clip A).** Two screens: Prometheus on the Table tab, where you run an expression today, and Kibana Discover in E-S-Q-L mode, which has a command for running prom-Q-L. Both look at the same metrics, because in this demo Prometheus ships its data to Elastic with one remote-write block added to its config. One setting to notice: the date picker is on the last hour, because the command reads only the data inside that range.
3. **Rung 1 (B1, B2): pick out some series.** The metric is `traces_span_metrics_calls_total`, a counter of calls that the OpenTelemetry Collector builds from traces. A label matcher (`service_name="frontend"`) picks out one service. Run it in Prometheus, then in Elastic. This is the one rung that teaches the wrapper: look inside the parentheses, the expression is the same text; around it, the wrapper makes three choices. The labels sit in a column instead of inline but are the same series. Did the expression change? No.
4. **Rung 2 (C1, C2): how fast.** A counter keeps climbing, which says little about right now, so `rate()` over `[5m]` gives the per-second average rate of increase, and `sum` makes one number: the frontend's calls per second. In Elastic: same expression, same wrapper; only the result name changes. Values and the seconds between the runs are spoken.
5. **Rung 3 (D1, D2): which service.** One number is rarely the question; the question is which service, so `sum by (service_name)` keeps one row per service. Row counts and the frontend row's value, side by side, with the seconds between the runs.
6. **The reveal (slide).** Close the loop on the objective: for these three, the same text ran in both places, and the numbers agreed. What changed is the wrapper, which here makes just three choices: where it runs, when it is evaluated, and what to call the answer. Say plainly that most, though not all, of prom-Q-L runs in Elastic: a few things don't run yet and a few behave differently at the edges. Then invite the viewer to try an expression of their own. A pointer to Video 2 (which services are failing, and how often) is not in the text; it can be added at assembly.

Each rung repeats the same rhythm: say why the step is wanted, show it in Prometheus, show it in Elastic inside the same wrapper, then state the values side by side with the gap in seconds. Every number is spoken, not captioned, and comes from the take.

---

## Slides

- **Three versions of each narration (the author's model, Oct 26).** An informal outline (this file); the **normalized narration** (narrative v2: what an instructor or the speech engine reads, free of the slide toolkit's shape rules); and a **slide-shape version** that triggers the toolkit's slide patterns. For this video only the two slides need the third version: the opener (**Shape A**, a skills list; an earlier Shape D decision of Oct 26 was superseded once the voice changed) and the recap (**Shape C**, peer cards, approved Oct 26). Both are in the run-sheet, beats 1 and 6, derived from the normalized text. How the toolkit times its reveals against audio read from the spoken version is not known here.
- Not a course opener, so no "Welcome to:" line.
- No screenshot references on slides unless we supply the screenshot.
- Spellings: `prom-Q-L`, `E-S-Q-L` and `S-L-Os` in voice-over; the slide generator turns them back into the written forms. How the speech engine reads them is still a listening-test question.

---

## Decisions

1. **Narration source. Decided Oct 25:** the approved narrative file is the source of truth. The run-sheet's voice-over blocks and the story document are regenerated from it. Numbers stay `{{placeholders}}` until the take log is filled; the audio is generated after the take with the real numbers.
2. **Recording workflow:** record the screen first (no audio), then generate the narration with the real numbers. The narrative is written and approved before the take; only its numbers wait for the footage. Since Oct 26: one continuous take per rung is the recommended default (the narration blocks stay separate), and the narration may play in the background as a pacing guide, which is the author's choice.
3. **Capture machine. Decided Oct 22:** the laptop (macOS), using `localhost`. The desktop is out. **Closed Oct 26 by the capture test:** the recorder is the macOS built-in one (Command+Shift+5, microphone off, 5-second timer, Control+Command+F full screen, Control+Tab between two tabs), browser zoom 125%, text easy to read, the cursor fine, 3456 × 2234 H.264 imports into Resolve, and the stack was unaffected. **Still open:** where the run-sheet is displayed during a take. Keep Prometheus's Status, Configuration page off camera (it can show the remote-write URL).
4. **Grafana as a second data source. Open.** Elastic's docs describe it; it is untested here. Not required for Video 1. Until it is tested, say "the same expression," never "the same query."
5. **Wording of "same". Decided:** "the same expression."
6. **Where `increase()` goes. Decided Oct 21:** Video 3, as the boundary-behavior example (R4). LO1 was updated to match.

## Dependencies

- Query lab verdicts: R1, R3 and R6 Same (Oct 20), recorded on the old dataset. They are rerun on a freshly reset stack as the rehearsal. R4 belongs to Video 3.
- **Stack state required (contract, section 6):** a freshly reset stack (`docs/shared/operations/reset-runbook.md`, Part B); a warm-up of at least 45 minutes (the run-sheet's existing rule, which the author may raise); `paymentFailure` off; the pre-roll checks passed (Part C of the runbook: uptime, the remote-write counters, the flags page; plus the browser and screen steps in the run-sheet).
- The one-time setup (new Serverless project and key, laptop readiness check, first start) comes first (`docs/shared/operations/reset-runbook.md`, Part A).
- Re-read the limitations page and record the retrieval date before the take; docs change often.
