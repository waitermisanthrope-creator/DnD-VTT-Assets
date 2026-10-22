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

The gallery thumbnails are bounded320x200 schematic projections of the actual
C# generator meshes, exported from d3efae76 and pinned by recipe SHA in
sources/dice-preview-geometry-v1.json. They show a representative d20, not a
Unity screenshot or a transfer of the original icon texture. The dice table
provides the actual interactive model. tools/dice_geometry_preview.py is used
by the existing preview producer/publisher. The previous75 JPEGs stay byte-identical;
new31 previews are activated in v5 only after public byte/SHA verification.

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

Status:31 sets/seven families and mixed/large request checks passed native
Android and Windows gates. Unity1.00.24 is published. Physical-device
verification remains separate; recipe generation alone is not device testing.

Verification: App candidate39810382192/source d3efae76 passed both targets
(60 face checks,129 PhysX throws and both11-die mixed requests per target),
real Windows install/upgrade/reinstall, Android original signature/identity.
Preview run39815906775 SUCCESS;106 public JPEGs verified before v5 activation
in5a351ce.31 dice schematics total220,272 bytes.75 old previews unchanged.
APK paired publication39814696908 SUCCESS (feed10024/ec040aa9); both actual
public installers size/SHA verified, actual public APK original v2/v3 certificate
independently checked. Physical-device validation remains pending. The linked icon must be installed first: the current
manager deliberately disables installation while a dependency is missing.

## Material revision1.1.0 (Unity1.00.26+)

Existing appearance publisher generates31 immutable JSON Release payloads with an embedded1024-square UV atlas (about3.5MB per independently installed set). No art in APK. Catalogv6 only; v5 recipes untouched.1.1 sets no longer require a launcher icon installation; the icon ID is an artistic association. Native choices include manual installed-set selection and explicit icon-following. Two specifically authored face regions target Abyss/Blood references; other palettes use tinted engraved silver, not31 exact separate sculpts. Do not advertise these as exact replicas. The old schematic preview is omitted until actual textured native renders can replace it.
