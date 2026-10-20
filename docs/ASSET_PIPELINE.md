# Asset distribution pipeline (design)

This public repository stores **metadata only**. Heavy Unity AssetBundles / Addressables output will be attached to immutable GitHub Releases initially, with a future move to object storage possible.

## Proposed flow

1. Obtain source assets with documented authorship and redistribution rights.
2. Review licenses and content. Do not accept unreviewed third-party uploads into the public repository.
3. Import into the controlled Unity project, validate textures/meshes/animations, set size limits, check references and build separate Android and Windows bundles.
4. Test with the target Unity runtime and both platform clients. Unity AssetBundles are platform-specific and should not be considered inherently safe.
5. Upload immutable release assets; record SHA-256, exact byte count, HTTPS download URLs and dependency IDs in the catalog.
6. Client selects the matching platform, verifies bytes and hash, stages the download and activates only after compatibility checks.

## Current status — 2026-10-20

- Live catalog publishes two small original CC0 JSON packages: primitive marker objects and map surface colors. These are declarative data, not AssetBundles.
- Source Release `makehuman-cc0-skins-v1` is published: 8,091,253-byte ZIP, SHA-256 `6e20613c2288034f618e63ed2a259cb118e8840577ea049abcfa9891f54c1d3d`. All six unique original files are byte-verified; original license/author metadata is retained. This archive is source-only and is not advertised for runtime installation.
- Unity's experimental branch implements verified streaming downloads, persistent installation, race creation integration and an object/material library. Pure C# lifecycle and character persistence tests pass; native/device verification remains separate.
- Trusted Editor builder generates script-free demo prefabs and platform-specific manifests for Android and Windows. Binary AssetBundles are not yet built or published; never advertise them as tested.
- Runtime schema: `schemas/catalog-entry-v1.schema.json`. Heavy bundles must go to immutable Release assets after trusted build, size/hash/platform/Unity checks and device QA.
- No original game file has been removed. Most legacy asset groups still need individual license/dependency review.
- Never commit large binaries, private submissions, personal data, saves, keys or executable mods to this repository.
