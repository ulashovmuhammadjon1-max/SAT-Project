/**
 * Exercise passage highlighting the way a student does it: drag a selection,
 * look at the popup, then click something else on the page.
 *
 * Checks the two reported faults directly.
 *   1. While the popup is open the selected words must be visibly marked. The
 *      browser drops its own selection styling as soon as focus moves into the
 *      note field, so a pending <mark> has to stand in for it.
 *   2. The first click on "Next" (or any control) while a popup is open must
 *      actually press it. A full-screen click-away catcher used to swallow it.
 *
 *   node drive_highlight.mjs <attemptId|--fresh> <outDir>
 */
import { chromium } from "playwright-core";
import { PrismaClient } from "@prisma/client";
import fs from "node:fs";

const [, outDir = "/tmp/hl"] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });

const prisma = new PrismaClient();
const user = await prisma.user.findFirstOrThrow({ where: { role: "STUDENT" } });
// Always start on a Reading & Writing module — Math has no passage pane, so
// there would be nothing to highlight.
const test = await prisma.test.findFirstOrThrow({ where: { title: "Test 6" } });
for (const a of await prisma.attempt.findMany({ where: { userId: user.id, testId: test.id } })) {
  await prisma.response.deleteMany({ where: { attemptId: a.id } });
  await prisma.moduleAttempt.deleteMany({ where: { attemptId: a.id } });
  await prisma.attempt.delete({ where: { id: a.id } });
}
const rwModule = await prisma.module.findFirstOrThrow({
  where: { testId: test.id, subject: "READING_WRITING", order: 1 },
});
const attempt = await prisma.attempt.create({
  data: {
    userId: user.id,
    testId: test.id,
    status: "IN_PROGRESS",
    currentModuleId: rwModule.id,
    moduleAttempts: { create: { moduleId: rwModule.id } },
  },
});
await prisma.$disconnect();

const browser = await chromium.launch({
  executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args: ["--no-sandbox"],
});
const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
const errors = [];
page.on("pageerror", (e) => errors.push(String(e)));

await page.goto("http://localhost:3000/login", { waitUntil: "networkidle" });
await page.fill('input[name="email"]', user.email);
await page.fill('input[name="password"]', "Student123!");
await page.click('button[type="submit"]');
await page.waitForURL((u) => !/\/login/.test(u.pathname), { timeout: 20000 });

await page.goto(`http://localhost:3000/exam/${attempt.id}`, { waitUntil: "domcontentloaded" });
await page.waitForSelector("text=Mark for Review", { timeout: 25000 });

// R&W modules have a passage pane; Math ones don't. Walk to a question that does.
for (let i = 0; i < 30 && !(await page.locator(".exam-passage").count()); i++) {
  await page.keyboard.press("ArrowRight");
  await page.waitForTimeout(150);
}
const passage = page.locator(".exam-passage").first();
if (!(await passage.count())) {
  console.log("no passage pane in this module — cannot test highlighting here");
  await browser.close();
  process.exit(1);
}

// Drag across the first line of the passage.
const box = await passage.boundingBox();
await page.mouse.move(box.x + 8, box.y + 10);
await page.mouse.down();
await page.mouse.move(box.x + 320, box.y + 10, { steps: 18 });
await page.mouse.up();
await page.waitForTimeout(500);
await page.screenshot({ path: `${outDir}/1-popup-open.png` });

const pendingMarks = await page.locator("mark.sat-highlight[data-pending]").count();
const pendingText = pendingMarks
  ? await page.locator("mark.sat-highlight[data-pending]").first().innerText()
  : "";
console.log(`pending highlight painted while choosing: ${pendingMarks > 0}`);
if (pendingMarks) console.log(`  it marks: ${JSON.stringify(pendingText.slice(0, 60))}`);

// Hovering a swatch should recolour the pending mark, previewing the result.
const pinkSwatch = page.locator('button[aria-label="pink highlight"]');
if (await pinkSwatch.count()) {
  await pinkSwatch.hover();
  await page.waitForTimeout(250);
  const color = await page
    .locator("mark.sat-highlight[data-pending]")
    .first()
    .getAttribute("data-color")
    .catch(() => null);
  console.log(`hovering the pink swatch previews it: ${color === "pink"}`);
  await page.screenshot({ path: `${outDir}/2-preview-pink.png` });
}

// The real regression: with the popup open, one click on Next must advance.
const counter = page.getByRole("button", { name: /Question \d+ of \d+/ });
const before = await counter.first().innerText();
await page.getByRole("button", { name: /^next$/i }).click();
await page.waitForTimeout(600);
const after = await counter.first().innerText();
console.log(`\nfooter before click: ${before.replace(/\s+/g, " ").trim()}`);
console.log(`footer after  click: ${after.replace(/\s+/g, " ").trim()}`);
console.log(`one click on Next advanced while a popup was open: ${before !== after}`);
await page.screenshot({ path: `${outDir}/3-after-next.png` });

console.log(errors.length ? `\npage errors:\n  ${errors.join("\n  ")}` : "\nno page errors");
await browser.close();
