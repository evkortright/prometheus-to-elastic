# Module 1 Demo Script: PromQL Compatibility
## Feature Highlight Video — Recording Guide

**Runtime:** ~8–10 minutes
**Validated:** August 14, 2026 — all timings confirmed from live dry run

---

## Pre-recording setup (do before hitting record)

- [ ] Stack is running: `docker compose ps` — all containers Up
- [ ] Kibana open at Discover → ES|QL mode
- [ ] Prometheus open in a second tab at `http://localhost:9090`
- [ ] Feature flags open in a third tab at `http://localhost:8080/feature`
- [ ] `paymentFailure` flag confirmed **off**
- [ ] Time picker in Kibana set to **Last 15 minutes**
- [ ] No API keys, terminal, or `.env.elastic` visible on screen
- [ ] Run the baseline query once before recording — confirm it returns results
- [ ] Switch to **chart view** — do not start in table view

---

## Scene 1 — The setup (60 seconds)

**Say:**
> "If you're running Prometheus today, this is your world: metrics flowing into Prometheus,
> Grafana dashboards on top, PromQL as your query language. You've invested in this stack.
> Your team knows PromQL. Your dashboards are built around it.
>
> The question isn't whether Elastic is powerful — it's whether migrating means
> throwing away everything you've built. Today I want to show you it doesn't."

**Do:** Show the Grafana demo dashboard briefly at `http://localhost:8080/grafana/`
— just enough to establish the source world. Don't linger.

---

## Scene 2 — The same query, new destination (2 minutes)

**Switch to Kibana Discover tab.**

**Say:**
> "This is Kibana. The data you're looking at came from Prometheus — via a single
> remote_write block I added to my Prometheus config. One change. Nothing else touched."

**Type and run Query 1** (already in chart view):

```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
```

**Say:**
> "This is PromQL. The exact same syntax you'd write in Grafana.
> I didn't change a single character. I just changed where it runs."

**Point at the chart** — multi-line, one per service.

> "Every service in the store. Frontend, checkout, payment, cart — all of them.
> Same metric, same query language, running against Elastic."

**Switch to table view briefly:**
> "Same query — table view this time. 1,500 results. Every service, every step interval."

**Switch back to chart.**

---

## Scene 3 — The side-by-side (90 seconds)

**Switch to Prometheus tab.**

**Say:**
> "Here's the same query in Prometheus."

**Type and run:**
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

> "19 result series. Same services. Same metric. Same PromQL.
> Your existing Prometheus stack — I didn't touch it. It's still running."

**Tab switch back to Kibana.**

> "And here it is in Elastic. Both systems have the same data.
> Your team doesn't need to relearn anything on day one."

---

## Scene 4 — Going further (90 seconds)

**Say:**
> "But here's where it gets interesting. PromQL is great at time-series math.
> What it can't do is pipe that result into something else.
> In Elastic, it can."

**Run Query 2:**

```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
| SORT request_rate DESC
| LIMIT 5
```

> "The PROMQL block is unchanged. The pipe after it is ES|QL.
> I'm sorting and limiting a Prometheus result set — something you can't do in pure PromQL."

---

## Scene 5 — Live failure injection (3–4 minutes)

**The query for this scene** — run in Kibana Discover, chart view:

```esql
PROMQL index=metrics-generic.prometheus-default
  error_rate=(sum(rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR", service_name="payment"}[5m])))
```

**Time picker:** Last 30 minutes — shows the organic error pattern clearly.

**⚠️ Key insight from dry run:** The payment service has an organic error cycle — errors
appearing at ~0.004 req/s in a repeating hump pattern every ~10 minutes. This is the load
generator hitting a payment edge case. Use this as your "before" baseline — it makes the
injected failure contrast much more dramatic and the story more realistic.

**Part 1 — Establish the baseline (60 seconds)**

**Run the query and switch to chart view. Point at the humps. Say:**

> "Before I inject anything, let me show you something interesting.
> The payment service already has an error pattern. See these humps?
> Errors appearing every few minutes, then dropping to zero.
> That's organic — the load generator hitting a payment edge case repeatedly.
>
> In Grafana, seeing this alongside your request rate means a separate panel,
> a separate query, a separate dashboard. Here I just changed the metric selector.
> Same PromQL. Same interface. One query."

**Part 2 — Inject the failure**

**Switch to feature flags tab** (`http://localhost:8080/feature`).

> "Now let me show you what happens when a real incident hits.
> I'm going to set payment failures to 25%."

**Set `paymentFailure` to `25%`. Save. Switch back to Kibana immediately.**

> "That baseline pattern you saw at around 0.004 requests per second?
> Watch what happens."

**Part 3 — Watch the spike (3–4 minutes)**

**Hit Search every 60 seconds. Stay in chart view the whole time.**

> *(after 1st refresh)* "Prometheus scrape interval is 60 seconds — give it a moment."
> *(after 2nd–3rd refresh, when spike appears)* "There it is."

**Point at the spike — error rate should jump from ~0.004 to ~0.04–0.06 req/s:**

> "That's a 10x increase in payment errors — visible in Elastic, automatically,
> because Prometheus is remote_writing everything it sees.
> I wrote one query. I didn't build a pipeline. I didn't configure an alert.
> I just asked: show me the payment error rate."

**Part 4 — Recovery**

**Switch to feature flags tab. Set `paymentFailure` back to `off`. Switch back to Kibana.**

> "Incident resolved. The rate will drain out of the 5-minute window in a few minutes.
> Watch the recovery in real time — the same way you would in Grafana."

---

## Timing summary (updated from September 10 dry run)

| Event | Time from flag toggle |
|---|---|
| Flag set to 25% | 0:00 |
| Spike visible in chart | ~3–4 min |
| Spike fully stabilized | ~5–6 min |
| Rate back to baseline after flag off | ~5 min (rate window drains) |

**Organic baseline error rate:** ~0.004 req/s (humped pattern, ~5 min on / ~5 min off)
**Injected error rate:** ~0.04–0.06 req/s (~10x baseline)

---

## Scene 6 — The close (30 seconds)

**Say:**
> "Same PromQL. Same metrics. Same query patterns your team already knows.
> The difference is what you can do next — pipe into ES|QL, join against other data,
> correlate with logs and traces in the same query.
>
> That's what we'll cover in the next module."

---

## Timing summary (from dry run)

| Event | Time from flag toggle |
|---|---|
| Flag set to 25% | 0:00 |
| First error rows in table (scroll required) | ~3–4 min |
| Error line visible in chart | ~3–4 min (check chart, not table) |
| Error line fully stabilized | ~8 min |
| Error line gone after flag off | ~5 min (rate window drains) |

---

## Contingency notes

**If errors don't appear after 5 minutes:**
- Check chart view — don't trust table sort order
- Verify flag is still set: `http://localhost:8080/feature` → Advanced view
- Check `paymentFailure` defaultVariant is `"25%"` not `"off"`

**If Kibana query is slow:**
- Normal — 2K documents processed, ~500–750ms is expected
- Don't apologize for it on camera — it's live data

**If asked about STATUS_CODE_UNSET:**
- It means the span completed without setting an explicit error status
- In OTel, success is the absence of an error status — UNSET = OK for most spans
- STATUS_CODE_ERROR is explicitly set by the application when something goes wrong

**If asked why flagd has errors:**
- It's the feature flag service polling for configuration changes
- Infrastructure noise — not application errors
- Good opportunity to say "this is why filtering by service_name matters"
