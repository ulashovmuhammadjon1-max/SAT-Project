"use client";

import { useState, useTransition } from "react";
import { Loader2, Send } from "lucide-react";
import { toast } from "sonner";

import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Textarea } from "@/components/ui/textarea";
import { messageProposalAuthor } from "@/server/actions/admin/research";

/**
 * Email one student about their proposal.
 *
 * Arrives prefilled from the server with the message that is almost always
 * the one being sent, so the common case is a single click and the text is
 * still editable for the case that is not. The send result is reported
 * honestly: the provider's own error text on failure, rather than a success
 * toast over a message that never left.
 */
export function ResearchMessage({
  proposalId,
  studentEmail,
  defaultSubject,
  defaultBody,
}: {
  proposalId: string;
  studentEmail: string | null;
  defaultSubject: string;
  defaultBody: string;
}) {
  const [open, setOpen] = useState(false);
  const [subject, setSubject] = useState(defaultSubject);
  const [body, setBody] = useState(defaultBody);
  const [sentTo, setSentTo] = useState<string | null>(null);
  const [pending, start] = useTransition();

  if (!studentEmail) {
    return (
      <p className="mt-3 text-xs text-muted-foreground">
        No email address on this account, so there is nothing to send to.
      </p>
    );
  }

  if (sentTo) {
    return (
      <p className="mt-3 text-xs font-medium text-emerald-600 dark:text-emerald-400">
        Sent to {sentTo}.
      </p>
    );
  }

  if (!open) {
    return (
      <Button
        size="sm"
        variant="outline"
        className="mt-3 gap-1.5"
        onClick={() => setOpen(true)}
      >
        <Send className="h-3.5 w-3.5" /> Email {studentEmail}
      </Button>
    );
  }

  function send() {
    start(async () => {
      const res = await messageProposalAuthor({ proposalId, subject, body });
      if (res.error) {
        toast.error(res.error);
        return;
      }
      setSentTo(studentEmail);
      toast.success(`Sent to ${studentEmail}.`);
    });
  }

  return (
    <div className="mt-3 space-y-2 rounded-lg border border-border p-3">
      <p className="text-xs text-muted-foreground">To: {studentEmail}</p>
      <Input
        value={subject}
        onChange={(e) => setSubject(e.target.value)}
        className="text-sm"
        placeholder="Subject"
      />
      <Textarea
        value={body}
        onChange={(e) => setBody(e.target.value)}
        rows={9}
        className="text-sm"
        placeholder="Message"
      />
      <div className="flex gap-2">
        <Button size="sm" disabled={pending} onClick={send} className="gap-1.5">
          {pending ? <Loader2 className="h-4 w-4 animate-spin" /> : <Send className="h-3.5 w-3.5" />}
          Send
        </Button>
        <Button size="sm" variant="ghost" disabled={pending} onClick={() => setOpen(false)}>
          Cancel
        </Button>
      </div>
    </div>
  );
}
