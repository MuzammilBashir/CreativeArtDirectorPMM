from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import json,sys

OUT=Path('outputs/board-study-02'); OUT.mkdir(parents=True,exist_ok=True)
blocks={
 'Y':dict(name='Yellow',color='#FFD43B',cells=[(3,3),(4,3),(3,4),(4,4)],gate=('bottom',3,2)),
 'B':dict(name='Blue',color='#3889F5',cells=[(2,5),(3,5),(4,5)],gate=('left',5,1)),
 'G':dict(name='Green',color='#39C97A',cells=[(3,6),(4,6),(4,7)],gate=('right',6,2)),
 'C':dict(name='Cyan',color='#39CBE0',cells=[(0,0),(0,1),(0,2),(1,2)],gate=('top',0,2)),
 'V':dict(name='Violet',color='#7954D9',cells=[(x,y) for x in (2,3) for y in range(3)],gate=('top',2,2)),
 'T':dict(name='Teal',color='#258C86',cells=[(x,y) for x in (4,5) for y in range(3)],gate=('top',4,2)),
 'W':dict(name='White',color='#DFE8EF',cells=[(x,y) for x in (6,7) for y in range(3)],gate=('top',6,2)),
 'R':dict(name='Coral',color='#EB626A',cells=[(x,y) for x in range(3) for y in (3,4)],gate=('left',3,2)),
 'O':dict(name='Orange',color='#ED963D',cells=[(x,y) for x in (5,6,7) for y in (3,4)],gate=('right',3,2)),
 'N':dict(name='Indigo',color='#4554BE',cells=[(x,y) for x in (6,7) for y in (5,6,7)],gate=('bottom',6,2)),
 'P':dict(name='Purple',color='#C77CE3',cells=[(0,6),(1,6),(0,7),(1,7)],gate=('bottom',0,2)),
}
custom=len(sys.argv)>1
if custom:
 data=json.loads(Path(sys.argv[1]).read_text())
 blocks=data['blocks'];OUT=Path(sys.argv[1]).parent
state={k:set(map(tuple,v['cells'])) for k,v in blocks.items()}
occupied=[c for cs in state.values() for c in cs]
assert len(occupied)==len(set(occupied))
assert len(occupied)==54
assert all(0<=x<8 and 0<=y<8 for x,y in occupied)
def legal(k,new):
 others=set().union(*(s for j,s in state.items() if j!=k))
 if new & others:return False
 side,start,width=blocks[k]['gate']
 for x,y in new:
  if 0<=x<8 and 0<=y<8:continue
  if side=='left' and x<0 and start<=y<start+width:continue
  if side=='right' and x>=8 and start<=y<start+width:continue
  if side=='top' and y<0 and start<=x<start+width:continue
  if side=='bottom' and y>=8 and start<=x<start+width:continue
  return False
 return True
assert not legal('Y',{(x,y+1) for x,y in state['Y']})
sequence=[('B',-1,0,5),('N',0,1,3),('G',1,0,5),('Y',0,1,5),('C',0,-1,3),('V',0,-1,3),('T',0,-1,3),('W',0,-1,3),('R',-1,0,3),('O',1,0,3),('P',0,1,2)]
if custom:sequence=[(k,dx,dy,1) for k,dx,dy in data['moves']]
steps=[]
for k,dx,dy,n in sequence:
 for step in range(n):
  nxt={(x+dx,y+dy) for x,y in state[k]}
  assert legal(k,nxt),(k,step)
  state[k]=nxt
 exited=all(not(0<=x<8 and 0<=y<8) for x,y in state[k])
 if not custom:assert exited
 if exited:state[k]=set()
 steps.append(dict(block=k,direction={(-1,0):'left',(1,0):'right',(0,1):'down',(0,-1):'up'}[dx,dy],cell_steps=n))
assert not any(state.values())
for k,b in blocks.items():
 axis=1 if b['gate'][0] in ('left','right') else 0
 span=max(c[axis] for c in b['cells'])-min(c[axis] for c in b['cells'])+1
 assert span==b['gate'][2]

