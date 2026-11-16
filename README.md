# OKARU (郁) · community palettes

**English** · [Español](#español)

Color palettes for [OKARU](https://github.com/MrAndyVF/okaru). OKARU reads this repository's `catalog.json` and
lists them in **Settings → Appearance** («Community» source); when you pick one, it downloads
`palettes/<Name>.json`.

## Contributing a palette

1. Create `palettes/<Name>.json` with a `dark` block and a `light` block. Required tokens in both:
   `mPrimary`, `mSecondary`, `mTertiary`, `mError`, `mSurface`, `mOnSurface` (hex `#rrggbb`). Optional:
   `mOnPrimary`, `mOnSecondary`, `mOnTertiary`, `mOnError`, `mSurfaceVariant`, `mOnSurfaceVariant`,
   `mOutline`, `mShadow`, `mHover`, `mOnHover` and `terminal`.
2. Run `python3 tools/build_catalog.py` and commit `catalog.json` in the same pull request.

The GitHub Action checks that `catalog.json` is up to date and that every palette has the required tokens.

## Included palettes

Written for OKARU from each theme's official colors (with OKARU's own roles and light mode when the original
has none): Atom One, Ayu, Catppuccin (Mocha, Frappé, Macchiato; Latte light), Dracula (Alucard light),
Eldritch, Everforest, GitHub (Primer), Gruvbox, Kanagawa (Wave/Lotus), Monokai, Nightfox (Dayfox), Nord,
Rosé Pine (Dawn), Solarized and Tokyo Night (Night, Storm, Moon; Day light).

## License

MIT. By opening a pull request you agree to publish your palette under this license; do not submit
third-party work without permission.

---

## Español

Paletas de color para [OKARU](https://github.com/MrAndyVF/okaru). OKARU lee `catalog.json` de este repo y las
muestra en **Ajustes → Apariencia** (fuente «Comunidad»); al elegir una, descarga `palettes/<Nombre>.json`.

### Aportar una paleta

1. Crea `palettes/<Nombre>.json` con un bloque `dark` y otro `light`. Tokens obligatorios en ambos:
   `mPrimary`, `mSecondary`, `mTertiary`, `mError`, `mSurface`, `mOnSurface` (hex `#rrggbb`). Opcionales:
   `mOnPrimary`, `mOnSecondary`, `mOnTertiary`, `mOnError`, `mSurfaceVariant`, `mOnSurfaceVariant`,
   `mOutline`, `mShadow`, `mHover`, `mOnHover` y `terminal`.
2. Ejecuta `python3 tools/build_catalog.py` y sube `catalog.json` en el mismo pull request.

La GitHub Action comprueba que `catalog.json` esté al día y que cada paleta tenga los tokens obligatorios.

### Paletas incluidas

Escritas para OKARU a partir de los colores oficiales de cada tema (roles y modo claro propios cuando el
original no tiene): Atom One, Ayu, Catppuccin (Mocha, Frappé, Macchiato; claro Latte), Dracula (claro
Alucard), Eldritch, Everforest, GitHub (Primer), Gruvbox, Kanagawa (Wave/Lotus), Monokai, Nightfox (Dayfox),
Nord, Rosé Pine (Dawn), Solarized y Tokyo Night (Night, Storm, Moon; claro Day).

### Licencia

MIT. Al enviar un pull request aceptas publicar tu paleta bajo esta licencia; no subas trabajo de terceros
sin su permiso.
