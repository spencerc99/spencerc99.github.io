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
    if not results.exported: 
        return
    with open(FITS_PATH_NAME, 'r') as f:
        fit_data = json.load(f)
        fits = fit_data['fits']
        fits_img_srcs = set([fit['imgSrc'] for fit in fits])
        if len(results.exported) > 1:
            verbose(f"warning: Found multiple files exported for same file! {photo.filename}")
        exported_filename = os.path.basename(results.exported[0])

        url_encoded_filename = urllib.parse.quote_plus(exported_filename)
        s3_bucket_url = f"https://personal-apple-photos.s3.us-west-2.amazonaws.com/fits-stream/{url_encoded_filename}"

        if url_encoded_filename in fits_img_srcs:
            verbose(f"Found {url_encoded_filename} inside the file, skipping adding")
            return
        

        new_object = {
            "description": photo.description or "",
            "imgSrc": s3_bucket_url,
            "date": photo.date.strftime("%Y-%m-%d"),
            "timestamp": photo.date.timestamp()
        }

        verbose(f"Inserting {url_encoded_filename} with {new_object}")
        fits.insert(0, new_object)

        # write all data, escaped for JSON to an object, separate them by lines in temp place?
        # when all over re-write the db file
        
    with open(FITS_PATH_NAME, 'w') as f:
        verbose("writing out to JSON")
        f.write(json.dumps(fit_data, indent = 4))
