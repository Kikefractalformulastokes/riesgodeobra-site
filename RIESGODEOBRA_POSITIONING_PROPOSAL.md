# RiesgoDeObra — Full-Lifecycle Positioning Proposal

Branch: `feature/full-lifecycle-positioning`. Not merged, not deployed. Planning-level proposal — new page HTML has not been written yet; this defines what would go into it and why, so it can be reviewed before any markup is produced.

## Recommended homepage headline
"Detectamos riesgos técnicos, documentales y contractuales antes de que se conviertan en sobrecostes, retrasos o litigios." — matches claim #1 in the register (SUPPORTED), and is a tightened version of the existing meta description, not a new promise.

## Proposed lifecycle architecture

**ANTES DE LA OBRA — Prevenir el riesgo** (`/pre-obra/`)
Links out to existing `/es/revision-presupuesto-obra/` and `/demos/pre-bid-obra-publica/`. Content: budget/BOQ review, drawing-vs-spec inconsistencies, missing documents, regulatory risk, pre-bid risk, technical due diligence. All SUPPORTED per register.

**DURANTE LA OBRA — Controlar desviaciones y evidencia** (`/control-de-obra/`)
This is the thin lane — no existing demo covers it. Proposed content is descriptive/roadmap: risk register, documentary traceability, change/deviation evidence, decision timeline, responsibility mapping. **Must be labeled as described capability, not demonstrated**, per register items #5-6 (ROADMAP).

**DESPUÉS DE LA OBRA — Estructurar reclamaciones y responsabilidades** (`/reclamaciones-defectos/`)
Links out to existing `/demos/defectos-constructivos-cendoj/` and `/demos/mega-claim-canal-panama/`. Content: defect-evidence matrices, chronology, gap-in-proof analysis, responsibility mapping, Claims Evidence Pack, LOE/CENDOJ methodology — carrying forward the existing demo disclaimers unchanged (public-source reconstruction, not live case work).

**`/que-es-riesgodeobra/`** — canonical definition page, tying the three lanes together, meant to be the page Google indexes as the entity definition (per audit §13-14 finding that no such hub currently exists).

## What does NOT change
- The 3 existing demo pages keep their current URLs, content, and disclaimers — preserving their existing SEO authority as instructed. New pages link *to* them; nothing is removed or rewritten.
- No pricing changes.
- No claims from the UNSUPPORTED list in the register are introduced anywhere.

## FAQ schema / Organization schema
Any new FAQ schema should reuse the register's SUPPORTED-only claims. Organization/Service schema should extend the existing clean `Organization` JSON-LD (already has no invented credentials) with `Service` entries for the three lifecycle lanes — again, no certifications, ratings, or client claims added.

## Still needed before this becomes real pages
1. Your review of the register/proposal above — particularly whether the `/control-de-obra/` lane should launch as "roadmap" copy or wait until there's a real demo to back it.
2. Explicit go-ahead to write and commit the actual HTML (I've deliberately stopped at planning-doc level rather than generating four new public pages and schema unreviewed).

## Rollback
Everything on `feature/full-lifecycle-positioning`; `main` is untouched. Deleting the branch fully reverts this work with zero effect on the live site.
