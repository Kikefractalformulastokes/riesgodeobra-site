# RiesgoDeObra — Claims Register (positioning proposal)

Every claim proposed for the new lifecycle pages, tagged per instruction. Nothing here is published — this is a planning artifact on `feature/full-lifecycle-positioning`.

| # | Claim | Tag | Basis |
|---|---|---|---|
| 1 | "Detectamos riesgos técnicos, documentales y contractuales antes de que se conviertan en sobrecostes, retrasos o litigios." | SUPPORTED | Matches existing homepage meta description and the actual content of the 5 existing pages (2 audit pages + 3 demos), which already cover technical/documentary/contractual angles. |
| 2 | Pre-obra: revisión de presupuesto y mediciones | SUPPORTED | `/es/revision-presupuesto-obra/` already exists and does this. |
| 3 | Pre-obra: detección de inconsistencias entre planos, memoria y mediciones | SUPPORTED | Same page covers this per its title/content. |
| 4 | Pre-obra: riesgo pre-bid en licitación pública | SUPPORTED | `/demos/pre-bid-obra-publica/` already exists and demonstrates exactly this. |
| 5 | Control de obra: registro de riesgos, trazabilidad documental | ROADMAP | No existing page/demo currently demonstrates a running risk register or change-tracking workflow — this is a described capability, not yet shown. |
| 6 | Control de obra: cronología de decisiones, mapa de responsabilidad | ROADMAP | Same — not demonstrated anywhere in the current site. |
| 7 | Reclamaciones: matriz defecto-evidencia | SUPPORTED | `/demos/defectos-constructivos-cendoj/` demonstrates this pattern (with explicit "reconstrucción metodológica" disclaimer, which must be preserved). |
| 8 | Reclamaciones: metodología LOE/CENDOJ | PARTIALLY_SUPPORTED | The CENDOJ demo exists and is methodologically framed, but is explicitly a reconstruction from public sources, not a live CENDOJ integration — any new copy must preserve that distinction, not upgrade it. |
| 9 | "Informe en 48h" | PARTIALLY_SUPPORTED | Appears in existing meta description already; I have no evidence (turnaround logs, fulfillment records) confirming actual delivery time — carrying it forward unchanged (already published), not escalating it, and not extending it to new pages without the same caveat status. |
| 10 | 65-70% time/cost reduction | UNSUPPORTED | No evidence anywhere in the repo. Explicitly prohibited by your instruction. Not included in any draft. |
| 11 | AES-256 / EU hosting / security certifications | UNSUPPORTED | No evidence found (checked `legal/privacidad`, which mentions hosting via "Vercel/Netlify" generically, no encryption-standard or region claims). Not included. |
| 12 | Automatic CENDOJ integration | UNSUPPORTED | Contradicted by the CENDOJ demo's own disclaimer (public-source reconstruction, not live integration). Not included. |
| 13 | Verified court success / existing corporate clients / field validation | UNSUPPORTED | No evidence anywhere in the repo (testimonials, case studies, or client logos absent). Not included. |

## Growth additions — 2026-08-08 (GREG_GROWTH_EXECUTION, order RO-GLOBAL-GROWTH-001)

New claims required by growth drafts, registered before use per hard rule. No existing entry reinterpreted.

| # | Claim | Tag | Evidence basis | Limitations |
|---|---|---|---|---|
| G1 | "Checklist gratuito: 21 riesgos en obras de rehabilitación" (lead magnet) | SUPPORTED | `descargas/21-riesgos-obra-rehabilitacion.pdf` exists in the published repo and is already linked from the funnel. | Content of the PDF not re-audited this cycle; claim limited to "existe y es descargable", no outcome promises. |
| G2 | "Demos públicas con metodología documentada (pre-bid, defectos/CENDOJ)" | SUPPORTED | `/demos/pre-bid-obra-publica/` and `/demos/defectos-constructivos-cendoj/` exist with explicit "reconstrucción metodológica basada en fuentes públicas" disclaimers. | Must always carry the reconstruction framing; never presented as client engagements. Canal de Panamá demo EXCLUDED from commercial use pending human review. |
| G3 | "Cobertura del ciclo de vida: pre-obra y reclamaciones demostradas; control de obra como capacidad planificada" | PARTIALLY_SUPPORTED | Pre-obra and reclamaciones lanes have live pages/demos (register #2–4, #7–8); control de obra is ROADMAP (register #5–6). | Any asset naming control de obra must label it as planned capability ("capacidad planificada / en desarrollo"), never demonstrated. |

## Net effect
Of 13 candidate claims for the new pages, **6 are already supported by existing site content**, **2 are roadmap-labeled capabilities** (control-de-obra lane is the thinnest today — this matches the audit's finding in §13/14), **1 carries forward an existing partially-supported claim unchanged**, and **4 prohibited claim types are explicitly excluded**, consistent with what the current-state audit found (zero prohibited claims currently published).
