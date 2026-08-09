/**
 * Meeting-provider contract.
 *
 * Split out from `index.ts` so a provider implementation can import the types
 * without importing the registry that imports it back.
 */

export interface MeetingRequest {
  bookingId: string;
  startsAt: Date;
  durationMinutes: number;
  studentName: string;
  studentEmail: string;
  title: string;
}

export interface MeetingResult {
  /** Null means "no link yet" — a valid, non-error outcome. */
  url: string | null;
  provider: string;
  externalId?: string | null;
}

export interface MeetingProvider {
  id: string;
  /** False when required credentials are absent. */
  isConfigured(): boolean;
  createMeeting(req: MeetingRequest): Promise<MeetingResult>;
  cancelMeeting(externalId: string): Promise<void>;
}
