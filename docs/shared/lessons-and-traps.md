# Lessons and traps

> Copied verbatim from docs/archive/handoff-module1-living.md, sections 11 and 12, on Oct 29, 2026, for path map v2 step 1. Numbers and wording are unchanged. The source is archived in step 3, with a one-line header only.

## 11. What we learned about the narrative

These came from reading Video 1's first draft as a viewer and iterating on it. The author's reaction: it "feels right and at the level we want", pending the speech-engine test.

1. **Put the motivation on the surface.** Say why a thing is wanted before showing it ("on its own, a counter just climbs; what you usually want is how fast"). The author likes that conclusions follow from stated reasons.
2. **One idea per beat.** The `SORT` detour was cut because it added a second idea to a rung.
3. **Order must match the demo.** The first opener listed `sum by` second while the demo ran `rate()` second. Check the agenda against the screen order.
4. **A question, then the reveal.** Frame the one big idea so it sticks: the wrapper answers three questions (where should this run, when, and what do we call the answer).
5. **Don't spoil the result.** "Judge the match yourself" earns more trust from a skeptical engineer than announcing the outcome. If the outcome is stated, confirm it against the footage.
6. **Don't leave a loose thread.** State a fact plainly rather than hinting that a later video explains it. A pointer is fine; a cliffhanger is not.
7. **Point to the next video, not the one after.** The recap says what Video 2 builds, then mentions the edges.
8. **"Rung" is a working label, not a spoken word.** The approved narrative never says "rung" aloud; its section headings and the outline use the word. Do not introduce the ladder in narration (the earlier plan of one "we'll climb a short ladder" sentence was dropped). Video 2's seed narration says "ideas".
9. **Slide narration and voice-over are different jobs.** Slide narrations follow `slide-narrative-guidance.md` (hook first, planted title phrase, counted items, no stage directions, about 90 to 180 words). Voice-over blocks over the demo contain only spoken words.
10. **Speech-engine spellings:** `prom-Q-L`, `E-S-Q-L`, metric names as words, symbols as words. The slide translator turned `prom-Q-L` back into `PromQL` correctly.
11. **Tone:** plain, direct, "we" and "you", technically energized, little drama.
12. **Rhythm of a rung:** motivate, show it in Prometheus, show it in Elastic inside the same wrapper, state the values side by side with the gap between runs. Repeating the same moves every rung is a strength.
13. **Record first, then narrate;** every number is a placeholder until the take log is filled.
14. **A style guide and a skill (planned):** first a short guide in the repo, written after the listening test; later a skill via the skill-creator workflow, after Video 2's script. Warn the skill against making every video sound templated. The slide guidance file stays authoritative for slide narrations.
15. **Read it end to end, as a viewer.** Assemble all the spoken blocks in order (the story document) and read them as one piece. This found a contradiction that block-by-block review missed: Clip B2 said the labels sit in a column "but the wrapper is everything that's new," and the label column is also new.
16. **Check each sentence against the one before it,** and the words against the picture. A full-screen recording hides the tab strip, so "two tabs" became "two screens."
17. **The aspiration** (the author's): the level of a great lecturer, patient and building intuition, with motivations and "whys" stated, honest about edges, technically energized, little drama. The author's reaction to iteration 1: it "feels right"; they like the motivations on the surface and conclusions that follow from explicit statements. They believe engineers enjoy playing with concepts they already know.
18. **The iteration loop:** the author listens through the speech engine and notes timestamps (where it drags, mispronunciations, pauses); the assistant revises the run-sheet blocks; the story document is regenerated.
19. **Why the first draft felt choppy (the author's reaction, Oct 22; the diagnosis was agreed):** every sentence short and declarative, so the rhythm never changed; the same three items announced in the opener, the ladder sentence and the recap; no tension, because the opener gave the answer away; lab-report phrasing in speech (differences in percent, seconds between runs); rungs bolted together instead of caused by each other.
20. **What fixed it:** a spine (the "find the seam" game), long building sentences followed by short landing ones, each rung created by a problem the previous one left (series, then a counter that only climbs, then one number that does not say which service), and a reveal that answers the opening question.
21. **Open with the viewer's fear:** the investment, and the question "would I have to rebuild all of it?" The author's earlier module introduction was the model; its absolutes were not carried over.
22. **Say "we" and "you";** avoid "I want to show you". The viewer is the investigator, not the audience of a pitch.
23. **Strictly standalone means restating, not referring.** Each video spends about 20 seconds on what it needs, and any pointer to another video can be cut without loss. The production rule follows: nothing carries over between videos, so every number comes from that video's own take.
24. **Absolute words in a narration are claims.** "Only", "all", "never" and "always" each need checking against the reference page. The Oct 25 docs check found that "the wrapper only answers three questions" overclaimed, because the command has more options than the three we set. A second example (Oct 26): the narrative's reveal said "now you know all of it", an absolute for the same reason. The Video 1 chat caught it, and the author approved "here it makes just three choices".
25. **A video's spoken text lives in two places:** the demo clips (the narrative and the run-sheet are identical) and the slide narrations (written in the run-sheet under the slide guidance's rules, 90 to 180 words each, derived from the narrative). They can differ from the narrative's opening and reveal blocks, so the arc review reads the spoken text (the story document), and a video chat keeps the two in sync or says which one wins.
26. **Paired comparisons need both runs inside one scrape minute.** Prometheus scrapes once a minute (phase about :37 in the first run), and Elastic receives each sample some time later. Two runs agreed to better than 1e-9 when both fell inside one scrape minute (the Prometheus click after about :40, the Elastic click before about :35 of the next minute). The explanation is a hypothesis (register row 59). Plan this per pair; Video 2 has more pairs.
27. **The trainer voice and the three versions** (`docs/shared/narration-voice-guide.md`): objective first, connected sentences, claims stated precisely, a viewing task instead of a game. Write the normalized narration first and derive the slide-shape version after.
28. **Observe, then write.** The Video 1 chat's own mistakes, kept as lessons: UI labels written before the screen was seen ("Run" was "Execute" and "Search"), numbers asserted without measuring, counters predicted instead of relationships tested (`failed` 0, `sent` growing), and stale text left in approved files. Test relations, not estimates.
29. **Concurrent chats collide.** The Video 2 chat modified Video 1's `scripts/fill_placeholders.py` at the author's request, and the Video 1 chat was not told. The helper has a digit-counting issue that Video 1's narration depends on. A chat's files change only through that chat while it is the active chat (agreement 15).

**How the story document is built.** A short script reads the run-sheet and pulls each spoken block with this pattern, then places it in viewing order (opener, Clips A, B1, B2, C1, C2, D1, D2, recap) with an italic note on what is on screen, followed by reviewer questions, a claims table and the open items:
````
\*\*(?:Voice-over|Narration): ([^*]+)\*\* \((\d+) words\)\n\n<details><summary>Show [a-z-]+</summary>\n\n```\n(.*?)\n```
````
After building, check that every quoted line appears verbatim in the run-sheet.


## 12. Traps we hit

- **Misread output:** treating a git-history search as proof of a negative. Check pasted output line by line.
- **A stale paste:** the R8 Prometheus result was actually the R7 table. When values look off, check the shape (a ratio is between 0 and 1).
- **Table pipes:** `ES|QL` inside a Markdown table cell splits the column. Write `ES\|QL` or keep it out of tables.
- **`apply-config.sh` permission bug** (section 5). Don't re-run it.
- **`down --volumes` removes containers and their logs;** save evidence first.
- **The picker width matters for long windows** (R4); keep the picker on Last 1 hour for the lab.
- **The first R7 row requested was `frontend`, but `frontend-proxy` was reported;** state exactly which row you need.
- **Prometheus's Table order is not alphabetical,** and Elastic's row order differs; point at a named row.
- **New files need `git add`;** `git commit -am` only covers files git already tracks.
- **Mixed time zones:** logs are UTC; the author thinks in Central.
- **"The key is safe because its project was deleted"** is true of the old key in git history only. The current key belongs to the live project.
- **A silent power-button restart and a crash look the same** in the event log (event 41); don't over-read it.
- **A sentence that contradicts the one before it** (Clip B2). Read the whole script in one pass, not block by block.
- **Words that disagree with the picture** (tabs versus full screen).
- **The run-sheet still describes the desktop, the Game Bar and WSL commands.** Update it after the laptop setup and the capture test.
- **Don't over-read Windows event 41.** A forced power-off and a crash look the same.
- **A zip made with `git archive` has no `.git`,** so the assistant cannot check commits or sync from it. Use `git fetch` and `git status -sb` on the laptop.
- **Count words with a script,** not by eye: the narrative draft was guessed at "roughly 700" words and counted 670.
- **All videos write to one data stream name** (`metrics-generic.prometheus-default`), so two stacks running at once would mix their data. Only one stack runs at a time.
- **The assistant's sandbox runs on UTC,** so a file timestamp can show a day ahead of the author's local date (the evening of Oct 25 local was Oct 26 UTC).
- **Fetched docs pages strip the "applies to" badges,** so a feature's status (preview or generally available) must be read from the author's browser, not from a fetch.
- **The root can drift into a video chat's work.** Before building a deliverable, check who owns it in the contract. The Video 2 narrative was written by the root first and had to be relabelled as a seed.
- **Not every Elasticsearch API exists on Serverless.** The field-mapping API returned `410 api_not_available_exception`. Try a new command on Serverless before it goes into the runbook (retro entry 88). The `_mapping?filter_path=...` form works (entry 89).
