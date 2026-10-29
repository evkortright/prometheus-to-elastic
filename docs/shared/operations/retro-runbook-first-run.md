# Runbook first run — retrospective

**Status:** Raw list, written during and just after the first run on Oct 26, 2026, before the retrospective itself. Owned by the root chat.
**What this is:** every finding from the first run of `docs/shared/operations/reset-runbook.md` (Parts A, B and C) on the laptop, with the facts of the run. The plan for the runbook revision is grouped at the end. Nothing here has been applied to the runbook yet.
**Result:** Parts A, B and C each ran once and passed, and the warm-up completed (66 minutes of clean remote write). One container restart mid-run is unexplained (entry 76). **Runbook v2 (Oct 26) applies every group except the automation track.**

## 1. Facts of the run (Oct 26, 2026; times are CDT, UTC minus 5)

| Item | Value |
|---|---|
| Elastic project | Serverless Observability, Azure Central US (Iowa), name `my-observability-project-b04674` |
| Elasticsearch endpoint | `https://my-observability-project-b04674.es.centralus.azure.elastic.cloud` (the console also showed a `:443` form and an `ingest` host form ending `/_es`) |
| Ingest path | The direct Elasticsearch remote-write endpoint, `/_prometheus/api/v1/write`. Decided by the author for Module 1. Elastic's docs recommend the managed Prometheus Remote Write endpoint for Serverless (register row 52) |
| Key | `prometheus-remote-write`, write-only (`auto_configure`, `create_doc` on `metrics-*`), 60 characters, stored only in `.env.elastic` (mode 600) |
| Docker Desktop | Memory 16 GB (16,745,295,872 bytes reported), 14 CPUs, swap 1 GB, **Disk usage limit 926.35 GB** |
| Demo | Tag 3.0.0, commit `1755859`, reused from Oct 19 after tidying (`.bak` and `.tmp` files deleted) |
| Images | 24 distinct: 18 demo images at `3.0.0-<service>`, none tagged `latest`. Third party: flagd v0.16.0, collector contrib 0.157.0, valkey 9.0.4, grafana 13.1.0, postgres 18.4, jaeger 2.19.0, prometheus v3.13.1 |
| Stack start 1 | `up` finished 10:55:04 (T0 about 10:55). First data in Elastic 10:54:47 |
| Reset | `down --volumes` 11:04:15 to 11:04:29 (14 s). Data stream deleted (acknowledged). `up` 11:10:25 to 11:10:56 (31 s) |
| Stack start 2 (the warm-up) | T0 **11:10:56**. The 45-minute warm-up ended 11:56 |
| End-of-warm-up check | 12:16:52 (uptime 66 minutes): `failed 0`, `retried 0`, `pending 3,757` equal to the gap, `in` 11,823,922, `sent` 11,820,165 (about 2,990 a second on average), 0 warning or error lines in Prometheus's log |
| Restarts | `product-catalog`: started 11:11:11 (15 s after T0, a startup race, as in the first stack). `checkout`: started 11:16:40 (5 min 44 s after T0, mid-run, cause unknown). Neither was OOM-killed. `checkout` writes nothing to its console, and Docker's event history returned nothing for that minute |
| Not yet checked | The "overlapping blocks" warning at Prometheus's first compaction (about 2 to 3 hours in; about 2:15 PM CDT if the stack stays up) |
| Elastic data, first stack | 386,321 documents at 11:01:54; 585,723 at 11:04:14 (nothing written after the stop) |
| Elastic data, after the reset | `MIN(@timestamp)` 11:10:38 (later than the restart began at 11:10:25); 201,506 documents at 11:14:48 |
| Data stream `index_uuid` | Before the reset `mavGBVpJT2mzg1cFOeChKg`; after `jJEpJ5oKTwuqdS1D4bfzmQ` (same index name, new uuid) |
| Send rate | about 956 samples a second at 3 minutes; 60,016 samples in one minute at about 2 minutes after the reset |
| Remote-write counters | `failed 0`, `retried 0` throughout. `pending` 1,427 to 3,893, and `in` minus `sent` equals `pending` (batching, not a backlog) |
| Prometheus log | 0 warning or error lines, 7 minutes in |
| Flag | `paymentFailure` default `off`, state `ENABLED`. Its "90%" variant has the value 0.95 |
| Cleanup | `docker image prune`, `docker builder prune` and eight old demo-image `rmi`: images 111 to 70, about 11 GB freed. Volumes (77) untouched |
| Leftovers on this laptop | Other projects' containers (8 to 11 months old), images and 77 volumes, including `prom-demo_grafana-storage` (Oct 1). Never prune them |

## 2. Findings (numbered in the order found)

### Part A: one-time setup

