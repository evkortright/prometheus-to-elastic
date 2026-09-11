# Module 1 — Feature Highlight Video: PromQL Compatibility
## Final Recording Script

**Runtime:** ~8–10 minutes
**Last rehearsed:** September 10, 2026 — all queries and timings validated

---

## Pre-recording checklist

Run through every item before hitting record.

**Stack:**
- [ ] Stop any unrelated containers first: `docker stop edu-ctfd-nginx-1 edu-ctfd-cache-1 edu-ctfd-db-1 2>/dev/null`
- [ ] Verify Prometheus is running and healthy:
  ```bash
  docker ps --filter "name=prometheus" --format "table {{.Names}}	{{.Status}}"
  curl -s 'http://localhost:9090/api/v1/query?query=up' | python3 -m json.tool | grep '"status"'
  ```
  Both should return `Up X minutes` and `"status": "success"`. If Prometheus is missing or exited:
  ```bash
  cd ~/personal/projects/elastic-migration/opentelemetry-demo
  docker compose -f compose.yaml -f compose.observability.yaml up --detach --force-recreate prometheus
  # Wait 5 minutes before continuing
  ```
- [ ] `docker compose -f compose.yaml -f compose.observability.yaml ps` — all other containers Up
- [ ] Stack has been running for **at least 15 minutes** — Prometheus needs this to build a stable rate window

**Browser tabs — set up in this order before recording:**
- [ ] **Tab 1 — Grafana:** `http://localhost:8080/grafana/` → Dashboards → Demo folder → **Spanmetrics Demo Dashboard** — confirm panels are populated
- [ ] **Tab 2 — Kibana Discover:** Query 1 already typed and run, **chart view**, time picker set to **Last 30 minutes**
- [ ] **Tab 3 — Prometheus:** `http://localhost:9090` → Query tab → Query 1 already typed and executed → **Graph tab** → time range set to **5m**
- [ ] **Tab 4 — Feature flags:** `http://localhost:8080/feature` → confirm `paymentFailure` is set to **off**

**Kibana Query 1 pre-loaded (Tab 2):**
```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
| WHERE service_name IN ("frontend", "checkout", "cart", "payment", "shipping", "recommendation")
```

**Prometheus Query pre-loaded (Tab 3):**
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

**Kibana Query 3 ready to paste (Scene 5):**
```esql
PROMQL index=metrics-generic.prometheus-default
  error_rate=(sum(rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR", service_name="payment"}[5m])))
```

**Final checks:**
- [ ] No terminal windows, `.env` files, or API keys visible anywhere on screen
- [ ] Kibana chart is showing stable flat lines — not ramping up
- [ ] Prometheus graph at 5m is showing stable flat lines — not ramping up
- [ ] Grafana Spanmetrics dashboard panels are all populated with data
- [ ] `paymentFailure` flag confirmed **off**

---

## Scene 1 — The setup (45 seconds)

**Tab: Grafana — Spanmetrics Demo Dashboard**

Scroll slowly to show both the latency gauges (top left) and the request rate bars (top right).
Pause for 5 seconds — let the audience take it in.

**Say:**
> "If you're running Prometheus today, this is your world. Metrics flowing in, Grafana on top,
> PromQL as your query language. You've invested in this stack. Your team knows it.
> Your dashboards are built around it.
>
> The question is — do you have to throw all of this away to move to Elastic?
> Let's find out."

---

## Scene 2 — The same query, new destination (2 minutes)

**Switch to Tab 2 — Kibana Discover, chart view, Query 1 already showing.**

**Say:**
> "This is Kibana. The data you're looking at came from Prometheus — via a single
> remote_write block I added to my Prometheus config. One change. Nothing else touched."

Point at the query text at the top of the screen.

> "And this query — this is PromQL. The exact same syntax you'd write in Grafana.
> I didn't change a single character. I just changed where it runs."

Point at the chart — multiple colored lines, one per service.

