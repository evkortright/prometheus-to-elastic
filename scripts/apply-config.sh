#!/usr/bin/env bash
# Generates the Prometheus config for the OTel demo from the committed template
# plus credentials in .env.elastic, so the real key never lives in a tracked file.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEMO_DIR="${DEMO_DIR:-$REPO_ROOT/opentelemetry-demo}"
ENV_FILE="${ENV_FILE:-$REPO_ROOT/.env.elastic}"
TEMPLATE="$REPO_ROOT/config/prometheus-config.yaml"
TARGET="$DEMO_DIR/src/prometheus/prometheus-config.yaml"
WRITE_PATH="/_prometheus/api/v1/write"

die() { echo "ERROR: $*" >&2; exit 1; }

[[ -f "$ENV_FILE" ]]  || die "Missing $ENV_FILE (copy config/.env.example and fill it in)."
[[ -f "$TEMPLATE" ]]  || die "Missing template $TEMPLATE."
[[ -d "$DEMO_DIR/src/prometheus" ]] || die "Demo folder not found at $DEMO_DIR."

set -a; source "$ENV_FILE"; set +a
[[ -n "${ES_ENDPOINT:-}" ]] || die "ES_ENDPOINT is empty in $ENV_FILE."
[[ -n "${ES_API_KEY:-}" ]]  || die "ES_API_KEY is empty in $ENV_FILE."

# Normalize: accept either the base endpoint or the full write URL, with or without :443.
BASE="${ES_ENDPOINT%/}"
BASE="${BASE%"$WRITE_PATH"}"
BASE="${BASE%/}"
BASE="${BASE%:443}"
WRITE_URL="${BASE}${WRITE_PATH}"

# Guard against the known payment-service break.
grep -q '^DEMO_VERSION=3.0.0' "$DEMO_DIR/.env" \
  || die "DEMO_VERSION in $DEMO_DIR/.env is not 3.0.0."

# Generate the config. Base64 keys contain no '|' so it is a safe sed delimiter.
sed -e "s|__ES_WRITE_URL__|${WRITE_URL}|" \
    -e "s|__ES_API_KEY__|${ES_API_KEY}|" \
    "$TEMPLATE" > "$TARGET"
chmod 600 "$TARGET"
grep -q '__ES_' "$TARGET" && die "Unreplaced placeholder left in $TARGET."

# Patched compose file (1GB Prometheus, WAL compression, retention cap).
cp "$REPO_ROOT/config/compose.observability.yaml" "$DEMO_DIR/compose.observability.yaml"

echo "Wrote $TARGET"
echo "Remote-write URL: $WRITE_URL"
echo "API key:          ${ES_API_KEY:0:4}... (${#ES_API_KEY} chars)"

# Connectivity checks (warn only).
c1=$(curl -s -o /dev/null -w '%{http_code}' -H "Authorization: ApiKey ${ES_API_KEY}" "$BASE" || true)
c2=$(curl -s -o /dev/null -w '%{http_code}' -H "Authorization: ApiKey ${ES_API_KEY}" "$WRITE_URL" || true)
echo "Base endpoint:      HTTP $c1  (200 or 403 is fine: a write-only key may be refused at the cluster root)"
echo "Write endpoint GET: HTTP $c2  (expect 405, POST only)"
if [[ "$c1" == 401 ]]; then
  echo "WARNING: 401 on the base endpoint means the API key was rejected. Check ES_API_KEY."
elif [[ "$c1" == 000 || "$c2" == 000 ]]; then
  echo "WARNING: could not connect. Check ES_ENDPOINT and your network."
elif [[ "$c2" != 405 ]]; then
  echo "WARNING: write endpoint returned $c2 instead of 405. Check the endpoint path."
else
  echo "OK: endpoint reachable. Data arriving in Elastic after the stack starts is the real test."
fi