S=2; W,H=1200,1440
im=Image.new('RGB',(W*S,H*S),'#101C34');d=ImageDraw.Draw(im)
def font(size,bold=False):return ImageFont.truetype('C:/Windows/Fonts/'+('arialbd.ttf' if bold else 'arial.ttf'),size*S)
def text(x,y,t,size=20,fill='#DCE5F6',bold=False):d.text((x*S,y*S),t,font=font(size,bold),fill=fill)
def rect(box,fill,outline=None,width=1):d.rectangle(tuple(v*S for v in box),fill=fill,outline=outline,width=width*S)
def line(points,fill,width=1):d.line([(x*S,y*S) for x,y in points],fill=fill,width=width*S)
def circ(box,fill,outline=None,width=1):d.ellipse(tuple(v*S for v in box),fill=fill,outline=outline,width=width*S)
text(90,46,'FREE THE YELLOW BLOCK',36,bold=True)
text(90,97,'CAD DRAWING 03  /  INTERLOCKING SHAPES' if custom else 'CAD DRAWING 02  /  DENSITY REVISION',19,fill='#8FA9CE',bold=True)
text(90,135,'8 x 8  |  54 filled / 10 empty  |  84.4% occupancy',22)
X,Y,T=200,250,100
rect((X-42,Y-42,X+842,Y+842),'#554A8B')
rect((X,Y,X+800,Y+800),'#253453')
for i in range(9):
 line([(X+i*T,Y),(X+i*T,Y+800)],'#475572',2)
 line([(X,Y+i*T),(X+800,Y+i*T)],'#475572',2)
for i in range(8):
 text(X+i*T+43,Y-78,str(i+1),20,fill='#90A5C5')
 text(X-80,Y+i*T+38,str(i+1),20,fill='#90A5C5')
for k,b in blocks.items():
 side,start,width=b['gate']; a=start*T; z=(start+width)*T
 box={'left':(X-42,Y+a,X,Y+z),'right':(X+800,Y+a,X+842,Y+z),'top':(X+a,Y-42,X+z,Y),'bottom':(X+a,Y+800,X+z,Y+842)}[side]
 rect(box,b['color'])
 cx=(box[0]+box[2])/2;cy=(box[1]+box[3])/2
 pts={'left':[(cx-9,cy),(cx+7,cy-10),(cx+7,cy+10)],'right':[(cx+9,cy),(cx-7,cy-10),(cx-7,cy+10)],'top':[(cx,cy-9),(cx-10,cy+7),(cx+10,cy+7)],'bottom':[(cx,cy+9),(cx-10,cy-7),(cx+10,cy-7)]}[side]
 d.polygon([(int(x*S),int(y*S)) for x,y in pts],fill='#FFFFFF')
for k,b in blocks.items():
 cells=set(map(tuple,b['cells'])); col=b['color']
 for x,y in cells:
  rect((X+x*T,Y+y*T,X+(x+1)*T,Y+(y+1)*T),col)
 for x,y in cells:
  x0=X+x*T;y0=Y+y*T
  for nb,edge in [((x,y-1),[(x0,y0+3),(x0+T,y0+3)]),((x,y+1),[(x0,y0+T-3),(x0+T,y0+T-3)]),((x-1,y),[(x0+3,y0),(x0+3,y0+T)]),((x+1,y),[(x0+T-3,y0),(x0+T-3,y0+T)])]:
   if nb not in cells:line(edge,'#14243E',5)
  for ox in (25,75):
   for oy in (25,75):
    cx=x0+ox;cy=y0+oy
    circ((cx-17,cy-14,cx+17,cy+20),'#172842')
    circ((cx-17,cy-18,cx+17,cy+16),col,'#E0F0FF',1)
    line([(cx-10,cy-10),(cx+5,cy-12)],'#FFFFFF',2)
text(90,1130,'REPOSITION BEFORE EXITING' if custom else 'VERIFIED ROUTE TO FREE YELLOW',22,bold=True)
text(90,1170,'L, T, cross, U, stair, S and P shapes; offset matching gates.' if custom else 'Blue left  >  Indigo down  >  Green L right  >  Yellow down',22)
text(90,1220,'11 blocks  |  11 matching gates  |  216 studs  |  Full clear verified',21)
text(90,1275,'TEST CONDITION: straight sliding; no rotation; matching-color exits only.',18,fill='#9CB2D2')
text(90,1310,'Geometry verified. Difficulty, ad pacing and final materials are not approved.',18,fill='#9CB2D2')
text(90,1360,'Coordinates: columns left to right; rows top to bottom. Gate arrows point out.',17,fill='#8198BC')
stem='board-study-03' if custom else 'board-study-02'
im.resize((W,H),Image.Resampling.LANCZOS).save(OUT/(stem+'.png'))
(OUT/(stem+'.json')).write_text(json.dumps(dict(grid=[8,8],occupied_cells=54,empty_cells=10,occupancy_percent=84.375,studs_per_cell=4,blocks=blocks,solution=steps,test_conditions=['axis-aligned sliding','no rotation','matching-color gate only'],checks=dict(overlap=False,uniform_cell_pitch=True,stud_count=len(occupied)*4,gate_spans_match=True,initial_yellow_down_blocked=True,full_clear_sequence_verified=True)),indent=2))
print(json.dumps(dict(occupied_cells=len(occupied),total_cells=64,studs=len(occupied)*4,verified_sequence=steps,output=str(OUT.resolve()))))
