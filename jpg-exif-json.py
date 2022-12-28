#!/usr/bin/python3
#
# JPG/JPEG Get Exif.
#
import os
import argparse
import pathlib
import json
from PIL import Image
from PIL.ExifTags import TAGS

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path, help="Input file.")
args = parser.parse_args()

if not args.file.exists():
    print(f'File not found.')
    exit(1)

image = Image.open(args.file)
exif = image.getexif()

result = {
    'Filename': str(args.file.resolve().absolute())
}

for id in exif:
    tag = TAGS.get(id, id)
    value = exif.get(id)

    if isinstance(value, bytes):
        value = value.decode(errors='ignore')

    if type(value) == int:
        value = int(value)
    else:
        value = str(value)
    result[tag] = value

json_obj = json.dumps(result, indent=4)
print(json_obj)
