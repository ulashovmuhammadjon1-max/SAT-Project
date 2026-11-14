#!/usr/bin/env bash
# Cut one voiceover take into per-line WAVs, trimmed and sped up the house way.
#
#   cut_lines.sh TAKE.mp3 RANGES.txt OUT_DIR
#
# RANGES.txt has one clip per line:  NAME  START  END  [TEMPO]
# (seconds into the take; TEMPO defaults to 1.2; lines starting with # are skipped)
# Find START/END by transcribing the take:  npx hyperframes transcribe TAKE.mp3
set -euo pipefail
take=$1; ranges=$2; out=$3
mkdir -p "$out"
while read -r name a b tempo; do
  [ -z "${name:-}" ] && continue
  case "$name" in \#*) continue ;; esac
  tempo=${tempo:-1.2}
  ffmpeg -nostdin -v error -y -ss "$a" -to "$b" -i "$take" \
    -af "silenceremove=stop_periods=-1:stop_duration=0.2:stop_threshold=-38dB:stop_silence=0.15,atempo=$tempo" \
    -ar 48000 -ac 1 "$out/$name.wav"
  printf '%s %.2fs\n' "$name" "$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$out/$name.wav")"
done < "$ranges"
