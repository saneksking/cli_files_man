# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# ---------------------------------------------------------
import os
import shutil


def check_file_size(file):
    file_properties = os.path.getsize(file) / (1024 * 1024)
    return file_properties


def get_size_recursive(folder):
    total_size = 0
    for dir_path, _, filenames in os.walk(folder):
        for filename in filenames:
            file_path = os.path.join(dir_path, filename)
            total_size += os.path.getsize(file_path)
            print(f'File size {filename}: {os.path.getsize(file_path) / (1024 * 1024)} Mb')
    print('-' * 86)
    return total_size


def rm_func(path):
    if os.path.isfile(path):
        os.remove(path)
        print('File deleted!')
    elif os.path.isdir(path):
        shutil.rmtree(path)
        print('Folder deleted')
