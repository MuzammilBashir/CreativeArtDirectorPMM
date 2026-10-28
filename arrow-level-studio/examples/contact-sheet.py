from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
root=Path(__file__).parent
names=['butterfly','rocket','fox','tropical-fish','sunflower']
image=Image.new('RGB',(1500,680),'#0b0d13')
d=ImageDraw.Draw(image)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',23)
for i,name in enumerate(names):
    d.text((i*300+18,14),name.replace('-',' ').title(),font=font,fill='#eee8db')
    for row,kind in enumerate(['source','preview']):
        tile=Image.open(root/f'{name}-{kind}.png').convert('RGBA').resize((296,296),Image.Resampling.LANCZOS)
        image.paste(tile,(i*300+2,55+row*310),tile)
image.save(root/'five-examples.png')
