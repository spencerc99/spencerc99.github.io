# Overview
My fits stream lives at https://spencerchang.me/fits. This involves a relatively automated process for uploading my outfits of the day to this ever-growing collection on my website. 

## Details
### Extraction
`upload_fits.sh` is the main file that powers the whole process. It uses the python library `osxphotos` which has meticulous functionality for exporting photos from your Apple photos library and taking advantage of all the structured metadata that Apple provides. I created my own script (`transform_exported_fits_to_db.py`) for post-processing the fits into a `fits.json` file that lives in the `data` folder for my hugo website for consumption to avoid the need for any sort of personal server to handle the data.

### Serving
After exporting, I upload all the files to a personal S3 bucket which has Cloudfront hooked up to serve the files from CDN. I also set up a CDN for the site itself, which is hosted on a different domain (assets.spencerchang.me).

### Fit Metadata
Using the post-processing script I gather a lot of metadata from the photos for display on the site and for other projects that operate on top of the fit data. Apple automatically assigns a bunch of labels using their ML models to each photo, and I've manually separated out the ones that are relevant to fits and clothing in `photo_clothing_labels.txt`. This was a manual 
