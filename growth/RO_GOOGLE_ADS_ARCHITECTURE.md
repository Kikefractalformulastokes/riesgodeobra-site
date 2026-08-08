# RO Google Ads Architecture — 2026-08-08 — PREPARE_ONLY (no account created, no spend)

Hard boundaries honored: no launch, no budget commitment, no "48h"/"Informe en 48h" in any
ad asset, no SLA language, no CENDOJ-integration language, no reduction percentages, no
Canal de Panamá references. Product name conflict ("Risk Scan 48h") escalated to owner —
all ad copy below uses "Risk Scan" pending that decision (delta audit D2 flag).

## Account structure (proposal)

CAMPAIGN 1 — [Search] Pre-obra / Presupuestos  (launch candidate #1)
- Ad groups: revisión de presupuesto | errores en mediciones | due diligence técnica
- Landing: /es/revision-presupuesto-obra/ (LIVE — no publication dependency)
- Keywords (exact/phrase seed): "revisión presupuesto obra", "revisar presupuesto reforma",
  "errores mediciones obra", "due diligence técnica edificio"
- Negatives (seed list): gratis, plantilla, excel, curso, empleo, software descargar
- Draft RSA headlines (≤30 chars, compliant):
  "Revisión de presupuesto de obra" · "Detecta sobrecostes antes" · "Evidencia antes de firmar"
  · "Auditoría documental de obra" · "Risk Scan desde 490 €"
- Draft descriptions (≤90 chars):
  "Analizamos presupuesto, mediciones y memoria. Riesgos claros antes de comprometer tu dinero."
  "Informe independiente sobre tu documentación de obra. Sin certificaciones, sin conflicto de interés."

CAMPAIGN 2 — [Search] Rehabilitación  (launch candidate #2)
- Ad groups: auditoría rehabilitación | riesgos rehabilitación (→ lead magnet page once approved)
- Landing: /es/auditoria-rehabilitacion-fachada/ (LIVE)
- Headlines: "Auditoría de rehabilitación" · "Riesgos de tu obra, claros" · "Antes de aprobar la derrama"
- Note: checklist ad group blocked until Rung-1 landing page is approved+published.

CAMPAIGN 3 — [Search] Reclamaciones y defectos  (launch candidate #3, higher CPC)
- Landing: /reclamaciones-defectos/ — BLOCKED until lifecycle branch merges (delta D1).
- Headlines: "Evidencia para tu reclamación" · "Matriz defecto–evidencia" · "Metodología LOE documentada"
- Description: "Organizamos la evidencia documental de tu reclamación con metodología basada en jurisprudencia pública."
- Compliance: never "ganamos reclamaciones", no success rates, no client references.

CAMPAIGN 4 — [Search] Brand protect (cheap, immediate once account exists)
- "riesgo de obra", "riesgodeobra". Landing: homepage.

NOT BUILT: control-de-obra campaign (ROADMAP capability — no ads on planned capability),
Display/PMax (no creative assets audited for compliance yet), UAE campaigns (backlog doc).

## Budget scenario (PROPOSAL, needs owner approval to spend anything)
Pilot: 20–30 €/day total, 60/25/15 across campaigns 1/2/4, 4-week test, decision gate at
~100 clicks/campaign. Campaign 3 only after merge. FACT: no keyword-volume/CPC data pulled
(no Ads account); INFERENCE: legal-adjacent Cluster-3 CPCs will be several × Cluster-1 CPCs.

## Pre-launch checklist (all owner-gated)
[ ] Owner decides product-name question (D2) [ ] Conversion tracking (Tally/Stripe) plan
[ ] Keyword Planner validation of volumes [ ] Owner approves budget [ ] Account created by owner
