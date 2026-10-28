import random,json,time,sys
from collections import deque
from pathlib import Path
random.seed(int(sys.argv[1]) if len(sys.argv)>1 else 38)
N=8
shapes=[[(0,0),(1,0),(0,1),(1,1)], # yellow
 [(1,0),(0,1),(1,1),(2,1),(1,2)], # cross
 [(0,0),(0,1),(0,2),(1,2),(2,2)], # long L
 [(0,0),(1,0),(2,0),(1,1),(1,2)], # T
 [(0,0),(2,0),(0,1),(1,1),(2,1)], # U
 [(0,0),(0,1),(1,1),(1,2),(2,2)], # stair
 [(0,0),(1,0),(0,1),(1,1),(0,2)], # P
 [(0,0),(0,1),(0,2),(1,2)], # L4
 [(0,0),(1,0),(1,1),(2,1)], # S4
 [(0,0),(0,1),(0,2),(0,3),(1,3),(2,3)], # L6
 [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]]
dirs=[(-1,0),(1,0),(0,-1),(0,1)]
def norm(s):
 ax=min(x for x,y in s);ay=min(y for x,y in s)
 return tuple(sorted((x-ax,y-ay) for x,y in s))
variants=[]
for s in shapes:
 vs=set()
 for _ in range(4):
  s=[(-y,x) for x,y in s];vs.add(norm(s));vs.add(norm([(-x,y) for x,y in s]))
 variants.append(list(vs))
def mask(cs):return sum(1<<(y*8+x) for x,y in cs)
placements=[]
for vs in variants:
 ps=[]
 for s in vs:
  w=max(x for x,y in s)+1;h=max(y for x,y in s)+1
  for y in range(9-h):
   for x in range(9-w):
    cs=tuple((a+x,b+y) for a,b in s);ps.append((mask(cs),cs))
 placements.append(ps)
def pack():
 board=[None]*len(shapes);board[0]=((3,3),(4,3),(3,4),(4,4))
 order=list(range(1,len(shapes)));random.shuffle(order)
 nodes=0
 def rec(i,occ):
  nonlocal nodes
  nodes+=1
  if nodes>3500:return False
  if i==len(order):return True
  k=order[i];ps=placements[k][:];random.shuffle(ps)
  for m,cs in ps:
   if m&occ:continue
   board[k]=cs
   if rec(i+1,occ|m):return True
  return False
 return board if rec(0,mask(board[0])) else None
def positions(cs,other):
 q=deque([(0,0)]);paths={(0,0):[]}
 while q:
  x,y=q.popleft()
  for dx,dy in dirs:
   p=x+dx,y+dy
   if p in paths:continue
   cells={(a+p[0],b+p[1]) for a,b in cs}
   if any(a<0 or a>=8 or b<0 or b>=8 for a,b in cells) or cells&other:continue
   paths[p]=paths[x,y]+[(dx,dy)];q.append(p)
 return paths
def gateof(cs,dx,dy):
 side='left' if dx<0 else 'right' if dx>0 else 'top' if dy<0 else 'bottom'
 vals=[y if dx else x for x,y in cs]
 return side,min(vals),max(vals)-min(vals)+1
def clear_ray(cs,other,dx,dy):
 for n in range(1,12):
  new={(x+n*dx,y+n*dy) for x,y in cs}
  if new&other:return None
  if all(x<0 or x>=8 or y<0 or y>=8 for x,y in new):return n
def allocate(board):
 remaining=set(range(len(board)));gates={};used=set();moves=[]
 while remaining:
  options=[]
  for k in remaining:
   other=set(c for j in remaining if j!=k for c in board[j])
   for (ox,oy),path in positions(board[k],other).items():
    cs=[(x+ox,y+oy) for x,y in board[k]]
    for dx,dy in dirs:
     gate=gateof(cs,dx,dy);side,start,width=gate
     if k==0 and gate!=('bottom',3,2):continue
     if any((side,i) in used for i in range(start,start+width)):continue
     # Every assigned gate is offset from its block's initial exit line.
     # Yellow is the sole exception; its initial line must be obstructed.
     initial_gate=gateof(board[k],dx,dy)
     if k!=0 and initial_gate==gate:continue
     n=clear_ray(cs,other,dx,dy)
     if n is None:continue
     if k==0 and not moves:continue
     # Prefer compact gates and modest repositioning; variation breaks ties.
     score=len(path)*0.15-width+random.random()*2
     options.append((score,k,gate,path+[(dx,dy)]*n))
  if not options:return None
  _,k,gate,path=max(options)
  gates[k]=gate;used.update((gate[0],i) for i in range(gate[1],gate[1]+gate[2]))
  moves.extend((k,dx,dy) for dx,dy in path);remaining.remove(k)
 return gates,moves
start=time.time();attempt=0
while time.time()-start<600:
 attempt+=1;board=pack()
 if not board:continue
 # Initial yellow downward movement must be blocked.
 other=set(c for j,cs in enumerate(board) if j for c in cs)
 if not all({(x+dx,y+dy) for x,y in board[0]}&other for dx,dy in dirs):continue
 result=allocate(board)
 if not result:continue
 gates,moves=result
 keys=list('YBCVTRGPNOW');colors=['#FFD43B','#3889F5','#39CBE0','#9364DA','#248B85','#DA657F','#45B969','#C787D4','#5360B6','#D68D45','#91ADB8']
 blocks={keys[k]:dict(name=keys[k],color=colors[k],cells=cs,gate=gates[k]) for k,cs in enumerate(board)}
 out=Path(sys.argv[2] if len(sys.argv)>2 else 'outputs/board-study-03');out.mkdir(exist_ok=True,parents=True)
 data=dict(blocks=blocks,moves=[(keys[k],dx,dy) for k,dx,dy in moves],attempts=attempt)
 (out/'layout.json').write_text(json.dumps(data,indent=2))
 print(json.dumps(data));break
else:print('No valid layout found within search budget')
