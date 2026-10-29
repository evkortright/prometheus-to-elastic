# Working agreements

> Copied verbatim from docs/archive/handoff-module1-living.md, sections 1, 2, 3, 9 and 15, on Oct 29, 2026, for path map v2 step 1. Numbers and wording are unchanged. The source is archived in step 3, with a one-line header only.

## 1. The author and the audience

- **The author** is a training developer and **not a PromQL specialist**. They own the content and the curriculum document (the original root chat no longer does). They can change anything that is in the learner's interest.
- They are **not in a rush**. They prefer understanding over speed and would rather start clean than explain data nobody can see again.
- They want **everything explained, nothing left to the imagination**, with every claim backed by a link or a test result. They ask many questions. Keep a running glossary (section 10).
- They lean toward **honesty over marketing**, including limitations, while still wanting Prometheus users to move to Elastic for good reasons. It is a technical video for a technical audience.
- **The viewer** is an SRE who uses PromQL and Grafana every day. Their question is "what do I have to change?" Answer it plainly and early.


## 2. How we work (the working agreements)

1. **Tiny steps, one at a time.** The author runs and tests; the assistant waits for the pasted output. Often only the first step of a series matters because it changes the next one, so give one step at a time.
2. **Expected output before every step.** Say what the output should look like, check the pasted output line by line against it, and say plainly when something is **inferred**, not verified.
3. **One question per message at most.**
4. **No status lists by default (the author's choice, Oct 28).** Replies do not end with a "Where we are" tracker or a "parked" list. Show a short status only when something changed materially, or when the author asks. The tracker in section 6 is the record.
5. **Every file delivery comes with apply, check, commit and push steps** (section 3), and the bracketed safety grep.
6. **Never ask for or print the API key.** It lives only in `.env.elastic` (gitignored). No `--force`, anywhere. Quote glob patterns (the laptop shell is zsh).
7. **Irreversible actions:** read first (for example `GET` before `DELETE`), use the exact name with no wildcards, and ask before running.
8. **Don't assume times.** The author checks uptime and clocks themselves. Use `date -u` for UTC; the author thinks in Central time.
9. **Re-read files before relying on them.** In a long chat, older tool output is dropped from the assistant's view. The assistant's sandbox copy of the repo can drift from the author's: ask for a fresh archive when starting a new chat.
10. **Verification.** Claims trace to Elastic or Prometheus docs (link them) or to a recorded test. Third-party sources are flagged as such. Search results can be docs preview builds (`docs-v3-preview.elastic.dev`), which are not canonical.
11. **Plain language.** Define a term the first time. A term the author hasn't met goes in the glossary with a source.
12. **The assistant's sandbox has no network for shell commands in this setup.** Use web search and web fetch (fetch works only for URLs that already appeared in results).
13. **Repo ownership (Oct 22).** The root chat (this one) is the only source of changes to shared files; video chats (planned) own only their own video's files. The assistant cannot run git, and a zip made with `git archive` has no `.git`, so the sync check is `git fetch` and `git status -sb` on the laptop (section 3, step 1).
14. **Authority (Oct 26).** A video chat is the source of truth for its video's files and state, while it is the active chat (agreement 15). It verifies the author's pasted output for its own deliveries (base hash, expected stat, commit) and keeps a video log (`docs/module1-videoN-log.md`). The root reviews only if the author asks, and otherwise handles the shared files, decisions that cross videos, the one-time setup, the voice guide and the final arc review.
15. **One active writer at a time (Oct 28).** The author names the active chat. Only the active chat produces deliveries that change the repo. Every other chat is advisory: it reads, answers and reviews, and writes notes, but does not deliver files. A note about another chat's files goes into that chat's log when it becomes active, and nobody edits another chat's files, even at the author's request. Switching chats is a baton pass: the active chat's last delivery is committed and pushed, the tree is clean, and the next chat starts from a fresh archive. The root is a chat like the others and is active only when the author says so. The author stays in the middle: they apply, check and commit every delivery and make every decision. A script may check or stage, and it never commits or decides.


## 3. The repo-update routine

Laptop (macOS), repo at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`.

| Step | Command | Expect |
|---|---|---|
| 1. Apply | `cd /Users/enriquekortright/personal/projects/prometheus-to-elastic`, then `git fetch`, then `unzip -o ~/Downloads/<name>.zip`, then `git status -sb` | First line `## main...origin/main` (clean and in sync), then ` M <file>` for an edited file or `?? <file>` for a new one. Anything else means the repo and the assistant's copy have drifted: stop and ask for a fresh archive |
| 2. Check | `git diff --stat`. For a **new** file: `git add <file> && git diff --cached --stat` | The exact insertions and deletions the assistant stated in advance |
| 2b. Safety grep | `grep -rn "OFQtLV9[K]" . --include="*.yaml" --include="*.md" --include="*.sh" \| grep -v opentelemetry-demo` | Nothing at all |
| 3. Commit and push | Edited files: `git commit -am "<message>" && git push`. New files (already added): `git commit -m "<message>" && git push` | A commit line with the same stat, then `main -> main` |

- The safety grep pattern is the first characters of the old, deleted key. The brackets stop this file from matching its own text.
- **The assistant computes the expected stat in advance** by copying the "before" file into a scratch git repo in `/tmp`, copying the "after" file over it, and running `git diff --stat`. State it before asking the author to run the check.
- **Delivery format:** a zip of the changed files with repo-relative paths, presented as a file. Browsers drop files that start with a dot, so deliver those as commands.
- The author asked for commit and push to be **one combined step** once the check matches.
- On the desktop, pull with `git pull --ff-only`.
- **Deliveries from a video chat:** run `unzip -l <zip>` first. It should list only that video's own files (`docs/module1-videoN-...`, never the contract, the handoff, the register, the lab or the map). If it lists anything else, do not unzip: paste the listing to the root chat. Then use the base hash and the stat the video chat states. The video chat that made the delivery checks the author's pasted output (base hash, stat, commit); the root reviews a delivery only if the author asks.


## 9. Claims discipline

- Every spoken or written claim traces to a row in the claims register (status doc, section 4) or, until the root copies it over at a milestone, to an entry in the video's log. Statuses: **Verified** (seen here), **Docs**, **Observed**, **Open**, **Retired**, plus **Decision**. Say "inferred" in conversation when something is.
- In narration: numbers come only from the take log, next to what they are compared with; agreement statements carry the gap in seconds between the two runs; no bare percentages; placeholders `{{LIKE_THIS}}` stay until the numbers are real.
- If a number disagrees with a sentence, rewrite the sentence; don't bend the number.
- Docs change often. Re-read the limitations page before each recording and record the retrieval date: `https://www.elastic.co/docs/reference/query-languages/promql/promql-limitations`. Its key sentence: the majority of PromQL expressions run unchanged.


## 15. Starter prompts (by role)

**Which chat is which.** The root chat owns this file and every shared file. Each video chat owns its own video. Attach a fresh archive to every new chat (the command is at the end of this section). The prompts below assume the archive is attached.

### 15.1 A replacement root chat

> I'm continuing as the root chat of a Prometheus-to-Elastic training track (Module 1). I've attached a fresh zip of the repo. The root chat owns the shared files: the living handoff, the claims register, the glossary, the query lab, the environment notes, the learning objectives, the video contract template and the three video contracts. Per-video chats own their own video's files. Please read `docs/handoff-module1-living.md` first, then the files it lists, then `docs/shared/video-contract-template.md` and the three contracts. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything and keep the glossary. The previous root chat is still open, so I can bring you its answers to questions you have.

### 15.2 A video chat

Each video's prompt is in section 11 of its contract: `docs/module1/video1/module1-video1-contract.md`, `docs/module1/video2/module1-video2-contract.md` and `docs/module1/video3/module1-video3-contract.md`. Copy it as is. It tells the chat to read the contract, then the files the contract lists, then the shared files (working agreements sections 1, 2, 3 and 9; glossary section 10; lessons and traps sections 11 and 12) (read-only); to follow the working agreements; to ask the author first what to do with any seed material; to act as the source of truth for its video's files and state (verifying the author's pasted output for its own deliveries and keeping a video log); and to send requests to the root chat only when its contract says to. A chat is advisory unless the author names it the active chat (section 2, agreement 15).

- **What can start now, with no stack:** Video 1, checklist rows 2, 4, 5 and 6; Video 2, rows 3 to 6; Video 3, rows 2 to 6 (each contract's section 8). Rehearsals and takes wait for the one-time setup and a reset (tracker rows 12 and 26).
- **Starting Video 2:** paste the contract's prompt (section 11), then the starter brief (`docs/module1/video2/module1-video2-starter-brief.md`), and attach a fresh archive. The archive now carries the voice guide and the scripts, so no separate pack is needed.
- **Requests for the root:** rare. A video chat sends one only when a shared file truly needs a change, when a decision crosses videos, or at a milestone. The author pastes it into the root chat at most once per session, and the root turns it into a delivery (a register row, a glossary term, a lab result, a handoff update).

### 15.3 A fresh archive

From the repo root, after the last commit is pushed: `git archive --format=zip -o ~/Downloads/prometheus-to-elastic-repo.zip HEAD`. It holds tracked files only, so no demo folder and no secrets, and it has no `.git` folder (section 12), so a new chat checks sync with `git fetch` and `git status -sb`, not from the archive.
