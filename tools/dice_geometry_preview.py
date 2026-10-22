"""Schematic projection of exported, validated C# meshes, not a Unity screenshot."""
import math
from PIL import ImageDraw,ImageColor,ImageFont

def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def norm(v):
 length=math.sqrt(dot(v,v));assert length>1e-12
 return tuple(x/length for x in v)

def render(canvas,model):
 forward=norm((.4,.8,-1));right=norm(cross(norm(cross(forward,(1,0,.4))),forward));up=norm(cross(forward,right));light=norm((-.5,1,-.7))
 assert model['sides']==20 and len(model['meshes'])<=80
 points=[v for m in model['meshes'] for v in m['vertices']]
 assert len(points)<=2000 and all(len(v)==3 and all(math.isfinite(x) and abs(x)<2 for x in v) for v in points)
 xs=[dot(p,right) for p in points];ys=[dot(p,up) for p in points]
 scale=min(296/(max(xs)-min(xs)),170/(max(ys)-min(ys)));cx=(min(xs)+max(xs))/2;cy=(min(ys)+max(ys))/2
 def project(p):return (160+(dot(p,right)-cx)*scale,91-(dot(p,up)-cy)*scale)
 items=[]
 for index,mesh in enumerate(model['meshes']):
  color=ImageColor.getrgb(model['body'] if index==0 else model['trim']);v=mesh['vertices'];indices=mesh['triangles'];assert len(indices)%3==0 and len(indices)<=400
  for i in range(0,len(indices),3):
   triangle=[v[j] for j in indices[i:i+3]];n=norm(cross(sub(triangle[1],triangle[0]),sub(triangle[2],triangle[0])))
   if dot(n,forward)<0:continue
   shade=.32+.68*max(0,dot(n,light));rgb=tuple(round(c*shade) for c in color)
   items.append((sum(dot(p,forward) for p in triangle)/3,'triangle',[project(p) for p in triangle],rgb))
 for face in model['faces']:
  if dot(face['normal'],forward)>.3:
   items.append((dot(face['center'],forward)+.003,'number',project(face['center']),str(face['value'])))
 draw=ImageDraw.Draw(canvas);font=ImageFont.load_default(size=13)
 for depth,kind,position,value in sorted(items,key=lambda item:item[0]):
  if kind=='triangle':draw.polygon(position,fill=value)
  else:draw.text(position,value,font=font,fill='#ffe9ae',anchor='mm')
 draw.text((8,184),'3D geometry / d20 / schematic',font=ImageFont.load_default(size=11),fill='#ddd8cf')
