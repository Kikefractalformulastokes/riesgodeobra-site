# Technical Audit — riesgodeobra.es

**Date:** 2026-08-11
**Ref:** RO-GLOBAL-GROWTH-001
**Scope:** Repository `kikefractalformulastokes/riesgodeobra-site` @ `claude/website-audit-seo-orh20f` (0 commits ahead/behind `main`, so this reflects the deployed source).
**Method:** Full static read of all 14 HTML pages, `robots.txt`, `sitemap.xml`, `assets/style.css`, `CNAME`, git history.
**Not verified:** Live HTTP responses. Outbound requests to `riesgodeobra.es` are blocked by this environment's proxy (403 on CONNECT). Anything marked *(live-only)* needs checking against the running site. Third-party form/checkout configuration (Tally field schema, Stripe success URLs, NDA step) is not in the repo and could not be inspected.

**Constraints observed in this audit:** no customers, partners, validations, benchmarks or guarantees have been invented; no price reductions are proposed; no NS-MDS claims are introduced. Grep confirms **zero** existing NS-MDS/MDS references in the repository — nothing to preserve or remove on that front.

**No site files were modified.** This document is the only change.

---

## 1. Current routes / pages

Static site, no build step, no framework, no JS. GitHub Pages served from repo root (`CNAME` → `riesgodeobra.es`, no `_config.yml`, no `.nojekyll`, no workflows).

| # | Route | Purpose | In sitemap | Indexable | Schema | OG tags |
|---|---|---|---|---|---|---|
| 1 | `/` | Home / all four services | ✅ | ✅ | Organization, WebSite | ✅ |
| 2 | `/es/revision-presupuesto-obra/` | Service LP — budget review | ✅ | ✅ | Service, Breadcrumb, FAQPage | ✅ |
| 3 | `/es/auditoria-rehabilitacion-fachada/` | Service LP — façade | ✅ | ✅ | Service, Breadcrumb, FAQPage | ✅ |
| 4 | `/demos/` | Demo hub | ✅ | ✅ | ❌ | ❌ |
| 5 | `/demos/defectos-constructivos-cendoj/` | Demo — LOE / defects | ✅ | ✅ | ❌ | ❌ |
| 6 | `/demos/mega-claim-canal-panama/` | Demo — GUPC/ACP claim | ✅ | ✅ | ❌ | ❌ |
| 7 | `/demos/pre-bid-obra-publica/` | Demo — LCSP pre-bid | ✅ | ✅ | ❌ | ❌ |
| 8 | `/recursos/21-riesgos-rehabilitacion/` | Lead-magnet LP | ❌ **missing** | ✅ | WebPage, Breadcrumb | ✅ |
| 9 | `/gracias/` | Post-download thank-you | ❌ (correct) | `noindex` + robots Disallow | ❌ | ❌ |
| 10–14 | `/legal/{aviso-legal, privacidad, cookies, condiciones-servicio, confidencialidad-documental}/` | Legal | ✅ | ✅ | ❌ | ❌ |
| — | `/descargas/21-riesgos-obra-rehabilitacion.pdf` | Gated asset (132 KB) | ❌ | **crawlable — not disallowed** | — | — |
| — | `/assets/style.css` | Single shared stylesheet | — | — | — | — |
| — | `404.html` | **Does not exist** | — | — | — | — |

**Structural observations**

- **IA inconsistency:** home lives at `/` but service pages sit under `/es/`, while demos, recursos and legal sit at root level. The `/es/` prefix implies a multilingual tree that does not exist (no `hreflang`, no `x-default`, no `/en/`). Pick one convention before adding pages — retrofitting redirects later is the expensive path.
- **`/recursos/21-riesgos-rehabilitacion/` is orphaned.** Zero internal links point to it anywhere in the site, and it is absent from `sitemap.xml`. The most recent commit (`697d10e`, "Rung-1 lead-magnet landing … step 1") shipped a landing page that is currently unreachable by both users and crawlers.
- `/recursos/` has no index page.
- Mobile nav (`@media(max-width:820px)`, `style.css:38`) hides **every** nav link except the Stripe CTA. Below 820 px there is no navigation to Fachadas, Presupuestos, Precios or FAQ, and no hamburger fallback.
- Dead CSS: `.highticket`, `.ht`, `.convert` are defined but used in zero HTML files.

