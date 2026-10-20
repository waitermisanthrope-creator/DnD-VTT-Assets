# DnD-VTT-Assets

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
