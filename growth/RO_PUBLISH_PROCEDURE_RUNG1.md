# One-step publish procedure — Rung-1 landing (EXECUTE ONLY ON EXPLICIT OWNER GO)

Asset: `/recursos/21-riesgos-rehabilitacion/index.html`
Isolated commit: `3e1d3d13039972677b2992ab53bff0cd0cf7c17c` (touches ONLY the landing file)

## The one action (on GO)
```
git fetch origin main
git checkout -B publish-rung1 origin/main
git cherry-pick 3e1d3d13039972677b2992ab53bff0cd0cf7c17c
git push -u origin publish-rung1   # then owner merges, or push to main if owner says so
```
No lifecycle-baseline content is involved: the commit is based on files/URLs that all
exist in production. Cherry-pick onto main applies cleanly (verified: the commit's only
parent-path `recursos/` does not exist on main → no conflict possible).

## Compliance verification (done at build time, 2026-08-08)
- Zero "48h" anywhere in the page (nav CTA label is "Risk Scan" per owner D2 decision).
- Claims used: G1 (checklist exists — production PDF `descargas/21-riesgos-obra-rehabilitacion.pdf`),
  G2 (demos referenced with methodological framing). No prices changed, no new offers,
  existing Stripe/Tally links only (Stripe Risk Scan link + Tally 9qyYMp).
- Footer scope-limitation disclaimer copied verbatim from production `index.html`.
- Every internal link + CSS verified to exist on PRODUCTION_MAIN_SHA `96d4a1c` (style.css
  classes checked: hero/kicker/grid/card/steps/btn variants all present).
- Canonical, OG, WebPage + BreadcrumbList schema included; no Offer/Rating schema.

## Optional follow-ups at publish time (owner choice, not required for GO)
1. Sitemap: add one `<url>` block for `/recursos/21-riesgos-rehabilitacion/` to main's
   sitemap.xml (do this on the publish branch, NOT via the lifecycle baseline's sitemap).
2. Known pre-existing gap (new delta finding D6, production-wide): og:image URLs across
   production (og-home.png, og-fachada.png) point to files that do not exist in the repo —
   social-share previews 404 today. The landing mirrors the homepage's og-home.png
   reference for consistency. Fixing = separate owner-approved production change.
