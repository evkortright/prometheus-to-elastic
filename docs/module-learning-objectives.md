# PromQL → Elastic Migration Track — Module Learning Objectives

**Instructional Design Reference**
*Last updated: September 2026 — added Module 3.5 (Field Name Alignment)*

---

Seven modules, each written to Bloom's Taxonomy. The first three **remove objections** — nothing breaks. The rest **make the case** — here's what's actually better — before a hands-on lab tests whether the case holds up.

```
Compatibility phase:  01 · 02 · 03 · 03.5
Capability phase:     04
Migration phase:      05
```

---

## Module 01 — PromQL Support
**Format:** Feature Highlight

### Learning Objectives

- **Recognize** which everyday PromQL query patterns — label selectors, aggregation, `rate()` / `increase()` on counters — carry over to Elastic with no syntax changes. *(Remember)*

- **Write and execute** PromQL queries — instant vectors, range vectors reduced by functions, aggregation, arithmetic, vector matching — against a live Elastic TSDS, reproducing results a Prometheus user would already expect. *(Apply)*

- **Identify** specific behavioral differences between Elastic's implementation and vanilla Prometheus — documented tech-preview gaps and any edge-case behavior at query boundaries. *(Analyze)*

### Skills & Knowledge Gained

PromQL syntax fluency on Elastic; TSDS conceptual grounding (series identity, dimensions, metric types); confidence that an existing Prometheus query maps over with its logic intact; an accurate, non-oversold picture of what's still incomplete.

---

## Module 02 — Ingestion Compatibility (Remote Write)
**Format:** Feature Highlight

### Learning Objectives

- **Describe** how the Prometheus Remote Write protocol maps onto Elasticsearch's TSDS ingestion model. *(Understand)*

- **Configure** a Remote Write–compatible agent to ship metrics directly into an Elastic deployment without modifying existing scrape configs or exporters. *(Apply)*

- **Assess** whether a given existing collection setup needs any changes to work against Elastic ingestion, and pinpoint exactly what, if anything, does. *(Evaluate)*

### Skills & Knowledge Gained

Practical Remote Write configuration; a working mental model of how raw ingested metrics become TSDS documents; the specific, narrow judgment of "does my collection layer need to change" rather than a vague sense of compatibility.

---

## Module 03 — Dashboard & Alert Migration Tooling
**Format:** Feature Highlight

### Learning Objectives

- **Explain** what the Observability Migration Platform automates when converting Grafana dashboards and PromQL-based alert rules into Kibana equivalents. *(Understand)*

- **Migrate** a sample exported Grafana dashboard and at least one alert rule using the migration tooling. *(Apply)*

- **Critique** the migrated output against the original for fidelity — distinguishing what transferred cleanly from what needs manual follow-up, and why. *(Evaluate)*

### Skills & Knowledge Gained

Hands-on familiarity with the migration tooling's actual workflow, not just its existence; a validation habit — never trust automated conversion blindly; realistic expectations of where tooling automation currently stops.

---

## Module 03.5 — Field Name Alignment: Preparing for Cross-Signal Correlation
**Format:** Feature Highlight + Lab Exercise
*Inserted after stakeholder review — prerequisite for Module 04*

### Why this module exists

When Prometheus `remote_write` lands data in Elastic, field names are Prometheus-native (underscore notation, flat labels): `service_name`, `host_name`. When traces and logs arrive via OTLP they follow OTel semantic conventions and ECS (dot notation): `service.name`, `host.name`. This mismatch breaks cross-signal correlation queries silently — joins return nulls — unless the gap is explicitly bridged before attempting Module 04.

### Learning Objectives

- **Explain** why Prometheus label naming conventions (underscores) and OTel semantic conventions / ECS (dot notation) diverge, and what the practical consequence is when joining metric results against trace or log data in ES|QL. *(Understand)*

- **Apply** at least two strategies for bridging the field name gap — runtime aliasing via ES|QL `EVAL`, and an Elasticsearch ingest pipeline — selecting the appropriate approach for a given scenario. *(Apply)*

- **Evaluate** the trade-offs between the three resolution options (runtime aliasing, index mapping alias, ingest pipeline) across dimensions of query complexity, operational overhead, and downstream compatibility. *(Evaluate)*

### Skills & Knowledge Gained

