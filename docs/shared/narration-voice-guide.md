# Narration voice guide (Module 1)

**Status:** shared standard, adopted by the root chat on Oct 27, 2026. Written by the Video 1 chat from the decisions the author made on Oct 26 while working on Video 1; the author adopted the *voice* for Video 1 (narrative v2, commit `86f6c71`). **The author has not yet read this written guide**, so it stays open to their edits. Where this guide and a contract disagree on a *factual* rule, the contract wins; on *voice*, this guide wins. Owned by the root chat.

**Why it exists:** the first drafts read like a feature highlight for a video channel. This is training. The voice is the thing that makes it feel like training, so it is written down once and applied to every narration.

---

## 1. The voice, in one paragraph

A professional trainer who is a subject-matter expert, speaking peer to peer to an SRE who writes PromQL every day. Calm authority, warm and direct, and quick. Conversational the way a good instructor is in a room: contractions, "you" and "we", and connectors that carry the listener from one idea to the next. It makes a claim and then shows the evidence. It respects what the viewer already knows, says plainly what is new, and is honest about limits. The energy comes from pace, specifics and the payoff of watching two systems agree, not from adjectives.

## 2. Three versions of every narration

| Version | What it is for | What binds it |
|---|---|---|
| Informal outline | The idea and the order. In the outline file. | Nothing |
| **Normalized narration** | What the instructor or the speech engine reads. It is the narrative of record. | This guide and the claims rules. **Not** the slide toolkit's rules. Length is free. |
| Slide-shape version | A derived text that triggers the slide toolkit's patterns, for the slides that have one. | `docs/shared/slide-narrative-guidance.md`: one shape per slide, short beats (about 150 characters), a title phrase. Short, staccato lines are fine here. |

Write the normalized narration first. Derive the slide-shape version from it afterwards. Never let the toolkit's rules flatten the spoken voice.

## 3. A training opening has five parts

1. **The viewer's stakes.** Their real question, in two sentences, with a contrast.
2. **The objective, in the learning objective's own words.** "By the end, you'll be able to…" This is the training move that a feature highlight does not make.
3. **The method and what is covered,** in one connected sentence.
4. **Level and scope.** What you assume they know, and a promise to be plain about the limits.
5. **A viewing task.** Two things to watch. This replaces any game.

Video 1's opener, in that order:

> You've spent years on your Prometheus setup, so the real question about Elastic isn't whether it's capable. It's whether you'd have to rebuild what you've already built. [stakes]
>
> So here's what this video is for. By the end, you'll be able to recognize which of your everyday prom-Q-L expressions run in Elastic using the same expression. [objective]
>
> To get there, we'll take three expressions you probably use every day and run each one twice, first in Prometheus, then in Elastic, against the same data. [method]
>
> I'll assume you're comfortable with prom-Q-L, so we'll spend our time on what's new. And at the end, we'll be plain about what doesn't carry over. [level and scope]
>
> Now, don't take my word for the result. As each pair runs, watch two things: whether the expression changes, and whether the numbers agree. [viewing task]

## 4. Sentence rules

| Do | Instead of |
|---|---|
| Contractions, "you" and "we" | "One can…", "the user…" |
| Connectors: "So", "Now", "To get there", "Between them" | Strings of short fragments and bare lists |
| Introduce each step with its purpose, run it, then say what appeared | Narrating clicks |
| Cue each execution with "Let's run it." | "Run it." alone, or no cue (a cue anchors the click when recording) |
| Confirm what was shown: "So, did the expression change? No." | Leaving the viewer to infer it |
| Define only what is new | Defining what an SRE who writes PromQL daily already knows |
| One idea per sentence, about 30 words at most | Long chained sentences that break in speech |
| An occasional dry aside about the work ("prom-Q-L you could write in your sleep"), at most one a minute | Jokes at the viewer's expense, or a joke on every beat |
| A deliberate pause for a question to the viewer ("Take a second."), used sparingly. Separate blocks for the question and the answer; the silence is added in the edit. | Rhetorical-question chains |

## 5. Claims, in spoken form

