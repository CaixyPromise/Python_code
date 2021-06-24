# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""

import tkinter as tk
import tkinter.messagebox
import os
import os.path

path = os.getenv("temp")
filename = os.path.join(path,"info.txt")

win = tk.Tk()
win.geometry("200x140")
label_name = tk.Label(win,text = "User Name:",justify = tk.RIGHT,anchor = "e",width = 80)
label_name.place(x = 10,y = 5,width = 80,height = 20)

var_Name = tk.StringVar(win,value="")
entry_Name = tk.Entry(win,width = 80,textvariable = var_Name)
entry_Name.place(x = 100,y = 5,width = 80,height = 20)

label_pwd = tk.Label(win,text = "User Pwd:",justify = tk.RIGHT,anchor = "e",width = 80)
label_pwd.place(x = 10, y = 30, width = 80,height = 20)

var_password = tk.StringVar(win,value= "")
entry_pwd = tk.Entry(win,show="*",width = 80,textvariable = var_password)
entry_pwd.place(x= 100,y = 30 ,width =80,height = 20)


try:
    with open(filename) as fp:
        n, p = fp.read().strip().split(",")
        var_Name.set(n)
        var_password.set(p)
except:
    pass

var_reme = tk.IntVar(win,value=1)
CheckReme = tk.Checkbutton(win,text="Remember Me?",variable = var_reme,onvalue = 1,offvalue = 0)
CheckReme.place(x = 30, y = 70, width = 120, height = 20)

def login():
    name = entry_Name.get()
    pwd = entry_pwd.get()
    if name == "admin" and pwd == "123":
        tk.messagebox.showinfo(title="恭喜",message="登录成功")
        if var_password.get() == 1:
            with open(filename,"w") as fp:
                fp.write(",".join((name,pwd)))
        else:
            try:
                os.remove(filename)
            except:
                pass
    else:
        tk.messagebox.showerror(title="错误",message="密码错误")

button = tk.Button(win,text = "Login",command = login)
button.place(x = 30, y =100, width=50,height = 20)

def cancel():
    var_Name.set("")
    var_password.set("")

buttonCancel = tk.Button(win,text = "Cancel",command = cancel)
buttonCancel.place(x = 90,y = 100,width = 50, height = 20)

win.mainloop()