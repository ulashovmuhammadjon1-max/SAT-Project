export interface ExamChoice {
  id: string;
  label: string;
  content: string;
  order: number;
}

export interface ExamQuestion {
  id: string;
  type: "MULTIPLE_CHOICE" | "FREE_RESPONSE";
  stem: string;
  imageUrl: string | null;
  order: number;
  passage: { id: string; title: string | null; content: string } | null;
  choices: ExamChoice[];
}

export interface ExamModule {
  id: string;
  subject: "READING_WRITING" | "MATH";
  order: number;
  difficulty: string;
  timeLimitMinutes: number;
  questions: ExamQuestion[];
}

export interface ExistingResponse {
  questionId: string;
  selectedChoiceId: string | null;
  freeResponseAnswer: string | null;
  flagged: boolean;
  timeSpentSeconds: number;
  changedAnswerCount: number;
  eliminatedChoiceIds: string[];
}

export interface QuestionState {
  selectedChoiceId: string | null;
  freeResponseAnswer: string;
  flagged: boolean;
  eliminated: string[];
  timeSpentSeconds: number;
  changedAnswerCount: number;
}