---

## 2. Published services and prices

All figures below are **exactly as published**. Prices are consistent across every page that shows them (`/`, both `/es/` pages, `/gracias/`) — no contradictions found. **No reductions are proposed anywhere in this audit.**

### Risk Scan 48h — self-serve, Stripe Payment Links

| Tier | Price | Scope as published | Stripe link |
|---|---|---|---|
| Express | **490 €** | "Diagnóstico sobre un presupuesto o memoria." | `…4F20j` |
| Pro *(badged "Más elegido")* | **990 €** | "Presupuesto + mediciones + memoria, con mapa de evidencia." | `…4F20k` |
| Advanced | **2.500 €** | "Revisión ampliada + informe completo + sesión." | `…4F20l` |

### High-ticket lines — deposit-first

| Service | Published floor | Deposit | Stripe link | Own landing page |
|---|---|---|---|---|
| Building Risk Due Diligence | **Desde 5.000 €** | 2.500 € | `…4F20m` | ❌ none |
| Construction Claims Evidence Pack | **Desde 10.000 €** | 5.000 € | `…4F20n` | ❌ none |
| Pre-Bid Public Works Risk Audit | **Desde 15.000 €** | 7.500 € | `…4F20o` | ❌ none (demo only) |

**Pricing terms published:** "Precios sin IVA." (all pricing blocks) · "Servicios de alto alcance (Due Diligence, Claims, Pre-Bid) arrancan con depósito y presupuesto cerrado tras revisar el alcance." · `condiciones-servicio` §7: Risk Scan fully refundable **before** analysis starts, non-refundable once started; deposits credited against the final invoice and non-refundable once scope work begins.

**Link distribution (26 total Stripe references):** the 490 € Express link appears **26 times** — it is the nav CTA on all 14 pages plus most section CTAs. The three high-ticket links appear **once or twice each**, and only two of them (Due Diligence, Claims) appear anywhere outside the home page. **Three revenue lines worth 5k–15k € are sold from a single card each on the home page.**

---

## 3. Existing claims — preserve vs. correct

### 3a. Preserve verbatim (do not touch during any rewrite)

1. **The disclaimer stack**, present in every footer: *"No emitimos certificaciones oficiales ni visados, no realizamos dirección facultativa ni dictamen pericial, y no sustituimos a arquitectos, aparejadores, ingenieros ni peritos."* This is the core liability boundary of the whole proposition. Any new page must carry it before publication.
2. **"Precios sin IVA"** on every block that shows a price.
3. **The 48h qualifier**: *"48 horas desde que recibimos la documentación completa."* Preserve the qualifier, not just the "48h".
4. **Demo disclaimers**, especially on the Canal de Panamá page: *"no acusa, no atribuye responsabilidad y no implica relación, afiliación, validación ni endorsement por parte de Sacyr, Webuild/Impregilo, Jan De Nul, CUSA, GUPC, ACP ni ninguna institución mencionada."* This is what makes naming those parties defensible.
5. **CENDOJ demo framing**: *"Caso ilustrativo compuesto… No se reproduce ni analiza una resolución judicial concreta."*
6. **The evidence chain**, used consistently as a brand asset: *Documento → Evidencia → Riesgo → Norma → Coste potencial → Pregunta crítica → Decisión.*
7. **LSSI identity block** (`aviso-legal`): Enrique Sánchez Lorenzo, NIF, Madrid address, email, phone — legally required, keep current.
8. **The independence positioning**: *"capa independiente de risk intelligence, sin conflicto con tu equipo técnico"* / *"Tú diriges y firmas; nosotros ordenamos la evidencia."* Consistent everywhere and materially differentiating.

