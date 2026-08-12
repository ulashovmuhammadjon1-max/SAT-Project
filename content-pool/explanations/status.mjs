/**
 * Progress across all agents, read from the append-only JSONL files.
 *
 * The whole durability story lives here: each agent appends one line per
 * finished explanation, so work is on disk the moment it is written. An agent
 * that stops — context exhausted, usage limit, crash — loses at most the
 * single line it was mid-write on, and a replacement resumes by skipping the
 * ids already present.
 *
 * A truncated final line (the one real risk of append-only writing) is dropped
 * rather than failing the read, so a partial file never blocks the pipeline.
 */
import { readFileSync, existsSync, readdirSync } from "fs";

const DIR = new URL(".", import.meta.url).pathname;

export function readJsonl(path) {
  if (!existsSync(path)) return [];
  const out = [];
  for (const line of readFileSync(path, "utf8").split("\n")) {
    if (!line.trim()) continue;
    try {
      out.push(JSON.parse(line));
    } catch {
      // Half-written last line from an interrupted agent. Skip it.
    }
  }
  return out;
}

export function agentNames() {
  return readdirSync(`${DIR}/out`)
    .filter((f) => f.endsWith(".slice.json"))
    .map((f) => f.replace(".slice.json", ""))
    .sort();
}

export function progress() {
  return agentNames().map((name) => {
    const slice = JSON.parse(readFileSync(`${DIR}/out/${name}.slice.json`, "utf8"));
    const done = readJsonl(`${DIR}/out/${name}.jsonl`);
    const doneIds = new Set(done.map((d) => d.questionId));
    // Only count ids that are actually in this agent's slice — a stray id is a
    // bug worth surfacing, not silent extra credit.
    const valid = done.filter((d) => slice.some((q) => q.id === d.questionId));
    return {
      name,
      total: slice.length,
      done: valid.length,
      stray: done.length - valid.length,
      remaining: slice.filter((q) => !doneIds.has(q.id)).length,
    };
  });
}

if (import.meta.url === `file://${process.argv[1]}`) {
  const rows = progress();
  let d = 0, t = 0;
  console.log("agent    done/total   remaining  stray");
  for (const r of rows) {
    console.log(
      `${r.name.padEnd(8)} ${String(r.done).padStart(4)}/${String(r.total).padEnd(5)} ${String(r.remaining).padStart(9)}  ${r.stray || ""}`
    );
    d += r.done; t += r.total;
  }
  console.log(`\n${d}/${t} explanations written (${Math.round((d / t) * 100)}%)`);
}
