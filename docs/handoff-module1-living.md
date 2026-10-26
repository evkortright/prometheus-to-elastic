# Handoff — Module 1 (living file)

**Repo:** `github.com/evkortright/prometheus-to-elastic` (private)
**Started:** October 22, 2026. **Last updated:** see the update log at the end (section 14).
**Supersedes:** `handoff-2026-10-20-module1-continuation.md`. Keep that file as history only; section 13 lists what in it is now out of date.
**This file is updated, not rewritten.** Add to it at every milestone (section 14 says how). If it disagrees with an older document, this file wins, unless the claims register says otherwise.

**Who changes the repo:** this chat is the **root chat** (it took ownership on Oct 22; the root role was agreed on Oct 25). It owns every shared file and is the only source of changes to them; the author is the oversight. The author applies, checks, commits and pushes (section 3); the assistant states the expected result first and checks the pasted output. Planned per-video chats own only their own video's files and send the root a list of requests for shared files (section 7, Oct 25). The first chat is a reference for what was done before.

**Read in this order:**
1. This file.
2. `docs/module1-status-2026-10-19.md`: section 2 (state), section 3 (open items), section 4 (claims register). The file name keeps its old date; do not rename it.
3. `docs/module1-query-lab.md`: the tested expressions and recorded results.
4. `docs/module1-video1-run-sheet.md`: the screen steps and the voice-over for Video 1. It is stale: the approved narrative (4a) is now the source of truth for the narration, and the run-sheet is rewritten from it.
4a. `docs/module1-video1-narrative.md`: Video 1 as one continuous narrative, the narrative of record (draft v1, commit `8f6f186`, one phrase changed Oct 25; the author listened to it and approved it). The run-sheet and the story document are regenerated from it.
5. `docs/module1-video1-story.md`: the reading version of Video 1, generated from the run-sheet (for hearing it aloud and for peer review).
6. `docs/module1-video1-outline.md` and `docs/module1-video2-outline.md` (Video 2 is committed; the author has not yet reviewed its nine open decisions).
7. `docs/slide-narrative-guidance.md`: the author's rules for slide narrations.
8. `docs/module-learning-objectives.md`: the Module 01 section and the design notes.
9. `docs/quickstart.md` (the reset section) and the README's "Local setup" section.

---

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
4. **Every reply carries a short numbered "Where we are" tracker,** and a "parked" list when relevant. Keep the numbering stable and move items forward.
5. **Every file delivery comes with apply, check, commit and push steps** (section 3), and the bracketed safety grep.
6. **Never ask for or print the API key.** It lives only in `.env.elastic` (gitignored). No `--force`, anywhere. Quote glob patterns (the laptop shell is zsh).
7. **Irreversible actions:** read first (for example `GET` before `DELETE`), use the exact name with no wildcards, and ask before running.
8. **Don't assume times.** The author checks uptime and clocks themselves. Use `date -u` for UTC; the author thinks in Central time.
9. **Re-read files before relying on them.** In a long chat, older tool output is dropped from the assistant's view. The assistant's sandbox copy of the repo can drift from the author's: ask for a fresh archive when starting a new chat.
10. **Verification.** Claims trace to Elastic or Prometheus docs (link them) or to a recorded test. Third-party sources are flagged as such. Search results can be docs preview builds (`docs-v3-preview.elastic.dev`), which are not canonical.
11. **Plain language.** Define a term the first time. A term the author hasn't met goes in the glossary with a source.
12. **The assistant's sandbox has no network for shell commands in this setup.** Use web search and web fetch (fetch works only for URLs that already appeared in results).
13. **Repo ownership (Oct 22).** The root chat (this one) is the only source of changes to shared files; video chats (planned) own only their own video's files. The assistant cannot run git, and a zip made with `git archive` has no `.git`, so the sync check is `git fetch` and `git status -sb` on the laptop (section 3, step 1).

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

## 4. Environments

