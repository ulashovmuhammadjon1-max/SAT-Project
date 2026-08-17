#!/usr/bin/env node
/**
 * Permanently delete student accounts that never confirmed their email.
 *
 *   node scripts/delete-unverified-students.mjs                 # dry run
 *   node scripts/delete-unverified-students.mjs --apply         # delete
 *   node scripts/delete-unverified-students.mjs --apply --force # include accounts with work
 *
 * Dry run is the default and prints the exact rows plus everything that would
 * be destroyed with them. There is no undo, so the safe thing has to be the
 * thing that happens when you forget a flag.
 *
 * Only STUDENT rows are ever considered. An unconfirmed ADMIN or REVIEWER is a
 * colleague who has not clicked a link, not a junk signup, and deleting the
 * operator's own account to tidy a list is not a trade worth making.
 *
 * Accounts carrying real work — an attempt, a graded response, question-bank
 * history, study days, a booking, a referral or an IELTS submission — are held
 * back unless `--force`. Coins are not in that list: the joining bonus is
 * automatic, so treating a balance as work holds back everybody.
 * "Delete the unverified signups" is said with junk accounts in mind; someone
 * with four hundred answered questions who never clicked the link is a real
 * student, and losing their history to a cleanup is the one outcome nobody
 * intends. They are listed either way, so the decision is visible rather than
 * silent.
 *
 * Connection comes from DATABASE_URL. To run against production, set it to the
 * production URL for that one command and do not write it into a file.
 */
import { PrismaClient } from "@prisma/client";

const APPLY = process.argv.includes("--apply");
const FORCE = process.argv.includes("--force");
const prisma = new PrismaClient();

/** Everything that would go with the account, per row. */
async function footprint(userId) {
  const [attempts, responses, qbank, studyDays, bookings, coinRows, referralsMade, ieltsW, ieltsS] =
    await Promise.all([
      prisma.attempt.count({ where: { userId } }),
      prisma.response.count({ where: { attempt: { userId } } }),
      prisma.questionAttempt.count({ where: { userId } }),
      prisma.studyActivity.count({ where: { userId } }),
      prisma.booking.count({ where: { userId } }),
      prisma.coinTransaction.count({ where: { userId } }),
      prisma.referral.count({ where: { referrerId: userId } }),
      prisma.ieltsWritingSubmission.count({ where: { userId } }),
      prisma.ieltsSpeakingSubmission.count({ where: { userId } }),
    ]);
  return { attempts, responses, qbank, studyDays, bookings, coinRows, referralsMade, ieltsW, ieltsS };
}

/**
 * Evidence the person actually used the platform.
 *
 * Coins are deliberately excluded. Signing up grants a joining bonus with no
 * action from the student, so counting a balance as work held back every
 * account that had ever existed — a guardrail that stops everything is
 * indistinguishable from a broken script, and gets bypassed on reflex. The
 * balance is still printed, it just does not decide anything.
 */
const hasWork = (f) =>
  f.attempts + f.responses + f.qbank + f.studyDays + f.bookings + f.referralsMade + f.ieltsW + f.ieltsS > 0;

const main = async () => {
  const candidates = await prisma.user.findMany({
    where: { role: "STUDENT", emailVerified: null },
    select: {
      id: true, email: true, name: true, createdAt: true,
      onboardedAt: true, coinBalance: true,
    },
    orderBy: { createdAt: "asc" },
  });

  if (candidates.length === 0) {
    console.log("No unverified student accounts. Nothing to do.");
    return;
  }

  const rows = [];
  for (const u of candidates) {
    const f = await footprint(u.id);
    rows.push({ ...u, f, work: hasWork(f) });
  }

  const clean = rows.filter((r) => !r.work);
  const withWork = rows.filter((r) => r.work);

  console.log(`${rows.length} unverified student account(s)\n`);
  const show = (r) => {
    const f = r.f;
    const bits = Object.entries(f).filter(([, v]) => v > 0).map(([k, v]) => `${k}=${v}`);
    if (r.coinBalance > 0) bits.push(`coins=${r.coinBalance}`);
    console.log(
      `  ${r.email.padEnd(34)} joined ${r.createdAt.toISOString().slice(0, 10)}` +
        `${r.onboardedAt ? "  onboarded" : "            "}` +
        (bits.length ? `  [${bits.join(" ")}]` : "")
    );
  };

  console.log(`-- no work attached (${clean.length}) --`);
  clean.forEach(show);

  if (withWork.length) {
    console.log(`\n-- HAS WORK ATTACHED (${withWork.length}) --`);
    withWork.forEach(show);
    console.log(
      FORCE
        ? "\n  --force given: these WILL be deleted, and their history with them."
        : "\n  Held back. These look like real students who never clicked the link.\n" +
          "  Re-run with --force to delete them too."
    );
  }

  const doomed = FORCE ? rows : clean;

  if (!APPLY) {
    console.log(`\nDRY RUN — nothing deleted. ${doomed.length} account(s) would go.`);
    console.log("Re-run with --apply to delete.");
    return;
  }

  if (doomed.length === 0) {
    console.log("\nNothing eligible to delete.");
    return;
  }

  const result = await prisma.user.deleteMany({ where: { id: { in: doomed.map((r) => r.id) } } });
  console.log(`\nDeleted ${result.count} account(s).`);
  const left = await prisma.user.count({ where: { role: "STUDENT" } });
  console.log(`${left} student account(s) remain.`);
};

main()
  .catch((e) => {
    console.error(e);
    process.exitCode = 1;
  })
  .finally(() => prisma.$disconnect());
