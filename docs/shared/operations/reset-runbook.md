# Setup and reset runbook (v2.2)

**Status:** v2.2, October 28, 2026. It applies the findings of the first run (`docs/shared/operations/retro-runbook-first-run.md`) except the automation track, plus what the Video 1 rehearsal found (the compaction warning and the weak `gap` check). Owned by the root chat (shared file). Video chats read it and never edit it.
**How to read the marks:** every command here ran on the author's laptop on Oct 26 unless it carries the mark **(new)**, which means it is a new form that has not run yet. The next run tests those.
**If something differs from what a step says to expect, stop and paste it to the root chat.**

## Conventions

- **Never paste an API key or the contents of `.env.elastic` into a chat.** Show output with the key cut off.
- **Never run a bare `git diff` in the demo folder.** The generated Prometheus config holds the key. Use `git diff --stat` or a named file that holds no secret.
- **Never run `docker system prune`, `docker volume prune` or `docker image prune -a` on this laptop** (section 0 says why).
- The repo is at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`. Docker commands run from its `opentelemetry-demo` folder.
- "The compose command" means `docker compose -f compose.yaml -f compose.observability.yaml`, always run from the demo folder.
- **Times:** Kibana's Dev Tools and Prometheus's `date -u` show UTC. Discover shows the browser's zone. The author is on CDT (UTC minus 5), and on CST (UTC minus 6) from Nov 1.
- **Write down T0** (the time `up` finishes) in the take log. Every uptime is measured from it.

---

## 0. Known facts about this laptop

| Item | Value |
|---|---|
| Docker Desktop settings | Memory 16 GB, CPUs 14, swap 1 GB, **Disk usage limit 926 GB** (Settings, Resources). Docker reports slightly less memory than the setting: 16 GB reports about 16.7 billion bytes; a 12 GB setting reports about 12.5 billion. The README's minimum is 12 GB |
| Other projects' Docker state | About 70 images, 5 stopped containers and 77 volumes from earlier work (for example `prom-demo_grafana-storage`). Not ours |
| Docker cleanup that is allowed | `docker image prune` (dangling images), `docker builder prune`, and `docker rmi` of old versions of this stack's own images. Pipe the output through `\| tail -3` |
| Docker cleanup that needs the author's review | Any other image, and every volume. List what is old first: `docker images --format 'table {{.Size}}\t{{.CreatedSince}}\t{{.Repository}}:{{.Tag}}' \| tail -25` |
| Docker cleanup that is never run | `docker system prune -a --volumes`, `docker volume prune` |
| Demo version | Tag `3.0.0`, pinned. The payment service fails to start on `latest` |
| Ingest path | The direct Elasticsearch remote-write endpoint, `/_prometheus/api/v1/write`. Elastic's docs recommend the managed Prometheus Remote Write endpoint for Serverless; the author chose to stay direct for Module 1 (register row 52) |

---

## Part A: one-time setup (once per machine)

### A0. Account checks (recommended; you may skip)

A precaution after the desktop incident, not a diagnosis. A new key does not help if the account that issues it is compromised. From the laptop, in a browser:
- GitHub: Settings, Security log; SSH and GPG keys; personal access tokens.
- Elastic Cloud account: active sessions, and any API keys you did not create.
- Passwords typed in the Chrome that was glitching: consider changing the important ones.

**Expect:** nothing you do not recognize. If something looks wrong, stop and tell the root chat before creating any credential.

### A1. The Elastic project (create or reuse)

Reuse your existing Serverless Observability project if you have one. Create a new one (Observability Complete) only when none exists. This is the one step that cannot be scripted.

Write down the project **name**, **region** and **Elasticsearch endpoint**. In the console, use the entry labelled Elasticsearch. It looks like `https://<project>.es.<region>.<provider>.elastic.cloud`. The console may show `:443` after it. The port is optional, and the script strips it. **Do not use** the `ingest` host form (it ends in `:443/_es`) or the managed Prometheus endpoint.

If you reuse a project, check it first (Kibana, Dev Tools, read-only):

```
GET /_security/api_key
GET _data_stream/metrics-generic.prometheus-default
```

**Expect:** a list of keys (names and ids, never secrets) and either the data stream or a not-found error. Retire (invalidate) keys you do not recognize or no longer use, in Kibana's API keys page. Give the root chat the name, region and endpoint (never a key) so the handoff can record them.

