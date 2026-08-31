#!/usr/bin/env sh
# Vercel "Ignored Build Step".
#
#   exit 1 -> BUILD          exit 0 -> SKIP
#
# Content authoring commits cannot change the deployed site. Everything the
# authoring pipeline writes lives under content-pool/, and nothing in src/,
# prisma/ or next.config.mjs imports from there -- the only four mentions of
# the directory anywhere in the app are comments naming a source file. Questions
# reach students through the database, written by a script against Neon's HTTP
# API, never through the bundle.
#
# So a build on a content commit produces a byte-identical site. In one six-hour
# authoring session this fired 66 times out of 69, because the per-topic commit
# rule -- which is what saves the run when an agent dies mid-topic -- pushes
# after every topic.
#
# The alternative was to batch the pushes, which trades the durability the
# commit rule exists to provide. This keeps both.
#
# DELIBERATELY CONSERVATIVE: a skipped build that was actually needed means the
# user's site silently does not update, which is far worse than a wasted build.
# So this skips only when EVERY changed file is one that provably cannot affect
# the output, and builds whenever it cannot prove that -- including when it
# cannot work out what changed at all.
set -u

BUILD=1
SKIP=0

PREV="${VERCEL_GIT_PREVIOUS_SHA:-}"

if [ -z "$PREV" ]; then
  echo "No previous SHA (first deploy or manual redeploy). Building."
  exit $BUILD
fi

# Vercel clones shallow, so the previous commit is often absent. Try to fetch
# it; if it still is not there, we cannot compute a diff and must build.
if ! git cat-file -e "${PREV}^{commit}" 2>/dev/null; then
  git fetch --depth=200 origin "$PREV" >/dev/null 2>&1 || true
fi
if ! git cat-file -e "${PREV}^{commit}" 2>/dev/null; then
  echo "Previous SHA $PREV is unreachable; cannot diff. Building."
  exit $BUILD
fi

CHANGED=$(git diff --name-only "$PREV" HEAD 2>/dev/null) || {
  echo "git diff failed. Building."
  exit $BUILD
}

if [ -z "$CHANGED" ]; then
  echo "No file changes against $PREV. Skipping."
  exit $SKIP
fi

# Paths that cannot reach the bundle. Keep this list short and boring; when in
# doubt leave a path OFF it, because being off it only costs a build.
OUTSIDE=$(printf '%s\n' "$CHANGED" | grep -vE '^(content-pool/|CLAUDE\.md$)' || true)

if [ -z "$OUTSIDE" ]; then
  echo "Only content-pool/ and CLAUDE.md changed; the build output cannot differ. Skipping."
  printf '%s\n' "$CHANGED" | head -5 | sed 's/^/  /'
  exit $SKIP
fi

echo "Files outside the content paths changed. Building."
printf '%s\n' "$OUTSIDE" | head -10 | sed 's/^/  /'
exit $BUILD
