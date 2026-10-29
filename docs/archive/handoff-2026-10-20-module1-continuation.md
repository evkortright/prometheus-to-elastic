# Handoff — Module 1 continuation (video production)

**Date:** October 20, 2026
**Repo:** `github.com/evkortright/prometheus-to-elastic` (private)
**Replaces:** `handoff-2026-10-19-module1-video.md` for anything about environment, queries, or plan. Keep the older one only as history.

**Read in this order:** this file, then `docs/module1-status-2026-10-19.md` (open items and the claims register), then `docs/module1-query-lab.md` (the tested queries and recorded results), then `docs/module1-video1-outline.md`, then `docs/slide-narrative-guidance.md`.

---

## 1. Who you are working with and how

The author builds the Prometheus-to-Elastic training track. They are a training developer and **not a PromQL specialist**. They want to learn by doing, which suits the goal: **granular modules where nothing is left to the imagination and everything is clear and intuitive for the target audience** (Prometheus and Grafana operators evaluating a move to Elastic).

Working agreements:

- **Teach as you build.** Expect many questions. For every query that goes into a narration, explain each part in plain language (metric, label matcher, range vector, `rate()`, `sum by`) and keep a running glossary. A `docs/module1-promql-primer.md` has not been created yet and would be a good output.
- **Claims never outrun evidence.** Every spoken or written claim must trace to a row in the claims register (status doc, section 4). Say *expression*, not *query*, when claiming sameness. Say *most* or *everyday*, never *all* or *any*. Mention *technical preview* once, plainly. A reviewer asked for no "always" or "never" claims, and the author agreed while keeping the marketing strength ("most of your PromQL runs as written, and here is where it doesn't").
- **Verify before asserting.** Earlier in this project two statements were wrong because output was misread (a git-history search was treated as proof the key never reached GitHub; it had). Check outputs line by line, and say "inferred" when it is.
- **Ask one question at a time.** The author answers in chunks and uploads screenshots from a laptop that reaches the desktop.
- **Every file delivery comes with apply, check, commit, and push steps.** The author asked for this explicitly. Quote glob patterns in commands (the laptop shell is zsh; an unquoted `--include=*.yaml` fails).
- **Never ask for or print the API key.** It lives only in `.env.elastic` (gitignored).
- The author does not want to use `--force` anywhere. A safety check before every commit: `grep -rn "OFQtLV9[K]" . --include="*.yaml" --include="*.md" --include="*.sh" | grep -v opentelemetry-demo` should print nothing. (The pattern is the first characters of the old, now-deleted key. The brackets stop this file from matching its own text. The old key lives in git history and is harmless because its project was deleted.)

## 2. Environments

