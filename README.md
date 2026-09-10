# Prometheus to Elastic Migration — Training Track

A hands-on training series for Prometheus and Grafana users migrating to the Elastic Stack. Built around the [OpenTelemetry Astronomy Shop](https://github.com/open-telemetry/opentelemetry-demo) as the source observability system.

## What this is

A complete curriculum — feature highlight videos, lab exercises, and Instruqt sandbox environments — that walks a Prometheus operator through migrating their metrics stack to Elastic Serverless, one step at a time.

The core message: **your PromQL works in Elastic unchanged**. The migration adds capability — ES|QL pipelines, cross-signal correlation, dashboard and alert migration tooling — without requiring your team to relearn their existing workflows on day one.

---

## Architecture

```
OTel Astronomy Shop (30 microservices)
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
| 1 | PromQL Compatibility | ✅ Complete — script, cheat sheet, rehearsed |
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
elastic-migration/
├── README.md
├── .gitignore
├── docs/
│   ├── environment-setup-guide.md   # Full setup plan, validated steps, open questions
│   └── diagrams/
│       ├── 01_source_state.svg      # OTel demo before migration
│       ├── 01_source_state.png
│       ├── 02_bridge_state.svg      # With remote_write bridge
│       ├── 02_bridge_state.png
│       ├── 03_module4_esql.svg      # ES|QL cross-signal correlation
│       ├── 03_module4_esql.png
│       ├── 04_edot_optional.svg     # EDOT as optional layer
│       └── 04_edot_optional.png
├── modules/
│   └── module1-promql-compatibility/
│       ├── recording-script-final.md   # Use this for recording
│       ├── promql-cheatsheet.md        # Query reference
│       └── demo-script.md              # Working draft (superseded by final)
├── config/
│   ├── prometheus-config.yaml          # With remote_write block — copy over otel demo default
│   ├── compose.observability.yaml      # With 512MB Prometheus memory limit fix
│   └── .env.example                    # Template — copy to .env.elastic and fill in values
└── instruqt/                           # To be built
    ├── track.yml
    └── challenges/
```

---

## Local setup

### Prerequisites

- Docker Desktop (Apple Silicon) with **≥12 GB RAM** allocated
- Docker Compose v2.x
- An Elastic Serverless **Observability Complete** project on [cloud.elastic.co](https://cloud.elastic.co)
- Git

### 1. Clone the OTel demo (pinned version)

```bash
mkdir -p ~/projects/elastic-migration
cd ~/projects/elastic-migration

git clone --depth 1 --branch 3.0.0 \
  https://github.com/open-telemetry/opentelemetry-demo.git

cd opentelemetry-demo
```

### 2. Apply config patches

```bash
# Copy the patched Prometheus config (includes remote_write block)
cp ../config/prometheus-config.yaml src/prometheus/prometheus-config.yaml

# Copy the patched observability compose (512MB Prometheus memory limit)
cp ../config/compose.observability.yaml compose.observability.yaml
```

### 3. Set up Elastic credentials

```bash
# Copy the template
cp ../config/.env.example ../.env.elastic

# Edit with your actual values
# ES_ENDPOINT=https://<project-id>.es.<region>.gcp.elastic.cloud
# ES_API_KEY=<your-encoded-api-key>
nano ../.env.elastic
```

> ⚠️ `.env.elastic` is gitignored — never commit it.

### 4. Verify connectivity

```bash
source ../.env.elastic

# Should return 200
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  "${ES_ENDPOINT}"

# Should return 405 (endpoint exists, POST only)
curl -s -o /dev/null -w "%{http_code}" \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  -H "Content-Type: application/x-protobuf" \
  "${ES_ENDPOINT}/_prometheus/api/v1/write"
```

### 5. Start the stack

```bash
cd ~/projects/elastic-migration/opentelemetry-demo

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

### 6. Verify data is flowing to Elastic

```bash
source ../.env.elastic
curl -s \
  -H "Authorization: ApiKey ${ES_API_KEY}" \
  "${ES_ENDPOINT}/_cat/indices/metrics-*?h=index,docs.count"
```

Expect a non-zero document count within 2–3 minutes.

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
The default 200MB memory limit in `compose.observability.yaml` is insufficient after several days of running with `remote_write` active. The patched `compose.observability.yaml` in this repo sets it to 512MB. If Prometheus crash-loops with exit code 137, check its memory limit.

**macOS Docker Desktop bind mount**
Editing `prometheus-config.yaml` on the host does not refresh inside the container automatically. Always restart the Prometheus container after editing:
```bash
docker restart prometheus
```

**Grafana Demo Dashboard shows "No data"**
The Demo Dashboard requires OpenSearch (logs) and Jaeger (traces). Use the **Spanmetrics Demo Dashboard** instead for Module 1 — it is driven purely by Prometheus metrics and populates immediately.

---

## Daily workflow

**Start:**
```bash
cd ~/projects/elastic-migration/opentelemetry-demo
docker compose -f compose.yaml -f compose.observability.yaml up --detach
# Wait 15+ minutes before recording — Prometheus needs time to build stable rate() windows
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

---

## Contributing

This repo is under active development. See `docs/environment-setup-guide.md` for the full project plan, open questions, and build order.

Planned next: Module 2 (Remote Write Configuration) and Instruqt sandbox setup.
