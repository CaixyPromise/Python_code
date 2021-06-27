# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

from os.path import isdir, join, splitext
from  os import remove, listdir

TypeList = [".tmp", ".log", ".obj", ".txt"]

def delCertainFiles(directory):
    if not isdir(directory):
        return 0
    for filename in listdir(directory):
        temp = join(directory, filename)
        if isdir(temp):
            delCertainFiles(temp)
        elif splitext(temp)[1] in TypeList:
            #print(temp)  输出文件名
            remove(temp)
            print(f"删除 ===> {temp}")

if __name__ == '__main__':
    directory = r"D:\pythonProject2"
    delCertainFiles(directory)