- **Laptop (MacBook Pro, macOS): the stack host and the recording machine from Oct 22.** Repo at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`. The author works with the assistant, commits and pushes here.
  - **Not yet checked:** the laptop's RAM, Docker Desktop's resources, and whether `opentelemetry-demo` and `.env.elastic` exist. The readiness check is pending (section 5). `.env.elastic` may be stale from the earlier laptop attempt.
  - The README says this stack was **validated on Apple Silicon with Docker Desktop**, with at least 12 GB of RAM and 4 CPUs allocated to Docker (about 10 GB in total). The "30 containers" figure in the older docs is stale: 25 run.
  - **macOS gotcha (README):** editing the bind-mounted Prometheus config on the host does not refresh it inside the container. Run `docker restart prometheus` after regenerating it.
  - **The permission bug may not occur on macOS,** because `apply-config.sh` was validated there (inferred). If Prometheus logs "permission denied" reading its config, `chmod 644` the generated file and restart Prometheus.
  - **Keep it awake while recording:** `caffeinate -d -i -s -t 14400` in a spare Terminal window (four hours), with the charger plugged in and the **lid open**. Per the man page, `-d` blocks display sleep, `-i` idle sleep, and `-s` system sleep (AC power only). A closed lid is a separate sleep path that caffeinate does not override. Check with `pmset -g assertions`.
  - **Recording:** macOS's built-in screen recording (I believe `Cmd + Shift + 5`; unverified) or OBS; the author edits in DaVinci Resolve. A full-screen browser hides the tab strip and the address bar (the address would be `localhost` anyway). On one machine the run-sheet cannot sit beside the recording, so use a phone, a tablet, a printout, or the desktop's screen.
- **Desktop (Windows with WSL Ubuntu, `DESKTOP-JET863K`): considered unreliable since Oct 22. Do not use it for the stack or for recording.**
  - It ran the stack until the morning of Oct 22. Its repo clone is at `~/personal/projects/prometheus-to-elastic`, with the demo in `opentelemetry-demo`. The previous run's evidence is in `~/evidence-2026-10-21/`.
  - Its time zone was set to Central on Oct 22 (zone only; the clocks agreed with the laptop). Sleep on AC was verified as never.
  - The incident (restarts, Malwarebytes findings, glitching screen) is in section 5. The author is investigating it in a **separate chat**.
  - **Resolved (Oct 22, author):** the old project is deleted and the desktop is not sending data any more.
- **Elastic (Oct 22, after the incident): a new Serverless project and a new write-only key are to be created.** The old project (`prometheus-to-elastic`, Azure Central US) was **deleted by the author**, so the old key no longer matters. **Project name, region and endpoint: record them here when the project exists** (never the key). Project type: Observability Complete (README). Data stream **`metrics-generic.prometheus-default`**, in time series mode, from the template `metrics-prometheus@template`; the name and the automatic re-creation were verified on the old project, and the same is expected on the new one (confirm). The new key has the same privileges (`auto_configure`, `create_doc` on `metrics-*`) and lives only in `.env.elastic`. A write-only key cannot delete or read the cluster root; deleting data needs Kibana Dev Tools under the author's own login.
- **Stack:** `docker compose -f compose.yaml -f compose.observability.yaml` is required (the base file lacks Prometheus and Grafana). 25 services run. Prometheus reports 18 `service_name` values. The Prometheus container runs as user `nobody` (uid 65534).
- **Narration voice:** Qwen3 TTS, with a voice the author created from a prompt and a favorite output used as the reference. Editing a line and regenerating the audio is the point (it replaces human re-recording). How it reads `prom-Q-L`, `E-S-Q-L` and `S-L-Os` is untested; the listening test will say.
- **Lowest priority, not tracked further:** a Mac Mini as an always-on server (the author's idea; the author will raise it).

## 5. Current state (update me)

**As of the second half of Oct 22, no stack is running.** The desktop is out and its project is deleted; the laptop is not set up yet. The plan is a fresh start: a new Serverless project, a new key, a new local stack, then a warm-up (length not decided).

**What the desktop run established.** The stack was fully reset using the quickstart's reset section on the desktop. **T0 = 2026-10-22 00:41:00 UTC** (7:41 PM CDT on Oct 21). The architecture ran cleanly for about 70 minutes before any trouble was logged.

| Check | Result |
|---|---|
| Prometheus data folder after the restart | Only `chunks_head`, `lock`, `queries.active`, `wal`, `wbl`: the old data is gone |
| Elastic data stream | Deleted (acknowledged), then **recreated automatically** by the first samples (generation 1) |
| Remote-write counters at +3 min | failed 0, retried 0, pending 0, in 91,328, sent 91,328 |
| At +12 min (00:52:57 UTC) | failed 0, retried 0, pending 182, gap 182 (gap equals pending) |
| At +70 min (01:50:35 UTC) | failed 0, retried 0, pending 10,390, in 10,585,694, sent 10,580,304, gap 5,390 |
| WARN or ERROR lines in the log | 0 at every check |

- The gap minus pending was exactly 5,000 at +70 min, which equals `max_samples_per_send` in the config. A batch in flight is a plausible reading (inferred, not confirmed).
- Sample rate rose with uptime: about 1,180 per second at minutes 3.5 to 12, about 2,860 per second at minutes 12 to 70. Oct 21's average was roughly 4,600 per second (approximate). Cause unknown; relevant to the stale sizing numbers.
- The first block compaction was expected around 03:00 UTC on Oct 22. **We never checked** whether the overlapping-blocks warning appeared.

**Pre-roll checks,** before any recording. They were written for Linux; run them in a macOS terminal on the laptop (BSD `sed` and `awk` should accept them; untested):
```
date -u; docker ps --format '{{.Names}}: {{.Status}}' | grep -E 'prometheus|flagd'
```
```
date -u; curl -s http://localhost:9090/metrics | sed 's/{[^}]*}//' | awk '/^prometheus_remote_storage_samples_failed_total/{f=$2} /^prometheus_remote_storage_samples_retried_total/{r=$2} /^prometheus_remote_storage_samples_pending/{p=$2} /^prometheus_remote_storage_samples_in_total/{i=$2} /^prometheus_remote_storage_samples_total/{t=$2} END{printf "failed %s | retried %s | pending %s | in %.0f | sent %.0f | gap %.0f\n", f, r, p, i, t, i-t}'; docker logs prometheus 2>&1 | grep -cE 'level=(WARN|ERROR)'
```
Also confirm the `paymentFailure` flag is off on the feature flags page.

**Desktop incident, Oct 22 morning:**
- **Symptom (author):** the screen went blank when typing in Chrome, sometimes recovered, sometimes needed a reboot. It **still glitches after the cleanup** below.
- **Windows event log (System, last 24 hours), local time, Central assumed:** no unexpected shutdowns and no sleep events overnight. At 9:37:12 AM event 41 (unexpected restart; 6008 says the previous shutdown at 9:08:16 AM was unexpected). At 9:38:51 AM `winlogon.exe` started a power off, then sleep (event 42, reason "Application API") and resume (107) one second apart. At 9:55:33 AM event 41 again (6008: previous shutdown at 9:37:16 AM). At 10:17:30 AM a restart started by `RuntimeBroker.exe` for user Enrique, then a clean shutdown (6006). No stop-error code appears in the messages. A four-second power-button hold also logs event 41, so a crash cannot be told from a forced power-off here.
- **Malwarebytes (trial) at 10:09 AM** quarantined five items within 5 seconds: `PUP.Optional.BrowserHijack`, three `PUP.Optional.SearchShield` entries (file, folder, registry value) and `PUP.Optional.PulseBrowser` (a scheduled-task folder). PUP means potentially unwanted program; by their names these look like adware or browser hijackers, not password stealers (inferred). The author deleted the detected apps. Other entries in the list may exist.
- **Cause of the glitching is unknown.** A graphics driver or Chrome hardware acceleration are plausible (inferred). The author is investigating security and the glitch in a **separate chat**.
- **State of the desktop stack:** moot. The old project is deleted and the desktop is not sending data (author, Oct 22).

**Migration plan (replaced on Oct 22): a fresh start on the laptop, in this order.** The author owns each step; the assistant gives expected output first. The earlier plan (create a new key, revoke the old key, delete the data stream) is superseded because the old project is deleted.
1. **Account checks (proposed; the author has not yet confirmed them),** listed below. They come before any new credentials: a new key does not help if the account that issues it is compromised. This is a precaution, not a diagnosis.
2. **Create the new Serverless project** (one-time; all three videos reuse it) (Observability Complete, per the README). Record its name, region and endpoint in section 4.
3. **Create the new write-only API key** (one-time) in Kibana Dev Tools with the README's "Create the Elastic credentials" call (privileges `auto_configure` and `create_doc` on `metrics-*`; give it a clear name). Copy the `encoded` value (shown once). **Never paste it in chat.**
4. **Laptop readiness check** (read-only), from the repo root:
```
sysctl -n hw.memsize | awk '{printf "%.0f GB RAM\n", $1/1024/1024/1024}'
docker info --format 'Docker has {{.MemTotal}} bytes and {{.NCPU}} CPUs'
ls -ld opentelemetry-demo .env.elastic
```
   The README wants at least 12 GB and 4 CPUs for Docker. The last line shows whether the demo folder and `.env.elastic` exist; it does not print the file.
5. **Set up the stack** per the README's "Local setup": clone the demo at the pinned version if missing, create `.env.elastic` from `config/.env.example` with the new endpoint and key (replace any stale file), run `scripts/apply-config.sh`, start with both compose files. If Prometheus logs "permission denied", `chmod 644` the generated config and `docker restart prometheus`.
6. **Warm up** with `caffeinate` running, for the time the video's contract states (Oct 25: warm-up is a per-video field, not a global rule). The lab's rule of thumb is at least 45 minutes. A longer run (for example overnight) would answer questions the desktop run left open: whether the overlapping-blocks warning appears at the first compaction, how often the organic payment errors occur, and whether the sample rate settles.
7. **Then:** the pre-roll checks, probes P1 to P8, the R1 rehearsal and the capture test.

**From the second video on (Oct 25):** the plan above is the one-time setup. Each video starts from a **reset runbook** (tracker row 26): stop the stack, delete the data stream in Kibana Dev Tools under the author's own login (the write-only key cannot), clear Prometheus's local data, start fresh, warm up, and run the pre-roll checks. Elastic recreates the data stream automatically (verified on the old project). The runbook is `docs/reset-runbook.md` (written Oct 26, not yet run): Part A repeats the one-time plan with the expected output of each step, Part B is the per-video reset, and Part C is the pre-roll.

**Account checks, from the laptop (proposed; to be confirmed by the author):** GitHub security log, SSH keys and tokens; the Elastic Cloud account's active sessions and any API keys the author did not create; passwords typed in that Chrome while the symptoms were active.

**What happened on the previous run (Oct 20 and 21), for context:**
- `samples_failed_total` was 38,122. Two log lines (HTTP 429, "rejected execution of coordinating operation", at 05:51:40 and 05:52:40 UTC on Oct 20) account for 629 of them. **The other 37,493 have no log line and remain unexplained.**
- Before the 05:51:17 UTC restart, Prometheus logged 24 "permission denied" errors reading its config (05:34:41 to 05:50:06). Cause, very likely: `scripts/apply-config.sh` runs `chmod 600` on the generated file, and the container user `nobody` cannot read a mode-600 file owned by the author. The author fixed it by hand (the file is now mode 644). **Do not re-run `apply-config.sh` until the script is fixed.** The quickstart's last paragraph tells people to re-run it and restart Prometheus, which would trigger the same failure.
- Nine "overlapping blocks" warnings appeared in Prometheus's local storage (cause not investigated).
- The old project is deleted, so these observations can no longer be investigated. They stay in the claims register as observations from the old project.

## 6. Work tracker (update me)

| # | Item | State |
|---|---|---|
| 1 | LO wording | Done (`4ae9f7f`) |
| 2 | Claims register update | Done (`f3f898a`) |
| 3 | Lab results R2, R5, R7, R8 | Done, all Same (`4a911b1`) |
| 4 | Clean restart on the desktop | Done on the desktop (T0 in section 5); to be repeated on the laptop as a fresh start with a new project |
| 5 | Video 1 outline | Done (`edf75cf`) |
| 6 | Video 1 run-sheet v4 with voice-over iteration 1 and two fixes | Done (`48717fa`); not yet heard through the speech engine; its voice-over is to be regenerated from the narrative file (row 24) once that is approved |
| 7 | Video 1 story document (reading version, generated from the run-sheet) | Done (`48717fa`); to be regenerated from the narrative file once approved |
| 8 | Video 2 outline | Committed (`1770043`). Decisions 1, 2, 4, 6, 8 and 9 approved Oct 25 and recorded in the outline (delivered with this update). Decisions 3, 5 and 7 are open, and a new decision 10 (strictly standalone) is approved |
| 9 | Listening test of the Video 1 narrative (row 24) | Done (author, Oct 25). No changes requested, so v1 stands as the narrative of record |
| 10 | Security investigation and glitch diagnosis on the desktop | In progress, separate chat (author) |
| 11 | Key rotation, revoke the old key, delete the data stream | **Superseded Oct 22:** the old project is deleted; a new project and a new key replace this (section 5, steps 2 and 3) |
| 12 | One-time setup: account checks, new project and key, laptop readiness check, first stack setup | Procedure written (`docs/reset-runbook.md`, Part A). Not yet run: the author, with the assistant |
| 13 | Capture test and R1 rehearsal on the laptop | After 12 and a warm-up |
| 14 | Opener and recap slide narrations, derived from the narrative file with an explicit shape for the slide generator | To do, after the narrative is approved |
| 15 | Real take for Video 1, then narration against the footage | After 9 and 13 |
| 16 | Housekeeping delivery: register rows for the clean start and the incident, the lab file's outdated "Feeds" header, the quickstart paragraph (corrected with the runbook), and the `apply-config.sh` fix | To do |
| 17 | Video 3 outline (from LO3, the lab's probe list and the register). It belongs to the Video 3 chat, with probes P1 to P8 and the R4 re-run in that chat's rehearsal | Video 3 chat, after the Video 3 contract (delivered, row 31) and the one-time setup |
| 18 | Video 2 and Video 3 narratives, drafted with placeholders like Video 1 | Hold lifted Oct 25. Video 2: the root's seed draft v1 is delivered (row 30); the Video 2 chat decides with the author whether to use it. Video 3: the Video 3 chat, after its outline |
| 19 | Peer-review package (the story documents, the reviewers' questions, the claims appendix) | After Video 1's take; Videos 2 and 3 when they have evidence |
| 20 | Voice-over style guide (repo file), later a skill | After the listening tests of Videos 1 and 2; until it exists, video chats read handoff sections 11 and 12 |
| 21 | Primer doc `docs/module1-promql-primer.md` | Not created; the glossary (section 10) is its seed |
| 22 | Module description | Write last |
| 23 | Mac Mini always-on server | Lowest priority; not tracked further |
| 24 | Video 1 narrative draft v1 ("find the seam"; the introduction opens Video 1; every number spoken) | Delivered (`8f6f186`). Listening test done Oct 25; v1 stands. To do: regenerate the run-sheet voice-over and the story document from it (rows 6 and 7) One phrase changed Oct 25 after the docs check (section 7) |
| 25 | Video contract template, then the contracts for Videos 1, 2 and 3; revise section 15 (starter prompts) for the root and video chats | Done: the template and the three contracts are committed (`a15a869`, `3f10600`, `cb98c81`), and section 15 was revised in this update |
| 26 | Reset runbook (stop, delete the data stream, clear Prometheus data, restart, warm up, pre-roll checks) | Written (`docs/reset-runbook.md`, Parts B and C). Untested on the laptop: its first run is the test |
| 27 | Arc review file `docs/module1-story-arc.md`: the three narratives end to end with the hand-overs marked | After the video chats have produced the three narratives and the author has approved them |
| 28 | Docs checks: the TSDS wording for Video 2 beat 2, and for Video 3 the feature's current status and the unsupported constructs | Done Oct 25 for the PROMQL command page, the TSDS pages and the limitations page (register rows 36 to 43), except the feature's current status, which needs the author's browser (row 44) |
| 29 | Video 1 narrative: fix the header line breaks | Done (delivered Oct 25) |
| 30 | Video 2 contract, and the root's narrative seed (draft v1: "build it up", four ideas, two pause-and-try questions, optional blocks for decisions 3 and 5) | Delivered (Oct 25); the Video 2 chat decides with the author whether to use the seed, rewrite it or ignore it |
| 31 | Video 3 contract (candidate beats as seed material; the Video 3 chat writes the outline and the narrative) | Delivered (Oct 25) |
| 32 | Start the video chats, each from the prompt in its contract (section 15.2) | Video 1's chat started (after `dcbb48e`); its first reply passed the checks in the decisions below. Videos 2 and 3: the author starts them when ready |
| 33 | `docs/README.md`, the one-page map of the repository | Delivered; the root updates it whenever a file is added, renamed or retired |
| 34 | First run of the runbook on the laptop: Part A, then Part B once | **Next (author, with the assistant)**, after the optional account checks in step A0 |

**Commits so far (Oct 20 to 22):** `4ae9f7f` LO update; `f3f898a` register; `4a911b1` lab results; `edf75cf` Video 1 outline; `232f594` run-sheet v1; `2e0a9f9` voice-over v2; `77f2204` run-sheet v3; `5b818e6` living handoff; `1770043` Video 2 outline and handoff update; `48717fa` run-sheet v4 and Video 1 story document; `1dc45af` (the parent of the next commit; its contents were not checked in this chat); `8f6f186` Video 1 narrative draft v1; `055718d` living handoff (this chat takes ownership, fresh-start plan, narrative decisions); `01ec577` root update (contracts plan, standalone rules, Video 2 decisions); `a15a869` video contract template and Video 1 contract; `6ded6e9` docs checks, the Video 1 phrase fix, the slides wording, and the "fulfilled" and package decisions; `3f10600` Video 2 contract and narrative seed, the seed-material rule, and handoff sections 11 and 12 in the starter prompts; `cb98c81` Video 3 contract, register rows 42 to 44, handoff rows 28 and 31; `dcbb48e` handoff section 15 (starter prompts by role); `8aaf08b` docs map (`docs/README.md`), the Video 1 contract set to Active, and the read-order fixes.

## 7. Decisions made (dated)

- **Oct 21, LO wording:** applied to the curriculum doc. LO1 names label selectors, aggregation and `rate()` and says "run in Elastic using the same PromQL expression"; LO2 uses "arithmetic between aggregated results" instead of "vector matching"; LO3 covers unsupported constructs, boundary behavior such as the date-picker window, and the feature's current status.
- **Limitations are mentioned, practically,** where the learner would meet them; the design note that said to wait until a learner raises them was replaced. Every limitation claim traces to a docs link or a test.
- **Status wording:** say PROMQL is "available on Elastic Cloud Serverless and in the Elastic Stack from 9.5". **Never say "preview."** The live command page shows Serverless and Stack GA 9.5+ (the Serverless badge has no lifecycle label; Elastic's what-is-PromQL page says GA on Serverless).
- **`increase()` moves to Video 3** as the boundary-behavior example.
- **Record the screen first, then write or time the narration.**
- **Oct 22: record on the laptop** (the desktop is unreliable). Full-screen browser, `localhost`. Paste commands rather than type them, and stage the Elastic line before recording the Prometheus clip. The narration says "two screens," not "two tabs."
- **Say "expression," not "query,"** when claiming sameness. Say "most" or "common," never "all". The Grafana data-source route is untested, so nothing may imply it.
- **Video 1 has three rungs:** selector (R1), `rate()` (R3), `sum by` (R6), in that order, because `sum by` builds on `rate()`.
- **The `| SORT` is dropped** from the rung 3 Elastic command.
- **Clean-start reset done** instead of explaining old counters.
- **Handoff is a living file** (this one).
- **Oct 22, after the incident:** rotate the live Elastic API key; treat the desktop as unreliable and do not use it; investigate the security incident in a separate chat.
- **Oct 22: the laptop hosts the stack too.** Keep it awake with `caffeinate`; run the stack for a couple of hours while capturing.
- **Oct 22: hold the Video 2 and Video 3 story scripts** until the evidence and the open decisions exist. The three-act spine (Video 1 asks whether the expressions run, Video 2 builds something real, Video 3 shows where it differs) is a note, not a plan. **Lifted Oct 25** (see below).
- **Oct 22: the story document is generated from the run-sheet.** If they differ, the run-sheet wins and the story is regenerated.
- **Oct 22: two fixes to Video 1's narration:** Clip B2's last sentence no longer contradicts itself ("that's only display; the only thing we changed is the wrapper"), and "Two tabs" became "Two screens."
- **Oct 22: this chat owns the repo.** Only changes from this chat reach it; the author applies, checks, commits and pushes. The other chat stays available for reference.
- **Oct 22: a fresh start** replaces the rotate, revoke and delete plan. The old project is deleted and the desktop is not sending data (author). A new Serverless project, a new write-only key and a new local stack, then a warm-up long enough for testing and demos (length not decided).
- **Oct 22: the Video 1 narrative is rewritten as one continuous piece** (`module1-video1-narrative.md`). Its spine is "find the seam": the viewer watches the expression and tries to catch it changing, and the reveal is that only the wrapper is new. Each rung exists because the previous one left a problem. The author's reaction: it "feels very good", pending the listening test.
- **Oct 22: the introduction opens Video 1** (option A). It names the investment (scrape configs, dashboards, PromQL) and the fear (rebuilding it all), then hands over to the game. A separate Module 1 introduction can be added later, written after the three videos are scripted. From the author's earlier sample we kept the structure, and did not carry over "runs unchanged", "single remote-write block" or "I want to show you". We say "one remote-write block added to its config", and "we" and "you".
- **Oct 22: every number is spoken, none is captioned.** TTS makes edits cheap, and the narration is the only place a number lives, so a re-capture means refilling the placeholder table and regenerating the audio. The author is not the final video editor, and captions would be a second thing to keep in sync. Each result keeps its 4-second hold so the viewer sees what is said. A spoken form for the numbers (rounding, words) is to be tested with Qwen3.
- **Oct 22: the narrative file becomes the source of truth once the author approves it.** Until then the run-sheet wins. This amends the earlier decision that the story document is generated from the run-sheet: after approval the run-sheet's voice-over blocks and the story document are regenerated from the narrative.
- **Oct 22: no hard word or length rules** (about five minutes per video, since each is a part of Module 1). The slide guidance does not constrain the narrative: slide narrations may tell the generator which shape to use.
- **Oct 22: the Mac Mini is the lowest item.** Not tracked further; the author will raise it.
- **Oct 25: the root structure (option A).** This chat is the root and owns the shared files (this handoff, the claims register, the glossary, the query lab, the environment notes, the voice guide). The author is the oversight. Each video gets its own chat, started from a contract handoff. A video chat owns only its own files and ends each turn with a short list of requests for shared files. Superseded by the "fulfilled" decision below: a video is fulfilled when its script is approved, its claims are verified against its own take log, its run-sheet is done, its narration is generated, and the author has captured the footage (editing in the video editor is the author's).
- **Oct 25: self-contained production.** No long-running or shared data between videos. One Serverless project and one key are reused. Each video starts from a reset (section 5, tracker row 26), and its contract states its own warm-up and stack state. Only one stack runs at a time, because all videos write to the same data stream: scripting can run in parallel, rehearsal and capture run one at a time.
- **Oct 25: the videos are strictly standalone.** Each restates what it needs (about 20 seconds; for example Video 2 recaps the wrapper and the metric) and teaches the date-picker rule itself in Video 3. A pointer to another video is a courtesy that can be cut without loss. Each contract lists its "entry knowledge". The learning objectives need no rewording (the assistant's reading: each is achievable alone, and the Remember, Apply, Analyze ladder is a design, not a prerequisite chain); the author may ask for edits.
- **Oct 25: Video 2's decisions.** Approved: 1 (the through-line is the per-service error ratio), 2 (R2, R5, R7 and R8 in full; R1, R3 and R6 as one-sentence reminders), 6 (two pause-and-try prompts), 8 (flexible length; optional beats are cut first), 9 (the same workflow as Video 1), and a new 10 (strictly standalone). Decided: 4 (nonzero values) uses the controlled `paymentFailure` flag, after its effect is measured on a fresh stack, because every video starts from a reset and we cannot wait for a natural error episode. Open: 3 (series slide, waits for the TSDS docs check), 5 (range chart) and 7 (percent form), both waiting for a rehearsal.
- **Oct 25: the hold on the Video 2 and Video 3 scripts is lifted.** They are drafted with placeholders and a claims-to-confirm table, as Video 1 was. This amends the Oct 22 hold.
- **Oct 25: "fulfilled" ends at the author's submission to the second editor.** The author is the first editor and assembles the whole video (slides, demos, voice-over) at production quality; a second editor then polishes it. A video chat's work is complete when the learning objective, outline, narrative and claims are approved and verified, every demo step has been run on a freshly reset stack, the run-sheet is final and the narration audio is generated. The author captures the footage, assembles and exports the video, and submits it (template, section 1).
- **Oct 25: the package for the second editor is the exported first-pass video plus the slide files.** The slide generator produces a `.pptx`; the author uploads it to Google Drive, opens it as Google Slides, and gives the second editor the link. On an earlier project the second editor took exactly this, animated the slides, and used the demo and audio from the video, with no transcripts. It changes only if something changes on the author's side.
- **Oct 25: one phrase changed in the Video 1 narrative after the docs check.** "The wrapper only answers three questions" became "here it makes just three choices", because the PROMQL command has more options than the three we set (register row 36). Approved by the author.
- **Oct 25: roles restated.** A video chat owns everything for its video: outline, narrative, slide narrations, run-sheet, rehearsal, take log and audio. The root owns the template, the contracts, the shared files, the docs checks, the reset runbook and the arc review. The root had drifted into writing the Video 2 narrative; the author caught it, and the rule is now written into the template.
- **Oct 25: seed material.** The root may hand a video chat work built before the chat existed. It is a proposal: the chat asks the author at the start whether to use it, rewrite it or ignore it, and owns the file afterwards. The first seed is the Video 2 narrative draft v1 (spine: the four ideas built one at a time; a setup block of about 30 seconds that restates the wrapper, the date picker and the metric; two pause-and-try questions as separate clips; optional blocks for decisions 3 and 5; payment's values stay placeholders until the flag's effect is measured). Video 1's narrative was also written before its chat, but the author approved it, so it is approved material, not a seed. Video chats now read handoff sections 11 and 12 as well, until a voice guide exists.
- **Oct 25: Video 3 contract.** The Video 3 chat writes the outline and the narrative. The contract carries candidate beats as seed material, each tied to the evidence it needs: probes P1 to P4 for the constructs that return a client error, P5 for the silent division, R4 for the picker-width boundary, P6 and P7 for windows and steps, the documented-but-untested items, and the feature's status. Video 3 teaches the date-picker rule itself, because it is this video's boundary-behavior objective. The through-line is open; the arc idea ("catch the expression changing") is offered as a bonus that nothing may depend on. Three behaviors stay distinct: a client error, no results, and a quiet difference. The feature's status is not claimed until the author reads the badges.
- **Oct 25: starter prompts by role.** Section 15 now holds a prompt for a replacement root chat, a pointer to the video chat prompts (section 11 of each contract) with what can start before the stack exists, and the fresh-archive command with a note that the archive has no `.git`.
- **Oct 25: the starter-prompt approach is validated.** The Video 1 chat's first reply, from the archive alone, read the contract and its files, restated the state in its own words (the narrative approved, the outline and run-sheet stale, no stack running), treated the narrative as approved material and not a seed, asked one question, proposed a stack-free next step (the outline revision), promised a scratch-repo diff stat, and ended with requests for the root. It also found real conflicts: the outline's sentence about the feature's availability against the contract's "no status statement" rule, `{{PCT_D}}` still in the run-sheet, and the run-sheet's "three parameters answer three questions" against the approved "three choices". Those belong to the Video 1 chat's lane.
- **Oct 25: `docs/README.md` added.** A one-page map of the repository (current files with owners, history files, code and configuration). The root updates it in the same delivery whenever a file is added, renamed or retired.
- **Oct 26: the runbook is `docs/reset-runbook.md`.** It consolidates the README's local setup, the quickstart's reset section and the run-sheet's pre-roll into three parts (one-time setup, per-video reset, pre-roll), each step with its expected output. The contracts and the template now point to it. The quickstart's closing paragraph no longer advises re-running `apply-config.sh` without a permission check. `apply-config.sh` itself is unchanged: the fix is decided after the first laptop run shows whether the problem occurs on macOS.

## 8. Open decisions and parked items

**Open decisions (author's call):**
- Reconcile the service count: `docs/otel-collector-reference.md` says 19 services and 16 microservices, while Prometheus reports 18 (register row 12; lab R6). The difference may be real (a service that emits no span metrics). Check when the stack is up; no video states a service count.
- The Video 3 through-line (the Video 3 chat decides with the author; the arc idea is one candidate).
- Whether the Video 2 chat uses, rewrites or ignores the narrative seed (the author decides at the start of that chat).
- Video 3's feature status (preview or generally available) is read from the author's browser when its script is written: the fetched docs pages strip the "applies to" badges (register row 3).
- Arc idea (suggested Oct 25, not decided): the "find the seam" game from Video 1 returns in Video 3, where the viewer finally catches the expression changing. It must stay a bonus, because the videos are standalone.
- Warm-up length: set per video in each contract (Oct 25). The lab's 45 minutes is the floor to test.
- Account checks (section 5): the author has not yet confirmed them.
- How Qwen3 reads the spellings (`prom-Q-L` or `PromQL`, `E-S-Q-L` or `ESQL`, `S-L-Os`), and the spoken form of the numbers.
- Shapes for the opener and recap slides, to give the slide generator explicitly. For Video 1 the Video 1 chat decides with the author, and the root records the outcome. The narrative's opening block names no items, so the outline's shape A (a list of three) needs the slide narration to name the three patterns.
- Video 2's decisions 3 (series slide, waits for the TSDS docs check), 5 (range chart) and 7 (percent form), both waiting for a rehearsal.
- Opener closing line: superseded on Oct 22 by the narrative's opening, which ends on the game (watch the expression and try to catch it changing).
- Copy-across idea for rung 1 (copy the expression from Prometheus and paste it into a staged Elastic skeleton).
- Recorder on the laptop: macOS's built-in recording or OBS. Test clip: cursor visible? text readable? resolution?
- Browser zoom level. (The address bar is hidden in full-screen, so the project ID is not visible; confirm in the test clip.)
- Where the run-sheet is displayed during a take (one machine).
- A Mac Mini as an always-on server (lowest priority; the author will raise it).
- Remote-write endpoint: Elastic's docs recommend the Managed Prometheus Remote Write endpoint for Serverless; this track uses the direct one. Matters for Module 2.
- Instruqt setup script (still unrestricted key, plain `docker compose up`).
- Incident demo (the spike and baseline are unmeasured; no "real-time detection" claims until tested).
- Fix for `apply-config.sh` (leading option: mode 644; the key is write-only, but it is a security trade-off to decide together). Decide after the first laptop run: step A8 of the runbook checks whether the permission problem happens on macOS at all.

**Parked (the housekeeping delivery, tracker row 16):** the clean-start results and readings; the `chmod 600` finding; the quickstart paragraph to correct; the 24 config errors and the overlapping blocks; the sleep reading; the lab file's outdated "Feeds" header (R4 moved to Video 3; Video 2 now uses R2, R5, R7, R8); the R7 Elastic row count; the unexplained 37,493 failed samples; the `offset` modifier (ambiguous on the limitations page); the payment error episode (0 at 11:22:53 CDT, 0.03125 at 11:26 CDT on Oct 21, flag off) and its intervals; stale figures (cheat sheet says 19 services, actual is 18; sizing numbers tied to 30 containers); the older-doc sweep for absolute claims (README tagline, cheat sheet, demo script).

## 9. Claims discipline

- Every spoken or written claim traces to a row in the claims register (status doc, section 4). Statuses: **Verified** (seen here), **Docs**, **Observed**, **Open**, **Retired**, plus **Decision**. Say "inferred" in conversation when something is.
- In narration: numbers come only from the take log, next to what they are compared with; agreement statements carry the gap in seconds between the two runs; no bare percentages; placeholders `{{LIKE_THIS}}` stay until the numbers are real.
- If a number disagrees with a sentence, rewrite the sentence; don't bend the number.
- Docs change often. Re-read the limitations page before each recording and record the retrieval date: `https://www.elastic.co/docs/reference/query-languages/promql/promql-limitations`. Its key sentence: the majority of PromQL expressions run unchanged.

