# Six-theme test catalogs —2026-10-23

Unity1.00.30 uses catalog/v8: six1.2.1 test profiles, numbered common atlas, organic movement/ice glide/blood/dust/roots/jelly effects implemented in client. Requires both app update and workshop pack update. Choose via3D table → Мои наборы. v6/1.1 retained for28; v7/1.2.0 belongs to29 candidate rejected in visual review (mirrored UV digits), never activated in-app.30 candidate39884231802 and all3jobs passed;85public native PNGs and both installers SHA verified, full6d20/all42forms/post-result frames reviewed. APK original v2/v3 signature verified. App30 activation2a5eb1817712901c94b2a820592325d71a3d7702 verified in plain/cache-busted feed. Preview39886887017/job120197028869 SUCCESS activates6native JPEGs133973bytes in6750d77db994c3a9543c11fb79a7454eea5d21e9; all public JPEGs and v8 plain/cache-busted catalog independently verified. No exact sculpt/full soft-body claim. Source/data are public; native model thumbnails must come from exact reviewed app renders, not texture sheets.

# Current client catalogs —2026-10-22

Unity1.00.28+ uses **catalog/v6/index.json**: optional1.1 UV-textured dice with independent installed-set selection and real native Unity previews. v5 remains for1.00.24/25, v4 for1.00.23; all old payloads retained. Material1.1 data is compatible with26+, but28 fixes world numeral depth, fit, contrast and overexposed tint. No exact31 sculpt claim:01/05 have reference-authored face art, other29 use tinted engraved material.

# DnD-VTT-Assets

> **Новый участник команды / ChatGPT:** прочитай [AGENTS.md](AGENTS.md), [атлас всех файлов](docs/FILE_ATLAS.md) и [руководство по созданию модов в Content](https://github.com/waitermisanthrope-creator/DnD-VTT-Content/blob/main/docs/MOD_AUTHOR_GUIDE.md). Для Unity1.00.24+ каталог ассетов: `catalog/v5/index.json`; v4 сохранён для1.00.23.

Public curated Unity asset registry.

- `catalog/v1/index.json`: original CC0 declarative marker objects and map surface colors, activated by the Unity workshop.
- `packages/`: tiny JSON definitions; these are not AssetBundles.
- `schemas/catalog-entry-v1.schema.json`: shared platform-aware runtime manifest.
- Release `makehuman-cc0-skins-v1`: exact original CC0 skin textures, license and author metadata. SHA-256 and byte counts included; source archive only, not registered for runtime installation.
- `migration/verified-copies-v1.json`: exact copied metadata. Original application files have not been removed.

Heavy binaries go to Releases. Unity Android/Windows AssetBundle builder is implemented in the application branch, but bundles have not yet been built or published. No arbitrary user projects, scripts, assemblies or unreviewed third-party resources are accepted.

## Modular client 1.00.08

`catalog/v2/index.json` is consumed by Unity 1.00.08+. The v1 catalog remains unchanged for 1.00.07 and earlier clients. New packages are individual declarative race/class/feat records and project map documents; manifests pin exact SHA-256 and byte lengths. Existing character IDs remain unchanged. No executable plugins are included.

The mechanical metadata has newly written short descriptions, without republishing sourcebook prose or art. Stat changes, initial character parameters and pending choices use the currently supported Unity handlers; full combat automation and class advancement are not provided by these data packages. Extra classes that replace a race remain import-only in Unity. Feat stat bonuses are applied; other feat effects and additional prerequisites require manual handling.

Legacy third-party PNG/model files have NOT been relicensed or republished. Their exact provenance review remains BLOCKED. The new map-surface package provides original procedural checker patterns under the same legacy map keys; these are replacements, not byte-identical copies of the original images. The original files stay in the application's source repository, outside the minimal player's dependency graph. Maps preserve model references and show placeholders when a model package is missing.

## Owner-created appearance library

- `catalog/v3/index.json`: Unity 1.00.17+ catalog, including 63 owner-authorized image packs (32 wallpapers, 30 dice images, original standard icon). v2 remains available for old clients.
- [owner-appearance-v1](https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/tag/owner-appearance-v1): 118,807,535 bytes of separate runtime JSON packages; all public sizes/SHA-256 verified before catalog activation. Nothing is automatically bundled into the application.
- `schemas/catalog-entry-v3.schema.json`: validated image-aware schema.
- `docs/OWNER_APPEARANCE.md`: author permission, AI provenance and conversion details. These images are not represented as CC0.

Native Unity supports selecting installed wallpapers, icon previews and PNG export. Downloadable images do not automatically replace the Android system launcher icon. Original application sources remain unchanged.

## Lightweight graphical previews — Unity 1.00.22+

`catalog/v4/index.json` preserves package identity, version, original authorship/license and payload SHA, adding independent bounded preview metadata. v3 remains unchanged for older clients. Release `workshop-previews-v1` physically contains 75 JPEGs totaling 672,045 bytes, plus preview-index.json with original-source attribution and checksums. Every public preview URL/size/SHA was verified before catalog activation.

Owner wallpapers/icons use scaled originals. Map previews are first-floor layout schematics, procedural materials use actual swatches, and the primitive marker pack uses a clearly labeled geometric schematic. Schematics are not presented as final 3D renders. The generator does not publish unknown binary models or unreviewed author projects.

New clients fetch only small previews of the current workshop page into an ephemeral bounded cache, clear it on exit, and do not download/install the full content package for browsing. Full package integrity checks and installation remain separate.

- `catalog/v5/index.json`: 31 icon-linked full procedural dice sets for Unity1.00.24+; v4 stays compatible with previous clients. See [dice data and collision contract](docs/DICE_THEMES.md).

Dice previews:31 real-generator geometry schematics (220,272 bytes total), added by the existing preview workflow after public SHA verification;75 previous previews remain unchanged. Runtime v5 / Unity1.00.24+.

## Native trays and living dice — Unity1.00.32

Current catalogv9 adds four tiny native tray recipes (spiral tower, pit tower, hexagon, octagon) while preserving all107existing payloads. Download then select on the dice screen with «Лоток / башня». Existing six1.2.1 sets use the new app's compliant every-vertex Abyss arms and bouncing slime; up to20physical bodies concurrently, unlimited total request streaming. Explicit opt-in phone shake requires actual accelerometer hardware. Native32 previews are pinned to reviewed app evidence via the same preview pipeline; real phone sensitivity/performance remains owner QA. See docs/DICE_THEMES.md. Beta remains free.
