# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

import os,shutil
scr_data = 'scr_move'  #  需要对比文件夹1
targer_data = 'targetFile'  # 需要对比文件夹2
move_data = 'movedata'  #  移动目的地

scr = os.listdir(scr_data)
target = os.listdir(targer_data)
count = 0
for i in range(len(scr)):
    if scr[i] not in target:
        print(f"发现：文件夹中的：{scr[i]} 不在主文件夹中，可以进行操作！")
        count += 1
        # shutil.copy(f"scr_move/{scr[i]}",move_data) # 复制文件；
        # shutil.move(f"scr_move/{scr[i]}",move_data) # 移动文件;
        # shutil.rmtree("scr_move") # 删除整个文件夹，无论其中是否有文件；
        # os.remove(f"scr_move/{scr[i]}")  # 删除文件。
print()
print("遍历文件夹完成!")
print("移动完成！")
print(f"移动总文件数：{count}")