## 10. Glossary (running) and key technical facts

| Term | Plain meaning | Status and source |
|---|---|---|
| Metric | A named measurement, such as `traces_span_metrics_calls_total` | Standard |
| Label | A key and value on a series, such as `service_name="frontend"` | Standard |
| Series | One metric name plus one unique set of labels | Standard |
| Label matcher | A condition on a label inside `{}`; `=`, `!=`, `=~`, `!~` | Verified: https://next.prometheus.io/docs/querying/basics |
| Fully anchored regex | A regex must match the whole label value, so `frontend\|checkout` does not match `frontend-proxy` | Verified in Prometheus docs and in lab R2 on both sides |
| Instant vector | One sample per series at a single moment | Verified (Prometheus docs) |
| Range vector | A window of samples per series, written in square brackets such as `[5m]` | Standard; Elastic's functions page says range vector functions return an instant vector |
| Table tab and Graph tab | Prometheus runs an instant query on Table and a range query on Graph | Verified (Prometheus docs) |
| Counter | A cumulative metric that only increases or resets to zero on restart | Verified: https://prometheus.io/docs/concepts/metric_types/ |
| `rate()` | The per-second average rate of increase of a series over the range | Verified in Elastic's wording: https://www.elastic.co/docs/reference/query-languages/promql/functions/range-vector |
| Aggregation operator, `sum by` | Combines one instant vector into fewer elements; `by` keeps the named labels | Verified: https://prometheus.io/docs/prometheus/latest/querying/operators/ |
| `PROMQL` command | An ES\|QL source command: `PROMQL [option=value ...] [result_name=](expression)` | Lab setup section (from the command docs) |
| `index=` | The data stream to query: `metrics-generic.prometheus-default` | Lab |
| `time=?_tend` | Makes an instant query at the end of the date picker's range; leave it out for a range query with a chart | Lab (command docs) and Kibana docs for `?_tend`: https://www.elastic.co/docs/explore-analyze/query-filter/languages/esql-where |
| Wrapper | Our narration's word for everything around the expression in Elastic: the `PROMQL` command, its options (`index`, `time`) and the result name. It answers three questions: where this runs, when it is evaluated, and what the answer is called | Our term, not Elastic's; the pieces are from the command docs (see `PROMQL` command above) |
| Contract | The handoff for one video chat: the learning objective, audience, through-line, entry and exit sentences, entry knowledge, allowed and forbidden claims, the evidence and stack state needed, acceptance checks, deliverables and the files the chat owns | Our term (Oct 25) |
| Reset | The per-video procedure that clears all data and restarts the stack, so no video depends on another's data | Our term (Oct 25); the runbook is tracker row 26 |
| Date picker | PROMQL reads only data inside its range, so a window longer than the picker sees less data (lab R4: 9,391 versus 18,925 versus Prometheus 18,960 for `increase(...[30m])`) | Tested |
| ES\|QL | Elasticsearch Query Language | Verified (Kibana docs) |
| Remote write | How Prometheus sends its data to Elastic in this demo | Verified (register row 9) |
| `_timeseries` | The Elastic result column that holds a series' labels as JSON | Lab R1 |
| `step` | The evaluation time in an Elastic PROMQL result | Lab |
| Division of two aggregates | Both sides aggregated alike works; a series missing on one side drops out of the result | Lab R8 (both systems agree) and the limitations page |
| TSDS | Time series data stream: dimensions, series identity, metric types | **Not yet verified; check the TSDS docs before writing about it** |

