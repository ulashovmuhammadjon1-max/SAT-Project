/**
 * Apply a manual migration file to a database over Neon's HTTP driver.
 *
 *   PROD_URL='postgresql://...' node scripts/apply-manual-migration.mjs \
 *     prisma/migrations/manual/022_ap_subjects_and_tests.sql
 *
 * The HTTP driver refuses multiple commands in one call, so the file is split
 * into statements first. Splitting on ";" alone would cut a `DO $$ ... $$;`
 * block in half — the block body legitimately contains semicolons — so the
 * splitter tracks whether it is inside a dollar-quoted string and only breaks
 * on semicolons outside one.
 *
 * Every migration under manual/ is written to be idempotent (IF NOT EXISTS,
 * ON CONFLICT DO NOTHING, duplicate_object handlers), so re-running a file is
 * safe and is the intended way to recover a partial application.
 */
import { neon } from "@neondatabase/serverless";
import { readFileSync } from "fs";

const file = process.argv[2];
if (!file) {
  console.error("usage: apply-manual-migration.mjs <file.sql>");
  process.exit(1);
}
if (!process.env.PROD_URL) {
  console.error("PROD_URL is not set");
  process.exit(1);
}

/** Split SQL into statements, treating $$-quoted blocks as opaque. */
function splitStatements(sql) {
  const out = [];
  let buf = "";
  let i = 0;
  let dollarTag = null;

  while (i < sql.length) {
    if (dollarTag) {
      if (sql.startsWith(dollarTag, i)) {
        buf += dollarTag;
        i += dollarTag.length;
        dollarTag = null;
        continue;
      }
      buf += sql[i++];
      continue;
    }

    // Line comments would otherwise hide a semicolon inside them.
    if (sql.startsWith("--", i)) {
      const nl = sql.indexOf("\n", i);
      const end = nl === -1 ? sql.length : nl + 1;
      buf += sql.slice(i, end);
      i = end;
      continue;
    }

    const tag = /^\$[A-Za-z_]*\$/.exec(sql.slice(i));
    if (tag) {
      dollarTag = tag[0];
      buf += dollarTag;
      i += dollarTag.length;
      continue;
    }

    if (sql[i] === ";") {
      out.push(buf.trim());
      buf = "";
      i++;
      continue;
    }

    buf += sql[i++];
  }
  if (buf.trim()) out.push(buf.trim());

  // Drop fragments that are only comments or whitespace.
  return out.filter((s) => s.replace(/--[^\n]*\n?/g, "").trim().length > 0);
}

const sql = neon(process.env.PROD_URL);
const statements = splitStatements(readFileSync(file, "utf8"));
console.log(`${statements.length} statement(s) in ${file}`);

let n = 0;
for (const statement of statements) {
  const label = statement.replace(/--[^\n]*\n/g, "").trim().slice(0, 70).replace(/\s+/g, " ");
  try {
    await sql.query(statement);
    n++;
    console.log(`  ok  ${label}`);
  } catch (err) {
    console.error(`  FAIL ${label}`);
    console.error(`       ${err.message}`);
    process.exit(1);
  }
}
console.log(`applied ${n}/${statements.length}`);