### A2. Host checks (read-only)

Docker Desktop must be running first.

```
sysctl -n hw.memsize | awk '{printf "%.0f GB RAM\n", $1/1024/1024/1024}'
docker info --format 'Docker has {{.MemTotal}} bytes and {{.NCPU}} CPUs'
df -h ~ | tail -1
docker system df
```

**Expect:**
- **RAM:** the laptop's total (48 GB here).
- **Docker:** about 16.7 billion bytes (16 GB) and at least 4 CPUs (14 here). Under about 12.5 billion bytes, raise it in Settings, Resources, and tell the root chat what you set.
- **`df`:** plenty of free space on `/System/Volumes/Data` (628 GiB free here).
- **`docker system df`:** compare its total with Docker Desktop's **Disk usage limit** (926 GB here), not with the Mac's free space. Docker keeps all its images inside its own disk image, and that limit is the cap that matters.

### A3. The demo folder

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic
ls -ld opentelemetry-demo
```

**If it does not exist** (a fresh machine), clone and pin it:

```
git clone --depth 1 --branch 3.0.0 https://github.com/open-telemetry/opentelemetry-demo.git
sed -i '' 's/^DEMO_VERSION=latest/DEMO_VERSION=3.0.0/' opentelemetry-demo/.env
grep -n "^DEMO_VERSION" opentelemetry-demo/.env
```

The `sed` is **(new)** as a fresh-clone step. **Expect** `4:DEMO_VERSION=3.0.0`. A fresh clone of the tag reads `latest`, and `apply-config.sh` refuses to run until it reads `3.0.0`.

**If it already exists** (a leftover folder), look before reusing it:

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic/opentelemetry-demo
grep -n "DEMO_VERSION" .env
git log -1 --format='%h %ad %d' --date=short
git status -sb --untracked-files=all
ls -l src/prometheus/
git diff .env
docker ps -a --format '{{.Names}}' | grep -c -E '^(prometheus|grafana|jaeger|opensearch|otel-collector|flagd|flagd-ui|frontend|frontend-proxy|kafka|postgresql|valkey-cart|payment|checkout|cart|currency|email|accounting|ad|quote|shipping|recommendation|product-catalog|image-provider|fraud-detection|load-generator|opamp-server)$'
```

**Expect:**
- `DEMO_VERSION=3.0.0`, and `1755859 2026-07-24 (grafted, HEAD, tag: 3.0.0)`.
- `git status`: only ` M .env`, ` M compose.observability.yaml` and ` M src/prometheus/prometheus-config.yaml`, and **no `??` lines**. The full list matters: `--untracked-files=all` and no `head`.
- `git diff .env`: one change, `DEMO_VERSION=latest` to `3.0.0`.
- The last command prints `0`. A higher number means a leftover container name that would collide.

**Tidy anything extra.** Look at the dates and modes first (`ls -l`). A `.bak` or `.tmp` copy of the generated config can hold an old key, and can be readable by other users. Delete them. If `src/flagd/demo.flagd.json` shows modified, it is usually only a missing trailing newline; restore it with `git checkout -- src/flagd/demo.flagd.json`.

### A4. `.env.elastic` and the key

**The file comes first, so the key has somewhere safe to go.**

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic
cp config/.env.example .env.elastic
sed -i '' 's|^ES_ENDPOINT=.*|ES_ENDPOINT=https://<project>.es.<region>.<provider>.elastic.cloud|' .env.elastic
git check-ignore -v .env.elastic
cat -n .env.elastic
```

Replace the URL with your endpoint. **Expect:**
- `git check-ignore -v` prints one line that starts with `.gitignore:` and ends in `.env.elastic`. If it prints nothing, stop.
- `cat -n` shows your endpoint with no path, and an `ES_API_KEY=` line that still holds a placeholder or nothing. Your file may have the template's eight lines or only two. Both are fine.

**Create the key.** In Kibana, Dev Tools:

```
POST /_security/api_key
{
  "name": "prometheus-remote-write",
  "role_descriptors": {
    "prw_writer": {
      "indices": [
        { "names": ["metrics-*"], "privileges": ["auto_configure", "create_doc"] }
      ]
    }
  }
}
```

**Expect:** JSON with `id`, `name`, `api_key` and `encoded`. The `encoded` value is shown **once**. The key has **no expiry**: an expiring key would stop the data in the middle of a project. Revoke it when the project ends.

**Put the key in the file without showing it.** Copy only the `encoded` value, with no quotes, then:

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic
sed -i '' "s|^ES_API_KEY=.*|ES_API_KEY=$(pbpaste)|" .env.elastic
pbcopy < /dev/null
chmod 600 .env.elastic
```

