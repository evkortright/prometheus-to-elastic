# Handoff — Module 1 (living file)

**Repo:** `github.com/evkortright/prometheus-to-elastic` (private)
**Started:** October 22, 2026. **Last updated:** see the update log at the end (section 14).
**Supersedes:** `handoff-2026-10-20-module1-continuation.md`. Keep that file as history only; section 13 lists what in it is now out of date.
**This file is updated, not rewritten.** Add to it at every milestone (section 14 says how). If it disagrees with an older document, this file wins, unless the claims register says otherwise.

**Read in this order:**
1. This file.
2. `docs/module1-status-2026-10-19.md`: section 2 (state), section 3 (open items), section 4 (claims register). The file name keeps its old date; do not rename it.
3. `docs/module1-query-lab.md`: the tested expressions and recorded results.
4. `docs/module1-video1-run-sheet.md`: the screen steps and the voice-over for Video 1.
5. `docs/module1-video1-outline.md`.
6. `docs/module1-video2-outline.md`, if it exists in the repo. It was drafted on Oct 22 and may not be committed yet; ask.
7. `docs/slide-narrative-guidance.md`: the author's rules for slide narrations.
8. `docs/module-learning-objectives.md`: the Module 01 section and the design notes.
9. `docs/quickstart.md`: the reset section.

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

## 3. The repo-update routine

Laptop (macOS), repo at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`.

| Step | Command | Expect |
|---|---|---|
| 1. Apply | `cd /Users/enriquekortright/personal/projects/prometheus-to-elastic`, then `unzip -o ~/Downloads/<name>.zip`, then `git status -sb` | ` M <file>` for an edited file, `?? <file>` for a new one |
| 2. Check | `git diff --stat`. For a **new** file: `git add <file> && git diff --cached --stat` | The exact insertions and deletions the assistant stated in advance |
| 2b. Safety grep | `grep -rn "OFQtLV9[K]" . --include="*.yaml" --include="*.md" --include="*.sh" \| grep -v opentelemetry-demo` | Nothing at all |
| 3. Commit and push | Edited files: `git commit -am "<message>" && git push`. New files (already added): `git commit -m "<message>" && git push` | A commit line with the same stat, then `main -> main` |

- The safety grep pattern is the first characters of the old, deleted key. The brackets stop this file from matching its own text.
- **The assistant computes the expected stat in advance** by copying the "before" file into a scratch git repo in `/tmp`, copying the "after" file over it, and running `git diff --stat`. State it before asking the author to run the check.
- **Delivery format:** a zip of the changed files with repo-relative paths, presented as a file. Browsers drop files that start with a dot, so deliver those as commands.
- The author asked for commit and push to be **one combined step** once the check matches.
- On the desktop, pull with `git pull --ff-only`.

## 4. Environments

- **Laptop (MacBook Pro, macOS):** where the author works with the assistant, commits and pushes. The browser reaches the desktop's Prometheus at `http://192.168.1.167:9090`.
- **Desktop (Windows with WSL Ubuntu, host name `DESKTOP-JET863K`):**
  - Repo clone: `~/personal/projects/prometheus-to-elastic`. The OpenTelemetry demo (pinned `DEMO_VERSION=3.0.0`) is in its `opentelemetry-demo` folder.
  - Prometheus at `http://localhost:9090`. Grafana, the demo store and the feature flags page are also reachable from the Windows browser.
  - **Time zone set to Central on Oct 22.** Only the zone changed, not the clock (checked: the laptop and the desktop read the same UTC time). Central is UTC−5 until the clocks change on Nov 1, then UTC−6 (the usual US rule; not verified here).
  - **Sleep:** the active plan is Balanced, and "sleep after" on AC is `0x00000000` (never), verified on Oct 21 with `powercfg`. On battery it is 900 seconds. No sleep or resume events in the 48 hours before Oct 21 (Windows System log, Kernel-Power events 42 and 107).
  - Screen capture: Windows Game Bar (Win + Alt + R); one monitor. The test clip is still to do.
- **Elastic:** Serverless project **`prometheus-to-elastic`**, Azure Central US (Iowa). The earlier Azure project was deleted by the author. Data stream **`metrics-generic.prometheus-default`**, in time series mode, created from the template `metrics-prometheus@template`. The write-only API key (`auto_configure`, `create_doc`) is in `.env.elastic`. A write-only key cannot delete or read the cluster root; deleting data needs Kibana Dev Tools under the author's own login.
- **Stack:** `docker compose -f compose.yaml -f compose.observability.yaml` is required (the base file lacks Prometheus and Grafana). 25 services run. Prometheus reports 18 `service_name` values. The Prometheus container runs as user `nobody` (uid 65534).

