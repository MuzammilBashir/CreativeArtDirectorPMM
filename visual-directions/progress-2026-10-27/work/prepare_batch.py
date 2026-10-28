from pathlib import Path
import subprocess,sys,json
from PIL import Image,ImageDraw,ImageFont
root=Path('outputs/mock-batch-01')
for folder in sorted(root.glob('blueprint-*')):
 if not (folder/'layout.json').exists() or (folder/'prompt.txt').exists():continue
 subprocess.run([sys.executable,'work/check_board03.py',str(folder/'layout.json')],check=True,capture_output=True)
 subprocess.run([sys.executable,'work/draw_board.py',str(folder/'layout.json')],check=True,capture_output=True)
 im=Image.open(folder/'board-study-03.png')
 im.crop((145,195,1055,1105)).resize((1200,1200),Image.Resampling.LANCZOS).save(folder/'blueprint.png')
 data=json.loads((folder/'layout.json').read_text())
 assert data['initial_direct_exits']==[]
 grid=[['.' for _ in range(8)] for _ in range(8)]
 for k,b in data['blocks'].items():
  for x,y in b['cells']:grid[y][x]=k
 manifest=dict(grid=[' '.join(row) for row in grid],blocks=data['blocks'])
 prompt='''Create ONE polished mobile puzzle game board mock from the supplied CAD blueprint.
Image 1 is the EXACT GEOMETRY MASTER. Image 2 is MATERIAL/FINISH reference only; do not copy its layout, colors or hand.
Apply polished rounded toy-plastic rendering, gently beveled connected block outlines, soft ambient shadows, subtle glossy highlights and raised round studs. Keep the strict orthographic top-down camera. Match the geometry master precisely. Dark blue board floor, purple frame. No hand, text, branding, added UI, particle effects or perspective.
HARD REQUIREMENTS: exactly 8x8 equal cells; 54 occupied cells, 10 blank cells; 11 connected blocks; 11 corresponding colored edge gates. Every occupied logical cell has EXACTLY FOUR studs arranged 2x2: 216 studs total. A 2x2-cell block thus has 16 studs, not four. All studs share one diameter and spacing. Cells of a single piece form one seamless solid shape, not separate tiles. Do not merge adjacent different pieces, fill empty cells, add/remove studs, rotate/shift blocks, or relocate/resize gates. Preserve all concave notches and holes. Retain the yellow 2x2 square in the exact center. Each gate is an actual full-width opening with colored sill and outward white arrow, with no wall blocking its aperture. Other border segments remain closed. Slight bevels must not alter footprints.
The cell map below is authoritative: rows top-to-bottom, columns left-to-right; '.' means empty. Coordinates in block metadata are ZERO BASED (x,y). Gate start and width refer to logical cell intervals along the edge. Colors are the block IDs' hex colors. IDs and the cell map must NOT appear as text in the final image. Reproduce the blueprint faithfully; do not solve or rearrange the puzzle.
'''+json.dumps(manifest,indent=2)
 (folder/'prompt.txt').write_text(prompt)
 print(str(folder/'blueprint.png'))
paths=sorted(root.glob('blueprint-*/blueprint.png'))
if paths:
 sheet=Image.new('RGB',(1500,660),'#101C34');d=ImageDraw.Draw(sheet)
 f=ImageFont.truetype('C:/Windows/Fonts/arialbd.ttf',23)
 for i,p in enumerate(paths):
  x=(i%3)*500;y=(i//3)*330
  sheet.paste(Image.open(p).resize((290,290)),(x+100,y+35));d.text((x+100,y+5),p.parent.name,fill='white',font=f)
 sheet.save(root/'blueprints-overview.png')