**Expect:** no output. The second command clears the clipboard, and the third restricts the file to you.

**Check it without showing it:**

```
awk -F'=' -v q="'" '/^ES_API_KEY=/{k=substr($0,index($0,"=")+1); l=length(k); first=substr(k,1,1); last=substr(k,l,1); printf "length %d | first char is a quote: %s | last char is a quote: %s | contains whitespace: %s\n", l, (first=="\""||first==q)?"YES":"no", (last=="\""||last==q)?"YES":"no", (k ~ /[ \t]/)?"YES":"no"}' .env.elastic
ls -l .env.elastic
git status -sb
```

**Expect:** `length 60` (roughly 60 or more), and `no` three times. Then a line starting `-rw-------`. Then `## main...origin/main` and nothing else. A `YES`, or a length of `0`, means the paste went wrong: repeat from "Create the key".

### A5. Generate the Prometheus config

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic
./scripts/apply-config.sh
```

**Expect** six lines, in this order:
1. `Wrote .../opentelemetry-demo/src/prometheus/prometheus-config.yaml`
2. `Remote-write URL: https://<project>.es.<region>.<provider>.elastic.cloud/_prometheus/api/v1/write` (no port)
3. `API key:          XXXX... (60 chars)` (the first four characters are harmless to paste)
4. `Base endpoint:      HTTP 403` (200 is fine too: a write-only key may be refused at the cluster root)
5. `Write endpoint GET: HTTP 405` (the write endpoint accepts POST only)
6. `OK: endpoint reachable. Data arriving in Elastic after the stack starts is the real test.`

A `WARNING` line is the signal to stop: `401` means the key was rejected, `000` means it could not connect, and any code other than `405` on the write endpoint means the path is wrong.

### A6. Pull and start

First see which images will be pulled:

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml config --images | sort
docker compose -f compose.yaml -f compose.observability.yaml config --images | grep -c 'ghcr.io/open-telemetry/demo:3.0.0-'
docker compose -f compose.yaml -f compose.observability.yaml config --images | grep -i -c 'latest'
```

**Expect:** 24 distinct images. **18** of them are `ghcr.io/open-telemetry/demo:3.0.0-<service>`, and **0** are tagged `latest`. The third-party images were: flagd v0.16.0, collector contrib 0.157.0, valkey 9.0.4, grafana 13.1.0, postgres 18.4, jaeger 2.19.0, prometheus v3.13.1.

Then pull and start:

```
date
docker compose -f compose.yaml -f compose.observability.yaml pull --quiet
date
docker compose -f compose.yaml -f compose.observability.yaml up --detach
date
sleep 60
docker compose -f compose.yaml -f compose.observability.yaml ps --format "table {{.Name}}\t{{.Status}}"
```

**Expect:**
- **`pull`:** seconds when the images are cached (3 s on the first run), minutes on a machine that has never pulled them.
- **`up`:** about 30 seconds. Docker shows only about 21 lines ("... 5 more"), so the `ps` after it is what counts.
- **`ps`:** 25 rows, each `Up`, most `(healthy)`. Six have no health label (cart, flagd, grafana, jaeger, otel-collector, prometheus). `health: starting` right after `up` is normal.
- **T0** is the third `date`. Write it down.

Then check restarts:

```
docker inspect --format '{{.Name}} restarts={{.RestartCount}} started={{.State.StartedAt}}' $(docker ps -q) | grep -v 'restarts=0'
```

This combined form is **(new)**. **Expect:** nothing, or `product-catalog` with a start time within about a minute of T0 (UTC). That is the known startup race, and it is accepted.

### A7. Verify that data flows

**1. Prometheus can read its config.**

```
docker logs prometheus --tail 30 2>&1 | grep -i "permission denied"
```

**Expect:** no output. On Docker Desktop for Mac, the script's mode 600 is fine. On a Linux host it breaks Prometheus: then `chmod 644 src/prometheus/prometheus-config.yaml` and `docker restart prometheus`.

**2. Prometheus is sending** (a minute apart):

```
for i in 1 2; do date; curl -s http://localhost:9090/metrics | grep -E '^prometheus_remote_storage_samples_(total|failed_total|retried_total|pending)' | sed 's/{[^}]*}//'; sleep 60; done
```

**Expect:** `samples_total` grows by about 60,000 in the minute (about 1,000 a second early on; the rate ramps to about 3,000 later). `failed` and `retried` stay at `0`. `pending` is a few thousand, not zero: it is the batching queue, not a backlog.

**3. Elastic created the data stream** (Dev Tools, in UTC):

```
GET _data_stream/metrics-generic.prometheus-default
```

**Expect:** `index_mode: time_series`, template `metrics-prometheus@template`, status `GREEN`, one backing index (`.ds-metrics-generic.prometheus-default-<date>-000001`), and `failure_store.indices` empty. **Write down the `index_uuid`.** The `temporal_ranges` start about two hours before the stream was created; that is normal.

**4. Elastic holds the data** (Discover, ES|QL mode, in the browser's zone):

```
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

