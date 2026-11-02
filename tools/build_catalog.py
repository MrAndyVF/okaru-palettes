#!/usr/bin/env python3
"""Genera catalog.json a partir de palettes/<Nombre>.json (formato que lee OKARU).

Cada paleta tiene "dark" y "light" con los tokens mPrimary, mSecondary, mTertiary, mError, mSurface…
Uso:
    python3 tools/build_catalog.py           # escribe catalog.json
    python3 tools/build_catalog.py --check   # falla si catalog.json no está al día
"""
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PALETTES = os.path.join(ROOT, "palettes")
CATALOG = os.path.join(ROOT, "catalog.json")
REQUIRED = ["mPrimary", "mSecondary", "mTertiary", "mError", "mSurface", "mOnSurface"]
HEX = re.compile(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$")
PREVIEW = {"primary": "mPrimary", "secondary": "mSecondary", "tertiary": "mTertiary", "error": "mError",
           "surface": "mSurface", "surfaceVariant": "mSurfaceVariant"}


def build():
    entries, errors = [], []
    for file in sorted(os.listdir(PALETTES)) if os.path.isdir(PALETTES) else []:
        if not file.endswith(".json"):
            continue
        name = file[:-5]
        path = os.path.join(PALETTES, file)
        raw = open(path, "rb").read()
        try:
            data = json.loads(raw)
        except json.JSONDecodeError as e:
            errors.append(f"{file}: JSON inválido ({e})")
            continue
        entry = {"name": name, "md5": hashlib.md5(raw).hexdigest()}
        for mode in ("dark", "light"):
            colors = data.get(mode, {})
            missing = [k for k in REQUIRED if not HEX.match(str(colors.get(k, "")))]
            if missing:
                errors.append(f"{file}: {mode} sin {', '.join(missing)}")
            entry[mode] = {k: colors[v] for k, v in PREVIEW.items() if v in colors}
        entries.append(entry)
    return entries, errors


def main():
    entries, errors = build()
    for e in errors:
        print("error:", e, file=sys.stderr)
    text = json.dumps(entries, indent=1, ensure_ascii=False) + "\n"
    if "--check" in sys.argv:
        current = open(CATALOG, encoding="utf-8").read() if os.path.exists(CATALOG) else ""
        if current != text:
            print("catalog.json no está al día: ejecuta python3 tools/build_catalog.py", file=sys.stderr)
            return 1
        return 1 if errors else 0
    with open(CATALOG, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"{len(entries)} paletas en catalog.json")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
