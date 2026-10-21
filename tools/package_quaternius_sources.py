"""Archive only the exact model/texture files matched to the CC0 Standard kit."""
import hashlib,json,urllib.request,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1];plan=json.loads((root/'migration/quaternius-source-release.json').read_text());out=root/'dist';out.mkdir(exist_ok=True)
archive=out/(plan['tag']+'.zip')
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 def add(name,data):
  info=zipfile.ZipInfo(name,(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data)
 for f in plan['files']:
  assert f['url'].startswith('https://raw.githubusercontent.com/waitermisanthrope-creator/DnD-VTT/'+plan['sourceCommit']+'/app/assets/3d/quaternius/')
  with urllib.request.urlopen(f['url'],timeout=60) as r:b=r.read(f['bytes']+1)
  assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'],f['path']
  add(f['path'],b)
 license=(root/'sources/quaternius-fantasy-props-standard/License_Standard.txt').read_bytes();assert hashlib.sha256(license).hexdigest()==plan['licenseSha256']
 add('License_Standard.txt',license);add('PROVENANCE.json',json.dumps(plan,indent=2).encode())
b=archive.read_bytes();h=hashlib.sha256(b).hexdigest()
(out/'quaternius-SHA256SUMS.txt').write_text(h+'  '+archive.name+'\n')
(out/'quaternius-release-manifest.json').write_text(json.dumps({'tag':plan['tag'],'bytes':len(b),'sha256':h,'sourceFiles':len(plan['files']),'sourceBytes':sum(f['bytes'] for f in plan['files']),'runtimeStatus':'source-only; trusted runtime AssetBundle publication still pending'},indent=2)+'\n')
print('QUATERNIUS_SOURCE_PACKAGE_VERIFIED',len(b),h)
