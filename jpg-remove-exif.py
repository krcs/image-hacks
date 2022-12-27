#
# JPG/JPEG Exif remover.
#
import os
import argparse
import pathlib
from exif import Image

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--source', required=True, type=pathlib.Path, help="Source file or directory.")
parser.add_argument('-o', '--output', type=pathlib.Path, help="Output file or directory.")
args = parser.parse_args()

if not args.source.exists():
    print()
    print('Error! Source does not exist.')
    print()
    exit(1)

if not args.output:
    args.output = args.source.parent
elif args.source.is_dir():
    if args.output.is_file() or args.output.suffix.startswith('.'):
        print()
        print('Error! Output cannot be file when input is a directory.')
        print()
        exit(1)

