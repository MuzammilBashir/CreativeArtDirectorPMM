const assert=require('assert'),E=require('./engine.js');
for(let seed=1;seed<=12;seed++){
 const n=18,mask=Array.from({length:n*n},(_,i)=>i%17===0?null:i%n<9?'#ff8800':'#4488ff');
 const a=E.generate(mask,n,n,seed);assert(a.validation.valid,JSON.stringify(a.validation));assert(a.coverage>.75);
 const order=a.validation.solution.order;assert.equal(order.length,a.arrows.length);
 // Play arbitrary legal choices, not just the stored solution.
 const active=new Set(a.arrows.map((_,i)=>i)),occ=new Set(a.arrows.flatMap(p=>p.cells.map(E.key)));
 while(active.size){const legal=[...active].filter(i=>E.free(a.arrows[i],occ,n,n));assert(legal.length,'Deadlock');const i=legal.at(-1);a.arrows[i].cells.forEach(p=>occ.delete(E.key(p)));active.delete(i);}
}
const blocked={width:5,height:1,arrows:[{cells:[[0,0],[1,0]],direction:[1,0],color:'red'},{cells:[[4,0],[3,0]],direction:[-1,0],color:'blue'}]};assert(!E.validate(blocked).valid);assert(!E.solve(blocked).solved);
assert(!E.validate({width:3,height:3,arrows:[{cells:[[0,0],[1,1]],direction:[1,0],color:'red'}]}).valid);
console.log('PASS: 12 generated boards, alternate legal clear orders, opposing-head deadlock, diagonal rejection');
