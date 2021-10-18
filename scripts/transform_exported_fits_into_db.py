import urllib.parse
from osxphotos import PhotoInfo, ExportResults
import json
import os

FITS_PATH_NAME = './data/fits.json'
#TODO: group by day under the same one, turn imgSrc into an array
def post_function(
    photo: PhotoInfo, results: ExportResults, verbose: callable, **kwargs
):
    # check state file to make sure not already in the json
    fit_data = None
    new_object = None
    # skip if nothing exported
    if not results.exported: 
        return

    exported_filename = os.path.basename(results.exported[0])

    # osxphotos appends `_preview` by default if it is the preview image that photos uses.
    # Skip processing if this is a preview file since we will have processed the original image.
    if '_preview' in exported_filename:
        verbose(f"skipping processing because it's a preview! {photo.filename}")
        return 
        
    if len(results.exported) > 1:
        verbose(f"warning: Found multiple files exported for same file! {photo.filename}")

    url_encoded_filename = urllib.parse.quote_plus(exported_filename)
    s3_bucket_url = f"https://assets.spencerchang.me/fits-stream/{url_encoded_filename}"

    def upsert_photo_properties(obj):
        obj["description"] = photo.description or ""
        obj["imgSrc"] = s3_bucket_url
        obj["date"] = photo.date.strftime("%Y-%m-%d")
        obj["timestamp"] = photo.date.timestamp()
        obj["width"] = photo.width
        obj["height"] = photo.height
    
    with open(FITS_PATH_NAME, 'r') as f:
        fit_data = json.load(f)
        fits = fit_data['fits']
        fits_img_srcs = set([fit['imgSrc'] for fit in fits])

        if s3_bucket_url in fits_img_srcs:
            verbose(f"Found {url_encoded_filename} inside existing data, updating")
            existing_fit = next(fit for fit in fits if fit['imgSrc'] == s3_bucket_url)
            upsert_photo_properties(existing_fit)
        else:
            new_object = {}
            upsert_photo_properties(new_object)
            verbose(f"Inserting {url_encoded_filename} with {new_object}")
            fits.insert(0, new_object)

        # ensure this updates as looks like its not carrying through updates
        fit_data['fits'] = fits
        
    with open(FITS_PATH_NAME, 'w') as f:
        verbose("writing out to JSON")
        f.write(json.dumps(fit_data, indent = 4))

# rewrite the file
# fit_data = None
# with open(FITS_PATH_NAME, 'r') as f:
#     fit_data = json.load(f)
#     fits = fit_data['fits']
#     print(f'Found {len(fits)} fits')
#     img_srcs = set([])
#     new_fits = []
#     for fit in fits:
#         if fit['imgSrc'] not in img_srcs:
#             img_srcs.add(fit['imgSrc'])
#             new_fits.append(fit)
#     print(f'New file will consist of {len(new_fits)} fits')
#     imgs_without_width = [fit for fit in new_fits if 'width' not in fit]
#     print(len(imgs_without_width))
#     print([fit['date'] for fit in imgs_without_width])
#     fits = new_fits
#     fit_data['fits'] = new_fits
#     print(len(fit_data['fits']))

# with open(FITS_PATH_NAME, 'w') as f:
#     f.write(json.dumps(fit_data, indent = 4))
