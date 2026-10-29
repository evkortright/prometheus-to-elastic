# Module 1, Video 3 — Contract

**Status:** Draft v1, October 25, 2026. Filled in from `docs/shared/video-contract-template.md`. Owned by the root chat.
**Under consideration (Oct 27):** the author is considering dropping Video 3. Nothing in this contract changes until the author decides (handoff, section 8).
**Unlike Videos 1 and 2,** this video has no outline and no narrative yet. The Video 3 chat writes both. The candidate beats in section 4 and the facts in the claims register are seed material, not decisions (section 10).

---

## 0. Header

| Field | Value |
|---|---|
| Video | 3, working title: "Where it differs" (the Video 3 chat may change it) |
| Contract version and date | v1, October 25, 2026 |
| Contract status | Draft |
| Chat | Not started yet |
| Root handoff | `docs/handoff-module1-living.md` (read-only for the video chat) |

## 1. The finish line

The contract is fulfilled when the author, as the first video editor, has assembled the complete video from the package in section 9 and can submit it to the second editor. The video chat's own work is complete at conditions 1 to 4 of the template's table (`docs/shared/video-contract-template.md`, section 1). Conditions 5 to 7 are the author's.

## 2. Identity

- **Learning objective (from `docs/shared/module-learning-objectives.md`):** **Identify** documented differences between Elastic's PromQL and Prometheus — unsupported constructs, behavior at query boundaries such as the date-picker window, and the feature's current status. *(Analyze)*
- **Module context (Module 01, PromQL Support; format: Feature Highlight):** the module aims at "PromQL syntax fluency on Elastic; TSDS conceptual grounding (series identity, dimensions, metric types); confidence that most everyday Prometheus expressions carry over, and the ability to check your own against the documented limits; an accurate, non-oversold picture of what's still incomplete." The learning-objectives file also says limitations are covered in the third video, and that every limitation claim traces to Elastic's documentation or to a recorded test result.
- **Audience:** an SRE who uses PromQL and Grafana every day. Their question here is "where does this stop working, and how will I know?"
- **Target length:** flexible, roughly 8 to 10 minutes; the chat proposes the beats. No hard limit.

## 3. Standalone rule

| What the viewer needs to know | Where it comes from | Time on screen |
|---|---|---|
| PromQL, and Prometheus's expression browser (Table tab) | Assumed (the audience) | none |
| What Discover's E-S-Q-L mode, Elastic's PROMQL command and the wrapper are (where it runs, when it is evaluated, what the answer is called) | Restated in a setup block | about 30 s |
| How the date picker's range limits what the command sees | **Taught in this video**, as the boundary-behavior example. It is a learning objective here, not a reminder | within the beat |
| Which metric we query and where it comes from | Setup block | one sentence |

- **Closing line:** proposed by the chat. It should state the honest limit on its own terms (what the viewer should now check before relying on an expression). Any pointer to another video is a courtesy that can be cut.

## 4. Story

- **Through-line:** proposed by the Video 3 chat with the author. Candidate (from the arc idea in the handoff, section 8): the viewer can finally *catch* the expression changing. In Video 1 it never did. Here the expression has to change, or it cannot run, or it quietly behaves differently. Because the videos are standalone, this must be a bonus for viewers of Video 1, and nothing may depend on it.
- **Narrative file:** `docs/module1-video3-narrative.md`, written by the Video 3 chat after its outline.
- **Outline file:** `docs/module1-video3-outline.md`, written by the Video 3 chat.

Candidate beats (a seed, not a decision), each tied to the evidence it needs:

