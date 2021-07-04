# -*- coding:utf-8 -*-

"""

CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""


import tkinter as tk
import tkinter.messagebox
import math
import re

win = tk.Tk()
win.geometry("300x270")
win.resizable(width=False,height=False)
win.title("Calc")

var_state = tk.StringVar(win,"")
state_entry = tk.Entry(win, textvariable = var_state)
state_entry.place(x = 10, y = 10, width = 280, height = 20)
state_entry["state"] = "readonly"

# def button
digits_data = [str(i) for i in range(0,10)] + [".","√"]
symbol_data = ("+","-","×","÷","^x","//")
index = 0

# 数字按钮
for dighBtnR in range(4):
    for dighBtnC in range(3):
        dighBtn = digits_data[index]
        index = index + 1
        digits_button = tk.Button(win, text = dighBtn, command = lambda x = dighBtn : clickButton(x))
        digits_button.place(x = 20 + dighBtnC*70, y = 80 + dighBtnR*50, width = 50, height = 25)
print(f"=== {var_state.get()}")
# 符号按钮
for index, symbol in enumerate(symbol_data):
    symbol_button = tk.Button(win, text = symbol, command = lambda x = symbol : clickButton(x))
    symbol_button.place(x = 230, y = 80 + index * 30, width = 50, height = 25)

# Clear Back = 按钮
clear_button = tk.Button(win, text = "CE", command = lambda : clickButton("C"))
clear_button.place(x = 20, y = 40, width = 70, height = 25)
backe_button = tk.Button(win, text = "BACK", command = lambda : clickButton("B"))
backe_button.place(x = 115, y = 40, width = 70, height = 25)
resul_button = tk.Button(win, text = "=", command = lambda : clickButton("="))
resul_button.place(x = 210, y = 40, width = 70, height = 25)

def clickButton(btn):
    state = var_state.get()
    if state.startswith("."):
        state = "0" + state
    if btn in "0123456789":
        state += btn
    elif btn == ".":
        symbols = re.split(r"\+|-|\*|%|/]", state)[-1]
        if "." in symbols:
            tk.messagebox.showerror(title="Error",message="There are too many decimal points")
            return
        else:
            state += btn
    elif btn == "B":
        state = state[:-1]
    elif btn == "C":
        state = ""
    elif btn == "=":
        try:
            expression = state
            if "^x" in state:
                state = state.replace("^x","**")
            if "×" in state:
                state = state.replace("×","*")
            if "÷" in state:
                state = state.replace("÷","/")
            state = str(eval(state))
            var_state.set(f"{expression} = {state}")
            return
        except:
            tk.messagebox.showerror(title="Error",message="Expression error!")
            return
    elif btn in symbol_data:
        if state.endswith(symbol_data):
            tk.messagebox.showerror(title="Error",message="Continuous operators are not allowed")
            return
        state = state + btn
    elif btn == "√":
        n = state.split(".")
        if all(map(lambda x : x.isdigit(),n)):
            state = math.sqrt(eval(state))
        else:
            tk.messagebox.showerror(title="Error",message="Expression error")
            return
    var_state.set(state)




if __name__ == '__main__':
    win.mainloop()