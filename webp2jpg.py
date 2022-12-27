#!/usr/bin/python3
#
# webp2jpg
#
import os
import random
import string
import argparse
import pathlib
import time
from PIL import Image

def generate_random_string(length):
    ld = string.ascii_letters+string.digits
    return ''.join([random.choice(ld) for n in range(length)])

def get_image(filename):
    with open(filename, 'rb') as image_file:
        result = Image(image_file)
    return result

def save_image(filename, image):
    with open(filename, 'wb') as image_file:
        image_file.write(image.get_file())

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, type=pathlib.Path, help="Input file or directory.")
parser.add_argument('-o', '--output', type=pathlib.Path, help="Output file or directory.")
parser.add_argument('-r', '--random-name', action="store_true",
        help="Genereate random file name. Ignored when output is a file.")
parser.add_argument('-rl', '--random-name-length', help="Random string length, default 8.", type=int, default=8)
args = parser.parse_args()

if not args.input.exists():
    print()
    print('Error! Input not exist.')
    print()
    exit(1)

if not args.output:
    args.output = args.input.parent

inputs = []

if args.input.is_dir():
    if args.output.is_file() or args.output.suffix.startswith('.'):
        print()
        print('Error! Output cannot be file when input is a directory.')
        print()
        exit(1)
    
    for obj in os.scandir(args.input):
        if obj.is_file():
           if obj.name.lower().endswith('.webp'):
               inputs.append(args.input.joinpath(obj.name))
else:
    inputs.append(args.input.absolute())

start_time = time.time()

for idx, input in enumerate(inputs):
    output = ''

    if args.output.is_file() or args.output.suffix.startswith('.'):
        output = args.output.absolute()
    else:
        output_name = ''

        if args.random_name:
            random_name = generate_random_string(args.random_name_length)
            output_name = f'{random_name}.jpg'

        else:
            output_name = f'{input.stem}.jpg'

        output = args.output.absolute().joinpath(output_name)

    print(f'[{idx+1}] - {input} -> {output}')
    image = Image.open(input).convert('RGB')
    image.save(output, 'jpeg')

seconds = time.time() - start_time
print('Done in', time.strftime('%H:%M:%S',time.gmtime(seconds)))