| Candidate beat | What it shows | Evidence |
|---|---|---|
| Hook and setup | The question, then the restated wrapper | none |
| Constructs that return an error | Explicit matching with `on()` (P1), a subquery (P2), the `@` modifier (P3) and the `and` operator (P4) each return a client error in Elastic | Probes P1 to P4 with Elastic's exact error text; register rows 4, 5, 40 |
| The silent one | A division between two different unaggregated metrics returns no results, not an error (P5), and the fix is to aggregate both sides | Probe P5; register rows 6 and 21 |
| The boundary | The same `increase()` expression gives about half the value when the date picker is narrower than the window, and the same value when the picker covers it (R4) | Lab R4 re-run on the fresh stack; register row 19 |
| Windows and steps | Omitting the range selector (P6) and controlling the step (P7); Elastic's own advice is to omit range selectors | Probes P6 and P7; register rows 7, 8 and 39 |
| What you can't test here | Staleness markers, time-bucket alignment, native histograms, and the HTTP API's constraints are documented but untested here | Register rows 24, 25, 27 and 42, 43 |
| Status | Whether the feature is generally available or in preview | The author's browser (the fetched pages strip the badges); register row 44 |
| Recap | The honest sentence: most, not all, and how to check your own expressions against the documented limits | Register row 1 |

## 5. Claims

- **Wording rules:** as in the template. Distinguish three behaviors, and never blur them: an unsupported construct returns a client error (4xx); some binary expressions return no results instead of an error; and some behaviors differ without any error (the boundary, time-bucket alignment).
- **Forbidden for this video:** "all"; "never"; "always"; any statement about the feature's status until the author has read it from the live page in a browser; "fails silently" for the constructs the docs say return a client error; any claim that Grafana works with Elastic (register row 15 is untested); alerting, detection or "real time" claims; any percentage without the seconds between the runs.
- **Claims-register rows used** (status doc, section 4): 1, 4, 5, 6, 7, 8, 19, 21, 22, 23, 24, 25, 26, 27, 28, 31 (open), 36, 39, 40, 42, 43 and 44.
- **Known edge:** the ES|QL PROMQL command and the HTTP API behave differently for selectors without a range. The command's implicit window is the larger of the step and the scrape interval (rows 7 and 36); the HTTP API's instant query looks back a fixed five minutes (rows 28 and 43). Keep them apart.

The claims-to-confirm table lives in the narrative file, once it exists.

## 6. Evidence plan

- **Lab items this video runs:** probes P1 to P8, and R4 re-run (the picker-width test: a 15-minute picker, then a 1-hour picker, against a 30-minute `increase()` window). The lab holds the expressions. The take log records the **exact error text** Elastic returns for P1 to P4, and the Prometheus result for each, including whether Prometheus rejects any of them.
- **Stack state required:** a freshly reset stack (`docs/shared/operations/reset-runbook.md`, Part B). Warm-up of at least 45 minutes: the R4 comparison needs the 30-minute window to be fully covered by data when the picker is set to one hour, which 45 minutes allows (confirm in the rehearsal). `paymentFailure` off. The pre-roll checks passed.
- **Not run, by design:** native histograms, the HTTP API, and staleness. Say so in the video, and do not claim results for them.
- **Status check:** at script time, the author reads the "applies to" badges on the PROMQL command page and the limitations page in a browser and reports them to the chat. The chat records them as a register request for the root (row 44).
- **Take log fields:** per probe, the Prometheus result, the Elastic result (the exact error text where there is one), the seconds between the runs where a value is compared, and retakes and notes.

The placeholder table lives in the narrative file, once it exists.

## 7. Narration rules

As in the template. For Video 3 specifically:
- The voice is the trainer voice, and the three-version model applies: see `docs/shared/narration-voice-guide.md`.
- Error texts are spoken as written on screen only if short and clean. Otherwise the narration says "a client error" and the screen shows the exact text, which is part of what the demo displays.
- The slide narrations are derived from the narrative file with an explicit shape for the slide generator. A limitations table is a natural candidate for a peer-card or comparison shape; the chat decides with the author.

