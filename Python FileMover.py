# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

import os,shutil
scr_data = 'scr_move'  #  Source folder1
targer_data = 'targetFile'  # Source folder2
move_data = 'movedata'  # Folders destination

scr = os.listdir(scr_data)
target = os.listdir(targer_data)
count = 0
for i in range(len(scr)):
    if scr[i] not in target:
        print(f"Found: folder:{scr[i]}is not in the main folder, you can operate!")
        count += 1
        # shutil.copy(f"scr_move/{scr[i]}",move_data) # Copying documents;
        # shutil.move(f"scr_move/{scr[i]}",move_data) # Moving files;
        # shutil.rmtree("scr_move") # remove folders.
        # os.remove(f"scr_move/{scr[i]}")  # delete file.
print()
print("Traversing the folder completed!")
print("End of program running")
print(f"Total files moved:{count}")
