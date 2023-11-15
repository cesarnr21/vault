#!/usr/bin/env python3

'''
used to create directories with specific names and 
locations to save drone footage. e.i. 23-04-22-san-francisco-airport

TODO:
- Idealy, the path locations would be copied as well. for example if /tmp/folder1/housing/file.dat
    is copied to /tmp/folder2, then a folder `housing` would be created.

FIXME:


'''

from pathlib import Path
import argparse
import shutil

DEFAULT_COPY = '/tmp/'
# switch to false to actually copy files instead of just printing them
TEST_MODE = False


def main():
    file_path, filetype, destination = parse_inputs()

    files = [f for f in file_path.glob(f'**/*') if f.is_file] if filetype is None \
        else [f for f in file_path.glob(f'**/*.{filetype}') if f.is_file]

    new_files = [destination / f.name for f in files]
    
    destination.mkdir(parents=True, exist_ok=True)

    print_files(data = files, target=new_files) if TEST_MODE else copy_files(data = files, target=new_files)


def copy_files(data, target: list) -> None:
    for file, copy in zip(data, target):
        try:
            shutil.copy(file, copy)
            print(f'Copied file {file} to {copy}')
        except PermissionError:
            print(f'skipping file {file} due to Permission')
            continue


def print_files(data, target: list) -> None:
    for file, copy in zip(data, target):
        print(f'Copy file {file} to {copy}')

    print(f'THIS IS TEST MODE, NOTHING WAS ACTUALLY SAVED')


def parse_inputs():
    parser = argparse.ArgumentParser()

    # TODO: should this be type list or string?
    parser.add_argument('path', type=Path,
                        help='path or file to be copied')
    parser.add_argument('-t', '--filetype', type=str, default=None,
                        help='filetype of files to be copied')
    parser.add_argument('-d', '--destination', type=Path, default=DEFAULT_COPY,
                        help='path where file copy will be saved')

    files = parser.parse_args()

    return files.path, files.filetype, files.destination



if __name__ == '__main__':
    main()
