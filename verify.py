#!/usr/bin/env python3
"""Verification script for the Low-Energy Days Handbook.

Checks:
- Required files exist
- LICENSE has the exact copyright line
- README credits Asdale Dynamics, LLC
- HTML files have basic valid structure
- Printable cards page has print CSS
- No secrets or personal data present
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
FAILURES = []


def check(condition, message):
    if not condition:
        FAILURES.append(message)
        print(f"FAIL: {message}")
    else:
        print(f"ok: {message}")


def read(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# 1. Required files exist
required_files = [
    "README.md",
    "LICENSE",
    ".gitignore",
    "docs/intro.md",
    "docs/pick-one-task.md",
    "docs/gentle-scheduling.md",
    "docs/rest-without-guilt.md",
    "docs/energy-tracking.md",
    "docs/low-demand-routines.md",
    "docs/routine-cards.md",
    "site/index.html",
    "site/cards.html",
    "site/css/style.css",
    "site/js/site.js",
]
for f in required_files:
    check(os.path.isfile(os.path.join(ROOT, f)), f"file exists: {f}")

# 2. LICENSE copyright line exact
license_text = read(os.path.join(ROOT, "LICENSE"))
check(
    "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text,
    "LICENSE has exact copyright line",
)

# 3. README credits Asdale Dynamics, LLC
readme_text = read(os.path.join(ROOT, "README.md"))
check("Asdale Dynamics, LLC" in readme_text, "README credits Asdale Dynamics, LLC")

# 4. HTML structure
for html_file in ["site/index.html", "site/cards.html"]:
    text = read(os.path.join(ROOT, html_file))
    check(text.strip().startswith("<!DOCTYPE html>"), f"{html_file}: starts with DOCTYPE")
    check("<html" in text, f"{html_file}: has html tag")
    check("</html>" in text, f"{html_file}: closes html tag")
    check("css/style.css" in text, f"{html_file}: links stylesheet")

# 5. Printable cards print CSS
cards_text = read(os.path.join(ROOT, "site/cards.html"))
check("@media print" in cards_text, "cards.html: has print media query")
check("window.print()" in cards_text or "Print Cards" in cards_text, "cards.html: has print trigger")
check("card-grid-print" in cards_text, "cards.html: has print card grid")

# 6. No secrets / personal data patterns
secret_patterns = [
    r"sk-[A-Za-z0-9]{20,}",           # OpenAI-style keys
    r"AKIA[0-9A-Z]{16}",              # AWS keys
    r"ghp_[A-Za-z0-9]{36,}",          # GitHub tokens
    r"[0-9]{3}-[0-9]{2}-[0-9]{4}",    # SSN-like
]
all_text = ""
for dirpath, _, files in os.walk(ROOT):
    if ".git" in dirpath:
        continue
    for fn in files:
        if fn.endswith((".md", ".html", ".css", ".js", ".py", ".txt", "LICENSE", ".gitignore")):
            try:
                all_text += read(os.path.join(dirpath, fn)) + "\n"
            except Exception:
                pass
for pat in secret_patterns:
    check(not re.search(pat, all_text), f"no secret pattern: {pat}")

# 7. No .github/workflows
check(
    not os.path.exists(os.path.join(ROOT, ".github", "workflows")),
    "no .github/workflows directory",
)

print()
if FAILURES:
    print(f"{len(FAILURES)} check(s) failed.")
    sys.exit(1)
print("All checks passed.")
sys.exit(0)
