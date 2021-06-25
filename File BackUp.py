# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

import os
import filecmp
import shutil
import sys

def autoBackup(scrDir,targetDir):
    if ((not os.path.isdir(scrDir)) or (not os.path.isdir(targetDir)) or
            (os.path.abspath(scrDir)!=scrDir) or (os.path.abspath(targetDir)!=targetDir)):
        usage()
    for item in os.listdir(scrDir):
        scrItem = os.path.join(scrDir,item)
        targetItem = scrItem.replace(scrDir,targetDir)
        if os.path.isdir(scrDir):
            if not os.path.exists(targetItem):
                os.makedirs(targetItem)
                print(f"make directory{targetItem}")
            autoBackup(scrDir,targetDir)

        elif os.path.isfile(scrItem):
            if (not os.path.exists(targetItem)) or (not filecmp.cmp(scrItem,targetItem,shallow = False)):
                shutil.copyfile(scrItem,targetItem)
                print(f"file{scrItem} ===> {targetItem}")

def usage():
    print("需写出绝对路径")
    print(rf"例如:{sys.argv[0]} C:\\olddir C:\\newdir")
    sys.exit(0)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    scrDir ,targetDir = sys.argv[1], sys.argv[2]
    autoBackup(scrDir, targetDir)