## 11. What we learned about the narrative

These came from reading Video 1's first draft as a viewer and iterating on it. The author's reaction: it "feels right and at the level we want", pending the speech-engine test.

1. **Put the motivation on the surface.** Say why a thing is wanted before showing it ("on its own, a counter just climbs; what you usually want is how fast"). The author likes that conclusions follow from stated reasons.
2. **One idea per beat.** The `SORT` detour was cut because it added a second idea to a rung.
3. **Order must match the demo.** The first opener listed `sum by` second while the demo ran `rate()` second. Check the agenda against the screen order.
4. **A question, then the reveal.** Frame the one big idea so it sticks: the wrapper answers three questions (where should this run, when, and what do we call the answer).
5. **Don't spoil the result.** "Judge the match yourself" earns more trust from a skeptical engineer than announcing the outcome. If the outcome is stated, confirm it against the footage.
6. **Don't leave a loose thread.** State a fact plainly rather than hinting that a later video explains it. A pointer is fine; a cliffhanger is not.
7. **Point to the next video, not the one after.** The recap says what Video 2 builds, then mentions the edges.
8. **Introduce a metaphor once.** "Rung" gets one sentence ("we'll climb a short ladder") before it is used.
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
24. **Absolute words in a narration are claims.** "Only", "all", "never" and "always" each need checking against the reference page. The Oct 25 docs check found that "the wrapper only answers three questions" overclaimed, because the command has more options than the three we set.

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

