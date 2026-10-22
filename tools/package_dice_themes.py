"""Small declarative, cross-platform physical dice sets tied to author-owned icons.
No source image is copied into the APK. Keep v4 unchanged for pre-generator clients.
"""
import hashlib,json,base64,sys,struct
from pathlib import Path
root=Path(__file__).resolve().parents[1]
# New material-bearing payloads are immutable Release assets; never overwrite v5 recipes.
if '--materials' in sys.argv:
 output=root/'dist/owner-appearance-v1';output.mkdir(parents=True,exist_ok=True)
 png=(root/'sources/dice-materials/gothic-atlas-v1.png').read_bytes()
 width,height=struct.unpack('>II',png[16:24]);assert (width,height)==(1024,1024) and len(png)<4*1024*1024
 image=dict(width=width,height=height,sha256=hashlib.sha256(png).hexdigest(),pngBase64=base64.b64encode(png).decode())
 catalog=json.loads((root/'catalog/v5/index.json').read_text())
 for manifest in catalog['packs']:
  if manifest.get('imageKind')!='dice':continue
  payload=json.loads((root/'packages'/(manifest['id']+'.json')).read_text())
  payload['version']='1.1.0';theme=payload['diceThemes'][0]
  suffix=manifest['id'].rsplit('.',1)[1]
  theme.update(albedo=image,faceTile=0 if suffix in ['01','29'] else 1 if suffix in ['05','17'] else 3,trimTile=2 if theme['shape']=='tentacles' else 3,tintTexture=suffix not in ['01','05'])
  data=(json.dumps(payload,ensure_ascii=False,separators=(',',':'))+'\n').encode();assert len(data)<=5*1024*1024
  filename=manifest['id']+'-1.1.0.json';(output/filename).write_bytes(data)
  manifest.update(version='1.1.0',minClientVersionCode=10026,dependencies=[],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),url='https://github.com/waitermisanthrope-creator/DnD-VTT-Assets/releases/download/owner-appearance-v1/'+filename,description='Текстурированный 3D-набор d4/d6/d8/d10/d12/d20/d100. Выбирается на столе в «Мои наборы», независимо от иконки Android. Новая текстура и металлические рёбра; это 3D-адаптация иллюстрации, не точная скульптурная копия. Старые версии 1.0.0 сохранены. Требуется Unity 1.00.26+.')
  manifest.pop('preview',None) # Old schematic is not a preview of the textured version.
 catalog['catalogId']='dnd-vtt-assets-v6'
 (output/'index-v6.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
 print('DICE_TEXTURED_PACKAGES_GENERATED',31,'immutable v1.1.0; v5 unchanged')
 sys.exit(0)
# Reviewed against the owner's 31 original icon images, not inferred by filenames.
rows=[
 ('01','Бездна','tentacles','#382054','#AC55EE',.18,.055),
 ('02','Арканум','filigree','#24144F','#D07DFF',.045,.03),
 ('03','Ледяная корона','crystal','#17426F','#95E7FF',.13,.055),
 ('04','Древняя бронза','filigree','#64411A','#F5BF66',.045,.035),
 ('05','Кровавые клыки','fangs','#491C25','#C1B1AE',.14,.06),
 ('06','Каменный страж','spikes','#393B3B','#A9ACAA',.11,.05),
 ('07','Алая кость','fangs','#C5BDB5','#8C3036',.12,.05),
 ('08','Нефритовый дракон','vines','#164842','#CAB56B',.10,.045),
 ('09','Серебряное кружево','filigree','#62647B','#D7E2EB',.045,.03),
 ('10','Ледяной призрак','tentacles','#3A6C7E','#B2F2EE',.12,.04),
 ('11','Костяное сплетение','fangs','#53332A','#DCC2A0',.13,.055),
 ('12','Ядовитые шипы','spikes','#263514','#A1C65D',.14,.045),
 ('13','Золотые черепа','rounded','#5B4814','#E7C94E',.08,.085),
 ('14','Астральный вихрь','filigree','#21204B','#B786F1',.04,.025),
 ('15','Звёздное золото','rounded','#142D63','#E5BE5A',.025,.03),
 ('16','Ночное небо','rounded','#132449','#F4CE6D',.025,.035),
 ('17','Багровый обсидиан','spikes','#29151B','#B94346',.07,.035),
 ('18','Морская пена','tentacles','#13536B','#A4EDFF',.10,.04),
 ('19','Лесная лоза','vines','#29351A','#B0B96A',.10,.045),
 ('20','Хрустальный туман','crystal','#52717D','#D0EAF2',.08,.03),
 ('21','Золотой дракон','fangs','#6F3B12','#F1BC53',.12,.055),
 ('22','Неоновый разлом','filigree','#17154A','#836AFF',.045,.025),
 ('23','Чистое золото','rounded','#AC7828','#FFDA72',.025,.025),
 ('24','Синие руны','filigree','#142A44','#62BDFF',.035,.025),
 ('25','Живая чаща','vines','#25371F','#C8B35C',.09,.04),
 ('26','Лавовый разлом','spikes','#4A1D12','#F28C25',.07,.035),
 ('27','Грозовой лёд','crystal','#174D8F','#79DFFF',.08,.04),
 ('28','Серебряная вязь','filigree','#363943','#D3D6DB',.04,.03),
 ('29','Энергия пустоты','tentacles','#3B1958','#C17CFA',.10,.035),
 ('30','Малахит','rounded','#284735','#C9AA64',.035,.04),
 ('default','Наследие','filigree','#564D38','#CAB98A',.04,.035)]
catalog=json.loads((root/'catalog/v4/index.json').read_text())
by_id={p['id']:p for p in catalog['packs']}
for icon,name,shape,body,trim,length,width in rows:
 package_id='dnd.dice.icon.'+icon;linked='dnd.appearance.icon.'+icon
 assert linked in by_id and package_id not in by_id
 theme=dict(id=package_id+'.theme',name=name,iconPackage=linked,shape=shape,body=body,trim=trim,length=length,width=width,sides=[4,6,8,10,12,20,100])
 payload=dict(schemaVersion=1,id=package_id,version='1.0.0',type='appearance',diceThemes=[theme])
 data=(json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode()
 path=root/'packages'/(package_id+'.json');path.write_bytes(data)
 manifest=dict(schemaVersion=1,id=package_id,name='3D Дайсы · '+name,version='1.0.0',author='waitermisanthrope-creator',license='Author-authorized DnD-VTT distribution',type='appearance',imageKind='dice',minClientVersionCode=10024,format='json',platform='any',unityVersion='',dependencies=[linked],bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),url='https://raw.githubusercontent.com/waitermisanthrope-creator/DnD-VTT-Assets/main/packages/'+path.name,description='Полный физический набор d4/d6/d8/d10/d12/d20/d100. Сначала установите «'+by_id[linked]['name']+'» из Оформление → Иконки. Связан с авторской иконкой. Выступы имеют объём и коллайдеры; набор не сертифицирован как равномерный. Требуется Unity 1.00.24+. Миниатюра — исходная иконка, ориентир стиля, не рендер 3D-модели.',preview=by_id[linked]['preview'])
 catalog['packs'].append(manifest)
catalog['catalogId']='dnd-vtt-assets-v5'
(root/'catalog/v5').mkdir(exist_ok=True)
(root/'catalog/v5/index.json').write_text(json.dumps(catalog,ensure_ascii=False,indent=2)+'\n')
print('DICE_PACKAGES_GENERATED',len(rows),'sets',len(rows)*7,'logical die types')
