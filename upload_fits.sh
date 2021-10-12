#!/bin/bash
# TODO: clean up using this file so that it works properly and test that it works for future updates.
# TODO: allow variable for verbose
helpFunction()
{
   echo ""
   echo "Usage: $0 -verbose -restart"
   echo -e "\t-verbose run verbose"
   echo -e "\t-restart regenerate export from fresh"
   exit 1 # Exit script after printing help
}

while getopts "verbose:restart:" opt
do
   case "$opt" in
      a ) verbose="$OPTARG" ;;
      b ) restart="$OPTARG" ;;
      ? ) helpFunction ;; # Print helpFunction in case parameter is non-existent
   esac
done

echo $verbose
echo $restart

# export from osxphotos
# if restart add --overwrite instead of update and pass arg into post function to clean json file
osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}" --update --convert-to-jpeg --post-function scripts/transform_exported_fits_into_db.py::post_function --preview --verbose ./fits-export
# osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}" --overwrite --convert-to-jpeg --post-function scripts/transform_exported_fits_into_db.py::post_function --preview --verbose ./fits-export

# upload to s3
aws s3 sync ./fits-export/  s3://personal-apple-photos/fits-stream/ --profile=personal-apple-photos --exclude "*" --include "*.jpeg" --include "*.jpg"

# do some logging?

# clean up generated data (or just ignore from git)
