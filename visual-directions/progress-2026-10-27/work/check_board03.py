import json,sys
from pathlib import Path
from collections import deque
p=Path(sys.argv[1] if len(sys.argv)>1 else 'outputs/board-study-03/layout.json');data=json.loads(p.read_text());blocks=data['blocks']
state={k:set(map(tuple,b['cells'])) for k,b in blocks.items()}
dirs=[(-1,0),(1,0),(0,-1),(0,1)]
used=set()
for k,b in blocks.items():
 side,start,width=b['gate'];slots={(side,i) for i in range(start,start+width)}
 assert not slots&used
 used|=slots
others=set().union(*(cs for k,cs in state.items() if k!='Y'))
assert all({(x+dx,y+dy) for x,y in state['Y']}&others for dx,dy in dirs)
def route(k,state):
 cells=state[k];other=set().union(*(cs for j,cs in state.items() if j!=k))
 side,start,w=blocks[k]['gate'];dx,dy={'left':(-1,0),'right':(1,0),'top':(0,-1),'bottom':(0,1)}[side]
 q=deque([(0,0,[])]);seen={(0,0)};options=[]
 while q:
  ox,oy,path=q.popleft();cs={(x+ox,y+oy) for x,y in cells}
  vals=[y if dx else x for x,y in cs]
  if min(vals)==start and max(vals)==start+w-1:
   for n in range(1,12):
    shifted={(x+dx*n,y+dy*n) for x,y in cs}
    if shifted&other:break
    if all(x<0 or x>7 or y<0 or y>7 for x,y in shifted):
     options.append(path+[(dx,dy)]*n);break
  for ax,ay in dirs:
   pp=(ox+ax,oy+ay)
   if pp in seen:continue
   new={(x+pp[0],y+pp[1]) for x,y in cells}
   if new&other or any(x<0 or x>7 or y<0 or y>7 for x,y in new):continue
   seen.add(pp);q.append((*pp,path+[(ax,ay)]))
 return min(options,key=len) if options else None
initial_routes={k:route(k,state) for k in state}
order=list(dict.fromkeys(k for k,dx,dy in data['moves']))
moves=[];gestures=[]
for k in order:
 path=route(k,state);assert path
 moves.extend((k,dx,dy) for dx,dy in path)
 for dx,dy in path:
  if gestures and gestures[-1][0:3]==[k,dx,dy]:gestures[-1][3]+=1
  else:gestures.append([k,dx,dy,1])
 state[k]=set()
data['moves']=moves;data['gestures']=gestures
data['initial_blocks_with_exit_after_repositioning']=[k for k,v in initial_routes.items() if v]
data['initial_direct_exits']=[k for k,v in initial_routes.items() if v and len(set(v))==1]
data['yellow_initially_blocked_in_all_four_directions']=True
p.write_text(json.dumps(data,indent=2))
print(json.dumps(dict(initial_exit_routes=data['initial_blocks_with_exit_after_repositioning'],initial_direct_exits=data['initial_direct_exits'],exit_order=order,gestures=gestures)))
