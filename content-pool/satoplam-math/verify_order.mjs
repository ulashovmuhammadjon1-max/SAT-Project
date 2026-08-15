import { neon } from '@neondatabase/serverless';
const sql = neon(process.env.PROD_URL);
const RANK={EASY:0,MEDIUM:1,HARD:2};
const mods = await sql.query(`SELECT m.id, m."order" mo, m.difficulty branch, t.title FROM "Module" m JOIN "Test" t ON t.id=m."testId" WHERE m.subject='MATH' ORDER BY t.title, m."order"`);
let bad=[], runs=[], gaps=[], n=0;
for (const mod of mods){
  const qs = await sql.query(`SELECT id,"order",difficulty,type FROM "Question" WHERE "moduleId"=$1 AND "isPublished" ORDER BY "order"`,[mod.id]);
  if(!qs.length) continue; n++;
  const where=`${mod.title} m${mod.mo}${mod.branch[0]}`;
  for(let i=1;i<qs.length;i++) if(RANK[qs[i].difficulty]<RANK[qs[i-1].difficulty]) { bad.push(`${where}: q${qs[i].order} ${qs[i].difficulty} after ${qs[i-1].difficulty}`); break; }
  let run=0,best=0; for(const q of qs){ run = q.type==='FREE_RESPONSE'?run+1:0; if(run>best)best=run; }
  if(best>=3) runs.push(`${where}: run of ${best}`);
  const ord=qs.map(q=>q.order);
  if(ord.length!==22 || ord[0]!==1 || ord[ord.length-1]!==22 || new Set(ord).size!==22) gaps.push(`${where}: orders ${ord[0]}..${ord[ord.length-1]} n=${ord.length} distinct=${new Set(ord).size}`);
}
console.log('math modules checked:', n);
console.log('difficulty not monotonic:', bad.length); bad.slice(0,5).forEach(x=>console.log('  '+x));
console.log('free-response runs >= 3:', runs.length); runs.slice(0,5).forEach(x=>console.log('  '+x));
console.log('order not 1..22 contiguous:', gaps.length); gaps.slice(0,5).forEach(x=>console.log('  '+x));