- **Laptop (macOS):** where the author works with Claude, commits, and pushes. Repo at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`. It reaches the desktop's Prometheus, Grafana, and Kibana from the browser.
- **Desktop (WSL/Ubuntu):** runs the OpenTelemetry demo (pinned `DEMO_VERSION=3.0.0`) and the Prometheus remote-write feed. Repo clone path may differ; ask. The author pulls with `git pull --ff-only`.
- **Elastic project:** a new Serverless Observability project was created for the desktop feed. Its name and region were not shared; ask. The earlier GCP project (`observabilityserverless-ac5280`) was deleted. An Azure project from the laptop attempt (`prometheus-to-elastic-bb86ab`) may still exist; ask whether to delete it.
- **Credentials:** write-only API key (`auto_configure`, `create_doc` on `metrics-*`) in `.env.elastic` at the repo root; `scripts/apply-config.sh` generates the demo's Prometheus config from the template. See README steps 2 to 3. A write-only key returns 403 on the cluster root; that is expected.
- **Stack facts (verified):** `docker compose -f compose.yaml -f compose.observability.yaml` is required (the base file alone lacks Prometheus and Grafana). 25 services run. Prometheus reports 18 `service_name` values. Data stream: `metrics-generic.prometheus-default`. To wipe data and start over, see the reset section in `docs/quickstart.md`.
- **Window for charts:** allow about 45 minutes after a start before recording, and set the Kibana time picker to **Last 1 hour** (see finding 1 below).

## 3. What was established (query lab, Oct 20, desktop environment)

Full details in `module1-query-lab.md`. Syntax confirmed from the docs: `PROMQL [option=value ...] [result_name=](expression)`; `time=?_tend` gives an instant query (one row per series); omit it for a range query with a chart.

| Rung | Result |
|---|---|
| R1 label selector | Same: 50 series on both sides, same labels. Presentation differs (labels in a `_timeseries` JSON column) |
| R3 `sum(rate(...[5m]))` | Same: 8.888018468 vs 8.888018465 |
| R4 `sum(increase(...[30m]))` | **Differs when the date picker is narrower than the window.** 15-minute picker gave 9,391; 1-hour picker gave 18,925; Prometheus gave 18,960 |
| R6 `sum by (service_name)(rate(...))` | Same: 18 services; busy ones within about 6%, small ones within about 13% (timing noise, inferred) |

Not yet run: R2, R5, R7, R8 and probes P1 to P8.

**Finding 1 (important):** PROMQL only reads data inside the date picker's range, so a fixed window longer than the picker sees less data and gives a smaller answer. The docs recommend omitting range selectors when porting queries. The docs do not spell out this specific effect in the parts read; it is recorded as measured.

**Other findings:**
- The line in Discover is not character-identical to a Prometheus query: it adds the `PROMQL` command, options, and a result name. The *expression* is the same. (The older scripts claim "didn't change a single character"; retire that.)
- The PROMQL command is a preview feature per the 9.4 docs; Serverless status was not found.
- The docs list as unsupported: explicit matching (`on`, `ignoring`, `group_left`, `group_right`), `and` / `unless`, the `@` modifier, and subqueries. Dividing two different unaggregated metrics returns no results rather than an error. These are the P1 to P5 probes (untested).
- After `rate()`, unaggregated Elastic rows still show `__name__` in `_timeseries`; Prometheus drops it. Unconfirmed whether that is real or a display detail.
- Payment's organic error series is sparse: one hump (about 0.004 for about 4 minutes) in about 30 minutes. The old scripts claim "every few minutes"; that is unsupported. Payment's call rate is about 0.11 to 0.15 per second, so a 25% failure flag would give roughly 0.03 errors per second (inferred; unmeasured).
- The Grafana "Prometheus data source" route and the Prometheus-compatible query endpoints are mentioned in the docs and untested. They might allow a literally unmodified query.

## 4. Plan

Three videos, one per learning objective, slower and friendlier than the original single script:

| Video | Objective | Content |
|---|---|---|
| 1 | LO1 Recognize | Same expression in Prometheus and Elastic: selector, `rate()`, `sum by` (about 5 minutes) |
| 2 | LO2 Apply | A ladder from raw metric to arithmetic and the error ratio (R1 to R8), possibly ending on the payment incident |
| 3 | LO3 Analyze | Where Elastic differs: picker-width and `increase()`, implicit versus fixed windows, unsupported constructs with real error text, preview status |

Slides use the shapes in `slide-narrative-guidance.md` (the author's rules for the slide toolkit). Likely: Video 1 opener is Shape A, recap is Shape C. The slide plugin skills (`slide-narrative-writer`, `slide-spec-translator`, `kokoro-script-converter`, `elastic-card-slides`) existed in the original chat's sandbox; a new account may not have them, which is why the guidance is saved in the repo.

**Order of work:** (1) author runs R2, R5, R7, R8 and shares results; (2) decide the open items below; (3) write Video 1's narration against the guidance, with the Q&A learning loop; (4) slides, scratch recording, final; (5) repeat for Videos 2 and 3, probes first; (6) write the module description last; (7) sweep older docs (README tagline, cheatsheet, demo script, LO doc) for absolute claims.

## 5. Open decisions (author's call unless noted)

1. **Where `increase()` goes.** Recommendation: move it to Video 3 (boundary behavior). LO1 currently names `increase()`.
2. **LO wording.** Proposals are in the status doc, item 14: remove "no syntax changes" from LO1; replace "vector matching" in LO2 with arithmetic and implicit matching; make explicit matching a documented gap in LO3. The root chat owns the curriculum doc.
3. **Recording workflow.** Recommendation: record the screen first, then write or time the narration, because typing time varies.
4. **Capture on the desktop,** and whether the Windows browser reaches WSL's `localhost:9090`.
5. **Remote-write endpoint.** Elastic's docs now recommend the Managed Prometheus Remote Write endpoint for Serverless; this track uses the direct endpoint. Matters for Module 2.
6. **Instruqt.** Its setup script in `environment-setup-guide.md` still assumes an unrestricted key and runs plain `docker compose up` (no Prometheus or Grafana). Needs fixing before any lab.
7. **Incident demo.** Whether and where it appears depends on measuring the real spike and the baseline; do not promise "real-time error rate detection" until tested.
8. **Stale figures.** The cheat sheet says "19 services" (actual: 18). Sizing numbers tied to 30 containers are stale.

## 6. Practical notes

- **Docs page:** `https://www.elastic.co/docs/reference/query-languages/esql/commands/promql` is about 2 MB. Fetch it with `curl` in the sandbox and extract text with a short Python snippet instead of reading it whole.
- **Downloads:** browsers drop files that start with a dot. Deliver such files as commands or zips of normal files.
- **File delivery pattern:** the assistant builds a zip of changed repo files with repo-relative paths; the author unzips at the repo root, checks `git status -sb` and `git diff --stat`, runs the key safety grep, commits, and pushes. Pull on the desktop with `git pull --ff-only`.
- **Starting a new chat:** upload a clean repo archive made with `git archive --format=zip --output=prometheus-to-elastic-repo.zip HEAD` (tracked files only; no demo folder, no secrets), then paste the starter prompt below.

## 7. Starter prompt for the new chat

> I'm continuing Module 1 of a Prometheus-to-Elastic training track. I've attached a zip of the repo. Please read `docs/handoff-2026-10-20-module1-continuation.md` first, then the files it lists, and then tell me (a) what you understand the current state to be, (b) what you need from me, and (c) the one next step you'd take. I'm not a PromQL specialist and I'll ask a lot of questions while we write the narration. I want everything explained clearly and nothing left to the imagination.
