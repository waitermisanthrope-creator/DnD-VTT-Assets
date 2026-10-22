"""Generate small, hashed workshop previews from already published reviewed JSON packages."""
import argparse,base64,hashlib,io,json,urllib.request,sys,re
from pathlib import Path
from PIL import Image,ImageDraw,ImageColor,ImageChops
from dice_geometry_preview import render as render_dice
DICE=json.loads((Path(__file__).resolve().parents[1]/"sources/dice-preview-geometry-v1.json").read_text());DICE_MODELS={m["id"]:m for m in DICE["models"]}
ROOT='https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/download/workshop-previews-v1/'
p=argparse.ArgumentParser();p.add_argument('--native-dice',action='store_true');p.add_argument('--fixtures',type=Path);p.add_argument('--out',type=Path,default=Path('dist/workshop-previews-v1'));args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True)
def fetch(url,limit):
 assert url.startswith(('https://raw.githubusercontent.com/waitermisanthrope-creator/DnD-VTT-Assets/main/','https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/download/'))
 with urllib.request.urlopen(url,timeout=90) as r:data=r.read(limit+1)
 assert len(data)<=limit;return data
if args.native_dice:
 source=json.loads(Path('sources/dice-native-render-v1.json').read_text())
 assert re.fullmatch(r'unity-v[1-9][0-9]{0,3}\.[0-9]{2}\.[0-9]{2}',source['release'])
 prefix='https://github.com/waitermisanthrope-creator/DnD-VTT/releases/download/'+source['release']+'/'
 def native(name,limit):
  assert '/' not in name and '..' not in name
  with urllib.request.urlopen(prefix+name,timeout=90) as response:raw=response.read(limit+1)
  assert len(raw)<=limit;return raw
 raw=native('dice-render-index.json',64*1024);assert hashlib.sha256(raw).hexdigest()==source['indexSha256']
 evidence=json.loads(raw);assert evidence['sourceCommit']==source['sourceCommit'] and evidence['buildRun']==source['candidateRun']
 by_name={item['name']:item for item in evidence['images']};assert len(by_name)==31
 catalog=json.loads(Path('catalog/v6/index.json').read_text());files=[]
 for m in catalog['packs']:
  if m.get('imageKind')!='dice':continue
  assert m['version']=='1.1.0' and m['sha256']==source['recipes'][m['id']]
  name=m['id']+'.theme-d20.png';entry=by_name[name];png=native(name,4*1024*1024)
  assert len(png)==entry['bytes'] and hashlib.sha256(png).hexdigest()==entry['sha256']
  image=Image.open(io.BytesIO(png));assert image.format=='PNG' and image.size==(768,640)
  canvas=image.convert('RGB')
  # Only remove uniform felt margins; never redraw or replace the native die.
  delta=ImageChops.difference(canvas,Image.new('RGB',canvas.size,canvas.getpixel((0,0))))
  channels=delta.split();mask=ImageChops.lighter(ImageChops.lighter(channels[0],channels[1]),channels[2]).point(lambda v:255 if v>12 else 0)
  box=mask.getbbox() or (0,0,canvas.width,canvas.height)
  box=(max(0,box[0]-24),max(0,box[1]-24),min(canvas.width,box[2]+24),min(canvas.height,box[3]+24))
  canvas=canvas.crop(box);canvas.thumbnail((384,320),Image.Resampling.LANCZOS)
  filename=m['id']+'-'+m['sha256'][:12]+'-'+source['release']+'.jpg';path=args.out/filename;canvas.save(path,'JPEG',quality=88,optimize=True);b=path.read_bytes();assert len(b)<=256*1024
  preview=dict(url=ROOT+filename,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),width=canvas.width,height=canvas.height,kind='dice-native-render')
  m['preview']=preview;m['description']+=' Предпросмотр — реальный рендер Unity d20 из проверенной сборки '+source['release'].removeprefix('unity-v')+'.'
  files.append(dict(name=filename,**preview,sourceId=m['id'],sourceSha256=m['sha256'],renderSha256=entry['sha256'],nativeCropBox=box,appSourceCommit=source['sourceCommit'],buildRun=source['candidateRun'],author=m['author'],license=m['license']))
 assert len(files)==31
 (args.out/'index.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
 (args.out/'preview-index-v6.json').write_text(json.dumps(dict(schemaVersion=1,previews=files),ensure_ascii=False,indent=2)+'\n')
 print('NATIVE_DICE_PREVIEWS_READY',len(files),sum(f['bytes'] for f in files))
 sys.exit(0)
catalog=json.loads((args.fixtures/'catalog/v5/index.json').read_text() if args.fixtures else fetch('https://raw.githubusercontent.com/waitermisanthrope-creator/DnD-VTT-Assets/main/catalog/v5/index.json',8*1024*1024))
files=[]
for m in catalog['packs']:
 if m.get('format')!='json':continue
 raw=(args.fixtures/'packages'/Path(m['url']).name).read_bytes() if args.fixtures else fetch(m['url'],5*1024*1024)
 assert len(raw)==m['bytes'] and hashlib.sha256(raw).hexdigest()==m['sha256']
 data=json.loads(raw);canvas=Image.new('RGB',(320,200),'#17191f');draw=ImageDraw.Draw(canvas);kind=None
 if data.get('diceThemes'):
  model=DICE_MODELS[m['id']];assert model['payloadSha256']==m['sha256']
  theme=data['diceThemes'][0];assert model['body']==theme['body'] and model['trim']==theme['trim']
  render_dice(canvas,model);kind='dice-geometry'
  m['description']=m['description'].replace('Миниатюра — исходная иконка, ориентир стиля, не рендер 3D-модели.','Миниатюра — схематичный вид реальной геометрии d20 из генератора; полный набор содержит все семь типов. Материалы и цифры в игре отображает Unity.')
 elif data.get('images'):
  image=data['images'][0];b=base64.b64decode(image['pngBase64'],validate=True) if 'pngBase64' in image else base64.b64decode(image['data'],validate=True)
  assert hashlib.sha256(b).hexdigest()==image['sha256']
  im=Image.open(io.BytesIO(b)).convert('RGBA');im.thumbnail((320,200),Image.Resampling.LANCZOS);canvas.paste(im,((320-im.width)//2,(200-im.height)//2),im);kind='image'
 elif data.get('maps'):
  doc=data['maps'][0]['document'];floor=doc['floors'][0];tiles=floor.get('tiles',{});coords=[tuple(map(int,k.split(','))) for k in tiles]
  if coords:
   x0=min(x for x,y in coords);y0=min(y for x,y in coords);w=max(x for x,y in coords)-x0+1;h=max(y for x,y in coords)-y0+1;scale=min(300/max(1,w),165/max(1,h))
   for x,y in coords:
    color='#947a55' if 'wood' in tiles[f'{x},{y}'] else '#707d8f';left=10+(x-x0)*scale;top=22+(y-y0)*scale;draw.rectangle((left,top,left+max(.5,scale-.4),top+max(.5,scale-.4)),fill=color)
  draw.text((8,5),f"Floor 1 / {len(doc['floors'])} - layout preview",fill='#f4ce69');kind='map-plan'
 elif data.get('surfaces'):
  entries=data['surfaces'];cols=8;size=34
  for n,item in enumerate(entries[:40]):
   x=6+n%cols*39;y=4+n//cols*39;base=item.get('color','#777777')[:7];alt=item.get('alternateColor',base)[:7]
   draw.rectangle((x,y,x+size,y+size),fill=base)
   if item.get('pattern')=='checker':
    for a in range(4):
     for b in range(4):
      if (a+b)%2:draw.rectangle((x+a*8,y+b*8,x+a*8+7,y+b*8+7),fill=alt)
  kind='swatches'
 elif data.get('objects'):
  for n,item in enumerate(data['objects'][:4]):
   x=45+n*78;c=item.get('color','#777777')[:7]
   if item['primitive']=='Cylinder':draw.rectangle((x,65,x+42,142),fill=c);draw.ellipse((x,53,x+42,77),fill=c,outline='#eeeeee');draw.arc((x,130,x+42,154),0,180,fill='#eeeeee')
   else:draw.polygon([(x,77),(x+30,60),(x+55,77),(x+55,126),(x+27,146),(x,129)],fill=c,outline='#eeeeee');draw.line([(x,77),(x+27,96),(x+55,77)],fill='#eeeeee');draw.line([(x+27,96),(x+27,146)],fill='#eeeeee')
  draw.text((8,5),'Object shapes - schematic preview',fill='#f4ce69');kind='object-schematic'
 if kind is None:continue
 name=m['id']+'-'+m['sha256'][:12]+'.jpg';path=args.out/name;canvas.save(path,'JPEG',quality=82,optimize=True);b=path.read_bytes();assert len(b)<=256*1024
 preview=dict(url=ROOT+name,bytes=len(b),sha256=hashlib.sha256(b).hexdigest(),width=320,height=200,kind=kind);m['preview']=preview;files.append(dict(name=name,**preview,sourceId=m['id'],sourceSha256=m['sha256'],author=m['author'],license=m['license']))
(args.out/'index.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
(args.out/'preview-index-v5.json').write_text(json.dumps(dict(schemaVersion=1,previews=files),ensure_ascii=False,indent=2)+'\n')
print('WORKSHOP_PREVIEWS_READY',len(files),sum(f['bytes'] for f in files))
