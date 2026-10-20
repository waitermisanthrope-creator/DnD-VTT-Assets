"""Build a deterministic source archive, never a Unity executable or plugin."""
import hashlib,json,urllib.request,zipfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
plan=json.loads((root/'migration/reviewed-source-release.json').read_text())
out=root/'dist';out.mkdir(exist_ok=True)
archive=out/'makehuman-cc0-skins-v1.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 def add(name,data):
  info=zipfile.ZipInfo(name,(2026,1,1,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o100644<<16;z.writestr(info,data)
 for f in plan['files']:
  assert f['url'].startswith('https://raw.githubusercontent.com/waitermisanthrope-creator/DnD-VTT/'+plan['sourceCommit']+'/app/assets/3d/makehuman/skins/')
  with urllib.request.urlopen(f['url'],timeout=60) as r:b=r.read(f['bytes']+1)
  assert len(b)==f['bytes'] and hashlib.sha256(b).hexdigest()==f['sha256'], f['path']
  add(f['path'],b)
 for p in sorted((root/'sources').rglob('*')):
  if p.is_file():add(str(p.relative_to(root/'sources')),p.read_bytes())
 add('PROVENANCE.json',json.dumps(plan,indent=2).encode())
b=archive.read_bytes();(out/'SHA256SUMS.txt').write_text(hashlib.sha256(b).hexdigest()+'  '+archive.name+'\n')
(out/'release-manifest.json').write_text(json.dumps(dict(tag=plan['tag'],bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),url='https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/download/'+plan['tag']+'/'+archive.name,sourceFiles=plan['files'],runtimeStatus='source-only; not a Unity bundle'),indent=2)+'\n')
print('SOURCE_PACKAGE_VERIFIED',len(b),hashlib.sha256(b).hexdigest())
