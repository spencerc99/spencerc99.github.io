import json
from .transform_exported_fits_into_db import FITS_PATH_NAME

labels = set()
with open(FITS_PATH_NAME, 'r') as f:
    fit_data = json.load(f)
    fits = fit_data['fits']
    for fit in fits:
            for label in fit['labels']:
                    labels.add(label)

seen_labels = None
with open('photo_clothing_seen_labels.txt', 'r'):
    seen_labels = set(line.strip() for line in f.readlines())

# read labels from photo_clothing_seen_labels.txt
# print out the new labels only
# manually add to photo_clothing_labels.txt

print("NEW LABELS:")
print(labels.difference(seen_labels))
