#!/usr/bin/env python3

'''
used to create directories with specific names and
 locations to save drone footage. e.i. 23-04-22-san-francisco-airport
'''


from pathlib import Path
import argparse
from datetime import date


def create_dir():
    parser = argparse.ArgumentParser()
    parser.add_argument('details',
                         type=str,
                         nargs='*',
                         help='enter the name of location with spaces'
                        )

    location = parser.parse_args()

    dir_name = create(location)
    check_name(dir_name)

    new_dir = Path(__file__).parent / dir_name
    new_dir.mkdir()
    print(f'created folder: {new_dir}')


def create(location):
    today = f'{date.today()}'
    components = [today]
    for word in location.details:
        components.append(f'{word}')

    dir_name = '-'.join(components)
    return dir_name


def check_name(dir_name):
    '''check that name is accepeted by user'''
    approved = ''
    while approved != 'y':
        print(f'\nfolder name: {dir_name}')
        approved = input('is that correct? [enter "y" if correct] ')

        if approved == 'n': exit()


if __name__ == '__main__':
    create_dir()
