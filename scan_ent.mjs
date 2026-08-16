import { neon } from '@neondatabase/serverless';
const sql = neon(process.env.PROD_URL);
const IMG = /<img[^>]*>/gi;
const SPAN = /\\\((.*?)\\\)|\\\[(.*?)\\\]/gs;
const ENT = /&(?:gt|lt|amp|le|ge|ne|minus|times|divide|deg|nbsp|quot|apos|#\d+|[a-zA-Z]+);/g;

const rows = await sql.query(`
  select q.id, q.stem, q.source, t.title, m."order" mo, m.difficulty branch, q."order" qo
    from "Question" q
    left join "Module" m on m.id=q."moduleId"
    left join "Test" t on t.id=m."testId"
   where q."isPublished"`);
const ch = await sql.query(`
  select a.id, a."questionId", a.content, a.label from "AnswerChoice" a
   join "Question" q on q.id=a."questionId" where q."isPublished"`);

function hits(html) {
  const out = [];
  const clean = (html||'').replace(IMG, ' ');
  let m;
  SPAN.lastIndex = 0;
  while ((m = SPAN.exec(clean)) !== null) {
    const inner = m[1] ?? m[2] ?? '';
    const e = inner.match(ENT);
    if (e) out.push(...new Set(e));
  }
  return [...new Set(out)];
}
const byQ = new Map(rows.map(r=>[r.id,r]));
let stemBad=[], chBad=[];
for (const r of rows) { const h=hits(r.stem); if (h.length) stemBad.push({...r, ents:h}); }
for (const c of ch) { const h=hits(c.content); if (h.length) chBad.push({...c, ents:h, q:byQ.get(c.questionId)}); }
console.log('stems with entities inside math:', stemBad.length);
console.log('choices with entities inside math:', chBad.length);
const cnt={};
for (const b of [...stemBad,...chBad]) for (const e of b.ents) cnt[e]=(cnt[e]||0)+1;
console.log('entity frequency:', cnt);
const src={};
for (const b of stemBad) { const k=(b.source||'').split(':')[0]; src[k]=(src[k]||0)+1; }
for (const b of chBad) { const k=(b.q?.source||'').split(':')[0]; src[k]=(src[k]||0)+1; }
console.log('by source prefix:', src);
console.log('\nsamples:');
for (const b of stemBad.slice(0,5)) console.log(` [${b.title} m${b.mo}${b.branch} q${b.qo}] ${b.ents} :: ${b.stem.replace(/<img[^>]*>/g,'[IMG]').slice(0,180)}`);
