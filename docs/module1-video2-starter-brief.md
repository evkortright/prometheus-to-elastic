# Video 2 starter brief, from the Video 1 chat (Oct 27, 2026)

> **Root note (Oct 27):** the pack's files now live in the repo. The voice guide is `docs/narration-voice-guide.md`, and the tools are in `scripts/` (`make_review_script.py`, `review-config.video2.example.json`, `fill_placeholders.py`, `take-values.example.json`). Where this brief names the pack, it means those files, so no separate pack is needed. This brief is seed material: the Video 2 chat owns it and may rewrite it.

**How to use it:** paste this into the new Video 2 chat right after the root's starter prompt (`docs/module1-video2-contract.md`, section 11), and attach a fresh repo archive plus the starter pack. **The contract is the authority on scope and the finish line; this brief adds what the Video 1 chat learned.** On *voice*, `narration-voice-guide.md` wins.

## 1. Read, in this order

1. `docs/module1-video2-contract.md`, then its outline and the root's seed narrative (draft v1).
2. **`narration-voice-guide.md`** (in the pack). This is the most important item.
3. Video 1 as exemplars: `module1-video1-narrative.md` v2 (the voice), `module1-video1-run-sheet.md` v6 (the run-sheet structure), and `module1-video1-log.md` sections 2, 7, 8 and 9 (decisions, observed UI facts, the step ledger, findings).
4. The handoff's sections 2, 3, 9, 10, 11 and 12, as the contract says.

## 2. How the Video 1 chat worked (keep it)

- **Tiny steps, one at a time.** Expected output before each step; one question at a time; the author pastes output and the chat checks it line by line before the next step.
- **The repo routine on every delivery:** a base-hash check of the files being replaced, `unzip -l` before unzipping, the diff stat, a safety grep, then commit. Replay the steps in a scratch repo first, so the expected output is real.
- **A step ledger** in the log: each step classed read-only, write, gate or guided, with PASS or FAIL. It shows which steps a script could run (the pre-roll checks are the obvious ones).
- **The log is the truth.** Decisions, claim confirmations with dates, results and findings go in `module1-video2-log.md` as they happen.

## 3. The voice (the short version)

A professional trainer, an SME, speaking peer to peer. Objective stated early in the learning objective's own words; the viewer's stakes first; a viewing task instead of any game; connected sentences with contractions and direct address; claims stated precisely, with no absolute words; every number spoken from the take, with the gap in seconds; "Let's run it" at each execution. The full rules, the opening skeleton, the retired words and a 15-point checklist are in the guide.

**What I noticed in the root's seed narrative** (for you and the author to decide, not to apply blindly). Its structure is good: four ideas, a question-and-answer device with planned pauses, and honest optional beats. It was written before the voice was set, so:

- **No objective is stated.** Learning objective 2 (write and execute PromQL, including arithmetic between aggregates) is not said to the viewer. The Hook ends well but never promises what they'll be able to do.
- **Absolute words that are claims:** "the only question that matters" (Hook), "That's all the not-equals did", "never shows up", "every series collapses", "just works", "That's the whole climb". "A counter on its own just climbs" needs "keeps climbing" (a counter resets on restart).
- **Old control names:** the screen notes say "then Run". The real controls are **Execute** in Prometheus and **Search** or **Cmd+Enter** in Discover.
- **The closing line** ("the edges are worth knowing before you rely on them") stands alone, but it invites "where?". See section 6.
- **Idea 4 needs the payment flag on,** and its effect is unmeasured, so the ratio's numbers stay placeholders until the rehearsal.

## 4. Stack and recording facts

- **The stack is shared, and the flag differs.** Video 1 needs `paymentFailure` off; Video 2's last idea needs it on. Prepare Video 2's stack after Video 1's takes, using the reset runbook (Part B, then Part C).
- **Prometheus scrapes once a minute** (the new sample lands at about :37), and Elastic receives it some seconds later. Two runs agree to better than 1e-9 when both fall inside one scrape minute: the Prometheus click after about :40, the Elastic click before about :35 of the next minute. Video 2 has more pairs, so plan this per idea.
- **One continuous take per pair** keeps the gap short. Read the gap from the footage, not a clock. **Do not take screenshots while recording** (the macOS thumbnail may appear in the video); collect numbers after you stop.
- **Observed UI facts and the recorder settings** are in Video 1's log (section 7) and run-sheet v6 ("How to use this sheet"). Record Video 2's own once, as facts, before writing steps.
- **Staging between takes** (proposed, to be judged on the first take): Prometheus ⋮, Remove query, Add query; Discover, a zero-row query, then clear and paste the next line.
- **The helpers** (outside the repo): `fill_placeholders.py` is Video 1's; adapt its placeholder list for Video 2 (its keys and the "digits agree" rule). `make_review_script.py` builds the review script.

## 5. What "ready for review" means here

The author wants a plain-text voice-over script to paste into a document beside the slides, and reviewers read the words. Once the author approves a valid narration:

1. Derive the slide-shape versions for the slides that need them (Hook and Recap).
2. Write the title-slide narration ("Welcome to … In this lesson, you will …").
3. Run `make_review_script.py` with a config (an example for Video 2 is in the pack; the Demo slide carries all the demo voice-over).
4. The author submits it for review; fold the feedback into the narrative, then move on to the takes.

## 6. Decisions coming from above

- **Strictly standalone** (Oct 25): the video restates what it needs; any pointer to another video is a cuttable courtesy.
- **No statement of the feature's status.**
- **Video 3 is under consideration for dropping.** Write Video 2's closing so it stands alone. If it is dropped, a durable pointer may replace the promise ("Elastic's documentation keeps the current list of limits, so check it before you move something you depend on"). Don't build on Video 3.

## 7. Mistakes to avoid (all mine, in Video 1)

- I wrote UI labels ("Run") before seeing the screen. Observe them once; then use them.
- I gave numbers and counts I hadn't measured ("160 words", "every sentence under 150 characters"). Measure before you claim.
- I predicted counters instead of stating relationships. Test relations (`failed` 0, `sent` growing), not estimates.
- I misread a screenshot (a tab group as a third tab). When a screenshot is ambiguous, say what you can see and ask.
- Markdown tables break on an unescaped pipe. Check every table.
- Approved files carried stale text (a status line, notes). Re-read what you rely on, and fix what's stale.
- I let a toolkit rule shape the spoken voice. Write the normalized narration first.

## 8. Settle with the author at the start

1. Voice-pass the seed (my suggestion, because its structure is good) or rewrite?
2. The optional beats: decision 3 (the series slide) and decision 5 (the range chart).
3. Does the Hook state learning objective 2 as an objective?
4. The closing line, given the Video 3 question.
5. The flag-on stack plan, and how long to wait after switching the flag on (the seed says at least one rate window, an inference to test).