> "Every core service in the store. Frontend, checkout, cart, payment, shipping,
> recommendation — all of them. Same metric, same query language, running against Elastic."

**Switch to table view** (click the table icon — middle of the three icons top left of results).

> "Same query — table view this time. One row per service per time step.
> Every data point Prometheus collected, queryable here."

**Switch back to chart view.**

---

## Scene 3 — The side-by-side (90 seconds)

**Switch to Tab 3 — Prometheus, Graph tab, 5m time range.**

> "Here's the same query in Prometheus."

Point at the query text.

> "Same metric. Same PromQL. Your existing stack — I didn't touch it. It's still running.
> These are the same services, the same traffic patterns you just saw in Kibana."

Point at the step-function lines.

> "Notice the steps — that's Prometheus's 60-second scrape interval.
> That's how Prometheus graphs look."

**Switch to Tab 2 — Kibana chart.**

> "And here it is in Elastic. Smoother interpolation, same data.
> Two systems. Both running. Both showing the same metrics.
> Your team doesn't need to relearn anything on day one."

Pause 3 seconds on the chart.

---

## Scene 4 — Going further (90 seconds)

**Stay in Tab 2 — Kibana. Clear the query and type Query 2. Switch to table view.**

**Query 2:**
```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
| WHERE service_name IN ("frontend", "checkout", "cart", "payment", "shipping", "recommendation")
| STATS max_rate = MAX(request_rate) BY service_name
| SORT max_rate DESC
```

**Say:**
> "But here's where it gets interesting."

Point at line 1–2 of the query.

> "The PROMQL block is unchanged — that's still the same rate query."

Point at lines 3–4.

> "The pipes after it are ES|QL. I asked: give me the peak rate per service,
> sorted highest to lowest. One query. No dashboard. No separate tool."

Point at the 6-group result table — frontend at top, payment at bottom.

> "In pure PromQL you'd reach for topk() — and you still couldn't get a clean
> ranked table like this. Here it's just a pipe.
>
> This is the beginning of what becomes possible when your metrics live in Elastic."

---

## Scene 5 — Live incident (4–5 minutes)

**Stay in Tab 2 — Kibana. Clear the query and type Query 3. Switch to chart view.**

**Query 3:**
```esql
PROMQL index=metrics-generic.prometheus-default
  error_rate=(sum(rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR", service_name="payment"}[5m])))
```

**Time picker: Last 30 minutes. Run it. Switch to chart view.**

**Part 1 — Establish the baseline (30 seconds)**

Point at the organic hump pattern.

> "Before I inject anything, let me show you something interesting.
> The payment service already has an error pattern. See these humps?
> Errors appearing every few minutes, then dropping back to zero.
> That's organic — the load generator hitting a payment edge case naturally."

> "In your current Grafana setup, seeing this alongside your request rate
> means a separate panel, a separate query, a separate dashboard.
> Here I just changed the metric selector. Same PromQL. Same interface."

**Part 2 — Inject the failure**

**Switch to Tab 4 — Feature flags.**

> "Now let me show you what happens when a real incident hits.
> The OTel demo has a feature flag system — I'm going to set payment failures to 25%."

**Set `paymentFailure` to `25%`. Save.**

**Switch immediately back to Tab 2 — Kibana.**

> "That baseline you saw — around 0.004 requests per second?
> Watch what happens."

**Part 3 — Watch the spike**

**Hit Search every 60 seconds. Stay in chart view.**

*(after 1st refresh — no change yet)*
> "Prometheus scrape interval is 60 seconds — give it a moment."

*(after 2nd refresh — spike starting to appear)*
> "There it is."

Point at the rising line on the right edge of the chart.

> "Payment errors climbing — visible in Elastic automatically,
> because Prometheus is remote_writing everything it sees.
> I wrote one query. I didn't build a pipeline. I didn't set up an alert.
> I just asked: show me the payment error rate."

