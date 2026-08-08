import { Prisma, type CoinTxnType, type PrismaClient } from "@prisma/client";

import { prisma } from "@/lib/prisma";

/**
 * The SATForge Coins ledger.
 *
 * Every balance change in the product goes through `credit` or `debit`. Both
 * write a `CoinTransaction` row and update `User.coinBalance` inside a single
 * database transaction, so the cached balance can never drift from the ledger.
 *
 * Three properties this file is responsible for:
 *
 *   1. **Server-authoritative.** Nothing here reads a balance supplied by a
 *      caller. `debit` re-reads the balance inside the transaction and decides
 *      for itself whether the spend is affordable.
 *   2. **No double-spend, no double-credit.** The balance update is expressed
 *      as a conditional write (`updateMany` with a `gte` guard), so two
 *      concurrent debits cannot both succeed against the same coins. Rewards
 *      carry an `idempotencyKey` whose unique index turns a retry into a no-op
 *      instead of a second payment.
 *   3. **No negative balances.** Enforced by the same conditional write, not by
 *      a check-then-write that a concurrent request could interleave with.
 */

/** A Prisma client or an interactive-transaction client. */
type Db = PrismaClient | Prisma.TransactionClient;

export class InsufficientCoinsError extends Error {
  constructor(
    readonly required: number,
    readonly available: number,
  ) {
    super(`Insufficient coins: needed ${required}, had ${available}`);
    this.name = "InsufficientCoinsError";
  }
}

export interface LedgerEntryInput {
  userId: string;
  /** Always positive; `credit` and `debit` apply the sign. */
  amount: number;
  type: CoinTxnType;
  description: string;
  bookingId?: string | null;
  referralId?: string | null;
  /** Admin who performed an adjustment. */
  actorId?: string | null;
  /**
   * Stable key derived from the triggering event, e.g. `signup:<userId>` or
   * `referral:<referralId>`. A replay of the same event hits the unique index
   * and is swallowed, so the user is paid exactly once.
   */
  idempotencyKey?: string | null;
}

export interface LedgerResult {
  /** False when an idempotency key meant this had already been applied. */
  applied: boolean;
  balance: number;
  transactionId?: string;
}

/**
 * Add coins.
 *
 * Safe to call from inside a caller's transaction by passing `db` — referral
 * rewards do this so the reward and the referral status flip commit together.
 */
export async function credit(input: LedgerEntryInput, db: Db = prisma): Promise<LedgerResult> {
  const amount = Math.floor(input.amount);
  if (amount <= 0) throw new Error(`credit() needs a positive amount, got ${input.amount}`);

  const run = async (tx: Prisma.TransactionClient): Promise<LedgerResult> => {
    if (input.idempotencyKey) {
      const existing = await tx.coinTransaction.findUnique({
        where: { idempotencyKey: input.idempotencyKey },
        select: { id: true, balanceAfter: true },
      });
      if (existing) {
        // Already paid. Report the balance as it stands now, not as it was.
        const user = await tx.user.findUnique({
          where: { id: input.userId },
          select: { coinBalance: true },
        });
        return { applied: false, balance: user?.coinBalance ?? existing.balanceAfter };
      }
    }

    const user = await tx.user.update({
      where: { id: input.userId },
      data: { coinBalance: { increment: amount } },
      select: { coinBalance: true },
    });

    const txn = await tx.coinTransaction.create({
      data: {
        userId: input.userId,
        amount,
        type: input.type,
        balanceAfter: user.coinBalance,
        description: input.description,
        bookingId: input.bookingId ?? null,
        referralId: input.referralId ?? null,
        actorId: input.actorId ?? null,
        idempotencyKey: input.idempotencyKey ?? null,
      },
      select: { id: true },
    });

    return { applied: true, balance: user.coinBalance, transactionId: txn.id };
  };

  try {
    return isTransactionClient(db) ? await run(db) : await prisma.$transaction(run);
  } catch (error) {
    // Two concurrent replays of the same event: one wins, the other trips the
    // unique index. That is success from the caller's point of view.
    if (
      input.idempotencyKey &&
      error instanceof Prisma.PrismaClientKnownRequestError &&
      error.code === "P2002"
    ) {
      const user = await prisma.user.findUnique({
        where: { id: input.userId },
        select: { coinBalance: true },
      });
      return { applied: false, balance: user?.coinBalance ?? 0 };
    }
    throw error;
  }
}

