# OTel Collector — Role Inside the Astronomy Shop

The OTel Collector is the central telemetry hub for the entire OTel Astronomy Shop. Understanding what it does is important for the training track because the metrics that land in Elastic via remote-write are shaped by the Collector, not just by the services themselves.

---

## What the Collector does

### 1. Receives telemetry from all services

All 16 microservices push their traces, metrics, and logs to the Collector via OTLP on port 4317 (gRPC) or 4318 (HTTP). The services do not know or care where the data goes — that is the Collector's responsibility. This is the OTel design principle: instrument once, route anywhere.

### 2. Generates span metrics (most important for this track)

The Collector runs a `spanmetrics` connector that derives RED metrics — Rate, Errors, Duration — from trace spans. This is where the following metrics come from:

- `traces_span_metrics_calls_total` — request rate per service and span
- `traces_span_metrics_duration_milliseconds_bucket/count/sum` — latency histograms

These metrics are **not emitted by the services themselves**. They are computed by the Collector from trace data. This is why they cover all 19 services in the demo — every service that emits traces automatically gets span metrics, without any additional instrumentation.

This is the primary metric used in the Module 1 feature highlight video.

### 3. Scrapes infrastructure metrics

The Collector also acts as a Prometheus scraper, collecting metrics from:

| Source | Metrics |
|---|---|
| Redis / Valkey | Memory, connections, commands, keyspace |
| PostgreSQL | Backends, operations, table stats, index stats |
| Kafka | Consumer lag, throughput, partition offsets |
| Docker | Container CPU, memory, network, block I/O |
| Host | CPU, memory, disk, network, filesystem |
| nginx (image provider) | Connections, requests |
| Ad service | Native `/metrics` endpoint — demonstrates bridging existing Prometheus instrumentation |

### 4. Exports to multiple backends

In the observability configuration (`otelcol-config-observability.yml`), the Collector fans out to three destinations:

| Destination | Signal | Protocol |
|---|---|---|
| Prometheus | Metrics | OTLP push to `http://prometheus:9090/api/v1/otlp` |
| Jaeger | Traces | OTLP gRPC |
| OpenSearch | Logs | OpenSearch HTTP |

Note: In v3.0.0, the Collector **pushes** metrics to Prometheus via OTLP. Prometheus does not scrape the Collector. This is the opposite of the traditional Prometheus pull model.

### 5. Manages OpAMP connection

The Collector maintains a WebSocket connection to the OpAMP server for remote configuration management. This is visible in the demo's OpAMP UI at `http://localhost:8080/opamp/`.

---

## Why this matters for the training track

**The metrics in Elastic are richer than a typical Prometheus setup.**
A standard Prometheus deployment scrapes exporters for infrastructure metrics. The Astronomy Shop goes further — it also computes span metrics from traces via the `spanmetrics` connector. A learner migrating from a vanilla Prometheus setup may not have `traces_span_metrics_*` metrics. This is worth calling out in Module 2 when discussing what is actually flowing via remote-write.

**The data flow is OTLP-first, not scrape-first.**
In v3.0.0, Prometheus receives metrics via OTLP push from the Collector, not by scraping a `/metrics` endpoint. This is a significant architectural shift from earlier versions of the demo and from traditional Prometheus deployments. The migration story is unchanged — Prometheus still holds the data and still supports remote-write — but the internal plumbing is different from what learners may expect.

**The extension point is `otelcol-config-extras.yml`.**
This file is intentionally empty and is loaded last, merging with the base configuration. It is the designed extension point for adding Elastic as a direct OTLP destination in Track 2, bypassing Prometheus entirely. See the architecture diagrams for the EDOT optional layer (Diagram 4).

---

## Config files reference

| File | Purpose |
|---|---|
| `src/otel-collector/otelcol-config.yml` | Base configuration — receivers, processors, core exporters |
| `src/otel-collector/otelcol-config-observability.yml` | Adds Jaeger, Prometheus, OpenSearch exporters |
| `src/otel-collector/otelcol-config-full.yml` | Adds Kafka receiver for the full stack |
| `src/otel-collector/otelcol-config-extras.yml` | Empty — extension point for custom exporters |
