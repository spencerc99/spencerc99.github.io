#!/bin/sh
remote="$1"
url="$2"

python ../../scripts/find_linked_articles.py

[[ -n $(git status -s) ]] && echo 'New linked articles found! Re-commit and push' && exit 1

exit 0
