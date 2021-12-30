#!/bin/sh
# Assumes run from root 

# Pull any other remote changes
# if [ -d "public" ] 
# then
cd public
git pull
cd ..	
# fi

# Build the project.
hugo --minify || exit

# Go To Public folder
cd public || exit

# Add changes to git.
git add .

# Commit changes.
msg="rebuilding site $(date)"
if [ -n "$*" ]; then
	msg="$*"
fi
git commit -m "$msg"