### 3b. Correct — ranked by severity

| # | Claim / issue | Where | Why it's a problem | Recommended correction |
|---|---|---|---|---|
| **C1** | **"Nota: Borrador base; revisar y adaptar con asesor legal antes de publicar."** | `legal/aviso-legal` L51-53, `legal/privacidad` L77-79, `legal/cookies` L41-43, `legal/confidencialidad-documental` L45-47 | **Four live legal pages tell every visitor their own terms are unreviewed drafts.** Self-invalidating in a business whose entire product is documentary rigour, and directly undercuts the confidentiality promise made on the commercial pages. | Remove the four `<blockquote>` notes. **Removing the note is not the same as the review having happened** — that legal review is your call and should precede removal. |
| **C2** | Cookie policy describes a consent banner that **does not exist**: *"Al acceder al sitio verás un aviso que te permite aceptar, rechazar o configurar las cookies"* + *"puedes cambiar tu elección desde el enlace de configuración de cookies"*. Also the unfinished parenthetical *"(Cuando se active la analítica, aquí se detallará la tabla concreta…)"*. | `legal/cookies` L36-38 | Verified: **zero** `<script>` tags site-wide other than JSON-LD, no analytics, no banner, no cookie set by the site. The policy describes controls the user cannot find. | Either (a) state factually that the site currently sets no non-essential cookies and that the table/banner arrive with analytics, or (b) ship analytics + banner and make the text true. Do **not** leave the two out of sync. |
| **C3** | **"Confidencialidad garantizada"** | `/` hero L50; `/es/revision-presupuesto-obra/` L59; `/es/auditoria-rehabilitacion-fachada/` L59 | An absolute guarantee. The legal pages promise *"medidas técnicas y organizativas **razonables**"* and cap liability at the amount paid. Marketing absolute ≠ contractual commitment. | Align to what is contractually offered, e.g. *"Acuerdo de confidencialidad firmado"* or *"Tratamiento confidencial de tu documentación"*. Your call on wording; the mismatch is the issue. |
| **C4** | **"Firmamos confidencialidad" / "Firmamos acuerdo de confidencialidad"** stated as part of intake | `/` step 1 L86; FAQ on both `/es/` pages | `confidencialidad-documental` is a **unilateral published clause**, not a signed bilateral NDA. Whether the Tally intake actually includes a signature step is not visible in the repo. | Verify the real intake flow. If no signature step exists, either add one or restate as *"Tratamos tu documentación bajo cláusula de confidencialidad"*. Don't assert a signature that doesn't happen. |
| **C5** | **"Sin compromiso tras el primer diagnóstico"** | `/` hero L50 | Reads as no-obligation, but the Risk Scan is **prepaid** via Stripe and non-refundable once analysis begins (`condiciones-servicio` §7). | Clarify intent — e.g. *"sin permanencia ni servicios recurrentes"* — or drop. As written it invites a refund dispute. |
| **C6** | **"Más elegido"** badge on the Pro tier | `/` L112, both `/es/` pages, `/gracias/` L53 | An unsubstantiated popularity claim. No customer base is disclosed anywhere on the site, and none should be invented. Under Ley 3/1991 (competencia desleal) an unsupported popularity claim is exposure. | Keep **only** if your Stripe data actually supports it. Otherwise replace with a non-factual framing such as *"Recomendado"*. |
| **C7** | **Mega-claim page dates have aged out.** *"Pendiente; vistas señaladas entre enero y abril de 2026"* and timeline entry *"2026 — Vistas sobre el fondo del arbitraje pendiente"* | `demos/mega-claim-canal-panama/` L74, L91 | Today is 2026-08-11 — those hearings are now in the past and the page still presents them as forthcoming. The page's credibility rests entirely on source fidelity, and there is **no visible publication date** to bound the claim. | Re-verify status **against the seven cited public sources** and update. **Do not update from memory or assumption.** Add a visible *"Fuentes consultadas a fecha de …"* stamp so future drift is self-limiting. |
| **C8** | `Organization.logo` → `/assets/logo-coresyn.png`; `og:image` → `/assets/og-home.png`, `og-fachada.png`, `og-presupuesto.png` | `/`, both `/es/`, `/recursos/…` | **None of these four files exist.** `assets/` contains only `style.css`. Broken Organization structured data and zero social preview on every shared link. *(live-only: confirm 404s.)* | Produce the four images or remove the properties. Broken > absent for structured data. |
| **C9** | Home page states "48h" **10 times with no qualifier anywhere** | `/` (meta description, hero, trust list, step 3, CTAs) | The *"desde documentación completa"* qualifier appears on both `/es/` pages and in `condiciones-servicio`, but **not once on the home page** — the page most likely to be the entry point. | Add the qualifier to the home pricing footnote at minimum. |
| **C10** | `Service.offers` declares `"price":"490"` alongside a 490–2500 `PriceSpecification`, with no VAT flag | both `/es/` pages, JSON-LD | Page says "sin IVA"; structured data doesn't. Search engines may surface "490 €" as *the* price. | Add `"valueAddedTaxIncluded": false` and consider `priceValidUntil`, so structured data matches the published claim. |
| **C11** | `"sameAs": []` — empty array | `/` Organization schema | Empty property, no value. | Populate with real profiles or remove. |
| **C12** | Home `og:title` is **English** (*"Riesgo de Obra by CoreSyn — Evidence before construction"*) while `og:description`, `<title>` and page are Spanish | `/` L10 | Inconsistent share previews for a Spanish-language audience. | Align to Spanish; keep the English tagline as body copy if wanted. |

