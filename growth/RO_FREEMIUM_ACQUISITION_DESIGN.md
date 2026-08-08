# RO Freemium Acquisition Design — 2026-08-08 (PREPARE_ONLY)

Constraint check: uses only existing assets (register G1/G2) + existing Tally forms +
existing Stripe offers. No price changes, no new paid services, no "48h" in new copy,
no SLA. Nothing here goes live without owner approval.

## Ladder (all rungs already exist except the email sequence)

RUNG 0 — Anonymous value (live today)
- 3 public demos (pre-bid, CENDOJ-defectos; Canal de Panamá EXCLUDED from promotion
  pending human review) + `/es/` audit pages. Role: prove method, zero friction.

RUNG 1 — Free download (live today, under-leveraged)
- `descargas/21-riesgos-obra-rehabilitacion.pdf` (G1), gated behind Tally `9qyYMp`
  (funnel already wired at `gracias/`).
- Delta this cycle: PROPOSAL for a dedicated long-form landing page
  "/recursos/21-riesgos-rehabilitacion/" wrapping the PDF (SEO Cluster 2). Draft copy
  below. Needs owner approval to publish (new page = production change).

RUNG 2 — Free micro-diagnóstico (PROPOSAL — new, needs owner approval)
- "Semáforo documental": user answers 8 yes/no questions about their project docs
  (¿tiene mediciones cerradas?, ¿memoria coherente con planos?, …) via a new Tally form;
  reply is a manual, templated 1-page traffic-light summary. Manual fulfillment = no
  capability claim needed; positions the paid Risk Scan as the obvious next step.
- Explicitly NOT promised as automated and NO turnaround-time promise.

RUNG 3 — Paid (unchanged, published)
- Risk Scan Express 490 € · Pro 990 € · Advanced 2.500 € via existing Stripe links.

## Draft landing copy — Rung 1 page (for owner review, not published)

H1: Los 21 riesgos que encarecen una obra de rehabilitación
Sub: Checklist gratuito elaborado a partir de los patrones de riesgo que revisamos en
presupuestos, mediciones y memorias de obra.
Bullets: detecta partidas ambiguas antes de firmar · anticipa sobrecostes típicos de
rehabilitación · llega a la reunión con tu comunidad o tu contratista con preguntas concretas.
CTA: Descargar checklist gratuito (→ Tally 9qyYMp)
Secondary CTA: Ver una revisión real de metodología (→ /demos/pre-bid-obra-publica/)
Footer disclaimer: reuses the standard CoreSyn scope-limitation block verbatim.
[Claims used: G1, G2 — both registered. No delivery-time, no reduction %, no security claims.]

## Email nurture (PROPOSAL — 3 touches, manual send, NOT mass outreach until approved)
1. Day 0: PDF delivery + one question ("¿En qué fase está tu obra?") — segmentation.
2. Day 4: one worked example from a demo (methodological framing verbatim).
3. Day 10: soft offer of the micro-diagnóstico (Rung 2) or Risk Scan (existing page).
No sends occur until owner approves sequence + tooling.

## Metrics to instrument once live
Download conversions (Tally), page→Stripe clickthrough, demo→download path. No analytics
tooling change proposed this cycle.
