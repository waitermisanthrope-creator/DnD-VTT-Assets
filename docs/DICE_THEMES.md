# Icon-linked procedural dice, generator v1 (Unity 1.00.24+)

31 independently downloadable sets correspond to all 30 author dice icons plus
`default`. Every set contains d4/d6/d8/d10/d12/d20 and the physical d100 pair.
Names, palettes and structural families were reviewed against the original images.
This is a stylized procedural interpretation, not an exact sculpted copy or a
promise of certified fair probability. Owner source artwork/license is unchanged.

`tools/package_dice_themes.py` deterministically writes the small JSON recipes,
byte lengths/SHA-256 and `catalog/v5`. v4 remains unchanged for old clients, which
cannot activate these recipes. The new client must validate the new data before
activation. The linked icon is an actual package dependency; uninstall protection
uses the existing workshop mechanism. Images are not duplicated into recipes.

The gallery thumbnail currently shows the linked original icon as a style
reference, explicitly disclosed in the package description; it is not a render
of the resulting 3D model. The dice table itself provides the real model preview.

Seven bounded physical families: spikes, curved tentacles, curved fangs, beveled
bodies, vines, crystals, raised filigree. Frusta are closed convex meshes,
with the identical mesh used for rendering and each compound collision piece.
Curves follow incident edges and remain compound shapes, not a single convex hull that fills empty gaps. Smooth sets clip physical corners while retaining original numbered face regions. Meshes are reused across batches in a bounded per-theme cache.
Numbering remains on the original readable face regions. Themed results require
an upward/downward dominant numbered face; ambiguous rests are retried with a
bounded explicit failure. Real irregular collisions can bias outcomes.

No code, shader source, URL to arbitrary executables, paid access or server
secret is accepted in a theme recipe. Color and geometry parameters are bounded
by the client's validator. Android/Windows share the same generator and data.

Status: recipes prepared; native candidate must pass all31 sets, all7 collision
families and mixed/large request tests before releasing the client. Do not claim
successful physical-device testing from recipe generation.
