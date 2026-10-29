# Video contract template (Module 1)

**Status:** Draft v1, October 25, 2026. Owned by the root chat.
**How this is used:** the root copies this file once per video (`docs/module1-videoN-contract.md`) and fills it in. A video chat starts from its contract. The contract is the video's whole job description, from the learning objective to the package that goes to the second editor.
**If this template and a video's contract disagree,** the contract wins for that video, and the root fixes the template.

---

## 0. Header

| Field | Value |
|---|---|
| Video | `<number and working title>` |
| Contract version and date | `<v1, date>` |
| Contract status | `<Draft / Active / Fulfilled>` |
| Chat | `<video chat, started on date>` |
| Root handoff | `docs/handoff-module1-living.md` (read-only for the video chat) |

## 1. The finish line

The contract is **fulfilled** when the author, as the first video editor, has assembled the complete video from the package below and can submit it to the second editor. The first-pass video stands on its own at production quality: slides, demos and voice-over. The second editor then polishes it.

The video chat's own work is complete at conditions 1 to 4. Conditions 5 to 7 are the author's, and the root ticks them when the author says so.

| # | Condition | Owner |
|---|---|---|
| 1 | The learning objective, outline and narrative are approved, and the author has listened to the narration and approved it | Author |
| 2 | Every demo step has been run on a freshly reset stack, with the results in this video's take log | Video chat guides, author runs |
| 3 | Every claim in the narration and on the slides is verified (a docs link or a recorded test result) | Video chat |
| 4 | The run-sheet is final, and the narration audio is generated from the approved text | Video chat and author |
| 5 | The footage is captured | Author |
| 6 | The first-pass video is assembled and exported, with slides, demos and voice-over | Author |
| 7 | The package is submitted to the second editor | Author |

## 2. Identity

- **Learning objective (word for word from `docs/shared/module-learning-objectives.md`, with its level):** `<text>`
- **Module context (quoted from the same file, not paraphrased):** `<format, skills and knowledge gained>`
- **Audience:** an SRE who uses PromQL and Grafana every day. Their question is "what do I have to change?"
- **Target length:** `<about N minutes; no hard limit>`

## 3. Standalone rule

The video is strictly standalone. It restates what it needs in about 20 seconds, and any pointer to another video is a courtesy that can be cut without loss.

| What the viewer needs to know | Where it comes from | Time on screen |
|---|---|---|
| `<item>` | `<assumed (audience) / taught in beat N>` | `<seconds>` |

- **Closing line:** `<the final sentence>`. Any pointer to another video in it is a courtesy.

## 4. Story

- **Through-line:** `<one sentence>`
- **Narrative file:** `docs/module1-videoN-narrative.md`. It is the source of truth once the author approves it.

| Beat | What | Capture clips | Target on screen |
|---|---|---|---|
| `<n>` | `<what>` | `<clips, or none for a slide>` | `<seconds>` |

## 5. Claims

- **Wording rules:** say "expression", not "query", when claiming sameness; say "most" or "everyday", never "all"; every number comes from this video's take log, next to what it is compared with, with the gap in seconds between the two runs; no bare percentages.
- **Forbidden for this video:** `<list>`
- **Claims-register rows used** (status doc, section 4): `<row numbers>`

| Sentence | Confirm against | Status |
|---|---|---|
| `<sentence from the narrative>` | `<docs link, register row, or take result>` | `<Open / Verified / Docs>` |

## 6. Evidence plan

- **Lab items or probes this video runs:** `<list>`
- **Stack state required:** a freshly reset stack (`docs/shared/operations/reset-runbook.md`, Part B); warm-up of at least `<minutes>`; `paymentFailure` `<on/off>`; pre-roll checks passed.
- **Take log fields:** `<fields>`

| Placeholder | Meaning | Source |
|---|---|---|
| `{{LIKE_THIS}}` | `<meaning>` | `<take log>` |

## 7. Narration rules

