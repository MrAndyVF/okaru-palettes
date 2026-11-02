# OKARU (郁) · paletas de la comunidad

Paletas de color para [OKARU](https://github.com/MrAndyVF). OKARU lee `catalog.json` de este repo y las
muestra en **Ajustes → Apariencia** (fuente «Comunidad»); al elegir una, descarga `palettes/<Nombre>.json`.

## Aportar una paleta

1. Crea `palettes/<Nombre>.json` con un bloque `dark` y otro `light`. Tokens obligatorios en ambos:
   `mPrimary`, `mSecondary`, `mTertiary`, `mError`, `mSurface`, `mOnSurface` (hex `#rrggbb`). Opcionales:
   `mOnPrimary`, `mOnSecondary`, `mOnTertiary`, `mOnError`, `mSurfaceVariant`, `mOnSurfaceVariant`,
   `mOutline`, `mShadow`, `mHover`, `mOnHover` y `terminal`.
2. Ejecuta `python3 tools/build_catalog.py` y sube `catalog.json` en el mismo pull request.

La GitHub Action comprueba que `catalog.json` esté al día y que cada paleta tenga los tokens obligatorios.

## Licencia

MIT. Al enviar un pull request aceptas publicar tu paleta bajo esta licencia; no subas trabajo de terceros
sin su permiso.
