# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

import psutil
import tkinter as tk
import threading
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup

win = tk.Tk()
win.overrideredirect(True)
win.attributes("-alpha",0.7)
win.attributes("-topmost",1)
win.geometry("140x150+100+100")

time_label = tk.Label(win)
time_label.pack(fill = tk.BOTH,expand = tk.YES)
time_label.config(bg = "gray")

var_X = tk.IntVar(value = 0)
var_Y = tk.IntVar(value = 0)
var_canMove = tk.IntVar(value = 0)
var_still = tk.IntVar(value = 1)

def onLeftButtonDown(event):
    win.attributes("-alpha",0.4)
    var_X.set(event.x)
    var_Y.set(event.y)
    var_canMove.set(1)
time_label.bind("<Button-1>",onLeftButtonDown)

def onLeftButtonUP(event):
    win.attributes("-alpha",0.7)
    var_canMove.set(0)
time_label.bind("<ButtonRelease-1>",onLeftButtonUP)

def onLeftButtonMove(event):
    if var_canMove.get() == 0:
        return
    newX = win.winfo_x() + (event.x - var_X.get())
    newY = win.winfo_y() + (event.y - var_Y.get())
    newG = f"140x150+{newX}+{newY}"
    win.geometry(newG)
time_label.bind("<B1-Motion>",onLeftButtonMove)

def onRightButtonDown(event):
    var_still.set(0)
    t.join(0.2)
    win.destroy()
time_label.bind("<Button-3>",onRightButtonDown)

def nowDateTime():
    # 天气爬虫
    url = "http://www.weather.com.cn/weather/101010100.shtml"
    resp = urlopen(url)
    soup = BeautifulSoup(resp,"html.parser")
    target_Today = soup.find("p",class_ = "tem")
    try:
        temperatureHight = target_Today.span.string
    except AttributeError:
        temperatureHight = target_Today.find_next("p",class_="tem").span.string

    temperatureLow = target_Today.i.string
    weather = soup.find("p",class_ = "wea").string

    traffic_io = psutil.net_io_counters()[:2]
    while var_still.get() == 1:
        day_date = time.strftime("%Y - %m - %d")
        dat_time = time.strftime("%H : %M : %S")
        day = f"{day_date}\n{dat_time}"
        traffic_ioNew = psutil.net_io_counters()[:2]
        diff = traffic_ioNew[0] - traffic_io[0],traffic_ioNew[1] - traffic_io[1]
        traffic_io = traffic_ioNew
        diff = tuple(map(lambda x: x*2/1024,diff))
        net_work = "↑{0[0]:.2f} kb/s \n ↓{0[1]:.2f}kb /s".format(diff)

        message = f"{day}\n{net_work}\nH:{temperatureHight}   L:{temperatureLow}\nW:{weather}"
        time_label["text"] = message
        time.sleep(0.5)

if __name__ == '__main__':
    t = threading.Thread(target=nowDateTime)
    t.daemon = True
    t.start()
    win.mainloop()