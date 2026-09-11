# PromQL → Elastic Migration — Training Curriculum

**Instructional Design Reference**
*Last updated: September 2026*

---

## The learning journey

This curriculum is designed for enterprise Prometheus operators. The migration is structured in two tracks that reflect how real infrastructure migrations actually happen in large organizations — not as a forced cutover, but as a deliberate, confidence-building journey at the learner's own pace.

**Track 1 is risk-free.** You add one `remote_write` block to Prometheus. If you don't like what you see, you remove it and nothing changed. There's no commitment, no downtime, no migration risk. Prometheus keeps running. Grafana keeps working. You explore Elastic alongside what you already have.

**Track 2 is the commitment.** You've been running both systems in parallel. You've rebuilt your dashboards and alerts. You've explored cross-signal correlation. You know Elastic works. Now you're ready to say goodbye to Prometheus — not because someone told you to, but because you chose to.

This is not a "rip and replace" story. It's a "try this alongside what you have, and decide for yourself" story. That distinction matters for enterprise audiences who cannot afford downtime or regret.

---

## The four stages of migration

```
Stage 1 — Metrics in Elastic, everything else unchanged
  Prometheus remote_writes to Elastic
  Grafana still works · Prometheus still runs
  → Covered by Track 1, Modules 1–3

Stage 2 — Field alignment + cross-signal preview
  Normalize field names for future signal joining
  Preview cross-signal correlation with metrics + lookup data
  → Covered by Track 1, Modules 3.5–4

Stage 3 — Full OTel signals to Elastic
  Traces + logs added via OTel Collector / EDOT
  Kibana becomes primary observability interface
  Prometheus still running in parallel
  → Covered by Track 2

Stage 4 — Decommission Prometheus and Grafana
  Historical data migration · parity validation
  Cutover · switch off Prometheus
  → Covered by Track 2
```

---

## Track 1: Prometheus to Elastic — Metrics Migration

**Audience:** Prometheus + Grafana operators considering Elastic
**Commitment required:** None — Prometheus keeps running throughout
**Ends with:** Metrics in Elastic, dashboards and alerts migrated, cross-signal correlation previewed, Prometheus still running in parallel

Seven modules written to Bloom's Taxonomy. The first three **remove objections** — nothing breaks. The rest **make the case** — here's what's actually better.

```
Compatibility phase:  01 · 02 · 03 · 03.5
Capability phase:     04
Migration phase:      05
```

---

### Module 01 — PromQL Support
**Format:** Feature Highlight

#### Learning Objectives

- **Recognize** which everyday PromQL query patterns — label selectors, aggregation, `rate()` / `increase()` on counters — carry over to Elastic with no syntax changes. *(Remember)*

- **Write and execute** PromQL queries — instant vectors, range vectors reduced by functions, aggregation, arithmetic, vector matching — against a live Elastic TSDS, reproducing results a Prometheus user would already expect. *(Apply)*

- **Identify** specific behavioral differences between Elastic's implementation and vanilla Prometheus — documented tech-preview gaps and any edge-case behavior at query boundaries. *(Analyze)*

#### Skills & Knowledge Gained

PromQL syntax fluency on Elastic; TSDS conceptual grounding (series identity, dimensions, metric types); confidence that an existing Prometheus query maps over with its logic intact; an accurate, non-oversold picture of what's still incomplete.

---

### Module 02 — Ingestion Compatibility (Remote Write)
**Format:** Feature Highlight

#### Learning Objectives

- **Describe** how the Prometheus Remote Write protocol maps onto Elasticsearch's TSDS ingestion model. *(Understand)*

- **Configure** a Remote Write–compatible agent to ship metrics directly into an Elastic deployment without modifying existing scrape configs or exporters. *(Apply)*

- **Assess** whether a given existing collection setup needs any changes to work against Elastic ingestion, and pinpoint exactly what, if anything, does. *(Evaluate)*

#### Skills & Knowledge Gained