**Expect:** `MIN(@timestamp)` within seconds of T0, `MAX(@timestamp)` within the last minute, and a `COUNT(*)` that grows each time (about 200,000 four minutes in, about 386,000 at seven). Do not expect the count to equal the samples Prometheus reports.

### A8. Keep the laptop awake, and warm up

In a **separate terminal tab**, with the charger in and the lid open:

```
caffeinate -dims
```

**Expect:** the command keeps running and prints nothing. Stop it with Control-C when you are done for the day. A sleeping laptop pauses the stack and leaves gaps in the data.

Wait the warm-up the video's contract asks for (at least 45 minutes), then run **Part C**.

---

## Part B: the per-video reset

Do this before every rehearsal and every take, so no video depends on another's data.

### B1. Read the video's stack state

Section 6 of the video's contract gives the minimum warm-up (minutes) and the state of the `paymentFailure` flag. Write both down.

### B2. Stop the stack and delete its local data

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic/opentelemetry-demo
date
docker compose -f compose.yaml -f compose.observability.yaml down --volumes --remove-orphans
date
docker ps --format '{{.Names}}' | wc -l
docker volume ls --filter label=com.docker.compose.project=opentelemetry-demo -q | wc -l
```

**Expect:** about 15 seconds (14 on the first run), with lines such as `Container prometheus Removed` (Docker shows only about 21 lines). Then `0` and `0`: no containers running, and none of this project's volumes left. Stopping first matters, so nothing writes to Elastic while you delete.

The volume check filters by the compose project label on purpose. A name search once matched another project's volume (`prom-demo_grafana-storage`). If the last number is above 0, run `docker volume ls --filter label=com.docker.compose.project=opentelemetry-demo` and tell the root chat before removing anything.

### B3. Check that nothing is still writing, and record the old uuid

In Discover (ES|QL), run this twice, at least 30 seconds apart:

```
FROM metrics-generic.prometheus-default
| STATS MAX(@timestamp), COUNT(*)
```

**Expect:** the same `MAX(@timestamp)` and the same `COUNT(*)` both times, with the newest timestamp about when `down` began. **If the count rises, stop.** Something else is writing: another stack, an old container, or another machine.

Then, in Dev Tools:

```
GET _data_stream/metrics-generic.prometheus-default
```

**Expect:** the data stream, with one backing index. **Write down its `index_uuid`**, because B6 compares against it.

### B4. Delete the data stream (its own step)

In Dev Tools, which runs under your own login (the write-only key cannot delete):

```
DELETE _data_stream/metrics-generic.prometheus-default
```

**Expect:** `{"acknowledged": true}`. Use the exact name, never a wildcard such as `metrics-*`. It removes the data stream and every backing index, and it cannot be undone. It is safe here, because B3 showed nothing is writing.

### B5. Restart

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic/opentelemetry-demo
date
docker compose -f compose.yaml -f compose.observability.yaml up --detach
date
sleep 60
docker compose -f compose.yaml -f compose.observability.yaml ps --format "table {{.Name}}\t{{.Status}}"
docker inspect --format '{{.Name}} restarts={{.RestartCount}} started={{.State.StartedAt}}' $(docker ps -q) | grep -v 'restarts=0'
```