/**
 * Spend coins. Throws `InsufficientCoinsError` if the balance will not cover it.
 *
 * The guard is the `updateMany ... where coinBalance >= amount` below: Postgres
 * evaluates the predicate and the write atomically, so of two requests racing
 * for the last 10 coins exactly one matches a row and the other sees count 0.
 * A read-then-write would let both pass the check.
 */
export async function debit(input: LedgerEntryInput, db: Db = prisma): Promise<LedgerResult> {
  const amount = Math.floor(input.amount);
  if (amount <= 0) throw new Error(`debit() needs a positive amount, got ${input.amount}`);

  const run = async (tx: Prisma.TransactionClient): Promise<LedgerResult> => {
    if (input.idempotencyKey) {
      const existing = await tx.coinTransaction.findUnique({
        where: { idempotencyKey: input.idempotencyKey },
        select: { id: true, balanceAfter: true },
      });
      if (existing) {
        const user = await tx.user.findUnique({
          where: { id: input.userId },
          select: { coinBalance: true },
        });
        return { applied: false, balance: user?.coinBalance ?? existing.balanceAfter };
      }
    }

    const updated = await tx.user.updateMany({
      where: { id: input.userId, coinBalance: { gte: amount } },
      data: { coinBalance: { decrement: amount } },
    });

    if (updated.count === 0) {
      const user = await tx.user.findUnique({
        where: { id: input.userId },
        select: { coinBalance: true },
      });
      throw new InsufficientCoinsError(amount, user?.coinBalance ?? 0);
    }

    const user = await tx.user.findUniqueOrThrow({
      where: { id: input.userId },
      select: { coinBalance: true },
    });

    const txn = await tx.coinTransaction.create({
      data: {
        userId: input.userId,
        amount: -amount,
        type: input.type,
        balanceAfter: user.coinBalance,
        description: input.description,
        bookingId: input.bookingId ?? null,
        referralId: input.referralId ?? null,
        actorId: input.actorId ?? null,
        idempotencyKey: input.idempotencyKey ?? null,
      },
      select: { id: true },
    });

    return { applied: true, balance: user.coinBalance, transactionId: txn.id };
  };

  return isTransactionClient(db) ? run(db) : prisma.$transaction(run);
}

/**
 * Apply a signed adjustment. Used by the admin panel, where the amount may be
 * either direction and must always leave a ledger row behind.
 */
export async function adjust(
  input: Omit<LedgerEntryInput, "amount"> & { amount: number },
  db: Db = prisma,
): Promise<LedgerResult> {
  if (input.amount === 0) throw new Error("adjust() needs a non-zero amount");
  return input.amount > 0
    ? credit({ ...input, amount: input.amount }, db)
    : debit({ ...input, amount: -input.amount }, db);
}

export async function getBalance(userId: string): Promise<number> {
  const user = await prisma.user.findUnique({
    where: { id: userId },
    select: { coinBalance: true },
  });
  return user?.coinBalance ?? 0;
}

/**
 * Recompute a balance from the ledger and report any drift.
 *
 * Nothing in the product calls this on the hot path; it exists so the admin
 * panel can prove the cached balance still agrees with the transactions, which
 * is the whole reason the ledger stores `balanceAfter`.
 */
export async function reconcile(userId: string) {
  const [agg, user] = await Promise.all([
    prisma.coinTransaction.aggregate({
      where: { userId },
      _sum: { amount: true },
    }),
    prisma.user.findUnique({ where: { id: userId }, select: { coinBalance: true } }),
  ]);
  const ledgerTotal = agg._sum.amount ?? 0;
  const cached = user?.coinBalance ?? 0;
  return { ledgerTotal, cached, drift: cached - ledgerTotal, ok: cached === ledgerTotal };
}

/** `$transaction(fn)` hands back a client without `$transaction` on it. */
function isTransactionClient(db: Db): db is Prisma.TransactionClient {
  return !("$transaction" in db);
}
