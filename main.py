#!/usr/bin/env python3
# Created by Master on 1/23/2023 at 6:01 PM

import os
import argparse
import glob
from PIL import Image

output_format = 'png'

crop_cover = True
cover_border_bar_width = 580
cover_width = 759

bar_border_left_width = 201
bar_border_right_width = 201

page_left_width = 759  # Second page
page_right_width = 759  # First page


def mango_cut(input_files: list[str], output_dir: str):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
        pass

    img_index = 1
    for i in range(len(input_files)):
        input_image = input_files[i]
        with Image.open(input_image) as image:
            if crop_cover and img_index == 1:
                img_cover = image.crop(
                    box=[
                        cover_border_bar_width,
                        0,
                        cover_border_bar_width + cover_width,
                        image.size[1]
                    ]
                )
                img_cover.save(f'{output_dir}{os.path.sep}{img_index:03}.{output_format}', format=output_format)
                img_index += 1
                continue

            img_right = image.crop(  # This might be the wrong implementation, but it works...
                box=[
                    bar_border_right_width + page_right_width,
                    0,
                    bar_border_right_width + page_right_width * 2,
                    image.size[1]
                ]
            )
            img_right.save(f'{output_dir}{os.path.sep}{img_index:03}.{output_format}', format=output_format)
            img_index += 1

            img_left = image.crop(
                box=[
                    bar_border_left_width,
                    0,
                    bar_border_left_width + page_left_width,
                    image.size[1]
                ]
            )
            img_left.save(f'{output_dir}{os.path.sep}{img_index:03}.{output_format}', format=output_format)
            img_index += 1
            pass
        continue
    return


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--input_format', dest='input_format')
    arg_parser.add_argument('--input', dest='input')
    arg_parser.add_argument('--output', dest='output')
    args = arg_parser.parse_args()

    input_files = []
    for i in glob.glob(f'*.{args.input_format}', root_dir=args.input):
        input_files.append(f'{args.input}{os.path.sep}{i}')
        continue
    del i

    mango_cut(input_files, args.output)
    return


if __name__ == '__main__':
    main()
    pass
