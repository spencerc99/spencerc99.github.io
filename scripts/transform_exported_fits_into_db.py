import urllib.parse
import click
from osxphotos import PhotoInfo, ExportResults
import json
import os
from append_fit_tweet import post_fit_to_twitter
from PIL import Image, ImageOps

FITS_EXPORT_PATH_NAME = './fits-export/'
FITS_PATH_NAME = './data/fits.json'
# Manually change this if you don't want to post to twitter.
# TODO: make this post to a bot account.
SHOULD_POST_TO_TWITTER = False
#TODO: group by day under the same one, turn imgSrc into an array
#TODO: this needs to handle deleting ones that are removed from album.
def post_function(
    photo: PhotoInfo, results: ExportResults, verbose: callable, **kwargs
):
    fits_export_list = os.listdir(FITS_EXPORT_PATH_NAME)
    # noext_filename, ext = os.path.splitext(photo.original_filename)
    # export_filename = f"{str(photo.date).split()[0]}:{noext_filename}"
    # if '{}_preview.jpeg'.format(export_filename) not in fits_export_list and '{}_edited_preview.jpeg'.format(export_filename) not in fits_export_list:
    #     print('\n{}_preview not found in {}, creating new preview'.format(export_filename, FITS_EXPORT_PATH_NAME))
    #     image = Image.open(FITS_EXPORT_PATH_NAME + export_filename + '.jpeg')
    #     fixed_image = ImageOps.exif_transpose(image)
    #     fixed_image.thumbnail((1600,1600), Image.LANCZOS)
    #     fixed_image.save(f'{FITS_EXPORT_PATH_NAME}{export_filename}_preview.jpeg')

    # skip if nothing exported
    if not results.exported: 
        return

    exported_filename = os.path.basename(results.exported[0])

    noext_filename, ext = os.path.splitext(exported_filename)
    if '{}_preview.jpeg'.format(noext_filename) not in fits_export_list:
        print('\n{}_preview not found in {}, creating new preview'.format(noext_filename, FITS_EXPORT_PATH_NAME))
        image = Image.open(FITS_EXPORT_PATH_NAME + exported_filename)
        fixed_image = ImageOps.exif_transpose(image)
        fixed_image.thumbnail((2000,2000), Image.LANCZOS,reducing_gap=7.0)
        fixed_image.save(f'{FITS_EXPORT_PATH_NAME}{noext_filename}_preview.jpeg')

    # check state file to make sure not already in the json
    fit_data = None
    new_object = None
        
    if len(results.exported) > 1:
        verbose(f"warning: Found multiple files exported for same file! {photo.filename}")

    url_encoded_filename = urllib.parse.quote_plus(exported_filename)
    s3_bucket_url = f"https://assets.spencerchang.me/fits-stream/{url_encoded_filename}"
    photo_timestamp = photo.date.timestamp()
    inserted_new_fit = False
    photo_date = photo.date.strftime("%Y-%m-%d")

    def upsert_photo_properties(obj):
        obj["description"] = photo.description or ""
        obj["imgSrc"] = s3_bucket_url
        obj["date"] = photo_date
        obj["timestamp"] = photo_timestamp
        obj["width"] = photo.width 
        obj["height"] = photo.height
        obj["favorite"] = photo.favorite
        obj["place"] = photo.place.name or "" if photo.place else ""
        obj["city"] = photo.place.names.city or "" if photo.place else ""
        if type(obj["city"]) == list:
            obj["city"] = obj["city"][0]
        obj["country"] = photo.place.names.country or "" if photo.place else ""
        if type(obj["country"]) == list:
            obj["country"] = obj["country"][0]
        obj["peopleCount"] = len(photo.persons) or 1
        obj["labels"] = sorted(photo.labels) or []
        obj["season"] = photo.search_info.season or "" if photo.search_info else ""
        obj["activities"] = sorted(photo.search_info.activities) or "" if photo.search_info else ""
        obj["venue_types"] =sorted( photo.search_info.venue_types) or "" if photo.search_info else ""
    
    with open(FITS_PATH_NAME, 'r') as f:
        fit_data = json.load(f)
        fits = fit_data['fits']
        fit_timestamps = set([fit['timestamp'] for fit in fits])

        if photo_timestamp in fit_timestamps:
            verbose(f"Found {url_encoded_filename} inside existing data, updating")
            existing_fit = next(fit for fit in fits if fit['timestamp'] == photo_timestamp)
            upsert_photo_properties(existing_fit)
        else:
            new_object = {}
            upsert_photo_properties(new_object)
            verbose(f"Inserting {url_encoded_filename} with {new_object}")
            fits.insert(0, new_object)
            inserted_new_fit = True

        # ensure this updates as looks like its not carrying through updates
        fit_data['fits'] = fits
        
    with open(FITS_PATH_NAME, 'w') as f:
        verbose("writing out to JSON")
        f.write(json.dumps(fit_data, indent = 4))

    if SHOULD_POST_TO_TWITTER and inserted_new_fit and click.confirm(f'\nPost new fit ({photo_date}) to twitter?'):
        verbose(f"Posting new fit ({photo_date}) to twitter")
        post_fit_to_twitter(results.exported[0], photo_date, description=photo.description)

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
