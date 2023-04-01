#!/bin/bash
# NOTE: this assumes running from root directory.
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
# --only-new seems to exclude preview??
# --ignore-signature handles photos that have been exported and then updated
# --force-update, this will handle updated metadata
osxphotos export --download-missing --album fits\ 🧢 --skip-live --skip-original-if-edited --only-new --filename "{created.date}:{original_name}" --force-update --ignore-signature --convert-to-jpeg --post-function ./scripts/transform_exported_fits_into_db.py::post_function ./fits-export
# osxphotos export --download-missing --album fits\ 🧢 --use-photokit  --skip-live --skip-original-if-edited --only-new --filename "{created.date}:{original_name}" --force-update --ignore-signature --convert-to-jpeg --post-function ./scripts/transform_exported_fits_into_db.py::post_function ./fits-export

# normal --update, this caches "last exported" so might miss some if out of order?
# osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}:{original_name}" --update --ignore-signature --convert-to-jpeg --post-function ./scripts/transform_exported_fits_into_db.py::post_function ./fits-export

# just re-export everything
# osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}:{original_name}"  --convert-to-jpeg --post-function ./scripts/transform_exported_fits_into_db.py::post_function ./fits-export

# overwrite the export, this will re-export everything lol
# osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}:{original_name}"  --overwrite --convert-to-jpeg --post-function ./scripts/transform_exported_fits_into_db.py::post_function ./fits-export

read -p "Continue with upload ('y' to confirm)?" choice
case "$choice" in 
  y|Y ) echo "proceeding with upload";;
  * ) echo "aborting"; exit;
esac

# upload to s3
aws s3 sync ./fits-export/  s3://personal-apple-photos/fits-stream/ --profile=personal-apple-photos --exclude "*" --include "*.jpeg" --include "*.jpg" --include "*.JPG" --include "*.JPEG" --delete

# do some logging?

# clean up generated data (or just ignore from git)