1. A1 assumes a brand-new project. The reuse path was improvised.
2. The handoff recorded the project as deleted. Section 4 needs the new project's details.
3. A1 describes the endpoint as a `.es.` base URL, but the console showed a port and also an `ingest` host form.
4. Elastic's docs now recommend the managed Prometheus Remote Write endpoint for Serverless. Our README, script and runbook use the direct endpoint. The author decided to stay direct for Module 1 and take up the managed path in Module 2.
5. The runbook should say to drop the port if the console shows one (revised by 24: the port is optional).
6. The runbook creates the key before the file that holds it. The file should come first.
7. Editing `.env.elastic` by hand in nano is error-prone. Give the `cp` and `sed` commands.
8. Run `cat -n .env.elastic` before and after, so a malformed file shows up at once.
9. The runbook needs a safe way to put the key in the file without displaying it (the clipboard route used here).
10. State the `encoded` value's rough length (60 here), and give the safe write and check commands.
11. Consider an expiration on the key, so a forgotten lab key does not live forever. It costs a stop in the middle of a project when it expires.
12. `chmod 600 .env.elastic` after the key is written.
13. Docker Desktop must be running before A3.
14. The memory threshold in bytes was too strict, because Docker reports less than the allocation (a 12 GB setting showed 12,525,842,432 bytes).
15. A4 assumes there is no demo folder. It needs a "leftover demo folder" path: version, git state, config age, containers and volumes.
16. **Confirmed:** after a fresh clone, the demo's `.env` reads `DEMO_VERSION=latest`. README step 1 and runbook A4 are wrong. A4 must include the pin (`sed -i '' 's/^DEMO_VERSION=latest/DEMO_VERSION=3.0.0/' .env`, then the grep). Otherwise A6 stops.
17. **Revised:** the flag file differed only by a missing trailing newline, so no flag-reset step is needed beyond the pre-roll's flag check.
18. Never run a bare `git diff` in the demo folder. The generated config holds the key.
19. The Docker host has unrelated old containers and volumes. Never prune. Check only for name collisions.
20. Stale `.bak` files can hold old keys. Delete them. `apply-config.sh` could refuse to leave them behind.
21. A4's inspection used `head -8` and hid a file. Use `git status -sb --untracked-files=all`.
22. The earlier hand-made setup left a `.tmp` file next to the config. List every untracked file and delete stale copies of the generated config.
23. That `.tmp` was dated Aug 13 and mode 644. A leftover folder can predate the last attempt by months, and files can be world-readable. Check dates and modes.
24. The script accepts a port and a full write URL (it strips `:443`). The template's "no path, no port" is stricter than the script.
25. Read Docker's memory from `docker info`. It should be 16 GB on this laptop. Record pull and start durations.
26. A7 should start with "which images will be pulled?" (`docker compose ... config --images | sort`).
27. A7a's expected result: 24 images, 18 of them demo images at 3.0.0, none tagged `latest`. Handoff section 4 should record the third-party versions.
28. A3 lacks a disk-space check.
29. **Revised:** A3's disk guidance should name Docker Desktop's **Disk usage limit** (926 GB here), not a "virtual disk limit". The worry about a small cap was a guess.
30. **Revised:** A3 should compare Docker Desktop's disk usage limit with the `docker system df` total, not the Mac's free space. The "40 GB" guess is withdrawn.
31. List this laptop's other-project Docker leftovers (111 images, 77 volumes) as a known condition, with "never prune" beside it.
32. Define the allowed Docker cleanup: dangling images and the build cache are safe, images and volumes need the author's review, and `system prune -a --volumes` is never run on this machine.
33. Before any cleanup, list what is old and sort it into ours, dangling and others. State the safe commands and the forbidden ones.
34. The prune output was very long to paste. Add `| tail -3` to cleanup commands.
35. First-run cleanup result: about 11 GB freed, 111 images to 70. Dangling images and old demo versions were the safe ones.
36. The pull took 3 seconds because the images were cached from Oct 19. Record both: a first-ever pull takes minutes, a cached one seconds.
37. `docker compose up` shows only the first ~21 lines ("... 5 more"). Always follow `up` with `ps`.
38. Write down T0 (the time the stack started) and put it in the take log's header.
39. A7a expects 24 images while `up` shows 25 services. Say "25 services, 24 distinct images" (one image is shared; to confirm).
40. A8 passed without the chmod fix on macOS (confirmed by A9). The runbook's "chmod 644 if you see permission denied" is for Linux. Make it conditional, and keep `apply-config.sh` as it is.
41. After `up`, run a restart-count check (`product-catalog` restarted once in the first stack).
42. Record the first-run numbers for comparison (see section 1).
43. A9's expected output should note that `samples_dropped_total` may not appear.
44. A9 should include the Dev Tools `GET _data_stream/...` check for `index_mode: time_series`.
45. A9 should check the data stream itself: `time_series`, template `metrics-prometheus@template`, status GREEN, one backing index.
46. A9 should include the failure store check (`failure_store.indices` empty), a free diagnostic for dropped documents.
47. Elastic output is in UTC. The author is UTC minus 5, and minus 6 from Nov 1.
48. Discover showed the browser's zone (`-05:00`) while Dev Tools showed UTC. Say which to trust.
49. A9 should not promise that Prometheus samples equal Elastic documents. Check the trend, `failed = 0` and an empty failure store.

