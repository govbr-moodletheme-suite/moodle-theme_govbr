#!/usr/bin/env bash
set -euo pipefail

# Build a distributable repository ZIP using git archive.
# export-ignore rules in .gitattributes remove development-only files.

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

SHORT_SHA="$(git rev-parse --short HEAD)"
STAMP="$(date +%Y%m%d)"
OUTPUT="theme_dsgovbr-${STAMP}-${SHORT_SHA}.zip"

git archive --format=zip --worktree-attributes --output "$OUTPUT" HEAD

echo "Created $OUTPUT"