Practical Remote Write configuration; a working mental model of how raw ingested metrics become TSDS documents; the specific, narrow judgment of "does my collection layer need to change" rather than a vague sense of compatibility.

---

### Module 03 — Dashboard & Alert Migration Tooling
**Format:** Feature Highlight

#### Learning Objectives

- **Explain** what the Observability Migration Platform automates when converting Grafana dashboards and PromQL-based alert rules into Kibana equivalents. *(Understand)*

- **Migrate** a sample exported Grafana dashboard and at least one alert rule using the migration tooling. *(Apply)*

- **Critique** the migrated output against the original for fidelity — distinguishing what transferred cleanly from what needs manual follow-up, and why. *(Evaluate)*

#### Skills & Knowledge Gained

Hands-on familiarity with the migration tooling's actual workflow, not just its existence; a validation habit — never trust automated conversion blindly; realistic expectations of where tooling automation currently stops.

---

### Module 03.5 — Field Name Alignment: Preparing for Cross-Signal Correlation
**Format:** Feature Highlight + Lab Exercise
*Prerequisite for Module 04 — inserted after validation confirmed silent join failures without it*

#### Why this module exists

When Prometheus `remote_write` lands data in Elastic, field names are Prometheus-native (underscore notation): `service_name`, `host_name`. When traces and logs arrive via OTLP they follow OTel semantic conventions and ECS (dot notation): `service.name`, `host.name`. This mismatch breaks cross-signal correlation queries silently — joins return nulls — unless the gap is explicitly bridged. This module bridges it before Module 04 attempts cross-signal work.

#### Learning Objectives

- **Explain** why Prometheus label naming conventions (underscores) and OTel semantic conventions / ECS (dot notation) diverge, and what the practical consequence is when joining metric results against trace or log data in ES|QL. *(Understand)*

- **Apply** at least two strategies for bridging the field name gap — runtime aliasing via ES|QL `EVAL`, and an Elasticsearch ingest pipeline — selecting the appropriate approach for a given scenario. *(Apply)*

- **Evaluate** the trade-offs between the three resolution options (runtime aliasing, index mapping alias, ingest pipeline) across dimensions of query complexity, operational overhead, and downstream compatibility. *(Evaluate)*

#### Skills & Knowledge Gained

A precise mental model of where the Prometheus → OTel naming gap lives and why it matters; practical fluency with both the quick-win (runtime `EVAL`) and production-ready (ingest pipeline) resolution approaches; the habit of checking field name alignment before building cross-signal queries.

#### Resolution options reference

| Option | Approach | Effort | Query impact |
|---|---|---|---|
| A — Runtime aliasing | `EVAL service.name = service_name` in each query | Low | Every query must include it |
| B — Index mapping alias | Field alias in index template | Medium | Transparent to queries |
| C — Ingest pipeline | Rename/copy fields on ingest | Higher | Fully transparent, production-ready |

*Module teaches Option A as the quick win, Option C as the production approach.*

---

> **The pivot — objections cleared, the case begins**

---

### Module 04 — Cross-Signal Correlation
**Format:** Deep Dive
*Requires Module 03.5 field alignment to be complete*

#### Learning Objectives

- **Describe** why PromQL's self-contained vector/matrix result model has no native join primitive, and how ES|QL's `LOOKUP JOIN` fills exactly that gap. *(Understand)*

- **Build** a query pipeline that starts with a `PROMQL` aggregation and continues into ES|QL operations to enrich metric results with non-metric data. *(Apply)*

- **Design** an investigative workflow that would require pivoting across multiple tools in a pure-Prometheus stack but runs as one pipeline in Elastic. *(Create)*

#### Skills & Knowledge Gained

Practical `LOOKUP JOIN` fluency; the ability to compose `PROMQL` and native ES|QL in a single pipeline; a concrete answer, backed by something built, to "what can this actually do that Prometheus can't."

---

### Module 05 — End-to-End Migration (Capstone)
**Format:** Hands-On Lab

#### Learning Objectives