### Part B: the per-video reset

50. B2 should end with a running-container count, so a failed stop is caught before the delete.
51. B3 should start with the "is anything still writing?" check (two identical counts with the stack down).
52. B2 should verify that the volumes are gone, because Docker's display cuts off after about 21 lines.
53. First-run timing: stop and wipe took 14 seconds.
54. B3's separate "check the name" is redundant once the "is anything still writing?" query has worked. Merge them.
55. Verify the project's volumes are gone with a command expecting `0`, and say what to do if it is not (inspect before removing).
56. Label which command produces which output in B3, and make the delete its own step.
57. The volume check must filter by the compose project label, not grep a name. Other projects' volumes can match (`prom-demo_grafana-storage`).
58. B5's proof should compare `MIN(@timestamp)` with the restart time, which is stricter than the delete time.
59. List the laptop's older leftovers: the `prom-demo` Grafana volume (Oct 1), and older images and containers.
60. B4 should say to wait a minute before `ps`. `health: starting` rows right after `up` look like trouble but are not.
61. B5 should compare the data stream's `index_uuid` before and after the reset. Record the uuid before B3.
62. First-run timing: `up` took 31 seconds from cached images.
63. B5 passed all three checks (timestamp, uuid, counters). The changed uuid is the strongest proof.

### Part C and later

64. Expected `pending` is a few thousand, not zero, at about 1,000 samples a second. The real health checks are `failed` and `retried` at 0, and `in` minus `sent` equal to `pending`.
65. Expected document count about four minutes after a reset is about 200,000, not tens of thousands.
66. Part C works unchanged on macOS. Its first command also lists `flagd-ui`, because the pattern matches both.
67. The demo's `paymentFailure` "90%" variant has the value 0.95. Verify it before Video 2 makes any claim about the flag (register row 14).

### Warm-up and restarts (after the first run)

