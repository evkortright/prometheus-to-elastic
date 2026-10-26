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

- **Learning objective (word for word from `docs/module-learning-objectives.md`, with its level):** `<text>`
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
- **Stack state required:** a freshly reset stack (reset runbook, handoff tracker row 26); warm-up of at least `<minutes>`; `paymentFailure` `<on/off>`; pre-roll checks passed.
- **Take log fields:** `<fields>`

| Placeholder | Meaning | Source |
|---|---|---|
| `{{LIKE_THIS}}` | `<meaning>` | `<take log>` |

## 7. Narration rules

- **Voice:** Qwen3 TTS with the author's voice. Editing the text and regenerating the audio is the revision method.
- **Spellings:** `prom-Q-L`, `E-S-Q-L`, `S-L-Os`, metric names as words, unless the listening test says otherwise.
- **Numbers:** spoken, never captioned. Each result keeps a 4-second hold on screen.
- **Slide narrations:** derived from the narrative file, with an explicit shape for the slide generator. The slide guidance does not limit the narrative.
- **Voice-over style guide:** `<file, when it exists>`

## 8. Deliverables and acceptance checklist

| # | Deliverable | Owner | State |
|---|---|---|---|
| 1 | `<item>` | `<owner>` | `<state>` |

## 9. Package for the second editor

- The exported first-pass video.
- The slide files.

This follows what worked on an earlier project: the second editor took the author's DaVinci Resolve export plus the slides, animated the slides, and used the demo and audio straight from the video, and asked for no transcripts. Everything else (take log, narrative, run-sheet, audio files, claims appendix) stays in the repo. **This section changes only if something changes on the author's side.**

## 10. Ownership and change rules

- **The video chat owns only this video's files:** `<list>`.
- **Shared files belong to the root:** the living handoff, the claims register (status doc), the glossary, the query lab, the environment notes, the voice guide, the learning objectives. A video chat reads them and never edits them.
- **Requests for shared files:** every turn ends with a short list of the changes the video chat needs in shared files (a register row, a glossary term, a lab result). The author passes the list to the root.
- **Changes after submission:** if the second editor or a reviewer finds a wrong claim, number or mispronunciation, the fix goes through the video chat (text and claims) and the author (re-export). The root then updates the shared files.
- **Repo routine:** the same as handoff section 3. The author applies, checks, commits and pushes; the video chat states the expected result first and checks the pasted output.

## 11. Video chat routine

1. At the start: read the contract, then the files it lists, then handoff sections 1, 2, 3, 9 and 10. Report (a) the current state, (b) what is needed, and (c) the one next step.
2. Follow the working agreements in handoff section 2: tiny steps, expected output before each step, one question at a time, and never ask for or paste secrets.
3. At the end of every turn: a short "where we are" list, then "requests for the root" (or "none").

## 12. Starter prompt for a video chat

```
I'm the author of a Prometheus-to-Elastic training track, and this chat produces one video of Module 1. Please read docs/<this video's contract file> first, then the files it lists, then sections 1, 2, 3, 9 and 10 of docs/handoff-module1-living.md (read-only). Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Don't edit shared files; end each turn with your requests for the root chat.
```