- **Execute** an end-to-end migration of a small, realistic Prometheus + Grafana setup — a Remote Write config, one dashboard, one alert rule — into a working Elastic deployment. *(Apply)*

- **Validate** that the migrated queries, dashboard, and alert produce results and behavior equivalent to the original stack, not just superficially similar output. *(Evaluate)*

- **Produce** a personal migration runbook capturing the steps, gotchas, and validation checks encountered during the lab — reusable on a real production migration. *(Create)*

#### Skills & Knowledge Gained

First-hand migration execution experience; a validation methodology for confirming migrated observability assets are actually equivalent; a reusable runbook that is the module's actual deliverable.

#### Scope decisions

- **Historical data:** Prometheus is retained as the historical record during cutover. Elastic becomes the system of record from migration day forward.
- **Parallel running:** Prometheus and Elastic run simultaneously — Prometheus for historical queries, Elastic for current data and new capabilities. There is no deadline to decommission.
- **Decommission:** Out of scope for Track 1. Covered in Track 2.

---

## Track 2: Full Elastic Observability — Complete Cutover
**Status:** Planned — not yet built

**Audience:** Learners who have completed Track 1 and are ready to commit
**Commitment required:** This is the real migration — Prometheus will be decommissioned
**Starts with:** Metrics already in Elastic, dashboards and alerts already migrated
**Ends with:** Prometheus off, Grafana off, full Elastic O11y as the sole system

### The narrative arc

Track 1 built confidence through parallel operation. The learner has been running Elastic alongside Prometheus — possibly for weeks or months. They've seen it work. They've rebuilt their dashboards. They've explored cross-signal correlation. Now they're ready to make the commitment.

Track 2 is not a tutorial. It's an execution guide for someone who has already decided.

### Planned modules

#### Track 2, Module A — Bringing in Traces and Logs
Add traces and logs to Elastic via the OTel Collector / EDOT. Configure `otelcol-config-extras.yml` to export to Elastic APM and Elastic logs alongside (or instead of) the existing Jaeger and OpenSearch destinations. Kibana becomes the primary observability interface for all three signals.

#### Track 2, Module B — Full Cross-Signal Correlation
With all three signals in Elastic, build the complete cross-signal workflows that were only previewed in Track 1 Module 04. Real traces + real logs + metrics in one ES|QL pipeline. No lookup index workarounds — the data is all there.

#### Track 2, Module C — Historical Data Migration
Migrate historical Prometheus data to Elastic so the timeline is unbroken after decommission. Approaches: Prometheus snapshot export, backfill via remote_write replay, or accepting a clean cutover date and archiving the Prometheus data separately.

#### Track 2, Module D — Parity Validation and Cutover
Validate that Elastic and Prometheus produce equivalent results for all critical queries and alerts before switching off Prometheus. Cutover procedure. Decommission checklist. Rollback plan.

---

## Design notes

**Modules 1–3 share a shape** (feature highlight, "nothing breaks") and reuse the same exercise pattern: a controlled setup verified live against a real deployment, with honesty about anything not yet confirmed.

**Module 3.5 is a bridge, not a detour.** It exists because Module 4 silently fails without it. Teaching the why before the what makes Module 4 land correctly.

**Module 4 is a different shape** (capability demonstration, not compatibility demonstration) — exercises should feel like "here's something you could not do before," not "here's proof nothing broke."

**Module 5 is the hinge Track 1 is graded on.** Everything before it is persuasion; this is where persuasion either converts into action or doesn't. Worth the most build investment.

**Track 2 requires Track 1 as a prerequisite.** A learner who attempts Track 2 without Track 1 experience is attempting a commitment without confidence. The parallel-running period is not optional ceremony — it's the confidence-building mechanism the whole curriculum depends on.

**Deferred, not abandoned:** A cardinality/storage-economics deep dive and a dedicated limitations appendix were scoped and cut per stakeholder review — limitations discussion should wait until a learner raises it, not be surfaced proactively. Both can be reintroduced without rebuilding from scratch.
