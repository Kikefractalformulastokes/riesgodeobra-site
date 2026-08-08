# RO Delta Audit — 2026-08-08 (Phase A/B, GREG_GROWTH_EXECUTION)

Scope per order RO-GLOBAL-GROWTH-001: **delta only** vs canonical baseline `51f8028`
(tip of `feature/full-lifecycle-positioning`). The canonical claims/pricing audit
(`RIESGODEOBRA_CURRENT_STATE_AUDIT.md`) and claims register were NOT redone.

## Phase B verdict first: baseline remains valid

FACT: `origin/main` is still `96d4a1c` (unchanged since the canonical audit of 2026-07-18).
FACT: `origin/feature/full-lifecycle-positioning` is still `51f8028`. No new commits anywhere.
FACT: Re-ran the prohibited-claims grep across the baseline tree (65%/70% reductions,
AES-256, CENDOJ "integración/integrado/tiempo real/real-time"): **zero matches**.
CONCLUSION: No evidence-backed deltas that invalidate the register. Register stands as-is,
plus the growth additions appended today (see `RIESGODEOBRA_CLAIMS_REGISTER.md` §Growth additions).

## Phase A deltas found

### D1 — Lifecycle pages are still UNPUBLISHED (stale branch, not merged)
FACT: The 4 canonical pages (`/que-es-riesgodeobra/`, `/pre-obra/`, `/control-de-obra/`,
`/reclamaciones-defectos/`), the sitemap additions and cross-links exist only on the
feature branch. Production (`main` → riesgodeobra.es via CNAME) does not have them.
INFERENCE: The SEO/entity gap identified in the canonical audit (§13–14) is therefore
still live in production — three weeks after the fix was built.
PROPOSAL: Owner approves merge of the lifecycle branch (after the D2 fix below) as the
single highest-leverage production change. Merging is a material production change →
**OWNER APPROVAL REQUIRED**; not executed this cycle.

### D2 — "Informe en 48h" was propagated to a NEW page on the baseline branch (rule breach in merge candidate)
FACT: `pre-obra/index.html` (new, unpublished) carried "Informe en 48h." in its meta
description — hard rule says keep 48h only where already published, do not propagate.
FACT: Fixed this cycle on branch `growth/ro-global-growth-001` (meta description now
omits the delivery-time claim). No published page was touched.
FLAG (owner decision, not fixed): the new pages also use the published product name
"Risk Scan 48h" as CTA text (que-es ×3, pre-obra ×5, control-de-obra ×1). The offer
name itself is already published on the homepage with live Stripe links, so this is
arguably "referencing the existing published offer", not a new claim — but a strict
reading of the rule catches it because the name embeds the delivery promise. Options:
(a) accept product-name references on new pages as-is; (b) rename CTA text to
"Solicitar Risk Scan" on new pages only. **Owner to choose before merge.**

RESOLUTION (2026-08-08, cycle 3): OWNER REJECTED option (a) — D2 not ratified. All 9
"Risk Scan 48h" occurrences on the three new pages replaced with "Risk Scan"; prices and
Stripe links unchanged; production untouched. Procedural correction recorded: a tag
disagreement must be raised as a BLOCKER, not resolved in-mission with a flag.

### D3 — Required growth artifacts did not exist
FACT: No `RO_GLOBAL_GROWTH_STATE.md`, no SEO map, no freemium design, no Ads
architecture, no lead/partner/tender research existed anywhere in the repo.
FACT: All created this cycle under `/growth/` (this directory) — all PREPARE_ONLY.

### D4 — Canal de Panamá demo commercial-use review still pending
FACT: The demo carries the "reconstrucción metodológica basada en fuentes públicas"
disclaimer (confirmed at baseline). The order still requires a full human-readable
review before any commercial use.
CONSEQUENCE: **No asset created this cycle references the Canal de Panamá demo.**
The other two demos (pre-bid, CENDOJ-defectos) are referenced only with their
methodological framing intact.

### D5 — Register additions needed for growth assets
FACT: Three claims used in the new draft assets were not explicitly in the register;
appended today as G1–G3 with label/evidence/limitations before use (per hard rule).

## Not re-audited (unchanged since canonical audit, out of delta scope)
Stripe links (6), Tally forms (2), legal pages (5), robots.txt, Organization/WebSite
schema, pricing (Express 490 € · Pro 990 € · Advanced 2.500 €). Pricing untouched per order.
