# RO_GLOBAL_GROWTH_STATE — Riesgo de Obra by CoreSyn

Owner: Enrique Sánchez · Role: GREG_GROWTH_EXECUTION · Order: RO-GLOBAL-GROWTH-001
Claims register: BINDING · Working branch: `growth/ro-global-growth-001`

## Dual references (governance addendum 2026-08-08 — mandatory every cycle)
- CANONICAL_BASELINE_SHA = `51f802829c26e0363677aa2d9154ec56ce995e77` (tip of `feature/full-lifecycle-positioning` — approved working baseline for claims/strategy; **NOT published**)
- PRODUCTION_MAIN_SHA = `96d4a1c3ab22f84d12a263cdf513fb80012e83b9` (`origin/main` — what is actually deployed at riesgodeobra.es)

Rules: never assume baseline content is published; every delta traceable against BOTH refs;
GREG does not merge the baseline branch or move main (OWNER decisions); if origin/main
advances, update PRODUCTION_MAIN_SHA in the next report and flag the change.
Last verified: 2026-08-08 cycle 2 (`git fetch` — both unchanged).

## Cycle log

### Cycle 1 — 2026-08-08
Done:
- Phase A/B delta audit → `growth/RO_DELTA_AUDIT_2026-08-08.md`. Baseline confirmed valid;
  5 deltas (D1–D5). Compliance fix applied on working branch: removed "Informe en 48h"
  from the NEW unpublished `/pre-obra/` meta description (D2).
- Claims register: appended G1–G3 (growth claims, registered before use). No existing entry changed.
- Spanish SEO / buyer-intent map → `growth/RO_SEO_BUYER_INTENT_MAP.md` (5 clusters, priorities).
- Freemium acquisition design → `growth/RO_FREEMIUM_ACQUISITION_DESIGN.md` (3-rung ladder,
  Rung-1 landing draft copy, Rung-2 micro-diagnóstico proposal).
- Google Ads architecture (PREPARE_ONLY) → `growth/RO_GOOGLE_ADS_ARCHITECTURE.md`
  (4 campaigns, compliant draft copy, budget scenario, launch checklist — nothing launched).
- Lead/partner/tender research → `growth/RO_LEADS_PARTNERS_TENDERS.md` (4 lead segments,
  3 partner types with session-verified example orgs, tender radar spec with CPV shortlist).
- UAE/Dubai backlog → `growth/RO_UAE_DUBAI_BACKLOG.md` (5 items, activation trigger defined).

### Cycle 2 — 2026-08-08 (governance addendum applied)
- Dual-reference reporting adopted; both SHAs re-verified via `git fetch` — unchanged.
  Confirmed constraint: GREG will not merge the lifecycle branch or move main.
- Despacho research: 11 real construction-law firms identified with public sources
  (`growth/RO_LEADS_PARTNERS_TENDERS.md` §C2); no contact data recorded.
- Tender radar validated: CPV 71300000/71310000 confirmed against real 2026 tenders
  (Paseo Verde del Suroeste ~2,7 M€; ETAP Villacarrillo; BLET Córdoba ~8,9 M€);
  added 71248000 + 71356200; contratos.gobierto.es identified as free radar UI.
  Play 1 (direct bidding) deprioritized — lot sizes far above RO; Play 2 (bidders as
  pre-bid leads) is the operative play.
- Drafts created under `growth/drafts/` (all HELD/PREPARE_ONLY): Cluster-1 and Cluster-3
  SEO content pieces, outreach templates T1–T3, CAF partner one-pager.
- Dual-ref traceability of drafts: Cluster-1 piece links only to production-live pages
  (publishable after page approval alone); Cluster-3 piece links to `/reclamaciones-defectos/`
  which exists ONLY at CANONICAL_BASELINE_SHA — publication additionally blocked on the
  owner's merge decision.

## Standing approvals needed (OWNER)
1. **Merge lifecycle branch to main** (publishes the 4 canonical pages; unblocks SEO
   priority 1 and Ads campaign 3). Includes decision D2: keep "Risk Scan 48h" product-name
   CTAs on new pages, or rename CTA text to "Risk Scan" on new pages.
2. Publish Rung-1 lead-magnet landing page (draft copy ready).
3. Approve any Ads spend (architecture ready; pilot scenario 20–30 €/day).
4. Approve outreach to ranked partner/lead segments (nothing sent).
5. Canal de Panamá demo: human-readable review before any commercial use (still pending;
   demo excluded from all growth assets meanwhile).

## Hard-rule compliance state
48h: not propagated to any new asset (one baseline breach found & fixed on branch, D2).
CENDOJ: methodology-only language everywhere. Prohibited claims: zero in all new assets.
Pricing/offers: untouched. Money spent: none. Outreach sent: none. Tenders submitted: none.

## Next 3 actions (cycle 3)
1. Draft Cluster-2 lead-magnet landing page as ready-to-publish HTML (held on branch) so the
   owner's approval → publish path is one step.
2. Radar sweep #1: pull adjudication docs for 2–3 recent CPV-71xxx lots and extract public
   bidder/awardee company names as Play-2 lead candidates (public data only).
3. Verify Boltas Boyé + AJF Legal/Real Abogados practice pages directly; personalize T1 for
   the top-3 despachos (still HELD until outreach approval).
