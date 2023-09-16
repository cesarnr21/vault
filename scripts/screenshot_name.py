#!/usr/bin/env python3

"""
A script to change the name of screenshots to something from parseable.
only works with linux so far

TODO:
* There is still a bug where files weren't saved in their original directories
"""

from pathlib import Path
import argparse
import datetime

def main():
    file = parse_input()
    if file.is_file():
        rename(file)

    elif file.is_dir():
        for path in file.iterdir():
            rename(path)


def rename(path):
    rm_str = 'Screenshot from '
    if rm_str in path.stem:
        date_time: str = path.stem.partition(rm_str)[2]
        date, space, time = date_time.partition(' ')

        new_name = f'screenshot_{date}_{time}.png'
        old_name = path.name

        # NOTE: should this function be renamed in order for it to not be confused with pathlib Path method?
        path.rename(new_name)
        print(f'Renamed {old_name} to {new_name}')


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=Path, help='enter path for file or directory with screenshots to be renamed')

    file = parser.parse_args()

    return file.path_file


if __name__ == '__main__':
    main()
