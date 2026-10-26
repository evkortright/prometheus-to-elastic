# Setup and reset runbook

**Status:** Draft v1, written by the root chat. Not yet run on the laptop. Every step states what you should see; if you see something else, stop and paste it to the root chat.
**Owner:** the root chat (shared file). Video chats read it and never edit it.
**Where this comes from:** the README's "Local setup", `docs/quickstart.md` (including its reset section), the run-sheet's pre-roll, and the observations from the desktop run (handoff section 5). Commands that were only ever run on the desktop's Linux shell are marked "untested on macOS".

There are three parts:

- **Part A: one-time setup.** Done once, ever: the Elastic project, the key, the demo folder, the first start.
- **Part B: the per-video reset.** Done before every rehearsal and every take, so no video depends on another's data.
- **Part C: pre-roll.** Done just before every take.

Rules for all three parts:
- **Never paste an API key or `.env.elastic` into a chat.** Show output with the key cut off.
- The laptop's repo is at `/Users/enriquekortright/personal/projects/prometheus-to-elastic`. Docker commands run from its `opentelemetry-demo` folder.
- The Docker Compose command is always `docker compose -f compose.yaml -f compose.observability.yaml ...` (called "the compose command" below).

---

## Part A: one-time setup

### A0. Account checks (recommended; you may skip)

A precaution after the desktop incident, not a diagnosis. A new key does not help if the account that issues it is compromised. From the laptop, in a browser:
- GitHub: Settings, Security log; SSH and GPG keys; personal access tokens. Look for anything you don't recognize.
- Elastic Cloud account: active sessions, and any API keys you did not create.
- Passwords you typed in the Chrome that was glitching: consider changing the important ones.

**Expect:** nothing you don't recognize. If something looks wrong, stop and tell the root chat before creating any new credentials.

### A1. Create the Elastic project

At cloud.elastic.co, create an **Observability Complete** Serverless project (the README's choice). Note its name, region and the Elasticsearch endpoint (a base URL: no path, no port).

**Expect:** the project opens in Kibana. Give the root chat the project name, region and endpoint (never the key) so the handoff's section 4 can record them.

### A2. Create the write-only key

In Kibana, Dev Tools, run:

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

**Expect:** a JSON response with `id`, `name`, `api_key` and `encoded`. The `encoded` value is shown only once. Copy it straight into `.env.elastic` (step A5). Do not paste it anywhere else.

### A3. Check the laptop (read-only)

From the repo root:

```
sysctl -n hw.memsize | awk '{printf "%.0f GB RAM\n", $1/1024/1024/1024}'
docker info --format 'Docker has {{.MemTotal}} bytes and {{.NCPU}} CPUs'
ls -ld opentelemetry-demo .env.elastic
```

**Expect:**
- The laptop's total RAM.
- Docker with at least 12 GB (about 12,884,901,888 bytes) and at least 4 CPUs (the README asks for 12 GB; the environment guide asks for 4 CPUs). If Docker has less, raise it in Docker Desktop, Settings, Resources.
- On a first run, the last command prints `No such file or directory` for one or both names. That is fine. If either exists, it is left over from an earlier attempt; tell the root chat before continuing.

### A4. Clone the demo at the pinned version

```
git clone --depth 1 --branch 3.0.0 https://github.com/open-telemetry/opentelemetry-demo.git
grep -n "DEMO_VERSION" opentelemetry-demo/.env
```

**Expect:** the second command prints a line ending `DEMO_VERSION=3.0.0`. The pin matters: the payment service fails to start on the latest version.

### A5. Create `.env.elastic`

```
cp config/.env.example .env.elastic
nano .env.elastic
```

Fill in `ES_ENDPOINT` (the base URL from A1) and `ES_API_KEY` (the `encoded` value from A2). Save and exit.

**Expect:** no output from `cp`. `.env.elastic` is blocked from commits by `.gitignore`; `git status -sb` must not list it.

### A6. Generate the Prometheus config

```
./scripts/apply-config.sh
```

**Expect:** these lines, in this order:
- `Wrote .../opentelemetry-demo/src/prometheus/prometheus-config.yaml`
- `Remote-write URL: https://<project>.es.<region>...elastic.cloud/_prometheus/api/v1/write`
- `API key: <first 4 characters>... (<length> chars)`
- `Base endpoint: HTTP 200` or `HTTP 403` (a write-only key may be refused at the cluster root)
- `Write endpoint GET: HTTP 405` (the write endpoint accepts POST only)
- `OK: endpoint reachable. Data arriving in Elastic after the stack starts is the real test.`

A `WARNING` line means the key or the endpoint is wrong. Stop and show the root chat the warning (never the key).

### A7. Start the stack

```
cd opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml pull --quiet
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```

**Expect:** the pull finishes without an authentication or network error. After about two minutes, this lists the containers as running:

```
docker compose -f compose.yaml -f compose.observability.yaml ps --format "table {{.Name}}\t{{.Status}}"
```

### A8. Check that Prometheus can read its config

```
docker logs prometheus --tail 30 2>&1 | grep -i "permission denied"
```

**Expect:** no output. On the desktop, the script's `chmod 600` very likely made Prometheus log "permission denied" (the container's user could not read the file). Whether this happens on macOS is **untested**. If lines appear:

