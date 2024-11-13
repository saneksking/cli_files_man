# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# ---------------------------------------------------------
import os

folder_name = f'{os.path.expanduser("~")}/PycharmProjects/cli_files_man/test_folder'
if os.path.exists(f'/{os.path.expanduser("~")}/PycharmProjects/cli_files_man/test_folder'):
    print('Files already created!')
else:
    os.mkdir(folder_name)
    for i in range(5):
        file_name = f'{folder_name}/file_{i}.txt'
        with open(file_name, 'wb+') as file:
            file.write(os.urandom(100))
            print(f'The file was created: {file_name}')
print('Program closed!')
