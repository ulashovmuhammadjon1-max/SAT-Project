import { neon } from '@neondatabase/serverless';
const sql = neon(process.env.PROD_URL);
const rows = await sql.query(`
  select t.title, m."order" mo, m.difficulty branch, q.difficulty qd, count(*)::int n
    from "Test" t join "Module" m on m."testId"=t.id and m.subject='MATH'
    join "Question" q on q."moduleId"=m.id and q."isPublished"
   where t.title = any($1) group by 1,2,3,4 order by 1,2,3,4`,
  [Array.from({length:10},(_,i)=>`Test ${i+22}`)]);
const per={};
for(const r of rows){ const k=r.title; per[k]=per[k]||{EASY:0,MEDIUM:0,HARD:0}; per[k][r.qd]+=r.n; }
console.table(Object.entries(per).map(([t,v])=>({test:t,...v,total:v.EASY+v.MEDIUM+v.HARD})));
const tot = Object.values(per).reduce((a,v)=>({EASY:a.EASY+v.EASY,MEDIUM:a.MEDIUM+v.MEDIUM,HARD:a.HARD+v.HARD}),{EASY:0,MEDIUM:0,HARD:0});
console.log('Tests 22-31 authored Math totals:', tot);