```
chmod 644 src/prometheus/prometheus-config.yaml
docker restart prometheus
```

then run the check again; it should print nothing. Tell the root chat either way, so the `apply-config.sh` decision can be made from a real result.

### A9. Check that data reaches Elastic

The key is write-only, so check from the Prometheus side. Run this twice, a minute apart:

```
curl -s http://localhost:9090/metrics | grep '^prometheus_remote_storage_samples'
```

**Expect:** `prometheus_remote_storage_samples_total` climbs between the two runs, and `prometheus_remote_storage_samples_failed_total` stays at `0`. Then, in Kibana Discover in ES|QL mode:

```
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

**Expect:** `MAX(@timestamp)` within the last two minutes, and a `COUNT` that grows when you run it again.

### A10. Keep the laptop awake while the stack runs

In a separate terminal tab, with the charger in and the lid open:

```
caffeinate -dims
```

**Expect:** the command keeps running and prints nothing. Stop it with Control-C when you are done for the day. A sleeping laptop pauses the stack and creates gaps in the data.

---

## Part B: the per-video reset

Do this before every rehearsal and every take. It wipes the local data and the Elastic data, so a video never depends on another video's data.

### B1. Read the video's stack state from its contract

Section 6 of the video's contract gives the minimum warm-up (in minutes) and the state of the `paymentFailure` flag. Write both down.

### B2. Stop the stack and delete its local data

```
cd /Users/enriquekortright/personal/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml down --volumes --remove-orphans
```

**Expect:** the containers and their volumes are removed. Your config files on disk are untouched. Stop first, so nothing writes while you delete in the next step.

### B3. Delete the data in Elasticsearch

The write-only key cannot delete. Use Kibana, Dev Tools, which runs under your own login:

```
GET _data_stream/metrics-generic.prometheus-default
```

**Expect:** the data stream with its exact name and its backing indices. If the name differs, stop.

```
DELETE _data_stream/metrics-generic.prometheus-default
```

**Expect:** `{"acknowledged": true}`. This removes the data stream and all its backing indices, and it cannot be undone. Use the exact name, never a wildcard such as `metrics-*`. Note the time you ran it.

### B4. Restart

```
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```

**Expect:** the containers start. After about two minutes, the `ps` command from step A7 lists them as running. Restart `caffeinate -dims` if you stopped it (A10).

### B5. Confirm the reset worked

Run the counters from step A9 twice, a minute apart: `samples_total` climbs and `samples_failed_total` stays at `0`. Then in Discover:

```
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

**Expect:** `MIN(@timestamp)` is **later than the time you ran the DELETE in B3** (so the old data is gone), and `MAX(@timestamp)` is within the last two minutes. Elastic is expected to recreate the data stream on its own when the first samples arrive; this was verified on the old project and is untested on the new one.

If `MIN(@timestamp)` is earlier than the DELETE, something replayed or the delete missed. Stop and tell the root chat.

### B6. Set the flag state

At `http://localhost:8080/feature`, set `paymentFailure` as the contract says. For a video that needs it on, note the time you switched it on. Its effect is unmeasured, so the video chat measures it in the rehearsal before the take.

### B7. Warm up

Wait the number of minutes in the contract, with `caffeinate -dims` running. The rule of thumb is at least 45 minutes after a reset. Do not record before then.

---

## Part C: pre-roll, just before a take

These were written for Linux and have only been run there. Run them in a macOS terminal; BSD `sed` and `awk` should accept them, but that is **untested**. If a command errors, paste the error and the root chat will adjust it.

**1. Uptime and clock**

```
date -u; docker ps --format '{{.Names}}: {{.Status}}' | grep -E 'prometheus|flagd'
```

**Expect:** the current time, then Prometheus and the flag service both `Up`, with an uptime at least as long as the contract's minimum.

**2. Remote-write counters**

```
date -u; curl -s http://localhost:9090/metrics | sed 's/{[^}]*}//' | awk '/^prometheus_remote_storage_samples_failed_total/{f=$2} /^prometheus_remote_storage_samples_retried_total/{r=$2} /^prometheus_remote_storage_samples_pending/{p=$2} /^prometheus_remote_storage_samples_in_total/{i=$2} /^prometheus_remote_storage_samples_total/{t=$2} END{printf "failed %s | retried %s | pending %s | in %.0f | sent %.0f | gap %.0f\n", f, r, p, i, t, i-t}'; docker logs prometheus 2>&1 | grep -cE 'level=(WARN|ERROR)'
```

**Expect:** `failed 0`, `retried 0`, a small `pending`, and the last number (the count of warning and error lines in the log) at `0`.

**3. The flag**

At `http://localhost:8080/feature`, confirm `paymentFailure` matches the contract (off for Video 1; as measured for Video 2; off for Video 3).

**After the take:** run command 2 again. `failed` should be unchanged from before the take.

---

## Known gaps

- Nothing here has run on the laptop yet. The first run is the test of this runbook.
- `scripts/apply-config.sh` still sets mode 600 on the generated config. Step A8 checks whether that matters on macOS. The fix (mode 644 is the leading option, a security trade-off for a write-only key on a single-user laptop) is decided after that result.
- Whether the overlapping-blocks warning appears at Prometheus's first compaction (a few hours in) is unchecked. A long warm-up, such as overnight, would answer it.