---

## 4. Missing high-intent landing pages

Ranked by revenue proximity. Every page below must ship with the §3a disclaimer stack.

### Tier 1 — services you already sell with no page to sell them on

| Proposed route | Service | Currently |
|---|---|---|
| `/es/due-diligence-tecnica-edificio/` | Building Risk Due Diligence — desde 5.000 € | One 40-word card on `/` |
| `/es/reclamacion-sobrecostes-obra/` | Construction Claims Evidence Pack — desde 10.000 € | One card on `/` + two demo CTAs |
| `/es/auditoria-pliego-obra-publica/` | Pre-Bid Public Works Risk Audit — desde 15.000 € | One card on `/` + a demo page that is methodology, not an offer |

This is the single largest gap in the site: **the three highest-value lines have no indexable commercial page, no scope detail, no FAQ, no objection handling and no qualification path.**

### Tier 2 — buyer segments and queries your existing copy already serves

| Proposed route | Intent it captures | Source material already written |
|---|---|---|
| `/es/comparar-presupuestos-obra/` | "comparar presupuestos de obra / cuál es más fiable" | FAQ answer on the presupuesto page; the "misma base" comparison method |
| `/es/derrama-comunidad-propietarios/` | Administradores de fincas, juntas, derramas | The façade page is already ~50% written for this reader |
| `/es/defectos-constructivos-reclamacion/` | Commercial counterpart to the CENDOJ demo | Demo covers method; no page converts the intent |
| `/es/perito-o-auditoria-documental/` | The "¿necesito un perito?" objection | Answered in FAQs on both service pages, buried |
| `/es/ite-iee-informe-evaluacion-edificio/` | ITE/IEE-adjacent rehabilitation intent | Named as an input document on the façade page |

### Tier 3 — conversion and trust infrastructure