71. Expected `sent` after about 66 minutes is about 11.8 million, with a rate that ramps from about 1,000 a second to about 3,000. A flat-rate estimate (2.5 million) was wrong by almost a factor of five. Show the ramp, as the desktop run did (about 1,180 rising to about 2,860).
72. Record each restarted container's `StartedAt`, not only the count, because a count cannot tell a startup race from a mid-run restart.
73. Baseline result: 66 minutes of uptime with zero failed or retried samples and zero warning or error log lines.
74. Run the restart-count check both right after `up` and at the end of the warm-up. `checkout` and `product-catalog` are the two to watch.
75. A restart within about a minute of T0 is a startup race. One later is a mid-run event to investigate. State the rule and give the command (`docker inspect --format '{{.Name}} started={{.State.StartedAt}} restarts={{.RestartCount}} oomkilled={{.State.OOMKilled}}' ...`).
76. `checkout` restarted once mid-run (5 min 44 s after T0). Its cause is unknown: its console log is empty, Docker's events returned nothing, and it was not OOM-killed. Accepted as a known behavior, with entry 79 as the gate for takes.
77. A container's console log can be empty (the demo's services probably log through the OpenTelemetry pipeline). The restart investigation should use `docker events` (the exit code) first and `docker logs` second.
78. `docker events` returned nothing for a restart about an hour earlier, so it cannot be relied on for later investigation. Capture restart facts at the time, with a pre-roll that prints `StartedAt` for any restarted container.
79. The take rule for restarts: within a minute of T0 is a startup race; a later one is recorded in the take log; one in the last 10 minutes before a take means reset and warm up again.
82. (From the Video 1 rehearsal.) "`gap` equals `pending`" is a weak check: it held on one of four readings while `failed` and `retried` stayed 0. Use `failed` and `retried` as the health checks, and say `pending` and `gap` are both small.
83. (From the Video 1 rehearsal.) Prometheus's first compaction, about 3 hours after the first sample, logs one `Overlapping blocks found during reloadBlocks` WARN (19:10:39 UTC on Oct 26). Remote write is unaffected. The "0 warnings" expectation needs an allowance. The cause is a hypothesis (the 30-minute out-of-order window), and the desktop run's nine warnings are probably the same.
84. Correction: `checkout` restarted 5 min 44 s after T0 (11:10:56 to 11:16:40), not 5 min 40 s.
85. `http://localhost:8080/feature/advanced` returns the flag JSON, a candidate for a scripted flag check.
86. The service count was 17 in one snapshot and 18 during the rehearsal (and in the lab): a snapshot, not a count.
87. The send rate was about 4,800 samples a second at 1 hour 40 minutes, so the "ramp to about 3,000" estimate was low. The expected-values table now has both readings.
88. (From the Video 2 work.) Not every Elasticsearch API exists on Serverless: the field-mapping API returned `410 api_not_available_exception`. The runbook's Dev Tools commands (`GET _data_stream/...`, `DELETE _data_stream/...`, the `_security/api_key` calls) all worked, but any new command must be tried on Serverless before it goes into the runbook.
89. (From the author's check, Oct 28.) After a day, the data stream has two backing indices (`...2026.10.26-000001` and `...2026.10.27-000002`), so it rolled over. The runbook's "one backing index" expectation (A7 step 3 and B6) holds on a fresh stack only. The `filter_path` form `GET metrics-generic.prometheus-default/_mapping?filter_path=*.mappings.properties.labels.properties.service_name` works on Serverless where the field-mapping form returns 410, and it showed `labels.service_name` as a keyword with `time_series_dimension: true` in both indices.

### Automation track (raised by the author, Oct 26)

68. After the retrospective, turn the runbook into scripts with PASS or FAIL output and a short run log. Most of Part A's checks, Part B's proofs and Part C are encodable. Keep as human gates: the account checks, key creation, the data stream delete, cleanup choices and the flag decision.
69. AI's role is to write and revise the scripts and to help on exceptions, not to run them unattended. Evaluate Claude Code in Plan or Ask-permissions mode with a PreToolUse hook that blocks destructive commands and logs every call, and Cowork's folder-scoped sandbox. Do not rely on a single layer: a late-2025 public issue reported that deny rules were not enforced (not confirmed fixed).
70. Decide first which credentials a script may hold. A script that checks or deletes in Kibana needs more than the write-only key.
80. Scripting order (the author's view, with a refinement): revise the runbook first, then run it by hand from the revised text a few more times before scripting. Script Parts B and C first, because they run before every video and pay back most. Script Part A last, because it runs once per machine. The one step that cannot be scripted is creating the Serverless project, and the plan is to reuse the existing one. Creating the key needs a privileged credential (entry 70).
81. Jev (TypeSafe AI's first "System One" model, in early access since Sep 15, 2026) returns typed, probabilistic decisions instead of text, for use as a fuzzy rule inside ordinary code. It could fit a script that must classify an unexpected output. Almost all our checks are plain comparisons that need no model. These are the vendor's own claims, not verified here. Revisit only if a real fuzzy decision appears.

## 3. Plan for the runbook revision (grouped)

| Group | Entries | What changes |
|---|---|---|
| Order and secrets | 6 to 12 | The file first, then the key; safe write and check commands; `chmod 600`; the key's length and expiry |
| Project and endpoint | 1 to 5, 24 | A "reuse a project" path; the port is optional; which endpoint form to copy; the ingest-path note |
| Host checks | 13, 14, 19, 25, 28 to 35 | Docker running; memory and disk from the right settings; the allowed and forbidden cleanup; the laptop's known leftovers |
| Leftover demo folder | 15 to 18, 20 to 23 | A path for an existing folder: the version pin, a full untracked-file list, stale `.bak` and `.tmp` files, dates and modes, never a bare `git diff` |
| Pull and start | 26, 27, 36 to 39, 41, 62 | List images first; `up` then `ps`; T0; restart counts; first-run versus cached timings |
| Verification | 40, 42 to 49, 64, 65, 71, 73, 88, 89 | The data stream and failure store checks; UTC versus local time; the right expectations for `pending` and counts |
| Part B | 50 to 61, 63 | The "still writing?" check, the project-label volume check, the uuid and restart-time proofs, labelled outputs |
| Part C | 66, 67, 85 | Macs are fine; the flag command lists two services; check the 0.95 variant before Video 2; a scripted flag check is possible |
| Warm-up and restarts | 71 to 79, 82 to 87 | The ramp in expected volume; restart facts at the time; the startup-race rule; the take gate; the weak `gap` check; the first-compaction warning |
| Automation | 68 to 70, 80, 81 | A separate track, after this revision: Parts B and C first, Part A last |

## 4. Handoff and register updates this run requires

- Handoff section 4: record the project, endpoint, Docker settings and third-party versions (done in the delivery that adds this file, except the versions, which live here).
- Register: row 52 (the ingest-path finding), added with this file.
- Register row 14 (the payment flag's effect) stays open; entry 67 adds the 0.95 observation.
- Handoff tracker row 34: the first run is done and passed, and the warm-up completed. The `checkout` restart is the one open anomaly.