- **Voice:** Qwen3 TTS with the author's voice. Editing the text and regenerating the audio is the revision method.
- **Spellings:** `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, unless the listening test says otherwise.
- **Numbers:** spoken, never captioned. Each result keeps a 4-second hold on screen.
- **Slide narrations:** derived from the narrative file, with an explicit shape for the slide generator. The slide guidance binds only the slide-shape version, not the narrative.
- **Voice-over style guide:** `docs/shared/narration-voice-guide.md`. On voice it wins; on factual rules the contract wins. Each narration has three versions: the informal outline, the normalized narration (the narrative of record), and the slide-shape version (derived).
- **Review script (before recording):** once the narration is valid, the author may submit a plain-text review script, organized by slide, to reviewers. Build it with `scripts/make_review_script.py` (voice guide, section 10). The package for the second editor does not change.

## 8. Deliverables and acceptance checklist

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | `<item>` | `<owner>` | `<state>` |

## 9. Package for the second editor

- The exported first-pass video.
- The slide files: the slide generator produces a `.pptx`; the author uploads it to Google Drive, opens it as Google Slides, and gives the second editor the link.

This follows what worked on an earlier project: the second editor took the author's DaVinci Resolve export plus the slides, animated the slides, and used the demo and audio straight from the video, and asked for no transcripts. Everything else (take log, narrative, run-sheet, audio files, claims appendix) stays in the repo. **This section changes only if something changes on the author's side.**

## 10. Ownership and change rules

- **The video chat owns only this video's files:** `<list>`, and its video log.
- **Authority and the video log (Oct 26):** the video chat is the source of truth for its video's files and for the video's state. It verifies the author's pasted output for its own deliveries (the base hash, the expected stat, the commit result) and does not route them through the root. It keeps `docs/module1-videoN-log.md`, which it creates with its first entry: the checklist state, claim confirmations with their retrieval dates, probe results, the take log, and the decisions the author makes with that chat (for example the slide shapes). Once the log exists, it is the truth about the video's state, ahead of the contract's checklist. The root reviews a delivery only if the author asks. This applies while the chat is the active chat: only one chat at a time delivers changes to the repo (handoff, section 2, agreement 15), and a chat the author has not named active is advisory.
- **Seed material:** the root may hand a video chat work it built before the chat existed (a draft narrative, a claims table). It is a proposal, not a decision. The contract lists it, the video chat asks the author at the start whether to use it, rewrite it or ignore it, and from then on the file belongs to the video chat. Approved material is not a seed: the chat changes it only to fix a claim, or with the author's approval.
- **Shared files belong to the root:** the living handoff, the claims register (status doc), the glossary, the query lab, the environment notes, the voice guide, the learning objectives. A video chat reads them and never edits them.
- **Requests for the root:** most turns say nothing about the root. A video chat sends a request only when a shared file truly needs a change (a register row, a glossary term, a lab result), when a decision crosses videos, or at a milestone (a checklist row changes state). It records confirmations and results in its video log first. The author passes a request to the root at most once per session.
- **Changes after submission:** if the second editor or a reviewer finds a wrong claim, number or mispronunciation, the fix goes through the video chat (text and claims) and the author (re-export). The root then updates the shared files.
- **Repo routine:** the same as handoff section 3. The author applies, checks, commits and pushes; the video chat states the expected result first and checks the pasted output.

## 11. Video chat routine

1. At the start: read the contract, then the files it lists, then handoff sections 1, 2, 3, 9, 10, 11 and 12 (sections 11 and 12 hold the narrative lessons and the traps, until a voice guide exists). If the contract lists seed material, ask the author whether to use it, rewrite it or ignore it. Report (a) the current state, (b) what is needed, and (c) the one next step.
2. Follow the working agreements in handoff section 2: tiny steps, expected output before each step, one question at a time, and never ask for or paste secrets.
3. Do not end turns with status lists unless something changed materially or the author asks. Add a request for the root only when section 10 says to; otherwise say nothing about the root.

## 12. Starter prompt for a video chat

```
I'm the author of a Prometheus-to-Elastic training track, and this chat produces one video of Module 1. Please read docs/<this video's contract file> first, then the files it lists, then sections 1, 2, 3, 9, 10, 11 and 12 of docs/handoff-module1-living.md (read-only). Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Don't edit shared files. You are the source of truth for this video's files and state: verify my pasted output for your own deliveries, keep a video log, and send requests to the root chat only when the contract says to (a shared file that truly needs a change, a decision that crosses videos, or a milestone). You are the active chat only when I say so; until then you are advisory: answer and review, but do not deliver files. Do not end replies with status lists unless something changed materially or I ask. If the contract lists seed material, ask me first whether to use it, rewrite it, or ignore it.
```