| Proposed route | Why |
|---|---|
| `/contacto/` | **No contact page exists.** Email and phone appear only inside legal pages. |
| `/es/precios/` | Pricing is only an `#precios` anchor — no URL to rank or link for price-intent queries |
| `/metodologia/` | The evidence chain is the differentiator and has no page of its own |
| `/recursos/` | Hub index; currently a directory with one orphaned child |
| `/es/quien-esta-detras/` | E-E-A-T. **Requires your input** — no credentials, bio or track record may be invented |
| `404.html` | None exists |

---

## 5. SEO / content gaps

**Indexing & crawl**
- `sitemap.xml` is missing `/recursos/21-riesgos-rehabilitacion/`; `lastmod` values (2026-07-16/17) predate that page's commit.
- `/descargas/*.pdf` is **not** disallowed in `robots.txt` — the gated PDF is crawlable and indexable, so search can route users straight past the Tally form. Decide: gate it (Disallow) or accept it as a discovery asset.
- `robots.txt` `Disallow: /gracias/` prevents crawling, which also prevents Google from *seeing* that page's `noindex`. Harmless here (nothing links to it), but redundant — `noindex` alone is the stronger signal.
- Referenced but non-existent: `/thank-you/`, `/admin/` in robots.txt (harmless).

**Metadata**
- Home `<title>` 76 chars and meta description 187 chars — both truncate in SERPs (~60 / ~155).
- **10 of 14 pages have no OG/Twitter tags at all** — all 4 demos, all 5 legal pages, `/gracias/`. The demos are the most shareable, credibility-building assets on the site and produce a bare-URL preview when posted to LinkedIn or WhatsApp.
- No favicon, no apple-touch-icon, no web manifest.
- No `hreflang` / `x-default` despite the `/es/` prefix.

**Structured data**
- Demos carry **no schema whatsoever** — no `Article`, no `WebPage`, no `datePublished`/`dateModified`, no `BreadcrumbList` despite rendering visual breadcrumbs. These are the pages with the strongest E-E-A-T signals (cited primary sources: BOE, CENDOJ, PLACSP, UNCTAD) and they emit nothing machine-readable.
- Legal pages: no `BreadcrumbList` despite visual breadcrumbs.
- No `ProfessionalService`/`LocalBusiness` with the published Madrid address — misses geo-qualified intent. *(Business decision: publishing a home address more prominently is yours to make.)*
- 4 near-identical FAQ Q&As are duplicated across the two `/es/` FAQPage blocks. *(Also worth verifying current Google guidance on FAQ rich-result eligibility before investing further in FAQ markup — it was materially restricted in 2023.)*

**Content depth**
- 14 pages total; **zero informational/blog content.** The site is entirely bottom-funnel plus three demos. Nothing targets the research phase where a comunidad, promotor or licitador starts.
- Internal linking is shallow: home → 2 service pages → home. Demos link out to service pages weakly; the lead magnet LP links to demos but nothing links back to it.
- **Zero images site-wide.** No diagram of the evidence chain, no sample report page, no report cover. No image-search surface, and a text-only presentation for a product whose output is a visual PDF report.
- No visible publication or update dates on demos (see C7).

---

## 6. Conversion gaps

Ranked by expected impact.

