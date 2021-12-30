#!/bin/sh
printf "\033[0;32mDeploying updates to GitHub...\033[0m\n"

./scripts/build-and-commit-changes.sh

# Push source and build repos.
cd public && git push origin master
