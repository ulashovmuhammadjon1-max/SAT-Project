"use client";

import { useState } from "react";
import { Loader, MessageCircle, Send, AlertCircle } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import { askSATTutor } from "@/server/actions/student/sat-tutor";
import { cn } from "@/lib/utils";

interface SATTutorProps {
  questionId: string;
  questionType: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
}

export function SATTutor({ questionId, questionType }: SATTutorProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [message, setMessage] = useState("");
  const [tutorResponse, setTutorResponse] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [remainingRequests, setRemainingRequests] = useState<number | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!message.trim() || isLoading) return;

    setIsLoading(true);
    setError(null);
    setTutorResponse(null);

    try {
      const response = await askSATTutor(questionId, message);

      if (response.ok && response.message) {
        setTutorResponse(response.message);
        setMessage("");
      } else if (response.error) {
        setError(response.error);
      }

      if (response.remainingRequests !== undefined) {
        setRemainingRequests(response.remainingRequests);
      }
    } catch (err) {
      setError("Something went wrong. Please try again.");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) {
    return (
      <Button
        onClick={() => setIsOpen(true)}
        variant="outline"
        size="sm"
        className="gap-2"
      >
        <MessageCircle className="h-4 w-4" />
        Get Help
        {remainingRequests !== null && (
          <span className="ml-1 text-xs text-muted-foreground">
            ({remainingRequests} left)
          </span>
        )}
      </Button>
    );
  }

  return (
    <div className="border border-amber-200 bg-amber-50 dark:border-amber-900/30 dark:bg-amber-900/10 rounded-lg p-4 space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-semibold text-sm flex items-center gap-2">
          <MessageCircle className="h-4 w-4" />
          SAT Tutor
        </h3>
        <Button
          onClick={() => {
            setIsOpen(false);
            setTutorResponse(null);
            setError(null);
          }}
          variant="ghost"
          size="sm"
        >
          ✕
        </Button>
      </div>

      {remainingRequests !== null && (
        <p className="text-xs text-muted-foreground">
          Free tier: {remainingRequests} requests remaining today
        </p>
      )}

      {error && (
        <div className="flex gap-2 rounded-md bg-red-50 dark:bg-red-900/20 p-3">
          <AlertCircle className="h-4 w-4 text-red-600 dark:text-red-400 mt-0.5 flex-shrink-0" />
          <p className="text-xs text-red-600 dark:text-red-400">{error}</p>
        </div>
      )}

      {tutorResponse && (
        <div className="space-y-2">
          <p className="text-xs text-muted-foreground">Tutor's hint:</p>
          <div className="bg-white dark:bg-card rounded p-3 border border-border text-sm leading-relaxed">
            {tutorResponse}
          </div>
          <Button
            onClick={() => {
              setTutorResponse(null);
              setMessage("");
            }}
            variant="outline"
            size="sm"
            className="w-full"
          >
            Ask another question
          </Button>
        </div>
      )}

      {!tutorResponse && (
        <form onSubmit={handleSubmit} className="space-y-2">
          <Textarea
            placeholder="What do you need help understanding about this question?"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            disabled={isLoading}
            className="min-h-24 text-sm"
          />
          <Button
            type="submit"
            disabled={isLoading || !message.trim()}
            className="w-full gap-2"
          >
            {isLoading ? (
              <>
                <Loader className="h-4 w-4 animate-spin" />
                Getting help...
              </>
            ) : (
              <>
                <Send className="h-4 w-4" />
                Get a hint
              </>
            )}
          </Button>
        </form>
      )}

      <p className="text-xs text-muted-foreground border-t pt-2">
        💡 The tutor gives hints, not answers. Work through the problem yourself!
      </p>
    </div>
  );
}
