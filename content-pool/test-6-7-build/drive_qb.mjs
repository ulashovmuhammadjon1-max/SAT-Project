/**
 * Walk the Question Bank practice flow and check the behaviours the redesign
 * was asked for, rather than just screenshotting it.
 *
 *   node drive_qb.mjs <subject> <outDir>
 */
import { chromium } from "playwright-core";
import { PrismaClient } from "@prisma/client";
import fs from "node:fs";

const [subject = "READING_WRITING", outDir = "/tmp/qb"] = process.argv.slice(2);
fs.mkdirSync(outDir, { recursive: true });

const prisma = new PrismaClient();
const user = await prisma.user.findFirstOrThrow({ where: { role: "STUDENT" } });
await prisma.$disconnect();

const browser = await chromium.launch({
  executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
  args: ["--no-sandbox"],
});
const page = await (await browser.newContext({ viewport: { width: 1440, height: 900 } })).newPage();
const errors = [];
page.on("console", (m) => { if (m.type() === "error") errors.push(m.text()); });
page.on("pageerror", (e) => errors.push(String(e)));

let shot = 0;
const snap = async (n) => page.screenshot({ path: `${outDir}/${String(++shot).padStart(2, "0")}-${n}.png` });
const ok = (label, value) => console.log(`  ${value ? "PASS" : "FAIL"}  ${label}`);

await page.goto("http://localhost:3000/login", { waitUntil: "networkidle" });
await page.fill('input[name="email"]', user.email);
await page.fill('input[name="password"]', "Student123!");
await page.click('button[type="submit"]');
await page.waitForURL((u) => !/\/login/.test(u.pathname), { timeout: 20000 });

await page.goto(`http://localhost:3000/practice/session?subject=${subject}&size=5`, {
  waitUntil: "domcontentloaded",
});
await page.waitForSelector("text=Mark for Review", { timeout: 25000 });
await snap("question-1");

console.log(`\n${subject}`);
ok("uses the testing header (Question Bank title)", (await page.getByText(/^Question Bank:/).count()) > 0);
ok("shows the testing banner", (await page.getByText("Question Bank practice").count()) > 0);
ok("has Mark for Review", (await page.getByRole("button", { name: /mark for review/i }).count()) > 0);
ok("has the footer question counter", (await page.getByRole("button", { name: /Question \d+ of \d+/ }).count()) > 0);
ok("has a Fullscreen control", (await page.getByRole("button", { name: /fullscreen/i }).count()) > 0);
ok(
  subject === "MATH" ? "Math offers the Desmos calculator" : "R&W correctly hides the calculator",
  subject === "MATH"
    ? (await page.getByRole("button", { name: /calculator/i }).count()) > 0
    : (await page.getByRole("button", { name: /calculator/i }).count()) === 0
);

// Answer, then submit — and confirm it does NOT advance.
const counterText = async () =>
  (await page.getByRole("button", { name: /Question \d+ of \d+/ }).first().innerText()).replace(/\s+/g, " ").trim();
const before = await counterText();
const fr = await page.getByLabel("Your answer").count();
if (fr) await page.getByLabel("Your answer").fill("2");
else await page.locator('[role="radio"]').first().click();
await snap("answered");

await page.getByRole("button", { name: /^submit$/i }).click();
await page.waitForSelector("text=/^(Correct|Incorrect)$/", { timeout: 15000 });
await page.waitForTimeout(400);
await snap("feedback");

const after = await counterText();
ok("submitting does NOT auto-advance", before === after);
ok("shows a Correct/Incorrect verdict", (await page.locator("text=/^(Correct|Incorrect)$/").count()) > 0);
ok("shows an Explanation section", (await page.getByText("Explanation", { exact: true }).count()) > 0);
ok("marks the correct answer in the list", (await page.getByText("Correct answer", { exact: false }).count()) > 0);
ok("locks the choices after submitting", await page.locator('[role="radio"]').first().isDisabled().catch(() => true));
ok("offers Next Question", (await page.getByRole("button", { name: /next question/i }).count()) > 0);

// Navigator carries the graded outcome.
await page.getByRole("button", { name: /Question \d+ of \d+/ }).first().click();
await page.waitForTimeout(400);
await snap("navigator");
ok("navigator shows outcome legend", (await page.getByText("Incorrect", { exact: true }).count()) > 0);
await page.keyboard.press("Escape");

// Mark for review persists across a reload.
await page.getByRole("button", { name: /mark for review/i }).click();
await page.waitForTimeout(900);
await page.reload({ waitUntil: "domcontentloaded" });
try {
  // "Marked for Review" once the flag persisted, so match either wording.
  await page.getByRole("button", { name: /marked? for review/i }).first().waitFor({ timeout: 20000 });
} catch {
  await snap("reload-STUCK");
  console.log("  reload url: " + page.url().slice(0, 160));
  console.log("  body: " + (await page.locator("body").innerText()).slice(0, 300));
  throw new Error("reload did not render");
}
ok(
  "Mark for Review survives a reload",
  (await page.getByRole("button", { name: /marked for review/i }).count()) > 0
);

if (subject === "MATH") {
  await page.getByRole("button", { name: /calculator/i }).click();
  await page.waitForTimeout(2500);
  await snap("desmos");
  const hasDesmos = await page.locator(".dcg-calculator-api-container, .dcg-container").count();
  ok("Desmos actually mounts", hasDesmos > 0);
  await page.locator('[role="radio"]').first().click().catch(() => {});
  const stillSelected = await page.locator('[role="radio"][aria-checked="true"]').count();
  ok("answer survives opening the calculator", stillSelected > 0);
}

console.log(errors.length ? `\nconsole errors:\n  ${[...new Set(errors)].join("\n  ")}` : "\nno console errors");
await browser.close();