A precise mental model of where the Prometheus → OTel naming gap lives and why it matters; practical fluency with both the quick-win (runtime `EVAL`) and production-ready (ingest pipeline) resolution approaches; the habit of checking field name alignment before building cross-signal queries.

### Resolution options reference

| Option | Approach | Effort | Query impact |
|---|---|---|---|
| A — Runtime aliasing | `EVAL service.name = service_name` in each query | Low | Every query must include it |
| B — Index mapping alias | Field alias in index template | Medium | Transparent to queries |
| C — Ingest pipeline | Rename/copy fields on ingest | Higher | Fully transparent, production-ready |

*Module teaches Option A as the quick win, Option C as the production approach.*

---

> **The pivot — objections cleared, the case begins**

---

## Module 04 — Cross-Signal Correlation
**Format:** Deep Dive
*Requires Module 03.5 field alignment to be complete*

### Learning Objectives

- **Describe** why PromQL's self-contained vector/matrix result model has no native join primitive, and how ES|QL's `LOOKUP JOIN` fills exactly that gap. *(Understand)*

- **Build** a query pipeline that starts with a `PROMQL` aggregation and continues into further ES|QL operations to enrich metric results with non-metric data — including traces and logs now flowing to Elastic alongside metrics. *(Apply)*

- **Design** an investigative workflow that would require pivoting across multiple tools in a pure-Prometheus stack but runs as one pipeline here. *(Create)*

### Skills & Knowledge Gained

Practical `LOOKUP JOIN` fluency; the ability to compose `PROMQL` and native ES|QL in a single pipeline rather than treating them as separate tools; a concrete answer, backed by something built, to "what can this actually do that Prometheus can't."

---

## Module 05 — End-to-End Migration (Capstone)
**Format:** Hands-On Lab

### Learning Objectives

- **Execute** an end-to-end migration of a small, realistic Prometheus + Grafana setup — a Remote Write config, one dashboard, one alert rule — into a working Elastic deployment. *(Apply)*

- **Validate** that the migrated queries, dashboard, and alert produce results and behavior equivalent to the original stack, not just superficially similar output. *(Evaluate)*

- **Produce** a personal migration runbook capturing the steps, gotchas, and validation checks hit during the lab — reusable on a real production migration. *(Create)*

### Skills & Knowledge Gained

First-hand migration execution experience, rather than only having watched one demonstrated; a validation methodology for confirming migrated observability assets are actually equivalent; a reusable artifact — the runbook — that is the module's actual deliverable, not just a byproduct of it.

### Scope decisions (validated)

- **Historical data:** Prometheus is retained as the historical record during the cutover period. Elastic becomes the system of record from migration day forward. A future advanced track will cover full historical migration and Prometheus decommission.
- **Parallel running:** Prometheus and Elastic run simultaneously during cutover — Prometheus available for historical queries, Elastic for current data and new capabilities.
- **Decommission:** Out of scope for this track. Covered in the planned follow-on advanced track.

---

## Design notes

**Modules 1–3 share a shape** (feature highlight, "nothing breaks") and can likely reuse the same exercise pattern already proven out in this track: a controlled synthetic setup, verified live against a real deployment, with honesty about anything not yet confirmed.

**Module 3.5 is a bridge, not a detour.** It exists because Module 4 silently fails without it — learners who attempt cross-signal correlation without field alignment get null results and lose confidence in the platform. Teaching the why before the what makes Module 4 land correctly.

**Module 4 is a different shape** (capability demonstration, not compatibility demonstration) — the exercises should feel like "here's something you could not do before," not "here's proof nothing broke."

**Module 5 is the hinge the whole track is graded on.** Everything before it is persuasion; this is where persuasion either converts into action or doesn't. Worth the most build investment.

**Deferred, not abandoned:** A cardinality/storage-economics deep dive and a dedicated limitations appendix were both scoped and cut per stakeholder review — the team felt neither belongs in this track's current form (limitations discussion should wait until a learner actually raises it, rather than being surfaced proactively). If either becomes relevant later, both sets of objectives still exist in the original document's revision history and can be reintroduced without rebuilding from scratch.

**Future track (planned):** Full Prometheus decommission — historical data migration, parity validation, cutover, decommission. This is where the "completely move to Elastic" story completes.
