# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

from  psutil import disk_partitions
from shutil import copytree
import time

while 1:
    time.sleep(3)
    for item in disk_partitions():
        if "removable" in item.opts:
            driver = item.device
            print("Found USB disk",driver)
            copytree(driver, r"C:\usedisk")
            break
    else:
        continue

    break
print("all file copy")