1. **No measurement of any kind.** No GA4, no Plausible, no server logs surfaced, no Meta/LinkedIn pixel, no Stripe attribution, no UTM handling. **Every number in any future growth decision is currently unobservable** — you cannot tell which of the 26 Stripe CTAs produces revenue, or whether the demos convert at all. Fix this before any optimisation work; everything else is guesswork until it exists. (Ships together with C2: analytics + banner + accurate cookie table.)
2. **Every primary CTA leaves the domain.** Zero `<form>` and zero `<input>` elements site-wide. 100% of conversion happens on `buy.stripe.com` or `tally.so`, with no on-site capture and no fallback for the visitor who isn't ready.
3. **Cold checkout as the default path.** The nav CTA on all 14 pages is a direct 490 € Stripe payment link, with no qualification step — for a service where *scope* determines the correct tier. Your own `/gracias/` page concedes this ("¿No sabes qué alcance necesitas?"). A qualify-then-buy path should be at least co-equal with buy-now.
4. **No human contact route on any commercial page.** Email and phone exist only in `/legal/`. Nobody buys a 15.000 € Pre-Bid audit from a payment link with no way to speak to a person first.
5. **No booking/scheduling anywhere**, although the process promises a *"Sesión de decisión"* as step 4. A calendar link is the natural qualification step for the three high-ticket lines.
6. **Broken lead-magnet gate.** The PDF is directly fetchable at a guessable URL and is crawlable (§5). The form can be bypassed entirely.
7. **The lead-magnet landing page is orphaned** — zero inbound internal links, absent from the sitemap. Rung-1 currently cannot receive traffic.
8. **No post-purchase handoff on-site.** `condiciones-servicio` §2 defines the flow as pay → intake form → upload. `/gracias/` serves the *checklist* download, not the *purchase*. Where Stripe sends a paying customer afterwards is not visible in the repo *(live-only)* — if it's Stripe's default confirmation, buyers land with no instruction on how to submit documents, which delays the 48h clock the whole offer depends on.
9. **Mobile navigation is effectively absent** below 820 px (§1). Community board members and administradores browsing on a phone can reach the Stripe link and nothing else.
10. **No credibility layer.** No named expert on any commercial page, no methodology page, no report sample, no "quién está detrás". For an evidence-intelligence brand this is the biggest unforced trust gap — and the one thing that cannot be fixed without your input, since nothing may be invented.
11. **No objection handling above 2.500 €.** The three high-ticket lines have no FAQ, no scope table, no deliverables list, no "what happens after the deposit".
12. **Single secondary conversion for the whole site** — one checklist. No sequence, no segment-specific magnet (e.g. one for licitadores, one for administradores).

---

## 7. Recommended file-level implementation plan

Phased, each phase independently shippable. Nothing here changes a published price. Nothing here adds a claim that isn't already substantiated on the site. **Phase 0 items are corrections you should approve individually before I touch them.**

### Phase 0 — Integrity fixes *(low effort, highest exposure reduction)*

| File | Change |
|---|---|
| `legal/aviso-legal/index.html` | Remove `<blockquote>` L51-53 (C1) |
| `legal/privacidad/index.html` | Remove `<blockquote>` L77-79 (C1) |
| `legal/cookies/index.html` | Remove `<blockquote>` L41-43 (C1); rewrite §2-§3 to match reality — no non-essential cookies today (C2) |
| `legal/confidencialidad-documental/index.html` | Remove `<blockquote>` L45-47 (C1) |
| `index.html` | Hero microcta L50 → fix "Confidencialidad garantizada" + "Sin compromiso" (C3, C5); step 1 L86 NDA wording (C4); pricing footnote L115 → add 48h qualifier (C9); `og:title` L10 → Spanish (C12); `sameAs` (C11) |
| `es/revision-presupuesto-obra/index.html` | L59 microcta (C3); FAQ NDA answer (C4); JSON-LD `valueAddedTaxIncluded:false` (C10) |
| `es/auditoria-rehabilitacion-fachada/index.html` | Same three (C3, C4, C10) |
| `demos/mega-claim-canal-panama/index.html` | **Only after you re-verify the sources** — update L74/L91 status, add a "fuentes consultadas a fecha de" stamp (C7) |
| all 4 pages with "Más elegido" | Decide: keep with data, or swap to "Recomendado" (C6) |

### Phase 1 — Reconnect what already exists *(no new content required)*