## 5. Current state of the stack (update me)

**Clean restart on Oct 22:** the stack was fully reset using the quickstart's reset section. **T0 = 2026-10-22 00:41:00 UTC** (7:41 PM CDT on Oct 21).

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
- **The first block compaction is expected around 03:00 UTC on Oct 22.** Check whether the overlapping-blocks warning appears (inferred from the Oct 21 timestamps).
- **Evidence from the previous run** is on the desktop in `~/evidence-2026-10-21/` (`prometheus.log`, `rw-metrics.txt`), outside the repo.

**Pre-roll checks** (desktop, WSL), before any recording:
```
date -u; docker ps --format '{{.Names}}: {{.Status}}' | grep -E 'prometheus|flagd'
```
```
date -u; curl -s http://localhost:9090/metrics | sed 's/{[^}]*}//' | awk '/^prometheus_remote_storage_samples_failed_total/{f=$2} /^prometheus_remote_storage_samples_retried_total/{r=$2} /^prometheus_remote_storage_samples_pending/{p=$2} /^prometheus_remote_storage_samples_in_total/{i=$2} /^prometheus_remote_storage_samples_total/{t=$2} END{printf "failed %s | retried %s | pending %s | in %.0f | sent %.0f | gap %.0f\n", f, r, p, i, t, i-t}'; docker logs prometheus 2>&1 | grep -cE 'level=(WARN|ERROR)'
```
Also confirm the `paymentFailure` flag is off on the feature flags page.

**What happened on the previous run (Oct 20 and 21), for context:**
- `samples_failed_total` was 38,122. Two log lines (HTTP 429, "rejected execution of coordinating operation", at 05:51:40 and 05:52:40 UTC on Oct 20) account for 629 of them. **The other 37,493 have no log line and remain unexplained.**
- Before the 05:51:17 UTC restart, Prometheus logged 24 "permission denied" errors reading its config (05:34:41 to 05:50:06). Cause, very likely: `scripts/apply-config.sh` runs `chmod 600` on the generated file, and the container user `nobody` cannot read a mode-600 file owned by the author. The author fixed it by hand (the file is now mode 644). **Do not re-run `apply-config.sh` until the script is fixed.** The quickstart's last paragraph tells people to re-run it and restart Prometheus, which would trigger the same failure.
- Nine "overlapping blocks" warnings appeared in Prometheus's local storage (cause not investigated).

## 6. Work tracker (update me)

| # | Item | State |
|---|---|---|
| 1 | LO wording | Done, committed (`4ae9f7f`) |
| 2 | Claims register update | Done (`f3f898a`) |
| 3 | Lab results R2, R5, R7, R8 | Done, all Same (`4a911b1`) |
| 4 | Clean restart | Done (T0 above) |
| 5 | Video 1 outline | Done (`edf75cf`) |
| 6 | Video 1 run-sheet with voice-over iteration 1 | Done (`77f2204`); not yet heard through the speech engine |
| 7 | Video 2 outline | Drafted (`video2-outline-2026-10-22.zip`); **not yet applied or committed by the author** |
| 8 | Speech-engine test of Video 1 and iteration 2 | Next (author, with fresh ears) |
| 9 | Capture test and R1 rehearsal on the fresh dataset | Next (author) |
| 10 | Opener slide regenerated from iteration 1 | To do (the existing slide came from the first draft) |
| 11 | Real take for Video 1, then narration against the footage | After 8 and 9 |
| 12 | Voice-over style guide (repo file), later a skill | After the listening test |
| 13 | Video 3 outline | Not started; depends on probes P1 to P8 and R4 |
| 14 | Primer doc `docs/module1-promql-primer.md` | Not created; the glossary (section 10) is its seed |
| 15 | Module description | Write last, after the three videos |

**Commits so far (Oct 20 to 22):** `4ae9f7f` LO update; `f3f898a` register; `4a911b1` lab results; `edf75cf` Video 1 outline; `232f594` run-sheet v1; `2e0a9f9` voice-over v2; `77f2204` run-sheet v3.

## 7. Decisions made (dated)