## 13. What in the Oct 20 handoff is now out of date

- "Mention technical preview once": **replaced** (section 7).
- Open decisions 1 to 4 (where `increase()` goes, LO wording, recording workflow, capture machine): **decided** (section 7).
- "The root chat owns the curriculum doc": **the author owns it now.**
- "Not yet run: R2, R5, R7, R8": **run, all Same.**
- The environment section's "ask for the project name and region": **known** (section 4).
- The delete-the-Azure-project question: **done.**
- "The PROMQL command is a preview feature per the 9.4 docs; Serverless status was not found": **superseded** by the status wording decision.
- The reading list and plan table are superseded by the ones here.
- The Oct 20 plan to capture on the desktop: **superseded** (the laptop, Oct 22).

## 14. How to update this file, and the update log

- **When:** after each commit batch, each decision, each new finding or trap, and each change to the stack's state.
- **How:** edit the section in place (tracker, state, decisions, open items), add one line to the log below, and ship it in the same delivery as the work it describes. Keep entries short.
- **Before the author leaves a chat:** make sure sections 5, 6, 7 and 8 reflect the latest state, and that the tracker has "next" marked.

| Date (UTC) | Update |
|---|---|
| 2026-10-22 | File created. Captures the working agreements, repo routine, stack state after the clean restart (T0 00:41:00 UTC, +70 min readings), decisions, narrative lessons, glossary, traps, and the parked list. |
| 2026-10-22 | Video 2 outline committed. Commit `5b818e6` added to the list. Read order and tracker row 7 updated. |
| 2026-10-22 | Desktop incident recorded (unexpected restarts, Malwarebytes PUPs, glitch persists). Key rotation plan and permission step added. Commit `1770043` added. Tracker rows 16 to 19 added. |
| 2026-10-22 | Combined update before handing off to a new chat: the laptop is now the stack host and the recording machine; migration plan (rotate key, revoke old key, delete the data stream, set up the laptop); story document and run-sheet v4 (`48717fa`); decisions, tracker, open items and narrative lessons refreshed; section 16 (anticipated questions) added. |
| 2026-10-22 | Update from this chat (it takes ownership of the repo): the fresh-start plan (new project, new key, new stack, warm-up) replaces the rotation plan; decisions on the narrative approach, the introduction, spoken numbers and the narrative file as the future source of truth; tracker row 24; glossary entry Wrapper; narrative lessons 19 to 22; two traps; four anticipated questions. Commit `8f6f186` added. |
| 2026-10-25 | Root-chat update: the root structure and the contracts plan, the self-contained and strictly standalone rules, the reset runbook (steps 2 and 3 of the plan are now one-time), Video 2 decisions approved, the script hold lifted, tracker rows 8, 9, 12, 17, 18 and 24 updated and rows 25 to 29 added, commit `055718d` added, glossary entries Contract and Reset, lesson 23, two traps, three anticipated questions. The Video 2 outline was updated in the same delivery. |
| 2026-10-25 | Docs checks and contracts: commits `01ec577` and `a15a869` added; the "fulfilled" and package decisions recorded (the second editor takes the exported video plus a Google Slides link); the Video 1 narrative phrase change; tracker rows 24, 25, 28 and 29 updated; section 8 cleaned; lesson 24; one trap; two anticipated questions. Register rows 7, 8, 31 revised and 36 to 41 added; the Video 2 outline's decision 3 annotated. |
| 2026-10-25 | Video 2 delivery and roles: the Video 2 contract and the narrative seed added; the template and the Video 1 contract revised (handoff sections 11 and 12 added to the starter prompts, seed material defined); commit `6ded6e9` added; tracker rows 17, 18, 20, 25 and 27 updated and row 30 added; two decisions; one trap; two anticipated questions. |
| 2026-10-25 | Video 3 contract and the limitations-page check: the Video 3 contract added; commit `3f10600` added; tracker rows 17, 25 and 28 updated and row 31 added; one decision; one anticipated question. Register rows 25 and 27 annotated and 42 to 44 added. |
| 2026-10-25 | Section 15 revised into starter prompts by role (a replacement root chat, the video chats, a fresh archive); commit `cb98c81` added; tracker row 25 closed and row 32 added; one decision; one anticipated question. |
| 2026-10-26 | Docs map and the Video 1 chat's first reply: `docs/README.md` added; the Video 1 contract set to Active; read-order items 4 and 4a corrected; commit `dcbb48e` added; tracker rows 32 and 33; the service-count item and the shape note added to section 8; two decisions; one anticipated question. |
| 2026-10-26 | Runbook delivery: `docs/reset-runbook.md` added; the quickstart's closing paragraph corrected; the map, the template and the three contracts point to the runbook; commit `8aaf08b` added; tracker rows 12, 16 and 26 updated and row 34 added; one decision; one anticipated question. |