| File | Change |
|---|---|
| `sitemap.xml` | Add `/recursos/21-riesgos-rehabilitacion/`; refresh `lastmod` |
| `index.html` | Add `/recursos/…` and `/demos/` to nav + footer; link the lead magnet section to the LP instead of jumping straight to Tally |
| `es/*/index.html` (×2) | Footer link to `/recursos/…` and `/demos/` |
| `assets/style.css` | Mobile nav: replace `display:none` (L38) with a CSS-only disclosure menu; drop dead `.highticket`/`.ht`/`.convert` |
| `robots.txt` | Decide `/descargas/` gating; drop the phantom `/thank-you/`, `/admin/` rules |
| `assets/` | Add the 4 missing images: `logo-coresyn.png`, `og-home.png`, `og-fachada.png`, `og-presupuesto.png` (C8) |
| `assets/favicon.ico` + `<link>` in all 14 heads | Favicon + apple-touch-icon |
| `404.html` (new) | Branded 404 routing to `/`, `/demos/`, `/es/` pages |

### Phase 2 — Measurement and conversion plumbing

| File | Change |
|---|---|
| all 14 heads | One analytics snippet (recommend a cookieless tool — it keeps C2 simple and avoids a banner entirely) |
| all CTA anchors | Consistent UTM/`data-cta` attributes so Stripe vs Tally vs demo paths become separable |
| `contacto/index.html` (new) | Email, phone, Calendly-style booking, plus a qualification form; `noindex` **not** applied |
| `gracias/index.html` | Split: keep checklist thank-you; add `gracias-compra/index.html` as the Stripe success URL with explicit "next: upload your documents" instructions *(needs the Stripe success URL set in dashboard — outside the repo)* |
| all commercial pages | Add a persistent contact/booking secondary CTA alongside the Stripe primary |

### Phase 3 — Tier-1 landing pages (the revenue gap)

New directories, each modelled on the existing `/es/revision-presupuesto-obra/` template (hero → problem → what we review → evidence chain callout → risks grid → profiles → deliverables → pricing/deposit → FAQ → CTA → footer disclaimer):

```
es/due-diligence-tecnica-edificio/index.html      → 5.000 € / depósito 2.500 € / link …4F20m
es/reclamacion-sobrecostes-obra/index.html        → 10.000 € / depósito 5.000 € / link …4F20n
es/auditoria-pliego-obra-publica/index.html       → 15.000 € / depósito 7.500 € / link …4F20o
```

Each ships with: `Service` + `BreadcrumbList` + `FAQPage` JSON-LD (with `valueAddedTaxIncluded:false`), self-referencing canonical, OG tags + image, the §3a disclaimer stack verbatim, a link from the matching demo page, and a `sitemap.xml` entry. Each high-ticket page leads with **booking/qualification**, not the deposit link.

### Phase 4 — Tier-2/3 pages and depth

`/es/precios/`, `/metodologia/`, `/recursos/` hub, then the five Tier-2 intent pages (§4), each cross-linked to its Tier-1 parent. `/es/quien-esta-detras/` **blocked pending your input** — bio, credentials and track record must come from you.

### Sequencing note

Phase 0 → 1 → 2 before Phase 3. Publishing three new high-ticket landing pages while the legal pages still say *"borrador base"* and while nothing is measurable would spend the content effort blind and against a weakened trust backdrop.

---

## Open questions for you

1. **C7** — what is the current status of the pending GUPC arbitration per the cited sources? I will not update that page from anything other than those sources.
2. **C4** — does the Tally intake actually include an NDA signature step?
3. **C6** — does Stripe data support "Más elegido" on Pro?
4. Stripe success URLs — where do the six payment links currently redirect after payment?
5. `/es/` vs root — commit to the prefix or flatten, before Phase 3 creates three more URLs under it?
6. Analytics preference — cookieless (no banner needed) or GA4 (banner + cookie table required)?

---

*Audit only. No site file was modified. Placed under `_audit/` so that Jekyll's default behaviour keeps it out of the published site if this branch is merged — verify before merge if the Pages build is ever switched to a static/Actions deploy.*
