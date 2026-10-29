# Prometheus to Elastic Migration — Training Track

A hands-on training series for Prometheus and Grafana users migrating to the Elastic Stack. Built around the [OpenTelemetry Astronomy Shop](https://github.com/open-telemetry/opentelemetry-demo) as the source observability system.

## What this is

A complete curriculum — feature highlight videos, lab exercises, and Instruqt sandbox environments — that walks a Prometheus operator through migrating their metrics stack to Elastic Serverless, one step at a time.

The core message: **your PromQL works in Elastic unchanged**. The migration adds capability — ES|QL pipelines, cross-signal correlation, dashboard and alert migration tooling — without requiring your team to relearn their existing workflows on day one.

---

## Architecture

```
OTel Astronomy Shop (16 microservices)
        │
        ▼ OTLP push
  OTel Collector
        │
        ▼ OTLP push
   Prometheus ──── remote_write ────► Elastic Serverless
        │                              (metrics-generic.prometheus-default)
        ▼
     Grafana                          Kibana · PromQL · ES|QL
  (unchanged)
```

One `remote_write` block added to `prometheus-config.yaml`. Nothing else changes.

---

## Training modules

| Module | Topic | Status |
|---|---|---|
| 1 | PromQL Compatibility | 🔶 In progress — script and cheat sheet drafted; re-validating on a rebuilt environment (see `docs/archive/module1-status-2026-10-19.md`) |
| 2 | Remote Write Configuration | 🔲 Planned |
| 3 | Dashboard Migration | 🔲 Planned |
| 3.5 | Field Name Alignment (Prometheus → OTel semconv) | 🔲 Planned |
| 4 | Cross-Signal Correlation | 🔲 Planned |
| 5 | End-to-End Migration Capstone | 🔲 Planned |

Each module has:
- A feature highlight video (recorded locally against Elastic Serverless)
- A hands-on lab (Instruqt sandbox)
- A recording script and query cheat sheet

---

## Repository structure

```
prometheus-to-elastic/
├── README.md
├── .gitignore
├── config/
│   ├── prometheus-config.yaml          # Template: remote_write block with placeholders (no credentials)
│   ├── compose.observability.yaml      # Patched: 1GB Prometheus memory, WAL compression, retention cap
│   └── .env.example                    # Template — copy to ../.env.elastic and fill in values
├── scripts/
│   └── apply-config.sh                 # Generates the demo's Prometheus config from the template + .env.elastic
├── docs/
│   ├── environment-setup-guide.md      # Full setup plan, validated steps, open questions
│   ├── quickstart.md                   # Daily launch and verification guide
│   ├── otel-collector-reference.md     # What the Collector does in the demo
│   ├── module-learning-objectives.md   # Two-track curriculum with Bloom's objectives
│   ├── module1-status-2026-10-19.md    # Environment change log and open Module 1 findings
│   ├── handoff-2026-10-19-module1-video.md  # Point-in-time handoff (endpoint details superseded)
│   └── diagrams/                       # 4 architecture diagrams (SVG + PNG)
├── modules/
│   └── module1-promql-compatibility/
│       ├── module1-recording-script-final.md   # Use this for recording
│       ├── module1-promql-cheatsheet.md        # Query reference
│       └── module1-demo-script.md              # Working draft (superseded by final)
└── instruqt/                           # To be built
    ├── track.yml
    └── challenges/
```

The OTel demo is cloned inside this folder as `opentelemetry-demo/` and is gitignored.

---

## Local setup

> The step-by-step version of this section, with the expected output of every step, is `docs/shared/operations/reset-runbook.md`. If the two differ, the runbook wins.

### Prerequisites

- Docker Desktop (Apple Silicon) with **≥12 GB RAM** allocated
- Docker Compose v2.x
- An Elastic Serverless **Observability Complete** project on [cloud.elastic.co](https://cloud.elastic.co)
- Git

### 1. Clone this repo and the OTel demo (pinned version)

```bash
git clone https://github.com/evkortright/prometheus-to-elastic.git ~/projects/prometheus-to-elastic
cd ~/projects/prometheus-to-elastic

git clone --depth 1 --branch 3.0.0 \
  https://github.com/open-telemetry/opentelemetry-demo.git

# Pin the version: a fresh clone reads DEMO_VERSION=latest, and the payment service fails to start on "latest"
sed -i '' 's/^DEMO_VERSION=latest/DEMO_VERSION=3.0.0/' opentelemetry-demo/.env
grep -n "^DEMO_VERSION" opentelemetry-demo/.env   # expect 4:DEMO_VERSION=3.0.0
```

### 2. Create the Elastic credentials

In your Serverless project, open Kibana → Dev Tools and create a key that can only write metrics:

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

Copy the `encoded` value from the response; it is shown only once. Then, from the repo root:

```bash
cp config/.env.example .env.elastic
nano .env.elastic
# ES_ENDPOINT=https://<project-id>.es.<region>.<cloud>.elastic.cloud   (base URL: no path; the port is optional)
# ES_API_KEY=<your-encoded-api-key>
```

> ⚠️ `.env.elastic` is gitignored — never commit it. The key is also written into the demo's generated Prometheus config (step 3), which lives in the gitignored demo folder.

### 3. Generate the Prometheus config

```bash
./scripts/apply-config.sh
```

The script builds `opentelemetry-demo/src/prometheus/prometheus-config.yaml` from the template and your `.env.elastic`, copies the patched compose file into the demo, and checks the endpoint. Expected output: `200` or `403` for the base endpoint (a write-only key may be refused at the cluster root) and `405` for the write endpoint. A `401` means the key was rejected.

### 4. Start the stack

```bash
cd opentelemetry-demo

# Pull images first (catches auth/network issues early)
docker compose -f compose.yaml -f compose.observability.yaml pull --quiet

# Start everything
docker compose -f compose.yaml -f compose.observability.yaml up --detach
```

Wait ~2 minutes, then verify:

```bash
docker compose -f compose.yaml -f compose.observability.yaml ps \
  --format "table {{.Name}}\t{{.Status}}"
```

### 5. Verify data is flowing to Elastic

The key is write-only, so check from the Prometheus side:

```bash
curl -s http://localhost:9090/metrics | grep '^prometheus_remote_storage_samples'
```

Run it twice, a minute apart: `samples_total` should climb and `samples_failed_total` should stay at `0`. Then open Kibana → Discover (ES|QL) and run:

```esql
FROM metrics-generic.prometheus-default
| STATS MIN(@timestamp), MAX(@timestamp), COUNT(*)
```

`MAX(@timestamp)` should be within the last couple of minutes.

---

## Service URLs

| Service | URL |
|---|---|
| OTel storefront | `http://localhost:8080` |
| Grafana | `http://localhost:8080/grafana/` |
| Prometheus | `http://localhost:9090` |
| Feature flags | `http://localhost:8080/feature` |
| Jaeger | `http://localhost:8080/jaeger/ui/` |

---

## Known issues

**Prometheus OOM after extended running**
The default 200MB memory limit in `compose.observability.yaml` is insufficient after several days of running with `remote_write` active. The patched `compose.observability.yaml` in this repo sets it to 1024MB and adds WAL compression and a local retention cap. If Prometheus crash-loops with exit code 137, re-run `./scripts/apply-config.sh` and recreate the container.

**macOS Docker Desktop bind mount**
Editing `prometheus-config.yaml` on the host does not refresh inside the container automatically. Always restart the Prometheus container after regenerating the config:
```bash
docker restart prometheus
```

**Grafana Demo Dashboard shows "No data"**
The Demo Dashboard requires OpenSearch (logs) and Jaeger (traces). Use the **Spanmetrics Demo Dashboard** instead for Module 1 — it is driven purely by Prometheus metrics and populates immediately.

**Write-only API key limits what you can check from the shell**
The key can write metrics but cannot list indices (`_cat/indices`) or read the cluster root. Use the Prometheus `/metrics` counters and Kibana queries to verify ingestion.

**Remote-write endpoint choice**
This track uses the direct Elasticsearch endpoint (`/_prometheus/api/v1/write`). Elastic's current documentation recommends the Managed Prometheus Remote Write endpoint for Serverless projects. The direct endpoint still works; which one the curriculum teaches is an open decision (see `docs/archive/module1-status-2026-10-19.md`).

---

## Daily workflow

**Start:**
```bash
cd ~/projects/prometheus-to-elastic/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml up --detach
# Wait 15+ minutes before recording — Prometheus needs time to build stable rate() windows
# (about 45 minutes after the first start on a new project, for a full Last 30 minutes chart)
```

**Stop (preserves data):**
```bash
docker compose -f compose.yaml -f compose.observability.yaml stop
```

**Full teardown:**
```bash
docker compose -f compose.yaml -f compose.observability.yaml down --volumes
# Note: this clears Prometheus local TSDB. Elastic data is unaffected.
```

To also delete the metrics stored in Elasticsearch (clean slate without a new project), follow "Reset: stop the stack and wipe all Prometheus data" in `docs/shared/quickstart.md`.

---

## Contributing

This repo is under active development. See `docs/shared/environment-setup-guide.md` for the full project plan, open questions, and build order.

Planned next: finish Module 1 (re-validation, slides, recording), then Module 2 (Remote Write Configuration) and Instruqt sandbox setup.
