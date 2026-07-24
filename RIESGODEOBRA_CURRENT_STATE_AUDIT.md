# RiesgoDeObra — Current State Audit (evidence-grounded, no edits made)

Repo: `riesgodeobra-site`, `main` @ `96d4a1c3ab22f84d12a263cdf513fb80012e83b9` (2026-07-18). All findings below are from reading the actual repo files this session.

## 1. Homepage positioning (as it exists today)
- `<title>`: "Auditoría de Riesgos de Obra, Rehabilitación e Inversión | Riesgo de Obra"
- Meta description: "Convertimos tu documentación de obra en evidencia accionable: sobrecostes, riesgos normativos y puntos críticos antes de construir, comprar, licitar o reclamar. Informe en 48h."
- This is **already lifecycle-flavored** ("antes de construir, comprar, licitar o reclamar") — it is not narrowly a claims/defects page. The narrower framing lives in the **demos**, not the homepage.

## 2. Offers and prices — every one found
6 live Stripe Payment Links present in `index.html` (URLs recorded, not decoded/tested — decoding a live payment link isn't something to do without explicit intent to test a transaction):
```
stripe.com/00wbIU7Od2d25jB3jQ4F20j
stripe.com/28E00c2tT04U27p4nU4F20m
stripe.com/3cI28k0lL7xmcM38Ea4F20n
stripe.com/5kQaEQ3xXdVK8vN1bI4F20l
stripe.com/8x26oAecB18Y7rJ07E4F20o
stripe.com/dRm9AMgkJbNCfYf07E4F20k
```
2 Tally intake forms:
```
tally.so/r/9qyYMp
tally.so/r/VLAaxJ
```
I did not open/submit either external link — that would create real records outside this session's authority.

## 3. Every Stripe link — status
Not tested end-to-end (would require an actual checkout attempt against a live payment processor, which I won't do without explicit instruction and awareness this may create real Stripe-side records). Presence confirmed structurally (6 distinct working-format Stripe Payment Link URLs embedded in production HTML).

## 4. Tally forms
Same — presence confirmed, not submitted.

## 5. Legal pages
All 5 present: `aviso-legal`, `condiciones-servicio`, `confidencialidad-documental`, `cookies`, `privacidad`. Every page carries the same disclaimer block: *"CoreSyn es una capa independiente de evidencia y risk intelligence. No emitimos certificaciones oficiales ni visados, no realizamos dirección facultativa ni sustituimos a arquitectos, aparejadores, ingenieros ni peritos."* — consistent scope-limitation language repeated across all pages, including the three demo pages. No placeholder markers (`[nombre]`, `Lorem ipsum`, `TODO`, `XXXX`) found anywhere in the legal tree.

## 6. Sitemap
7 URLs listed: homepage, 2 `/es/` audit pages, `/demos/` index + 3 demo pages, plus 5 legal pages (11 total including legal). **No `/que-es-riesgodeobra/`, `/pre-obra/`, `/control-de-obra/`, or `/reclamaciones-defectos/`** — confirmed these don't exist yet.

## 7. Robots
Standard `Allow: /` with `Disallow: /gracias/, /thank-you/, /admin/` (thank-you page correctly excluded from indexing) and a sitemap pointer. No issues.

## 8. Structured data
Homepage carries `Organization` schema (`name`, `legalName: "CoreSyn Construction Evidence Intelligence"`, `areaServed: "ES"`, `sameAs: []`) and `WebSite` schema. **No invented credentials, certifications, or claims in the schema** — clean. `sameAs: []` (no social profiles linked) and no `AggregateRating`/`Review` schema anywhere (good — no fabricated ratings).

## 9. Demos — content and framing
Three demo pages (`defectos-constructivos-cendoj`, `mega-claim-canal-panama`, `pre-bid-obra-publica`) plus 2 Spanish audit-specific pages (`auditoria-rehabilitacion-fachada`, `revision-presupuesto-obra`). Every demo carries an explicit disclaimer that it's a **"reconstrucción metodológica basada en fuentes públicas"** — not a real case file, no implied client relationship, no implied liability finding against named parties. This is well-hedged content, already.

## 10. Internal linking
Currently **zero internal links exist to a canonical `/que-es-riesgodeobra/` page** because it doesn't exist. Demos link to each other and to the homepage; there's no lifecycle hub yet. This confirms the actual gap Phase 4 is meant to close — not a defect, just the current state before that work.

## 11. Mobile / accessibility
Viewport meta tag present on all 9 checked pages (index, demos index, both `/es/` pages, all 5 legal pages). No `<img>` tags found missing `alt` text on the pages scanned. Not a full WCAG audit (no contrast-ratio or screen-reader pass done).

## 12. Unsupported/ambiguous claims — scanned, not found
Grepped the entire repo (all HTML) for: 65%/70% time-reduction figures, AES-256, "hosting UE/EU," automatic CENDOJ integration language, "éxito judicial/en los tribunales," claims of existing corporate clients, "validación de campo," and certification claims. **Zero matches.** The site as it stands does not currently make any of the prohibited claims listed in your Phase 4 instructions. This is good news, not a gap — there's nothing to walk back, only lifecycle-breadth to add.

## 13. Current SEO entity definition
Homepage title/description already gesture at the full lifecycle ("antes de construir, comprar, licitar o reclamar"), but the **only page-level, in-depth content that exists is the CENDOJ defects demo, the Panama Canal mega-claim demo, and the pre-bid demo** — i.e., three worked examples that are disproportionately claims/litigation-flavored relative to the (thinner) pre-construction and control-de-obra content. A crawler forming an entity model from crawl depth and worked-example density would plausibly weight this site toward "claims and defects software," even though the homepage copy itself doesn't say that.

## 14. Could Google reasonably read this as claims/defects-only software?
**Plausible but not inevitable** — the homepage metadata resists that reading; the demo mix doesn't. This matches your Phase 4 premise: the fix is adding equal-depth pre-obra/control-de-obra canonical pages and internal links, not walking back anything currently published (nothing currently published needs walking back — see §12).

## Summary
The site is more disciplined than the "one CENDOJ demo defines the company" framing suggested — real legal hedging, real schema hygiene, no prohibited claims found anywhere. The actual gap is structural: **no canonical lifecycle pages exist yet**, and the demo content skews toward the claims/litigation lane by volume. Phase 4's proposed fix (add `/que-es-riesgodeobra/`, `/pre-obra/`, `/control-de-obra/`, `/reclamaciones-defectos/`, cross-link from every demo) is well-targeted to the actual, verified gap.
