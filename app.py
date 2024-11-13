# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# ---------------------------------------------------------
import os
import sys
from tools import check_file_size, get_size_recursive, rm_func


def main():
    if len(sys.argv) < 2:
        print('You did not pass a path to a file or folder!\n Program closed!')
        sys.exit(1)

    path = sys.argv[1]
    print(path)
    if os.path.exists(path) and os.path.isfile(path):
        file_size = check_file_size(path)
        print(f'File size: {file_size} Mb')
    elif os.path.exists(path) and os.path.isdir(path):
        folder_size = get_size_recursive(path)
        print(f'Folder size: {folder_size / (1024 * 1024)} Mb')
    else:
        print('You specified a non-existent file or folder.\nProgram closed!')
        sys.exit(1)
    try:
        choice = int(input('Choose action:\n'
                           '1. Delete;\n'
                           '0. Exit.\n'
                           ': '))
        if choice == 1:
            rm_func(path)
        elif choice == 0:
            print('Program closed!')
            sys.exit(1)

    except TypeError:
        print('You entered a non-number\n'
              'Program closed!')


if __name__ == '__main__':
    main()
