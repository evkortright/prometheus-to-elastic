# Environment Setup Plan: PromQL → Elastic Migration Training Track

> **Scope** — Two environments:
> 1. **Local + Elastic Serverless** — for recording feature highlight videos
> 2. **Instruqt Sandbox** — for learner-facing lab tracks
>
> **Source system:** OpenTelemetry Astronomy Shop v3.0.0 (the canonical OTel reference app) shipping metrics to Prometheus + Grafana.
> **Destination:** Elastic Serverless (Observability Complete project).
> **Last validated:** August 13, 2026 — all steps below were executed and confirmed working.

---

## What we learned from validation (read this first)

v3.0.0 of the OTel demo changed several things from earlier versions. These are not assumptions — they are confirmed facts from a live run:

| What changed | Old assumption | Validated reality |
|---|---|---|
| Compose filename | `docker-compose.yml` | `compose.yaml` |
| Prometheus + Grafana included | Needed `-f compose.observability.yaml` | Included by default in `compose.yaml` |
| Prometheus config filename | `prometheus.yml` | `prometheus-config.yaml` |
| Grafana URL | `http://localhost:3000` | `http://localhost:8080/grafana/` (proxied) |
| Prometheus port | `:9090` | `:9090` ✓ unchanged |
| Storefront URL | `http://localhost:8080` | `http://localhost:8080` ✓ unchanged |
| Metrics flow to Prometheus | Collector exposes `:9464`, Prometheus scrapes | Collector pushes via OTLP to `http://prometheus:9090/api/v1/otlp` |
| Prometheus version | v3.7.3 | v3.13.1 (pinned in `.env`) |
| OTel demo version | 1.11.x | 3.0.0 (latest stable as of August 2026) |
| Container count | ~20 | 30 containers |
| Docker Desktop bind mount | Refreshes live | **Requires container restart** to pick up host file edits |

**Architecture note:** In v3.0.0, Prometheus no longer scrapes the OTel Collector. Instead the Collector pushes metrics to Prometheus via OTLP. This does not affect the migration story — Prometheus still holds the data and still supports `remote_write` out. The learner's experience is identical.

---

## Architecture overview

```
┌─────────────────────────────────────────────────────────────────────┐
│  OTel Astronomy Shop (Docker Compose) — 30 containers               │
│  16 microservices → OTel Collector ──OTLP push──► Prometheus        │
│                                                        │            │
│                      Grafana ◄──── PromQL queries ─────┤            │
│                                                        │            │
│                                          remote_write  ▼            │
│                                        Elastic Serverless           │
└─────────────────────────────────────────────────────────────────────┘
```

The training narrative: a Prometheus customer adds one `remote_write` block to their Prometheus config. Grafana keeps working unchanged. Elastic gets the same metrics simultaneously. The migration happens in layers across the modules.

---

## Stage 1 — Local laptop + Elastic Serverless

### Prerequisites (validated on Apple Silicon + Docker Desktop)

