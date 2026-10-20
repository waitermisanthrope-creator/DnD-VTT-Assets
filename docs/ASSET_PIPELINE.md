# Asset distribution pipeline (design)

This public repository stores **metadata only**. Heavy Unity AssetBundles / Addressables output will be attached to immutable GitHub Releases initially, with a future move to object storage possible.

## Proposed flow

1. Obtain source assets with documented authorship and redistribution rights.
2. Review licenses and content. Do not accept unreviewed third-party uploads into the public repository.
3. Import into the controlled Unity project, validate textures/meshes/animations, set size limits, check references and build separate Android and Windows bundles.
4. Test with the target Unity runtime and both platform clients. Unity AssetBundles are platform-specific and should not be considered inherently safe.
5. Upload immutable release assets; record SHA-256, exact byte count, HTTPS download URLs and dependency IDs in the catalog.
6. Client selects the matching platform, verifies bytes and hash, stages the download and activates only after compatibility checks.

## Current status

- Catalog is empty; no bundles or releases have been published.
- This is a design contract, not a claim that Unity already installs AssetBundles or Addressables.
- The existing Unity content manager prototype downloads JSON only. Implementing bundle installation, asset registry and cross-platform builds is future work.
- Avoid committing large binaries to Git history, executable mods, personal data or secrets.