*(after 3rd refresh — spike fully visible, ~5x baseline)*
> "That's a 5 to 10x increase in payment errors against the organic baseline.
> The kind of signal that would page your on-call engineer."

**Part 4 — Recovery**

**Switch to Tab 4. Set `paymentFailure` back to `off`. Switch back to Tab 2.**

> "Incident resolved. Watch the right edge of the chart over the next few minutes —
> the rate will drain out of the 5-minute window as the errors stop accumulating.
> Recovery, visible in real time. The same way it would work in Grafana —
> except now it's in Elastic, ready for everything we'll show in the next module."

---

## Scene 6 — The close (30 seconds)

**Stay in Tab 2 — Kibana, error rate chart showing the full incident arc.**

> "Same PromQL. Same metrics. Same query patterns your team already knows.
>
> What changed is what you can do next. Pipe into ES|QL. Sort, filter, aggregate —
> right here, on top of your Prometheus data, without a separate tool.
>
> In Module 2 we'll look at how the Remote Write configuration works under the hood —
> so you understand exactly what's flowing, and how to set it up yourself from scratch."

---

## Timing reference

| Scene | Duration | Key action |
|---|---|---|
| Scene 1 | 45 sec | Show Grafana Spanmetrics dashboard |
| Scene 2 | 2 min | Run Query 1, chart + table |
| Scene 3 | 90 sec | Tab switch Kibana ↔ Prometheus Graph |
| Scene 4 | 90 sec | Run Query 2, table view |
| Scene 5 | 4–5 min | Error rate chart, flag toggle, spike, recovery |
| Scene 6 | 30 sec | Close on error chart |
| **Total** | **~10 min** | |

---

## Query reference card

**Query 1 — Multi-service request rate (Scenes 2 & 3):**
```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
| WHERE service_name IN ("frontend", "checkout", "cart", "payment", "shipping", "recommendation")
```

**Query 2 — Peak rate per service ranked (Scene 4):**
```esql
PROMQL index=metrics-generic.prometheus-default
  request_rate=(sum by (service_name) (rate(traces_span_metrics_calls_total[5m])))
| WHERE service_name IN ("frontend", "checkout", "cart", "payment", "shipping", "recommendation")
| STATS max_rate = MAX(request_rate) BY service_name
| SORT max_rate DESC
```

**Query 3 — Payment error rate (Scene 5):**
```esql
PROMQL index=metrics-generic.prometheus-default
  error_rate=(sum(rate(traces_span_metrics_calls_total{status_code="STATUS_CODE_ERROR", service_name="payment"}[5m])))
```

**Prometheus Query (Scene 3):**
```promql
sum by (service_name) (rate(traces_span_metrics_calls_total[5m]))
```

---

## Contingency notes

**If Grafana panels show "No data" (Scene 1):**
- Switch to the **Linux** or **OpenTelemetry Collector** dashboard instead — both are driven purely by Prometheus metrics and always populate quickly after startup.

**If Kibana chart toggle is missing:**
- You likely have a pipe after PROMQL that breaks chart rendering.
- For Query 3 specifically: use curly-brace label selectors inside PromQL, NOT a WHERE pipe.

**If Prometheus graph is still ramping (Scene 3):**
- Extend the wait — you need 15+ minutes of stable data.
- Set Prometheus time range to 5m to hide the ramp if needed.

**If spike doesn't appear after 5 minutes (Scene 5):**
- Check chart view — don't trust table sort order.
- Go to `http://localhost:8080/feature` → Advanced view → confirm `paymentFailure` defaultVariant is `"25%"`.

**If asked about STATUS_CODE_UNSET:**
- In OTel, success is the absence of an error status. UNSET means the span completed without explicitly setting an error — effectively OK for most spans.
- STATUS_CODE_ERROR is explicitly set by the application when something goes wrong.

**If asked about the organic error humps:**
- The load generator hits a payment edge case at regular intervals.
- It's a feature of the demo, not a bug — and it makes the incident injection more realistic.
