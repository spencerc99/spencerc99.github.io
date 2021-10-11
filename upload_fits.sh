# TODO: clean up using this file so that it works properly and test that it works for future updates.

# export from osxphotos
osxphotos export --download-missing --album fits\ 🧢 --use-photokit --skip-live --skip-original-if-edited --filename "{created.date}" --update --convert-to-jpeg --post-function scripts/transform_exported_fits_into_db.py::post_function --verbose ./fits-export

# upload to s3
aws s3 sync ./fits-export/  s3://personal-apple-photos/fits-stream/ --profile=personal-apple-photos --exclude "*" --include "*.jpeg" --include "*.jpg"

# do some logging?

# clean up generated data (or just ignore from git)
