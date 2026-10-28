const fs=require('fs'),path=require('path');
fs.writeFileSync(path.join(__dirname,'panda-source.js'),'const PANDA_SVG='+JSON.stringify(fs.readFileSync(path.join(__dirname,'panda.svg'),'utf8'))+';');
const pictures={panda:{name:'Sleeping red panda',svg:fs.readFileSync(path.join(__dirname,'panda.svg'),'utf8')}};
for(const [id,name] of [['butterfly','Butterfly'],['rocket','Rocket'],['fox','Fox'],['tropical-fish','Tropical fish'],['sunflower','Sunflower']])pictures[id]={name,svg:fs.readFileSync(path.join(__dirname,'examples',id+'.svg'),'utf8')};
fs.writeFileSync(path.join(__dirname,'example-sources.js'),'const EXAMPLES='+JSON.stringify(pictures)+';');
