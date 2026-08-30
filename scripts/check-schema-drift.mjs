import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";
const sql = neon(process.env.PROD_URL);
const schema = readFileSync("prisma/schema.prisma", "utf8");

// Parse model -> scalar field names (skip relations and block attributes).
const models = {};
for (const m of schema.matchAll(/^model\s+(\w+)\s*\{([\s\S]*?)^\}/gm)) {
  const [, name, body] = m;
  const fields = [];
  for (const line of body.split("\n")) {
    const t = line.trim();
    if (!t || t.startsWith("//") || t.startsWith("@@") || t.startsWith("///")) continue;
    const fm = /^(\w+)\s+([\w\[\]?]+)/.exec(t);
    if (!fm) continue;
    const [, field, type] = fm;
    // Relation fields and list types have no column of their own.
    if (/^[A-Z]/.test(type.replace(/[\[\]?]/g, "")) && !["String","Int","Boolean","DateTime","Float","Decimal","BigInt","Json","Bytes"].includes(type.replace(/[\[\]?]/g,""))) continue;
    if (type.endsWith("[]")) continue;
    fields.push(field);
  }
  models[name] = fields;
}

let problems = 0;
for (const [name, fields] of Object.entries(models)) {
  const rows = await sql.query(
    "SELECT column_name FROM information_schema.columns WHERE table_name = $1", [name]);
  if (rows.length === 0) { console.log(`MISSING TABLE  ${name}`); problems++; continue; }
  const have = new Set(rows.map(r => r.column_name));
  const missing = fields.filter(f => !have.has(f));
  if (missing.length) { console.log(`MISSING COLUMNS ${name}: ${missing.join(", ")}`); problems++; }
}
console.log(problems === 0 ? "\nNo drift: every schema.prisma column exists in the database." : `\n${problems} model(s) drifted.`);