- **Oct 21, LO wording:** applied to the curriculum doc. LO1 names label selectors, aggregation and `rate()` and says "run in Elastic using the same PromQL expression"; LO2 uses "arithmetic between aggregated results" instead of "vector matching"; LO3 covers unsupported constructs, boundary behavior such as the date-picker window, and the feature's current status.
- **Limitations are mentioned, practically,** where the learner would meet them; the design note that said to wait until a learner raises them was replaced. Every limitation claim traces to a docs link or a test.
- **Status wording:** say PROMQL is "available on Elastic Cloud Serverless and in the Elastic Stack from 9.5". **Never say "preview."** The live command page shows Serverless and Stack GA 9.5+ (the Serverless badge has no lifecycle label; Elastic's what-is-PromQL page says GA on Serverless).
- **`increase()` moves to Video 3** as the boundary-behavior example.
- **Record the screen first, then write or time the narration.**
- **Record on the desktop,** with `localhost`, using Game Bar (OBS is the fallback). Paste commands rather than type them; stage the Elastic line before recording the Prometheus clip.
- **Say "expression," not "query,"** when claiming sameness. Say "most" or "common," never "all". The Grafana data-source route is untested, so nothing may imply it.
- **Video 1 has three rungs:** selector (R1), `rate()` (R3), `sum by` (R6), in that order, because `sum by` builds on `rate()`.
- **The `| SORT` is dropped** from the rung 3 Elastic command.
- **Clean-start reset done** instead of explaining old counters.
- **Handoff is a living file** (this one).

## 8. Open decisions and parked items

**Open decisions (author's call):**
- Video 2's through-line (per-service error ratio) and the other eight open decisions in its outline.
- Opener closing line: "you can judge the match yourself" (iteration 1) or "observe essentially the same results".
- Copy-across idea for rung 1 (copy the expression from Prometheus and paste it into a staged Elastic skeleton).
- Recorder: Game Bar or OBS. Test clip: cursor visible? text readable? resolution?
- Whether the Kibana address bar (it contains the project ID) is shown, cropped or blurred.
- Browser zoom level.
- Remote-write endpoint: Elastic's docs recommend the Managed Prometheus Remote Write endpoint for Serverless; this track uses the direct one. Matters for Module 2.
- Instruqt setup script (still unrestricted key, plain `docker compose up`).
- Incident demo (the spike and baseline are unmeasured; no "real-time detection" claims until tested).
- Fix for `apply-config.sh` (leading option: mode 644; the key is write-only, but it is a security trade-off to decide together).

**Parked for the next file delivery:** the clean-start results and readings; the `chmod 600` finding; the quickstart paragraph to correct; the 24 config errors and the overlapping blocks; the sleep reading; the lab file's outdated "Feeds" header (R4 moved to Video 3; Video 2 now uses R2, R5, R7, R8); the R7 Elastic row count; the unexplained 37,493 failed samples; the `offset` modifier (ambiguous on the limitations page); the payment error episode (0 at 11:22:53 CDT, 0.03125 at 11:26 CDT on Oct 21, flag off) and its intervals; stale figures (cheat sheet says 19 services, actual is 18; sizing numbers tied to 30 containers); the older-doc sweep for absolute claims (README tagline, cheat sheet, demo script).

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

## 13. What in the Oct 20 handoff is now out of date

- "Mention technical preview once": **replaced** (section 7).
- Open decisions 1 to 4 (where `increase()` goes, LO wording, recording workflow, capture machine): **decided** (section 7).
- "The root chat owns the curriculum doc": **the author owns it now.**
- "Not yet run: R2, R5, R7, R8": **run, all Same.**
- The environment section's "ask for the project name and region": **known** (section 4).
- The delete-the-Azure-project question: **done.**
- "The PROMQL command is a preview feature per the 9.4 docs; Serverless status was not found": **superseded** by the status wording decision.
- The reading list and plan table are superseded by the ones here.

## 14. How to update this file, and the update log

- **When:** after each commit batch, each decision, each new finding or trap, and each change to the stack's state.
- **How:** edit the section in place (tracker, state, decisions, open items), add one line to the log below, and ship it in the same delivery as the work it describes. Keep entries short.
- **Before the author leaves a chat:** make sure sections 5, 6, 7 and 8 reflect the latest state, and that the tracker has "next" marked.

| Date (UTC) | Update |
|---|---|
| 2026-10-22 | File created. Captures the working agreements, repo routine, stack state after the clean restart (T0 00:41:00 UTC, +70 min readings), decisions, narrative lessons, glossary, traps, and the parked list. |

## 15. Starter prompt for the next chat

> I'm continuing Module 1 of a Prometheus-to-Elastic training track. I've attached a fresh zip of the repo. Please read `docs/handoff-module1-living.md` first, then the files it lists, and then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. Follow the working agreements in section 2 of the handoff: tiny steps, expected output before each step, one question at a time, and the repo routine in section 3. I'm not a PromQL specialist; explain everything and keep the glossary.

To make a fresh archive on the laptop, from the repo root: `git archive --format=zip -o ~/Downloads/prometheus-to-elastic-repo.zip HEAD` (tracked files only, so no demo folder and no secrets). I have not verified how the original archive was made.
