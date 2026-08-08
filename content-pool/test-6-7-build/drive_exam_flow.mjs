/**
 * Drive a whole attempt through the exam interface and shoot every screen it
 * passes through: module questions, Check Your Work, the module-over
 * interstitial, the section break, and the first question of the next module.
 *
 * Exists because the module-to-module handoff is the one part of the exam no
 * static screenshot can verify -- the bug it was written for (the shell keeping
 * its previous module's state across the transition) only appears once you
 * actually end a module.
 *
 *   node drive_exam_flow.mjs <testTitle> <outDir>
 */
import { chromium } from "playwright-core";
import { PrismaClient } from "@prisma/client";
import fs from "node:fs";

const [testTitle = "Test 6", outDir = "/tmp/flow"] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });

const prisma = new PrismaClient();
const user = await prisma.user.findFirstOrThrow({ where: { role: "STUDENT" } });
const test = await prisma.test.findFirstOrThrow({ where: { title: testTitle } });

// Fresh attempt on the opening module, so the preparing curtain shows too.
for (const a of await prisma.attempt.findMany({ where: { userId: user.id, testId: test.id } })) {
  await prisma.response.deleteMany({ where: { attemptId: a.id } });
  await prisma.moduleAttempt.deleteMany({ where: { attemptId: a.id } });
  await prisma.attempt.delete({ where: { id: a.id } });
}
const first = await prisma.module.findFirstOrThrow({
  where: { testId: test.id, subject: "READING_WRITING", order: 1 },
});
const attempt = await prisma.attempt.create({
  data: {
    userId: user.id,
    testId: test.id,
    status: "IN_PROGRESS",
    currentModuleId: first.id,
    moduleAttempts: { create: { moduleId: first.id } },
  },
});
await prisma.$disconnect();

const browser = await chromium.launch({
  executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args: ["--no-sandbox"],
});
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
const page = await ctx.newPage();
const errors = [];
page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
page.on("pageerror", (e) => errors.push(String(e)));

let shot = 0;
const snap = async (name) => {
  shot += 1;
  await page.screenshot({ path: `${outDir}/${String(shot).padStart(2, "0")}-${name}.png` });
};
const heading = async () =>
  (await page.locator("h1, [class*='font-semibold']").first().innerText().catch(() => "")).slice(0, 60);

await page.goto("http://localhost:3000/login", { waitUntil: "networkidle" });
await page.fill('input[name="email"]', user.email);
await page.fill('input[name="password"]', "Student123!");
await page.click('button[type="submit"]');
await page.waitForURL((u) => !/\/login/.test(u.pathname), { timeout: 20000 });

await page.goto(`http://localhost:3000/exam/${attempt.id}`, { waitUntil: "domcontentloaded" });

// The preparing curtain is short-lived; catch it before it lifts.
await page.waitForTimeout(500);
await snap("preparing");
console.log("preparing screen:", await heading());

try {
  await page.waitForSelector("text=Mark for Review", { timeout: 15000 });
} catch {
  await snap("STUCK");
  console.log("STUCK. body text:\n" + (await page.locator("body").innerText()).slice(0, 600));
  await browser.close();
  process.exit(1);
}
await snap("module1-q1");

// Answer the first two, then walk to the end of the module with the keyboard.
// Past the last question `goNext` opens the review page, which is the route a
// student actually takes to End Module.
for (const label of ["A", "B"]) {
  await page.locator('[role="radio"], button:has(span:text-is("' + label + '"))').first().click().catch(() => {});
  await page.keyboard.press("ArrowRight");
  await page.waitForTimeout(200);
}
await page.locator("button:has-text('Question 3 of')").first().click().catch(() => {});
await page.waitForTimeout(400);
await snap("navigator");
await page.keyboard.press("Escape");

const total = Number((await page.locator("button:has-text('Question')").first().innerText()).match(/of (\d+)/)?.[1] ?? 27);
for (let i = 0; i < total; i++) await page.keyboard.press("ArrowRight");
await page.waitForTimeout(600);
await snap("check-your-work");
console.log("review page heading:", await page.locator("h1").first().innerText().catch(() => "(none)"));

// End the module and watch the handoff.
await page.getByRole("button", { name: /end module/i }).click();
await page.waitForTimeout(400);
await snap("module-over");
console.log("after End Module:", await heading());

// A section break is expected only when crossing R&W -> Math; module 1 -> 2
// should land straight on question 1 of the next module.
await page.waitForTimeout(3500);
await snap("after-transition");
const landed = await heading();
console.log("landed on:", landed);

const onQuestion1 = await page.locator("text=Question 1 of").count();
const sectionLabel = await page.locator("text=/Section \\d, Module/").first().innerText().catch(() => "");
console.log(`section label: ${sectionLabel}`);
console.log(`shows "Question 1 of": ${onQuestion1 > 0}`);

// Round two: end R&W Module 2, which crosses into the Math section and so must
// stop at a break instead of advancing straight through.
const total2 = Number((await page.locator("button:has-text('Question')").first().innerText()).match(/of (\d+)/)?.[1] ?? 27);
for (let i = 0; i < total2 + 1; i++) await page.keyboard.press("ArrowRight");
await page.waitForTimeout(500);
await page.getByRole("button", { name: /end module/i }).click();
await page.waitForTimeout(2500);
await snap("section-break");
console.log("\nafter ending the last R&W module:", await page.locator("h1").first().innerText().catch(() => "(no h1)"));

const resume = page.getByRole("button", { name: /resume testing/i });
console.log("break screen has Resume Testing:", (await resume.count()) > 0);
if (await resume.count()) {
  await resume.click();
  await page.waitForTimeout(3500);
  await snap("math-module1");
  console.log("after resuming:", await page.locator("text=/Section \\d, Module/").first().innerText().catch(() => "(none)"));
  console.log("calculator available:", (await page.getByText("Calculator", { exact: false }).count()) > 0);
}

console.log(errors.length ? `\nconsole errors:\n  ${[...new Set(errors)].join("\n  ")}` : "\nno console errors");
await browser.close();
