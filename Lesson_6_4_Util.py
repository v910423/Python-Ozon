import os
import shutil

while True:
    choice = input('wht 2 do? \nCreate - C. \nDelete - D \nQuit - Q\n').upper()
    if choice == 'Q':
        exit()
    elif choice == 'C':
        dir_name = input('enter directory"s name: ')
        os.mkdir(dir_name)
    elif choice == 'D':
        dir_name = input('enter name of dir to delete: ')
        shutil.rmtree(dir_name)