- Docker Desktop with **≥12 GB RAM** and **≥4 CPUs** allocated
- Docker Compose v2.x (`docker compose version` — note: no hyphen)
- An Elastic Serverless **Observability Complete** project on [cloud.elastic.co](https://cloud.elastic.co)

### 1.1 — Elastic Serverless project (one-time setup)

You need two things from your project:

**ES endpoint** — from the project overview page, looks like:
```
https://<project-id>.es.<region>.gcp.elastic.cloud
```

**API key** — in Kibana → Stack Management → API Keys → Create API key:
- Name: `metrics-writer`
- Type: Personal
- Control security privileges: OFF (unrestricted is fine for dev)
- Click **Create** and copy the **Encoded** value immediately — it is only shown once

**Verify connectivity** before touching anything else:
```bash
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  "${ES_ENDPOINT}"
# Expect: 200

curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  -H "Content-Type: application/x-protobuf" \
  "${ES_ENDPOINT}/_prometheus/api/v1/write"
# Expect: 405 (endpoint exists, only accepts POST with protobuf body)
```

**Store credentials** in a file outside the git repo (never committed):
```bash
cat > ~/projects/elastic-migration/.env.elastic << 'EOF'
ES_ENDPOINT=https://<your-project-id>.es.<region>.gcp.elastic.cloud
ES_API_KEY=<your-encoded-key>
EOF

# Verify (without exposing the key)
grep -o "ES_.*=.*" ~/projects/elastic-migration/.env.elastic | sed 's/=.*/=***/'
```

### 1.2 — Clone and start the OTel demo

```bash
mkdir -p ~/projects/elastic-migration
cd ~/projects/elastic-migration

# Pin to 3.0.0 — do not clone main
git clone --depth 1 --branch 3.0.0 \
  https://github.com/open-telemetry/opentelemetry-demo.git

cd opentelemetry-demo
```

**Pull images before starting** (catches auth/network issues early):
```bash
docker compose pull --quiet 2>&1 | tail -5
```

**Start the stack** (Prometheus and Grafana are included by default — no extra `-f` flags needed):
```bash
docker compose up --detach
```

This starts ~30 containers. Wait about 2 minutes, then verify:
```bash
docker compose ps --format "table {{.Name}}\t{{.Status}}" | grep -v healthy
# Only containers without (healthy) status should appear
# Some containers don't have healthchecks — that's normal
```

**Confirm Prometheus has data:**
```bash
curl -s 'http://localhost:9090/api/v1/query?query=traces_span_metrics_calls_total' \
  | python3 -m json.tool | head -5
# Expect: "status": "success" with non-empty result array
```

### 1.3 — Add remote_write to Prometheus

**Make a backup first:**
```bash
cp src/prometheus/prometheus-config.yaml \
   src/prometheus/prometheus-config.yaml.bak
```

**Source your credentials:**
```bash
source ~/projects/elastic-migration/.env.elastic
```

**Append the remote_write block** (values hardcoded — do not use `${VARIABLE}` syntax, Prometheus does not expand shell variables):
```bash
cat >> src/prometheus/prometheus-config.yaml << EOF

remote_write:
  - url: "${ES_ENDPOINT}/_prometheus/api/v1/write"
    name: elastic-serverless
    authorization:
      type: ApiKey
      credentials: "${ES_API_KEY}"
    queue_config:
      capacity: 10000
      max_shards: 50
      max_samples_per_send: 5000
      batch_send_deadline: 5s
EOF
```

**Verify the URL expanded correctly** (not a literal `${...}`):
```bash
grep "url:" src/prometheus/prometheus-config.yaml
# Should show the actual https:// URL, not a variable reference
```

If you see `${ES_ENDPOINT}` literally, fix it:
```bash
sed -i.tmp "s|\${ES_ENDPOINT}|${ES_ENDPOINT}|g" src/prometheus/prometheus-config.yaml
sed -i.tmp "s|\${ES_API_KEY}|${ES_API_KEY}|g" src/prometheus/prometheus-config.yaml
```

**⚠️ macOS Docker Desktop gotcha:** Editing a bind-mounted file on the host does NOT refresh inside the container automatically. You must restart the Prometheus container to pick up the change:

```bash
docker restart prometheus
```

**Verify the config loaded inside the container:**
```bash
docker exec prometheus wc -c /etc/prometheus/prometheus-config.yaml
# Should show non-zero byte count matching your file

curl -s 'http://localhost:9090/api/v1/status/config' \
  | python3 -m json.tool | grep "remote_write"
# Should show your endpoint URL
```

### 1.4 — Verify data is flowing to Elastic

Wait 30–60 seconds after the Prometheus restart, then:

```bash
source ~/projects/elastic-migration/.env.elastic

# Check document count in Elastic
curl -s \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  "${ES_ENDPOINT}/_cat/indices/metrics-*?h=index,docs.count"
# Expect: .ds-metrics-generic.prometheus-default-<date>-000001  <large number>
```

In Kibana → Discover → switch to ES|QL:
```esql
FROM metrics-generic.prometheus-default
| LIMIT 5
```

You should see rows with hundreds of metric fields including `traces_span_metrics_calls_total`, `http_server_request_duration_seconds_*`, `service_name`, `host_name`, and rich Kafka, PostgreSQL, Redis, and JVM metrics.

### 1.5 — Service URLs reference

| Service | URL | Notes |
|---|---|---|
| OTel storefront | `http://localhost:8080` | Live shopping app with load generator |
| Grafana | `http://localhost:8080/grafana/` | 10 pre-provisioned dashboards |
| Prometheus UI | `http://localhost:9090` | Query, targets, config |
| Jaeger | `http://localhost:8080/jaeger/ui/` | Traces |
| Feature flags | `http://localhost:8080/feature` | Toggle demo scenarios |
| OpAMP UI | `http://localhost:8080/opamp/` | Collector management |

**Note:** Grafana is proxied through the frontend on port 8080, not directly on 3000. Do not use `localhost:3000`.

### 1.6 — Pre-built Grafana dashboards

| Dashboard | Best for showing |
|---|---|
| Demo Dashboard | End-to-end request rates, latency, error rates |
| Spanmetrics Demo Dashboard | Trace-derived metrics — great for showing span_metrics |
| APM Dashboard (Jaeger, Prometheus, OpenSearch) | Cross-signal correlation in the source world |
| Linux | Host-level metrics from the collector |
| OpenTelemetry Collector | Collector self-observability |
| PostgreSQL | DB metrics from the collector |

### 1.7 — Recording checklist

Before hitting record for each video:

- [ ] `docker compose ps` — all containers show Up
- [ ] `http://localhost:8080` loads the storefront
- [ ] `http://localhost:8080/grafana/` shows populated dashboards (give it 5–10 min after first start)
- [ ] Prometheus at `:9090` shows data for `traces_span_metrics_calls_total`
- [ ] Elastic index has documents: `curl ... /_cat/indices/metrics-*`
- [ ] Kibana Discover ES|QL query returns rows
- [ ] `.env.elastic` file not visible anywhere on screen
- [ ] Terminal history cleared if API key was recently echoed

### 1.8 — Daily start/stop

**Start:**
```bash
cd ~/projects/elastic-migration/opentelemetry-demo
docker compose up --detach
# Give it 2 minutes, then verify with docker compose ps
```

**Stop (preserves data):**
```bash
docker compose stop
```

**Full teardown (removes all data):**
```bash
docker compose down --volumes
```

After a full teardown, you will need to re-apply the `remote_write` block from a backup — the Prometheus config is restored from the source file on disk, which should already have the block if you saved it.

---

## Stage 2 — Instruqt sandbox

### Goal
A fully self-contained environment a learner can spin up in a browser with zero local setup. Everything runs in Instruqt's sandboxed VMs. The Elastic Serverless project is pre-provisioned with credentials injected by the Instruqt challenge setup script.

### 2.1 — Instruqt track structure

```
Track: PromQL to Elastic Migration

  Challenge 1 (Module 1): PromQL Compatibility
    - Sandbox: Linux VM with Docker Compose (OTel demo + Prometheus + Grafana)
    - Credentials: ES_ENDPOINT + ES_API_KEY injected as env vars
    - remote_write: pre-configured and running
    - Learner task: verify PromQL queries return same results in both systems

  Challenge 2 (Module 2): Remote Write Config
    - Same sandbox, remote_write block commented out
    - Learner task: uncomment + fill in credentials, restart Prometheus, verify data flows

  Challenge 3 (Module 3): Dashboard Migration Tooling
    - Adds: Elastic dashboard migration tooling
    - Learner task: export Grafana dashboard JSON, run migration, compare output

  Challenge 3.5 (Module 3.5): Field Name Alignment — Preparing for Cross-Signal Correlation
    - Teaches the Prometheus (underscores) vs OTel semconv/ECS (dots) field name mismatch
    - Shows three approaches: runtime aliasing (quick win), index alias, ingest pipeline
    - Learner task: write an ES|QL EVAL that bridges service_name to service.name
    - Learner task: create an ingest pipeline that normalizes fields on ingest
    - This module is a prerequisite for Module 4

  Challenge 4 (Module 4): Cross-Signal Correlation
    - Requires Module 3.5 field alignment to be complete
    - Same sandbox, traces and logs now also flowing to Elastic via OTel Collector
    - Learner task: write ES|QL pipeline joining metrics + traces on service.name
    - Learner task: write ES|QL pipeline joining metrics + logs on service.name

  Challenge 5 (Module 5): End-to-End Migration (capstone)
    - Full migration: remote_write config, field alignment, dashboard, alert rule
    - Historical data: Prometheus retained as historical record,
      Elastic as system of record from migration day forward
    - Learner produces a runbook as the deliverable
```

### 2.2 — Instruqt sandbox spec

```yaml
# instruqt-track/track.yml (skeleton)
slug: promql-to-elastic-migration
title: PromQL to Elastic Migration
teaser: Migrate a live Prometheus + Grafana observability stack to Elastic Serverless
level: intermediate
owner: elastic

virtual_machines:
  - name: sandbox
    image: ubuntu-2204-lts
    machine_type: n1-standard-4   # 4 vCPU, 15 GB RAM — 30 containers need headroom
    allow_external_ingress:
      - service: http
        port: 8080   # OTel storefront + Grafana (/grafana/) + Jaeger (/jaeger/ui/)
      - service: http
        port: 9090   # Prometheus UI
```

**Why n1-standard-4:** The OTel demo runs 30 containers. 2 vCPU/8 GB is borderline; 4 vCPU/15 GB gives learners a responsive experience and avoids OOM kills mid-challenge.

### 2.3 — Challenge setup scripts

Each challenge has a `setup-sandbox` script. Pattern for Challenge 1:

```bash
#!/bin/bash
# challenges/01-promql-compat/setup-sandbox
set -euo pipefail

### 1. Install Docker + Compose
apt-get update -qq
apt-get install -y docker.io docker-compose-plugin jq curl

### 2. Pull OTel demo — pinned to 3.0.0
git clone --depth 1 --branch 3.0.0 \
  https://github.com/open-telemetry/opentelemetry-demo.git \
  /opt/otel-demo

### 3. Patch prometheus-config.yaml with remote_write
# Note: hardcode values — Prometheus does not expand shell variables
cat >> /opt/otel-demo/src/prometheus/prometheus-config.yaml << EOF

remote_write:
  - url: "${ELASTIC_ES_ENDPOINT}/_prometheus/api/v1/write"
    name: elastic-serverless
    authorization:
      type: ApiKey
      credentials: "${ELASTIC_API_KEY}"
    queue_config:
      capacity: 10000
      max_shards: 50
      max_samples_per_send: 5000
      batch_send_deadline: 5s
EOF

### 4. Start the stack
cd /opt/otel-demo
docker compose up --detach

### 5. Wait for Prometheus to be healthy (up to 3 min)
echo "Waiting for Prometheus..."
timeout 180 bash -c 'until curl -sf http://localhost:9090/-/healthy; do sleep 5; done'

### 6. Wait for data in Elastic (up to 3 min)
echo "Waiting for data in Elastic..."
timeout 180 bash -c "
  until curl -sf \
    -H 'Authorization: ApiKey ${ELASTIC_API_KEY}' \
    '${ELASTIC_ES_ENDPOINT}/_cat/indices/metrics-*?h=docs.count' \
    | grep -qE '^[1-9]'; do sleep 10; done"

echo "Setup complete."
```

**Important notes for Instruqt scripts:**
- The remote_write block uses `"${VARIABLE}"` in a double-quoted heredoc, so values ARE expanded at script runtime — this is correct and intentional (opposite of the macOS local setup where we use `cat >>` after sourcing the env file).
- No container restart needed in Instruqt — the config is patched before the containers start.
- There is no bind-mount refresh issue on Linux — Docker on Linux reflects file changes immediately.

**Check script for Challenge 2** (learner configures remote_write themselves):

```bash
#!/bin/bash
# challenges/02-remote-write/check-sandbox

# Confirm Prometheus config has remote_write pointing at Elastic
if ! grep -q "elastic.cloud" /opt/otel-demo/src/prometheus/prometheus-config.yaml; then
  echo "FAIL: remote_write not configured in prometheus-config.yaml"
  exit 1
fi

# Confirm data appears in Elastic
RESPONSE=$(curl -sf \
  -H "Authorization: ApiKey ${ELASTIC_API_KEY}" \
  "${ELASTIC_ES_ENDPOINT}/_cat/indices/metrics-*?h=docs.count")

if [[ -z "$RESPONSE" || "$RESPONSE" == "0" ]]; then
  echo "FAIL: No data in Elastic yet — check remote_write config and restart Prometheus"
  exit 1
fi

echo "PASS"
exit 0
```

### 2.4 — Elastic project provisioning for Instruqt

**Option A — Shared project per cohort (recommended to start)**
Provision one Elastic Serverless project, store endpoint + API key as Instruqt track-level secrets. Inject via `track-start` lifecycle hook:

```bash
# track-start
agent variable set ELASTIC_ES_ENDPOINT "${ELASTIC_ES_ENDPOINT}"
agent variable set ELASTIC_API_KEY "${ELASTIC_API_KEY}"
```

**Option B — Per-learner Elastic project (for production scale >50 concurrent)**
Use the Elastic Cloud API to create a project per track start and delete at track end. Adds ~90 seconds to startup. Verify the correct API endpoint path against current Elastic Cloud API docs before implementing.

### 2.5 — Resource and timing estimates

| Component | Memory | Notes |
|---|---|---|
| OTel Astronomy Shop (30 containers) | ~8–10 GB | Validated on Apple Silicon |
| Prometheus | ~512 MB | OTLP receiver + remote_write — **default 200MB limit is insufficient after a few days of running; increase to 512MB in compose.observability.yaml** |
| Grafana | ~100 MB | Pre-provisioned dashboards |
| **Total** | **~10 GB** | Use n1-standard-4 (15 GB) |

> ⚠️ **Known issue:** The default Prometheus memory limit in `compose.observability.yaml` is 200MB.
> After running for several days with remote_write active, Prometheus will OOM and crash-loop.
> Fix: edit `compose.observability.yaml` and change `memory: 200M` to `memory: 512M` under the
> Prometheus `resources.limits` block, then recreate the container:
> `docker compose -f compose.yaml -f compose.observability.yaml up --detach --force-recreate prometheus`
> The `llm` container may also OOM under memory pressure but recovers once Prometheus stabilizes.

Startup time from `docker compose up` to data visible in Kibana: **~3–4 minutes** (images pre-pulled in Instruqt sandbox image).

Recommended Instruqt challenge time limits:
- Challenges 1–3: 20 min each
- Challenge 4: 25 min
- Challenge 5 (capstone): 45 min

---

## Build order (validated sequence)

Steps 1–3 are complete as of August 13, 2026. Pick up from step 4.

1. ✅ **Provision Elastic Serverless project** — confirmed endpoint reachable, API key valid
2. ✅ **Clone OTel demo v3.0.0** — 30 containers running, Grafana dashboards populated
3. ✅ **Add remote_write block** — data flowing to Elastic (237k+ documents confirmed)
4. **Record Module 1 video** — PromQL compatibility: same query in Prometheus and Elastic
5. **Record Module 2 video** — show the exact `prometheus-config.yaml` edit from step 3
6. **Build Instruqt Challenge 1 setup script** — test in a fresh Ubuntu VM
7. **Build check scripts for Challenge 2** — most critical automated check
8. **Build remaining challenges iteratively**, one per module

---

## Key files (local repo structure)

```
~/projects/elastic-migration/
├── .env.elastic                          # credentials — gitignored, never committed
├── opentelemetry-demo/                   # cloned at tag 3.0.0
│   ├── compose.yaml                      # main compose file (includes Prometheus + Grafana)
│   ├── compose.observability.yaml        # already merged into compose.yaml in v3.0.0
│   ├── src/
│   │   ├── prometheus/
│   │   │   ├── prometheus-config.yaml    # EDITED: remote_write block added at bottom
│   │   │   └── prometheus-config.yaml.bak  # backup before edit
│   │   └── otel-collector/
│   │       ├── otelcol-config.yml
│   │       ├── otelcol-config-observability.yml
│   │       └── otelcol-config-extras.yml  # extension point for future Elastic OTLP path
└── instruqt/                             # to be built
    ├── track.yml
    ├── challenges/
    │   ├── 01-promql-compat/
    │   ├── 02-remote-write/
    │   ├── 03-dashboard-migration/
    │   ├── 04-cross-signal/
    │   └── 05-capstone/
    └── scripts/
        ├── install-docker.sh
        └── wait-for-elastic.sh
```

---

## Open questions (carry forward)

### Instruqt sandbox

1. **Existing sandbox audit** — there is an existing Instruqt sandbox with a Serverless project and an OTel store build. Before revising it, determine:
   - What version of the OTel demo is it running? (v1.x vs v3.0.0 are significantly different)
   - How is Prometheus configured? (scrape vs OTLP push)
   - Is `remote_write` already configured or does the learner set it up?
   - What Elastic Serverless project is it pointing at, and is it still active?
   - Is the sandbox image pre-built or does it pull and build on start? (affects startup time significantly)

2. **Sandbox startup time** — the OTel demo v3.0.0 pulls ~30 container images. If images are not pre-baked into the Instruqt sandbox base image, learners will wait 5–10 minutes at challenge start. Determine whether to pre-bake images into a custom Instruqt VM image or accept the pull time.

3. **Elastic project per learner vs shared** — for the Instruqt tracks, decide between:
   - Shared project per cohort (simpler, risk of data pollution between learners)
   - Per-learner project via Elastic Cloud API (cleaner, adds ~90s startup, needs API endpoint verification)

4. **Elastic Cloud API path for Option B** — verify the correct project creation endpoint against current Elastic Cloud API docs before implementing per-learner provisioning.

### Migration tooling (Modules 3 and 5)

5. **Dashboard migration tooling** — which internal Elastic tool handles Grafana → Kibana dashboard migration? The Challenge 3 setup script needs to know:
   - What to install in the sandbox
   - How to invoke it (CLI? UI? API?)
   - What it produces (Kibana dashboard JSON? Direct import?)
   - Known limitations (which panel types migrate cleanly, which don't)

6. **Alert rule migration** — the capstone migrates a Prometheus alerting rule. Determine:
   - Does the Elastic tooling handle alert migration or is it manual?
   - What is the source format? The OTel demo has Grafana-managed alerts but no `prometheus/alerts.yml`. We may need to add one specifically for the training.
   - What does the migrated alert look like in Kibana?

### Capstone track design (Module 5 — full migration)

7. **Historical data migration** — `remote_write` only forwards new samples. For the capstone "full migration" story, decide how to handle historical data:
   - **Option A:** Accept that historical data stays in Prometheus (realistic — most migrations do this). Frame it as "Elastic becomes your system of record from day one forward."
   - **Option B:** Demonstrate a Prometheus snapshot export and backfill into Elastic. Complex, but shows the complete picture.
   - **Option C:** Ignore historical data in the capstone and focus on config, dashboards, and alerts only.

8. **Capstone deliverable** — the learner produces a runbook. Define what the runbook should contain:
   - `remote_write` config block (validated)
   - Migrated dashboard (from Module 3 tooling)
   - Migrated alert rule (from Module 6 tooling)
   - Cutover checklist (when to decommission Prometheus)
   - Rollback plan

9. **Prometheus alert source for training** — the OTel demo has a `CartAddItemHighLatency` Grafana-managed alert (visible in the Grafana logs). Consider whether to use this as the migration source or write a purpose-built `alerts.yml` that demonstrates a realistic Prometheus alerting rule (e.g., payment error rate > threshold).

### Field name alignment (Module 3.5)

10. **Prometheus vs OTel semconv field name mismatch** — when `remote_write` lands data in Elastic, field names are Prometheus-native (underscores, flat labels):
    - `service_name`, `host_name`, `http_server_request_duration_seconds_count`

    When traces and logs arrive via OTLP they follow OTel semantic conventions and ECS (dot notation):
    - `service.name`, `host.name`, `http.server.request.duration`

    This mismatch breaks cross-signal correlation queries silently (nulls returned from joins). Three approaches to resolve, in order of complexity:
    - **Option A — Runtime aliasing (quick win):** Add `EVAL service.name = service_name` in each ES|QL query before joining. No data changes needed, but every query requires it.
    - **Option B — Index mapping alias:** Add a field alias in the `metrics-generic.prometheus-default` index template. Zero query changes, but requires index template management.
    - **Option C — Ingest pipeline (production-ready):** Add an Elastic ingest pipeline to the data stream that renames/copies fields to OTel semconv names on ingest. Most complete, fully transparent to queries downstream.

    **Recommendation:** Teach Option A as the quick win in Module 3.5, then Option C as the production approach. This turns a friction point into a teaching moment about why semantic conventions matter.

11. **Module 3.5 lab design** — determine the exact set of fields to normalize for the training dataset. At minimum: `service_name` → `service.name`, `host_name` → `host.name`. Verify whether the OTel demo's Prometheus labels already include dot-notation variants via the `promote_resource_attributes` config in `prometheus-config.yaml` — if so, both forms may already exist in the data.

12. **Traces and logs path for Module 4** — bringing traces and logs into Elastic requires adding Elastic as an exporter in `otelcol-config-extras.yml`. This is Path B/C from the EDOT architecture diagram. Determine:
    - Which exporter to use: `otlp/elastic` or `elasticsearch`?
    - Does this require EDOT specifically or will the upstream OTel Collector contrib work?
    - What index/data stream patterns do traces and logs land in?
    - Confirm field names match OTel semconv so Module 3.5 alignment work pays off immediately in Module 4.

### EDOT / future modules

13. **EDOT as post-migration steady state** — `otelcol-config-extras.yml` is the designed extension point for adding Elastic as a direct OTLP destination, bypassing Prometheus entirely. This is the natural "where do you go after migration" story. Consider as a bonus module or capstone appendix showing Path C from the architecture diagram.

14. **Full decommission track (future)** — a follow-on advanced track covering:
    - Historical data migration from Prometheus to Elastic (Prometheus snapshot + backfill)
    - Validating data parity between Prometheus and Elastic before cutover
    - Decommissioning Prometheus safely
    - Running Elastic as the sole system of record
