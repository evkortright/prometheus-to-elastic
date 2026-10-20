# Quickstart — Daily Stack Launch and Verification

Use this guide every time you return to work on the project. It assumes the stack has already been installed following the README. If you have not done that yet, start there.

---

## Step 1 — Check if the stack is already running

```bash
cd ~/personal/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml ps \
  --format "table {{.Name}}\t{{.Status}}"
```

**If all containers show `Up`** — skip to Step 3 to verify data is flowing.

**If the output is empty or containers show `Exited`** — continue to Step 2.

**If one or two containers show `Restarting`** — check their logs before proceeding:
```bash
docker logs <container-name> --tail 20 2>&1
```

---

## Step 2 — Start the stack

**First run, or after editing `.env.elastic`?** Generate the Prometheus config first. From the repo root:
```bash
./scripts/apply-config.sh
```
This writes the real endpoint and key into the demo's Prometheus config (never into a tracked file) and copies the patched compose file. A healthy result prints `200` or `403` for the base endpoint (a write-only key may be refused at the cluster root) and `405` for the write endpoint. A `401` means the key was rejected.

Then start the stack:

```bash
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```

Wait 2 minutes, then re-run the status check from Step 1. All containers should show `Up`.

**Common issues:**

**Payment service crash-loops with MODULE_NOT_FOUND:**
The `DEMO_VERSION` in `.env` is set to `latest` instead of `3.0.0`. Fix it:
```bash
sed -i.bak 's/DEMO_VERSION=latest/DEMO_VERSION=3.0.0/' .env
docker compose -f compose.yaml -f compose.observability.yaml pull --quiet
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```

**Prometheus exits with code 137 (OOM):**
The memory limit needs increasing. Check `config/compose.observability.yaml` — Prometheus should have `memory: 1024M`. If not, re-apply the patched file from the repo (the script copies it for you):
```bash
../scripts/apply-config.sh
docker compose -f compose.yaml -f compose.observability.yaml up --detach --force-recreate prometheus
```

**CTFd containers consuming memory:**
Stop them before starting the OTel stack:
```bash
docker stop edu-ctfd-nginx-1 edu-ctfd-cache-1 edu-ctfd-db-1 2>/dev/null
```

---

## Step 3 — Verify Prometheus is healthy

```bash
# Confirm Prometheus is up
docker ps --filter "name=prometheus" --format "table {{.Names}}\t{{.Status}}"

# Confirm it is receiving metrics
curl -s 'http://localhost:9090/api/v1/query?query=up' \
  | python3 -m json.tool | grep '"status"'
```

Expected output:
- `prometheus   Up X minutes`
- `"status": "success"`

If Prometheus is missing or exited, restart it:
```bash
docker compose -f compose.yaml -f compose.observability.yaml up --detach --force-recreate prometheus
# Wait at least 15 minutes before recording — Prometheus needs time to build a stable rate window
```

---

## Step 4 — Verify data is flowing to Elastic

Check from the Prometheus side. The API key for this project is write-only, so it cannot list indices and the old `_cat/indices` check no longer works.

```bash
curl -s http://localhost:9090/metrics | grep '^prometheus_remote_storage_samples'
```

Run it twice, about a minute apart. `samples_total` should increase and `samples_failed_total` should stay at `0`. `samples_pending` should stay near `0`.

These counters are only available on the `/metrics` page here. Querying them through `/api/v1/query` returned no results when tested on October 19, 2026.

Also scan the Prometheus log for remote-write errors:
```bash
docker logs prometheus --tail 30 2>&1 | grep -i -E "remote|error|401|403"
```
A healthy start shows the `elastic-serverless` queue starting and the WAL replaying, with no 401 or 403 lines.

---

## Step 5 — Verify Kibana is returning data

Open Kibana and run this query in Discover with ES|QL:

```esql
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

The `MAX(@timestamp)` should be within the last 2 minutes. If it is stale, Prometheus is not remote-writing — check Step 3.

---

## Step 6 — Ready to record checklist

Once all steps above pass:

- [ ] Stack has been running for **at least 15 minutes** — Prometheus needs this for stable `rate()` windows. Allow about **45 minutes** after the first start on a new Elastic project if you want a full "Last 30 minutes" chart
- [ ] Kibana chart for Query 1 shows stable flat lines — not ramping up
- [ ] Prometheus graph at `5m` time range shows stable flat lines
- [ ] Grafana Spanmetrics dashboard panels are populated
- [ ] `paymentFailure` feature flag is set to **off** at `http://localhost:8080/feature`
- [ ] No terminal windows or credentials visible on screen

---

## Daily stop

When you are done for the day:

```bash
cd ~/personal/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml stop
```

This stops containers but preserves their state. Next time you start, data resumes immediately without a full reinitialisation.

**Full teardown** (only if you need a clean slate):
```bash
docker compose -f compose.yaml -f compose.observability.yaml down --volumes
```
Note: this clears Prometheus local storage. Elastic data is unaffected.

---

## Reset: stop the stack and wipe all Prometheus data

Use this for a clean slate without creating a new Elastic project. **Order matters:** stop the stack first so nothing writes while you delete, and wipe the local data before restarting so Prometheus cannot replay old samples into the emptied data stream.

**1. Stop the local stack and delete its data**
```bash
cd ~/personal/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml down --volumes --remove-orphans
```
This removes the containers and their volumes, including Prometheus's local storage. Your config files on disk are untouched.

**2. Delete the data in Elasticsearch**

The remote-write API key is write-only and cannot delete. Use Kibana → Dev Tools, which runs under your own login:
```
GET _data_stream/metrics-generic.prometheus-default
DELETE _data_stream/metrics-generic.prometheus-default
```
The `GET` confirms the exact name first. The `DELETE` removes the data stream **and all of its backing indices**, and it cannot be undone. Use the exact name; do not use wildcards such as `metrics-*`, which would also delete any other metrics in the project.

**3. Restart and rebuild the baseline**
```bash
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```
The data stream is expected to be recreated automatically when the first new samples arrive (the key has the `auto_configure` privilege). Confirm with the Step 4 and Step 5 checks, then allow about 45 minutes before recording.

If you only changed credentials and did not delete the data, you do not need this section. Re-run `./scripts/apply-config.sh` and `docker restart prometheus` instead.
