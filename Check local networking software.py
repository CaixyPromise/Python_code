# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""
from os.path import basename
from  psutil import  net_connections,Process

for connect in net_connections("all"):

    laddr, raddr, status, pid = connect[3:]
    if not raddr:
        continue
    try:
        filname = basename(Process(pid).exe())
    except:
        pass
    else:
        mag = f"\n程序文件名:{filname}\n本地地址:{laddr}\n远程地址:{raddr}\n连接状态:{status}"
        print(mag)