"""Reviewed author images -> individual runtime JSON release assets. No Git binaries."""
import base64,hashlib,io,json,re,sys
from pathlib import Path
from PIL import Image
import cairosvg
root=Path(sys.argv[1]); out=Path('dist/owner-appearance-v1');out.mkdir(parents=True,exist_ok=True)
sha=lambda b:hashlib.sha256(b).hexdigest()
config=json.loads(Path('migration/owner-appearance.json').read_text())
packs=[]; provenance=[]
for entry in config['files']:
 path=root/entry['path']; original=path.read_bytes()
 if sha(original)!=entry['sha256']:raise ValueError('Source changed: '+str(path))
 if path.suffix.lower()=='.svg':
  text=original.decode()
  if re.search(r'href\s*=|url\s*\(|<script|<!DOCTYPE|<!ENTITY',text,re.I):raise ValueError('SVG external/active content')
  image=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=original))).convert('RGBA')
 else:image=Image.open(io.BytesIO(original)).convert('RGBA')
 if max(image.size)>2048 or image.width*image.height>4194304:raise ValueError('Dimensions')
 buf=io.BytesIO();image.save(buf,format='PNG',optimize=True);png=buf.getvalue()
 if Image.open(io.BytesIO(png)).convert('RGBA').tobytes()!=image.tobytes():raise ValueError('Pixel mismatch')
 data={'schemaVersion':1,'id':entry['id'],'version':'1.0.0','type':'appearance','images':[{'id':entry['id']+'.image','name':entry['name'],'kind':entry['kind'],'width':image.width,'height':image.height,'sha256':sha(png),'pngBase64':base64.b64encode(png).decode()}]}
 payload=json.dumps(data,ensure_ascii=False,separators=(',',':')).encode()
 if len(payload)>5*1024*1024:raise ValueError('JSON size cap')
 filename=entry['id']+'.json';(out/filename).write_bytes(payload)
 packs.append({'schemaVersion':1,'id':entry['id'],'name':entry['name'],'version':'1.0.0','author':'waitermisanthrope-creator','license':'Author-authorized DnD-VTT distribution','type':'appearance','format':'json','platform':'any','unityVersion':'','dependencies':[],'bytes':len(payload),'sha256':sha(payload),'url':'https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/download/owner-appearance-v1/'+filename,'description':'Авторское оформление. Создано владельцем проекта с использованием нейросетей; преимущественно Gemini и ChatGPT. Иконка — изображение оформления, не автоматическая замена системного значка Android.','imageKind':entry['kind']})
 provenance.append(dict(entry,sourceBytes=len(original),pngBytes=len(png),pngSha256=sha(png),renderedPixelsSha256=sha(image.tobytes())))
base=json.loads(Path('catalog/v2/index.json').read_text());base['packs']+=packs;base['catalogId']='dnd-vtt-assets-v3'
(out/'index.json').write_text(json.dumps(base,ensure_ascii=False,indent=2)+'\n')
(out/'provenance.json').write_text(json.dumps({'author':config['author'],'permission':config['permission'],'sourceCommit':config['sourceCommit'],'files':provenance},ensure_ascii=False,indent=2)+'\n')
(out/'SHA256SUMS.txt').write_text(''.join(sha(p.read_bytes())+'  '+p.name+'\n' for p in sorted(out.glob('*.json'))))
print('OWNER_APPEARANCE_PACKAGES_PASS',len(packs),sum(p['bytes'] for p in packs))
