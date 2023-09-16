#!/usr/bin/env python3

'''
used to fix issues with photography compatability

issues:
* Some file extensions are capitalized
* pictures taken with phone are saved with .HEIC file extension, should be 
    saved as jpeg?
    * are these bigger?
'''


from pathlib import Path



def main():
    current_dir = Path(__file__).parent


if __name__ == '__main__':
    main()
