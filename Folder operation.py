# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

import os

totalSize, filename, dirNum = 0, 0, 0

def checkDir(path):
    global totalSize, filename, dirNum
    for lists in os.listdir(path):
        sub_path = os.path.join(path, lists)
        if os.path.isfile(sub_path):
            filename = filename + 1
            totalSize = totalSize + os.path.getsize(sub_path)
        elif os.path.isdir(sub_path):
            dirNum += 1
            checkDir(sub_path)

def sizeConvert(size):
    K, M, G = 1024, 1024**2 , 1024**3
    if size >= G:
        return "{:.2f} G bytes".format(size/G)
    elif size >= M:
        return "{:.2f} M bytes".format(size/M)
    elif size >= K:
        return "{:.2f} K bytes".format(size/K)
    else:
        return "{:.2f} bytes".format(size)

def output(path):
    print(f"文件夹 {path} 中空间大小 : {sizeConvert(totalSize)}")
    print(f"文件夹 {path} 中文件总数: {filename}")
    print(f"文件夹 {path} 中目录总数: {dirNum}")

def main(path):
    if not os.path.isdir(path):
        print(f"Error: {path} is not a directory or does not exist.")
        return 0
    else:
        checkDir(path)

if __name__ == '__main__':
    path = r"D:\pythonProject2"
    main(path)
    output(path)