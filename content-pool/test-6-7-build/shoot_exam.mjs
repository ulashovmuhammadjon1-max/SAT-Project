/**
 * Screenshot every question of a seeded attempt in the REAL exam interface.
 *
 * CLAUDE.md requires this before shipping content: the admin preview and
 * /exam/{attemptId} have matched every time so far, but the exam page is what
 * the student sees and is the only check that counts.
 *
 *   node shoot_exam.mjs <attemptId> <outDir> [count]
 */
import { chromium } from "playwright-core";
import { PrismaClient } from "@prisma/client";
import fs from "node:fs";

const [attemptId, outDir, countArg] = process.argv.slice(2);
if (!attemptId || !outDir) throw new Error("usage: shoot_exam.mjs <attemptId> <outDir> [count]");
fs.mkdirSync(outDir, { recursive: true });

const prisma = new PrismaClient();
const user = await prisma.user.findFirst({ where: { role: "STUDENT" } });
await prisma.$disconnect();

const browser = await chromium.launch({
  executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args: ["--no-sandbox"],
});
const ctx = await browser.newContext({ viewport: { width: 1440, height: 1000 } });
const page = await ctx.newPage();

const errors = [];
page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
page.on("pageerror", (e) => errors.push(String(e)));

// sign in as the seeded student
await page.goto("http://localhost:3000/login", { waitUntil: "networkidle" });
await page.fill('input[name="email"]', user.email);
await page.fill('input[name="password"]', "Student123!");
await page.click('button[type="submit"]');
await page.waitForURL((u) => !/\/login/.test(u.pathname), { timeout: 20000 })
  .catch(async () => {
    const msg = await page.locator("body").innerText();
    throw new Error("login did not leave /login:\n" + msg.slice(0, 400));
  });
await page.waitForLoadState("networkidle");

await page.goto(`http://localhost:3000/exam/${attemptId}`, { waitUntil: "networkidle" });
// dismiss any pre-module splash
for (const label of ["Begin", "Start", "Continue", "Resume"]) {
  const b = page.getByRole("button", { name: label, exact: false });
  if (await b.count()) { await b.first().click().catch(() => {}); await page.waitForTimeout(600); break; }
}

const count = Number(countArg || 22);
for (let i = 1; i <= count; i++) {
  await page.waitForTimeout(450);
  await page.screenshot({ path: `${outDir}/q${String(i).padStart(2, "0")}.png`, fullPage: true });
  const next = page.getByRole("button", { name: /next/i });
  if (!(await next.count())) break;
  await next.first().click().catch(() => {});
}

console.log(`shot ${count} questions into ${outDir}`);
if (errors.length) {
  console.log(`\n${errors.length} console errors:`);
  for (const e of [...new Set(errors)].slice(0, 10)) console.log("  " + e);
}
await browser.close();
