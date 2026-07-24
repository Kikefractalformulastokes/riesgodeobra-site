#!/usr/bin/env python3
"""RiesgoDeObra static-site checks. Run from the repo root: python3 tests/site_checks.py

Exits non-zero if any check fails. No external dependencies beyond the
standard library, so it runs in CI without a build step.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# (pattern, negation_window) — if a negation word (no/sin/nunca/jamás) appears
# within `negation_window` chars before the match, it's denial language
# ("no hay integración automática...") and must NOT be flagged.
PROHIBITED_PATTERNS = [
    (r"\b6[0-9]\s?%\s*(de\s+)?(reducci[oó]n|ahorro|menos tiempo)", 0),
    (r"\b7[0-9]\s?%\s*(de\s+)?(reducci[oó]n|ahorro|menos tiempo)", 0),
    (r"AES-?256", 0),
    (r"hosting\s+(en\s+)?(la\s+)?(UE|EU|europ)", 40),
    (r"integraci[oó]n\s+autom[aá]tica.{0,20}CENDOJ", 40),
    (r"CENDOJ.{0,20}autom[aá]tic", 40),
    (r"[ée]xito\s+(judicial|en\s+los\s+tribunales|en\s+juicio)", 40),
    (r"clientes?\s+(corporativos|actuales|existentes)\b", 40),
    (r"validaci[oó]n\s+de\s+campo", 40),
    (r"ISO\s?27001|SOC\s?2|GDPR\s+certif", 40),
]
NEGATION_RE = re.compile(r"\b(no|sin|nunca|jam[aá]s|ni)\b", re.I)

# Case-sensitive: real placeholder markers are written in caps
# ("TODO:", "FIXME"). Case-insensitive would false-positive on the common
# Spanish word "todo" (all/everything).
PLACEHOLDER_PATTERNS = [
    r"[Ll]orem ipsum", r"\bTODO\b", r"\bFIXME\b", r"\bXXXX+\b",
    r"example\.com", r"REPLACE_ME", r"\[nombre\]", r"\[cif\]",
]


def find_pages():
    return sorted(glob.glob("**/index.html", recursive=True))


def check_json_ld(pages):
    errors = []
    for path in pages:
        d = open(path, encoding="utf-8").read()
        for m in re.finditer(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', d, re.S):
            try:
                json.loads(m.group(1))
            except Exception as e:
                errors.append(f"{path}: invalid JSON-LD ({e})")
    return errors


def check_duplicate_titles_and_descriptions(pages):
    titles, descriptions = {}, {}
    errors = []
    for path in pages:
        d = open(path, encoding="utf-8").read()
        tm = re.search(r"<title>(.*?)</title>", d, re.S)
        dm = re.search(r'<meta name="description" content="([^"]*)"', d)
        if tm:
            titles.setdefault(tm.group(1).strip(), []).append(path)
        if dm:
            descriptions.setdefault(dm.group(1).strip(), []).append(path)
    for title, paths in titles.items():
        if len(paths) > 1:
            errors.append(f"Duplicate <title> across {paths}: {title!r}")
    for desc, paths in descriptions.items():
        if len(paths) > 1:
            errors.append(f"Duplicate meta description across {paths}: {desc!r}")
    return errors


def check_internal_links(pages):
    errors = []
    for path in pages:
        d = open(path, encoding="utf-8").read()
        for href in re.findall(r'href="(/[^"]*)"', d):
            clean = href.split("#")[0]
            if not clean or clean.startswith("http"):
                continue
            target = "." + clean + ("index.html" if clean.endswith("/") else "")
            if not os.path.isfile(target):
                errors.append(f"{path}: broken internal link {href!r}")
    return errors


def check_prohibited_and_placeholders(pages):
    errors = []
    for path in pages:
        d = open(path, encoding="utf-8").read()
        for pat, window in PROHIBITED_PATTERNS:
            for m in re.finditer(pat, d, re.I):
                before = d[max(0, m.start() - window):m.start()] if window else ""
                after = d[m.end():m.end() + 5]
                if window and NEGATION_RE.search(before):
                    continue  # denial language, e.g. "no hay integración automática..."
                if window and after.lstrip().startswith("?"):
                    continue  # a question ("¿Tenéis...?"), not a claim
                errors.append(f"{path}: matches prohibited-claim pattern {pat!r}: {m.group(0)!r}")
        for pat in PLACEHOLDER_PATTERNS:
            m = re.search(pat, d)
            if m:
                errors.append(f"{path}: matches placeholder pattern {pat!r}: {m.group(0)!r}")
    return errors


def check_canonical_present(pages):
    errors = []
    for path in pages:
        d = open(path, encoding="utf-8").read()
        if '<link rel="canonical"' not in d:
            errors.append(f"{path}: missing canonical link")
        if 'name="viewport"' not in d:
            errors.append(f"{path}: missing viewport meta")
    return errors


def check_sitemap_routes_resolve():
    errors = []
    sm = open("sitemap.xml", encoding="utf-8").read()
    for loc in re.findall(r"<loc>(.*?)</loc>", sm):
        path = loc.replace("https://riesgodeobra.es", "").lstrip("/")
        target = path + ("index.html" if path.endswith("/") or path == "" else "")
        if target and not os.path.isfile(target):
            errors.append(f"sitemap.xml: route {loc!r} does not resolve to a file ({target})")
    return errors


def main():
    pages = find_pages()
    all_errors = []
    checks = [
        ("JSON-LD validity", check_json_ld),
        ("Duplicate titles/descriptions", check_duplicate_titles_and_descriptions),
        ("Internal links resolve", check_internal_links),
        ("No prohibited claims / placeholders", check_prohibited_and_placeholders),
        ("Canonical + viewport present", check_canonical_present),
    ]
    for name, fn in checks:
        errs = fn(pages)
        status = "OK" if not errs else f"FAIL ({len(errs)})"
        print(f"[{status}] {name}")
        for e in errs:
            print(f"    - {e}")
        all_errors.extend(errs)

    sm_errors = check_sitemap_routes_resolve()
    status = "OK" if not sm_errors else f"FAIL ({len(sm_errors)})"
    print(f"[{status}] Sitemap routes resolve")
    for e in sm_errors:
        print(f"    - {e}")
    all_errors.extend(sm_errors)

    print(f"\n{len(pages)} pages checked, {len(all_errors)} total failures")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