- **Every absolute word is a claim.** "All", "never", "always", "only", "exactly", "every", "just works", "that's all it did", "the whole thing" each need a recorded result or a docs link. Replace them with "most", "everyday", or a scope ("here", "in these three runs").
- **Echo the source's own framing.** Elastic's documentation says most, though not all, of PromQL is supported; so does the narration.
- **No statement about the feature's status** unless it is confirmed from the docs, and no claims about alerting, detection or "real time".
- **Numbers are spoken, never captioned, and come only from the take.** State each pair's numbers together, with the gap in seconds between the two runs. No bare percentages: when the difference is tiny, say how many digits agree. If a number disagrees with a sentence, rewrite the sentence.
- **Every claim traces to a docs link or a recorded result,** in the narrative's claims table, with a status and a retrieval date.

## 6. For the speech engine

- **Spellings:** `prom-Q-L`, `E-S-Q-L`, `S-L-Os`; metric names as words ("traces span metrics calls total"); symbols as words ("equals", "square brackets"); `frontend proxy` for the service name with the hyphen.
- **One block per on-screen action.** The italic line above a block says what is on screen.
- **Placeholders** are `{{LIKE_THIS}}`, filled after the take from a values file; they never appear in the final audio.
- **Listen before you generate:** read it aloud or hear a rendering; the listening test settles spellings and drag.

## 7. Before and after, from Video 1

| Before (v1) | After (v2, approved) |
|---|---|
| "Let's find out, with a little game. … Your job is simple. Watch the expression, and try to catch it changing." | "Now, don't take my word for the result. As each pair runs, watch two things: whether the expression changes, and whether the numbers agree." |
| "First move: choose which series you're looking at." | "Let's start with the first expression: choosing which series we're looking at." |
| "So, did you catch the expression changing? No. Only the wrapper is new." | "So, did the expression change? No. What's new is the wrapper." |
| "… and the values are within {{PCT_C}} percent of each other." | "… and the values agree to {{DIGITS_C}} digits." |
| "Run it." | "Let's run it." |
| An early staccato draft: "Three expressions, run twice: first in Prometheus, then in Elastic, against the same data. … Select series with a label matcher. Take the rate of a counter. Aggregate with sum by." | "To get there, we'll take three expressions you probably use every day and run each one twice, first in Prometheus, then in Elastic, against the same data. Between them, we'll select series with a label matcher, take the rate of a counter, and aggregate with sum by." |

## 8. Words to retire

"game", "try to catch", "let's find out right now", "dive in", "let's go", "amazing", "seamless", "powerful" (as praise), "simply", "just" (as a minimizer), "easy", "basically", "obviously", "in a nutshell", "magic", and "move" for a step.

## 9. A valid narration: the checklist

1. The objective appears in the first minute, in the learning objective's own words.
2. The opening gives the viewer's stakes and a viewing task.
3. No term the audience knows is defined; every new term is.
4. Sentences are connected, with contractions and direct address, and there are no lists of fragments in the spoken version.
5. Every execution has a "Let's run it" cue, and every pair states what appeared, with the numbers and the gap in seconds.
6. No absolute word without a recorded result; scopes are stated.
7. None of the retired words.
8. No statement of the feature's status, and nothing about alerting or "real time".
9. Every number is a placeholder with a defined source and form; there are no bare percentages.
10. The recap closes the loop on the objective and states the limit plainly.
11. The video stands alone; any pointer to another video is a courtesy that can be cut.
12. Every claim is in the claims table with a status and a source.
13. The speech-engine spellings are applied, and the blocks line up with the screen actions.
14. The slide-shape versions are derived and pass the toolkit's rules.
15. The author has read or heard it and approved it.

## 10. Ready for review

When the narration is valid, produce the **review script**: a plain-text voice-over script, organized by slide, to paste into a document next to the slides.

- **Contents:** the title slide's narration (the pattern: "Welcome to *course*. In this lesson, you will see *what*, and *check or learn what*." It teases; it does not repeat the opener's objective word for word), then one section per slide in order (typically Opening, a single Demo slide that carries all the demo voice-over with short bracketed labels, and Recap), with the placeholders still in `{{double braces}}` and a one-line note saying so.
- **How:** `make_review_script.py` builds it from the narrative and a small config, copying every block character for character. It regenerated Video 1's review script byte for byte.
- **What stays out of it:** claims tables, run-sheets and timings. A reviewer reads the words.

## 11. Open

- The spoken form of numbers (a proposal: counts whole, rates to three decimals, seconds whole).
- Whether to say "lesson" or "video" consistently (Video 1's title narration says "lesson"; its opener says "video" once).
- Whether the speech engine needs the hyphenated spellings (the listening test answers it).
- How the slide toolkit times its reveals against audio read from the normalized version.
