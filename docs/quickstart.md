# Quickstart — Daily Stack Launch and Verification

Use this guide every time you return to work on the project. It assumes the stack has already been installed following the README. If you have not done that yet, start there.

---

## Step 1 — Check if the stack is already running

```bash
cd ~/personal/projects/elastic-migration/opentelemetry-demo
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
The memory limit needs increasing. Check `config/compose.observability.yaml` — Prometheus should have `memory: 1024M`. If not, copy the patched file from the repo:
```bash
cp ../config/compose.observability.yaml compose.observability.yaml
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
# Wait 5 minutes before recording — Prometheus needs time to build a stable rate window
```

---

## Step 4 — Verify data is flowing to Elastic

```bash
source ~/personal/projects/elastic-migration/.env.elastic

curl -s \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  "${ES_ENDPOINT}/_cat/indices/metrics-*?h=index,docs.count"
```

Expected output: a non-zero document count in the `metrics-generic.prometheus-default` index. If the count is the same after 2 minutes, remote-write may have stopped — restart Prometheus.

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

- [ ] Stack has been running for **at least 15 minutes** — Prometheus needs this for stable `rate()` windows
- [ ] Kibana chart for Query 1 shows stable flat lines — not ramping up
- [ ] Prometheus graph at `5m` time range shows stable flat lines
- [ ] Grafana Spanmetrics dashboard panels are populated
- [ ] `paymentFailure` feature flag is set to **off** at `http://localhost:8080/feature`
- [ ] No terminal windows or credentials visible on screen

---

## Daily stop

When you are done for the day:

```bash
cd ~/personal/projects/elastic-migration/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml stop
```

This stops containers but preserves their state. Next time you start, data resumes immediately without a full reinitialisation.

**Full teardown** (only if you need a clean slate):
```bash
docker compose -f compose.yaml -f compose.observability.yaml down --volumes
```
Note: this clears Prometheus local storage. Elastic data is unaffected.