## 15. Starter prompts (by role)

**Which chat is which.** The root chat owns this file and every shared file. Each video chat owns its own video. Attach a fresh archive to every new chat (the command is at the end of this section). The prompts below assume the archive is attached.

### 15.1 A replacement root chat

> I'm continuing as the root chat of a Prometheus-to-Elastic training track (Module 1). I've attached a fresh zip of the repo. The root chat owns the shared files: the living handoff, the claims register, the glossary, the query lab, the environment notes, the learning objectives, the video contract template and the three video contracts. Per-video chats own their own video's files. Please read `docs/handoff-module1-living.md` first, then the files it lists, then `docs/video-contract-template.md` and the three contracts. Then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything and keep the glossary. The previous root chat is still open, so I can bring you its answers to questions you have.

### 15.2 A video chat

Each video's prompt is in section 11 of its contract: `docs/module1-video1-contract.md`, `docs/module1-video2-contract.md` and `docs/module1-video3-contract.md`. Copy it as is. It tells the chat to read the contract, then the files the contract lists, then handoff sections 1, 2, 3, 9, 10, 11 and 12 (read-only); to follow the working agreements; to ask the author first what to do with any seed material; and to end every turn with its requests for the root chat.

- **What can start now, with no stack:** Video 1, checklist rows 2, 4, 5 and 6; Video 2, rows 3 to 6; Video 3, rows 2 to 6 (each contract's section 8). Rehearsals and takes wait for the one-time setup and a reset (tracker rows 12 and 26).
- **Requests for the root:** the author pastes the video chat's list into the root chat, and the root turns it into a delivery (a register row, a glossary term, a lab result, a handoff update).

### 15.3 A fresh archive

From the repo root, after the last commit is pushed: `git archive --format=zip -o ~/Downloads/prometheus-to-elastic-repo.zip HEAD`. It holds tracked files only, so no demo folder and no secrets, and it has no `.git` folder (section 12), so a new chat checks sync with `git fetch` and `git status -sb`, not from the archive.

## 16. Anticipated questions (answers from the previous chat)

| Question | Answer |
|---|---|
| Why was the desktop dropped? | It restarted unexpectedly twice on Oct 22, its screen still glitches, and Malwarebytes found adware on it. The author judged it unreliable and moved everything to the laptop. The cause is being investigated separately. |
| Why a 45-minute warm-up? | The lab's rule: the `rate` windows and charts need data, and the Kibana date picker is set to the last hour. It was set for the lab on Oct 20 and has not been re-derived. |
| Why "expression," not "query"? | The line in Discover wraps the expression in the PROMQL command, options and a result name, so the line is not identical to a Prometheus query. The older scripts' "didn't change a single character" is wrong and retired. |
| Why is `increase()` in Video 3? | It differs when the date picker is narrower than the window (lab R4: 9,391 and 18,925 in Elastic against 18,960 in Prometheus). That makes it the boundary-behavior example. |
| Why paste instead of typing, and why stage the Elastic line? | The lines are long, short gaps between the two runs gave tighter agreement (inferred), and editors may auto-close brackets (unverified). Staging means the Elastic line is in the editor before the Prometheus clip is recorded. |
| Why "rung"? | A ladder metaphor, introduced in one sentence at the start of Clip B1. Video 2 climbs higher. |
| What are the wrapper's three questions? | Where should this run (`index`), when is it evaluated (`time`), and what do we call the answer (the result name). |
| Why is `sum by` third? | Because `sum by (service_name) (rate(...))` builds on `rate`. |
| Why never "preview"? | The live command page shows Serverless and Stack GA 9.5+. Earlier docs said preview for 9.4. |
| Where do the numbers in the narration come from? | Only from the take log, as `{{placeholders}}`. If a number disagrees with a sentence, rewrite the sentence. |
| Why was `SORT` dropped from the rung 3 Elastic line? | One idea per beat. R7 and R8 ran without a sort. The line without it has not been run exactly and is part of the rehearsal. |
| What is still unexplained? | The 37,493 failed samples with no log line, the nine overlapping-blocks warnings, and the payment error episode on Oct 21 (flag off). |
| Why not re-run `apply-config.sh`? | It sets mode 600 on the generated config, which the Prometheus container could not read on the desktop. It may be fine on macOS (inferred). Test on the laptop; fix the script in the housekeeping delivery. |
| How fast does the author want to go? | Not in a rush. Tiny steps, quality over speed, and everything explained. |
| How should I spell terms for the speech engine? | `prom-Q-L` and `E-S-Q-L` in voice-over; metric names as words. The slide generator turned `prom-Q-L` back into PromQL correctly. |
| Why does this chat own the repo? | The author decided on Oct 22 that only changes from this chat reach the repo, so nothing drifts. The author applies, checks, commits and pushes; the assistant states the expected result first. |
| Why are all the numbers spoken, not captioned? | TTS makes editing cheap: change the text, regenerate. A number that lives only in the narration is refilled in one place after a re-capture. A caption would be a second place to keep in sync, in the video editor. |
| Why was the narrative rewritten? | The first draft was choppy: uniform short sentences, the same list announced three times, no tension, and report-style numbers. The new draft has a spine (find the seam), each rung caused by the last, and an opening that names the viewer's fear. See section 11, items 19 to 22. |
| Why a new project instead of rotating the key? | The author deleted the old project and the desktop no longer sends data, so a new project, a new key and a new local stack are a cleaner start than rotating. |
| Why one Serverless project for all the videos? | Each video starts from a reset that deletes the data stream and restarts the local stack, so a new project per video adds nothing. The project and the write-only key are one-time setup. |
| Why must every video be strictly standalone? | The author does not want production to depend on data, uptime or recording order from another video, and a viewer may start anywhere. Each video restates what it needs; pointers to other videos are cuttable. |
| Who edits the shared files once there are per-video chats? | Only the root chat. A video chat owns its own video's files and sends the root a list of requests for the handoff, the claims register, the glossary, the query lab and the environment notes. |
| What does the second editor receive? | The exported first-pass video and the slide files (a Google Slides link made from the generator's `.pptx`). Transcripts, audio files and the take log stay in the repo. |
| Why "three choices" in the Video 1 narrative, not "three questions"? | The PROMQL command has more options (index, step, buckets, start, end, time, scrape_interval, and a result name), all optional. "Only answers three questions" suggested those three were the whole story; "makes just three choices" is true. |
| What is seed material? | Work the root built before a video chat existed, handed over as a proposal. The video chat asks the author whether to use it, rewrite it or ignore it. Approved material (Video 1's narrative) is not a seed. |
| Why does Video 3 teach the date-picker rule instead of pointing back to Video 1? | The videos are strictly standalone, and the rule is Video 3's own boundary-behavior objective. A viewer may start anywhere, so the video teaches it. A pointer to Video 1 would be a cuttable courtesy at most. |
| How do I start a video chat? | Open a new chat, attach a fresh archive (section 15.3), and paste the prompt from section 11 of that video's contract. The chat starts by asking you about any seed material, then reports its state, its needs and one next step. |
| Where is the map of the repository? | `docs/README.md`: each file, its owner, and when to open it, plus the history files that current work does not use. |
| Where are the setup and reset procedures? | `docs/reset-runbook.md`: Part A (one-time setup), Part B (the reset before every rehearsal and take) and Part C (pre-roll), each step with the output to expect. |
| Why are the pause-and-try questions separate clips? | The speech engine should not have to produce silence. The question and its answer are generated as two clips, and the 3-second pause is placed in the edit. |
