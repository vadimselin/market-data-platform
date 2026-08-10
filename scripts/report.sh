#!/bin/bash
set -euo pipefail

DATE="${1:-}"

if [ -z "$DATE" ]; then
  echo "использование: $0 YYYY-MM-DD" >&2
  exit 1
fi

FILE="trades_${DATE}.csv"

if [ ! -f "$FILE" ]; then
  echo "файл не найден: $FILE" >&2
  exit 2
fi

echo "обрабатываю $FILE"

TOTAL=$(grep -vc '^ts,' "$FILE")
echo "всего сделок: $TOTAL"

echo "по символам:"
awk -F',' 'NR>1 {n[$2]++} END {for (s in n) printf "  %-8s %d\n", s, n[s]}' "$FILE" | sort