**Expect:** the `up` takes about 30 seconds and creates the network and fresh volumes. After a minute, 25 rows, each `Up`. The restart line (the combined **(new)** form from A6) prints nothing, or `product-catalog` within about a minute of T0 (the startup race). **T0 is the second `date`.** Write it down. Restart `caffeinate -dims` if it is not running (A8).

### B6. Prove the reset worked

**1. Prometheus is sending** (the counters loop from A7, step 2). **Expect:** `samples_total` restarted from a low number and grows; `failed` and `retried` are `0`.

**2. Elastic holds only new data** (Discover, ES|QL, in the browser's zone):

```
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

**Expect:** `MIN(@timestamp)` **later than the time `up` began**. That proves none of the earlier documents survived. `MAX(@timestamp)` is within the last minute, and `COUNT(*)` is small and growing (about 200,000 four minutes in).

**3. Elastic made a new index** (Dev Tools):

```
GET _data_stream/metrics-generic.prometheus-default
```

**Expect:** the same name and template, one backing index (the name repeats because it is date-based), **an `index_uuid` that differs from the one you wrote down in B3**, status `GREEN`, and `failure_store.indices` empty. A changed uuid is the strongest proof that the old index was deleted.

If `MIN(@timestamp)` is earlier than the restart, or the uuid is unchanged, **stop and tell the root chat**: the delete missed.

### B7. Set the flag state

Open `http://localhost:8080/feature` and set `paymentFailure` as the contract says. For a video that needs it on, note the time you switched it on. **Expect** the default, `off` with state `ENABLED`, when the contract says off. Its effect is unmeasured, so a video chat measures it in the rehearsal. The demo's `"90%"` variant has the value `0.95`, not `0.9`: check it before any claim.

### B8. Warm up

Wait the number of minutes in the contract, with `caffeinate -dims` running. At least 45 minutes after a reset. Then run **Part C**. Do not record before then.

---

## Part C: pre-roll (before a take, and at the end of every warm-up)

C1 and C2 ran unchanged on macOS on Oct 26. C3 uses the combined restart command marked **(new)** in A6.

**C1. Uptime and the flag service**

```
date -u; docker ps --format '{{.Names}}: {{.Status}}' | grep -E 'prometheus|flagd'
```

**Expect:** the current UTC time, then `flagd`, `flagd-ui` and `prometheus` all `Up`, with an uptime at least as long as the contract's minimum.

**C2. Remote-write counters**

```
date -u; curl -s http://localhost:9090/metrics | sed 's/{[^}]*}//' | awk '/^prometheus_remote_storage_samples_failed_total/{f=$2} /^prometheus_remote_storage_samples_retried_total/{r=$2} /^prometheus_remote_storage_samples_pending/{p=$2} /^prometheus_remote_storage_samples_in_total/{i=$2} /^prometheus_remote_storage_samples_total/{t=$2} END{printf "failed %s | retried %s | pending %s | in %.0f | sent %.0f | gap %.0f\n", f, r, p, i, t, i-t}'; docker logs prometheus 2>&1 | grep -cE 'level=(WARN|ERROR)'
```

**Expect:** `failed 0` and `retried 0` (these are the health checks), and `pending` and `gap` both small (a few thousand, up to about 10,000). **Do not require `gap` to equal `pending`:** it held on one of four readings. The final number counts warning and error lines in Prometheus's log. It is `0`, except for **one** `Overlapping blocks found during reloadBlocks` warning when Prometheus makes its first compaction, about 3 hours after the first sample (seen at 19:10:39 UTC). Remote write is unaffected (`failed` and `retried` stayed 0). The cause is a hypothesis (the 30-minute out-of-order window), and the desktop run's nine warnings are probably the same. After 66 minutes `sent` was about 11.8 million, and at 1 hour 40 minutes about 22.2 million (about 4,800 a second), so do not expect a flat rate.

**C3. Restarts, and the rule for takes**

```
docker inspect --format '{{.Name}} restarts={{.RestartCount}} started={{.State.StartedAt}}' $(docker ps -q) | grep -v 'restarts=0'
```

**Expect:** nothing. If a container appears, compare its `started` time (UTC) with T0:
- **Within about a minute of T0:** the startup race. Accept it. `product-catalog` did this on both stacks.
- **Later:** a mid-run restart. Write the container and the time in the take log. If it happened in the **last 10 minutes before the take, reset (Part B) and warm up again.** If earlier, accept it.

Capture the facts now. A container's console log can be empty (`checkout` writes nothing), and `docker events` held nothing for a restart an hour earlier. To rule out memory, `docker inspect --format '{{.Name}} oomkilled={{.State.OOMKilled}}' <name>` should print `false`.

**C4. The flag**

At `http://localhost:8080/feature`, confirm `paymentFailure` matches the contract: off for Video 1, as measured for Video 2, off for Video 3. (`http://localhost:8080/feature/advanced` returns the same flags as JSON, a candidate for a scripted check.)

**After the take,** run C2 again. `failed` should be unchanged from before the take.

---

## Expected values from the first run (Oct 26)

| Moment | What was seen |
|---|---|
| Pull, cached images | 3 seconds |
| `up` | 30 seconds |
| Reset: stop and wipe | 14 seconds |
| First data in Elastic | 13 seconds after start |
| Two minutes in | about 82,000 samples sent |
| Seven minutes in | 386,321 documents in Elastic |
| Four minutes after a reset | 201,506 documents |
| Send rate | about 956 a second early, about 1,000 at two minutes, about 3,000 on average over 66 minutes, about 4,800 a second at 1 hour 40 minutes |
| 66 minutes in | `failed 0`, `retried 0`, `sent` 11,820,165, 0 warnings or errors. `gap` equalled `pending` there, but only on one of four later readings, so it is not an invariant |
| 1 h 40 min and 3 h 47 min | `failed 0`, `retried 0`; `sent` 22,220,532 and 60,049,606 |
| About 3 hours in | One `Overlapping blocks found during reloadBlocks` WARN at Prometheus's first compaction (19:10:39 UTC, 3.0 hours after the first sample). Remote write unaffected |
| Restarts | `product-catalog` 15 seconds after T0 (startup race); `checkout` 5 minutes 44 seconds after T0 (cause unknown, accepted) |
| Services reported by Prometheus | 17 in one snapshot about 70 minutes in, 18 during the Video 1 rehearsal, 18 in the lab; the reference file says 19. No video states a service count |

## If something goes wrong

| What you see | Likely cause | What to do |
|---|---|---|
| `ERROR: DEMO_VERSION ... is not 3.0.0` from the script | The demo's `.env` still reads `latest` | Run the pin step in A3 |
| `401` on the base endpoint | The key was rejected | Check `ES_API_KEY` (A4), or create the key again |
| `000` from the script | No connection, or a wrong endpoint | Check `ES_ENDPOINT` and the network |
| The write endpoint is not `405` | The endpoint path is wrong | Use the base `.es.` endpoint, not the `ingest` form |
| `port is already allocated` | Another program holds that port | Paste the line; do not stop other projects' containers |
| `permission denied` in Prometheus's log | A Linux host with the script's mode 600 | `chmod 644 src/prometheus/prometheus-config.yaml`, then `docker restart prometheus` |
| `no space left on device` | Docker's disk image is full | Compare `docker system df` with the Disk usage limit; clean only what section 0 allows |
| The count rises with the stack down (B3) | Something else is writing | Stop. Find the other sender before deleting |
| `410 api_not_available_exception` in Dev Tools | That API exists but is not available on Serverless (seen on the field-mapping API) | Use another form. `GET _data_stream/...` and `DELETE _data_stream/...` work. A `410` is not a mistake in your command |
| `failed` or `retried` rising | A key, endpoint or network problem | Check `ES_API_KEY` and the failure store in A7 step 3 |

## Version history

- **v1 (Oct 25):** the first runbook. Tested only on Linux for the pre-roll.
- **v2 (Oct 26):** applies the first run on the laptop: the key after the file, a leftover-folder path, the version pin, Docker memory and disk guidance, the cleanup rules, a project-label volume check, the "still writing?" check, the uuid and restart-time proofs, and the restart rule for takes.
- **v2.1 (Oct 27):** `gap` equal to `pending` is no longer required; the first-compaction warning is allowed; the `/feature/advanced` note; corrected restart timing and service count; later `sent` readings.
- **v2.2 (Oct 28):** a Serverless `410` row in "If something goes wrong".
