"use client";

import { useEffect, useState, useTransition } from "react";
import { useRouter } from "next/navigation";
import { Loader2, Search, X } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { cn } from "@/lib/utils";
import { grantCoins, searchCoinRecipients, type CoinRecipient } from "@/server/actions/admin/coins";

const MIN_WORDS = 10;
const countWords = (t: string) => t.trim().split(/\s+/).filter(Boolean).length;
const label = (u: CoinRecipient) => u.name ?? (u.username ? `@${u.username}` : u.email ?? "Unnamed account");

export function GrantCoinsForm() {
  const router = useRouter();
  const [query, setQuery] = useState("");
  const [results, setResults] = useState<CoinRecipient[]>([]);
  const [searching, setSearching] = useState(false);
  const [recipient, setRecipient] = useState<CoinRecipient | null>(null);
  const [amount, setAmount] = useState("");
  const [reason, setReason] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  // Debounced search: one request per pause in typing, not per keystroke.
  useEffect(() => {
    if (recipient) return;
    const q = query.trim();
    if (q.length < 2) {
      setResults([]);
      return;
    }
    let cancelled = false;
    setSearching(true);
    const t = setTimeout(async () => {
      const found = await searchCoinRecipients(q);
      if (!cancelled) {
        setResults(found);
        setSearching(false);
      }
    }, 250);
    return () => {
      cancelled = true;
      clearTimeout(t);
    };
  }, [query, recipient]);

  const words = countWords(reason);
  const amountNum = Number.parseInt(amount, 10);
  const ready = recipient && amountNum >= 1 && words >= MIN_WORDS;

  function submit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    if (!recipient) return setError("Choose who receives the coins.");
    startTransition(async () => {
      const res = await grantCoins({ userId: recipient.id, amount: amountNum, reason });
      if (!res.ok) {
        setError(res.error);
        return;
      }
      toast.success(`Added ${amountNum} coins to ${res.name}. New balance: ${res.balance}.`);
      setRecipient(null);
      setQuery("");
      setAmount("");
      setReason("");
      router.refresh();
    });
  }

  return (
    <form onSubmit={submit} className="space-y-5">
      <div className="space-y-1.5">
        <Label htmlFor="coin-recipient">Who receives the coins</Label>
        {recipient ? (
          <div className="flex items-center justify-between gap-3 rounded-lg border border-primary/40 bg-primary/5 px-3 py-2.5">
            <div className="min-w-0">
              <p className="truncate text-sm font-medium">{label(recipient)}</p>
              <p className="truncate text-xs text-muted-foreground">
                {[recipient.username && `@${recipient.username}`, recipient.email].filter(Boolean).join(" · ")}
                {" · "}balance {recipient.coinBalance}
              </p>
            </div>
            <Button type="button" variant="ghost" size="sm" onClick={() => setRecipient(null)} aria-label="Choose someone else">
              <X className="h-4 w-4" />
            </Button>
          </div>
        ) : (
          <>
            <div className="relative">
              <Search aria-hidden className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-muted-foreground" />
              <Input
                id="coin-recipient"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Search by username, email or name"
                autoComplete="off"
                className="pl-9"
              />
              {searching && (
                <Loader2 className="absolute right-3 top-1/2 h-4 w-4 -translate-y-1/2 animate-spin text-muted-foreground" />
              )}
            </div>
            {query.trim().length >= 2 && !searching && results.length === 0 && (
              <p className="text-xs text-muted-foreground">No account matches that.</p>
            )}
            {results.length > 0 && (
              <ul className="divide-y divide-border rounded-lg border border-border">
                {results.map((u) => (
                  <li key={u.id}>
                    <button
                      type="button"
                      onClick={() => setRecipient(u)}
                      className="flex w-full items-center justify-between gap-3 px-3 py-2 text-left hover:bg-secondary focus-visible:bg-secondary focus-visible:outline-none"
                    >
                      <span className="min-w-0">
                        <span className="block truncate text-sm font-medium">{label(u)}</span>
                        <span className="block truncate text-xs text-muted-foreground">
                          {[u.username && `@${u.username}`, u.email, u.role === "ADMIN" ? "Admin" : null]
                            .filter(Boolean)
                            .join(" · ")}
                        </span>
                      </span>
                      <span className="shrink-0 text-xs tabular-nums text-muted-foreground">{u.coinBalance} coins</span>
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </>
        )}
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="coin-amount">Coins to add</Label>
        <Input
          id="coin-amount"
          type="number"
          inputMode="numeric"
          min={1}
          max={10000}
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
          className="max-w-[12rem]"
          required
        />
      </div>

      <div className="space-y-1.5">
        <Label htmlFor="coin-reason">Reason</Label>
        <Textarea
          id="coin-reason"
          value={reason}
          onChange={(e) => setReason(e.target.value)}
          rows={3}
          maxLength={500}
          placeholder="Why these coins are being given. The student sees this in their wallet history."
          aria-describedby="coin-reason-count"
          required
        />
        <p
          id="coin-reason-count"
          className={cn("text-xs", words >= MIN_WORDS ? "text-success" : "text-muted-foreground")}
          aria-live="polite"
        >
          {words} of at least {MIN_WORDS} words
        </p>
      </div>

      {error && (
        <p role="alert" className="rounded-lg bg-destructive/10 px-3 py-2 text-sm text-destructive">
          {error}
        </p>
      )}

      <Button type="submit" disabled={!ready || isPending}>
        {isPending && <Loader2 className="h-4 w-4 animate-spin" />}
        {amountNum >= 1 ? `Add ${amountNum} coins` : "Add coins"}
      </Button>
    </form>
  );
}