## 8. Deliverables and acceptance checklist

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | Learning objective | Author | Done (approved Oct 21) |
| 2 | Outline, with the through-line decided | Video chat and author | Not started |
| 3 | Narrative drafted (with placeholders and a claims-to-confirm table) | Video chat | Not started |
| 4 | Narrative approved | Author | Not started |
| 5 | Slide narrations, with explicit shapes | Video chat | Not started |
| 6 | Run-sheet written from the approved narrative | Video chat | Not started |
| 7 | One-time setup and a stack reset (`docs/shared/operations/reset-runbook.md`, Parts A and B) | Root and author | Not started |
| 8 | Probes P1 to P8 and the R4 re-run, with exact error texts | Video chat guides, author runs | Not started |
| 9 | The feature's status read from the live pages in a browser | Author | Not started |
| 10 | Claims confirmed against the docs and the take | Video chat | Not started |
| 11 | The take: footage and the take log | Author | Not started |
| 12 | Placeholders filled; narration regenerated with the real numbers; audio generated and listened to | Video chat and author | Not started |
| 13 | The first-pass video assembled and exported | Author | Not started |
| 14 | Package submitted to the second editor | Author | Not started |

## 9. Package for the second editor

- The exported first-pass video.
- The slide files: the slide generator produces a `.pptx`; the author uploads it to Google Drive, opens it as Google Slides, and gives the second editor the link.

Everything else stays in the repo. **This section changes only if something changes on the author's side.**

## 10. Ownership and change rules

- **The Video 3 chat owns:** `docs/module1-video3-outline.md`, `docs/module1-video3-narrative.md`, `docs/module1-video3-log.md` (created with its first entry), and the Video 3 run-sheet and story document when they exist.
- **Seed material:** the candidate beats in section 4, and the docs findings already in the claims register (rows 36 to 44). They are proposals, not decisions. The chat asks the author at the start whether to use them, rewrite them or ignore them.
- **Shared files belong to the root** (see the template, section 10). Known needs (record them in the video log first and send them at a milestone): register rows for the probe results and the exact error texts once they exist, a row for the feature's status once the author has read the badges, and the lab's probe tables once filled.
- **Authority and the video log (Oct 26):** this chat is the source of truth for this video's files and for the video's state. It verifies the author's pasted output for its own deliveries (the base hash, the expected stat, the commit result) and does not route them through the root. It keeps `docs/module1-video3-log.md`, which it creates with its first entry: the checklist state, claim confirmations with their retrieval dates, probe results, the take log, and the decisions the author makes with this chat (for example the slide shapes). Once the log exists, it is the truth about the video's state, ahead of section 8 of this contract. The root reviews a delivery only if the author asks. This applies while the chat is the active chat: only one chat at a time delivers changes to the repo (handoff, section 2, agreement 15), and a chat the author has not named active is advisory.

## 11. Video chat routine and starter prompt

As in the template (sections 11 and 12). The starter prompt, with this file's name filled in:

```
I'm the author of a Prometheus-to-Elastic training track, and this chat produces Video 3 of Module 1. Please read docs/module1/video3/module1-video3-contract.md first, then the files it lists, then sections 1, 2, 3, 9, 10, 11 and 12 of docs/handoff-module1-living.md (read-only). Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Don't edit shared files. You are the source of truth for this video's files and state: verify my pasted output for your own deliveries, keep a video log, and send requests to the root chat only when the contract says to (a shared file that truly needs a change, a decision that crosses videos, or a milestone). You are the active chat only when I say so; until then you are advisory: answer and review, but do not deliver files. Do not end replies with status lists unless something changed materially or I ask. If the contract lists seed material, ask me first whether to use it, rewrite it, or ignore it.
```

Files to read, in order: this contract; `docs/module1/module1-query-lab.md` (probes P1 to P8 and R4); `docs/module1-status-2026-10-19.md` (the claims register, section 4); `docs/module1/video2/module1-video2-outline.md` (for the format of an outline only); `docs/shared/slide-narrative-guidance.md`; `docs/module1/video1/module1-video1-narrative.md` and `docs/module1/video2/module1-video2-narrative.md` (for the voice only; Video 3 must not depend on them).

Work that can start before the one-time setup (no stack needed): checklist rows 2 to 6, and the docs reading the chat needs for its claims table.
