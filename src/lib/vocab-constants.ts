// A vocab set counts as passed once its quiz is cleared at or above this
// fraction of its questions correct, which is what unlocks the next set in
// the sequence. Percentage-based (not a fixed count) so it still makes sense
// for a set whose quiz has fewer than the usual 10 questions.
export const VOCAB_SET_PASS_FRACTION = 0.8;

export function passThresholdFor(totalQuestions: number) {
  return Math.ceil(totalQuestions * VOCAB_SET_PASS_FRACTION);
}
