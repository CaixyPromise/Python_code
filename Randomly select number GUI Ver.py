# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''
import os, csv, random
import tkinter as tk
import tkinter.messagebox
from tkinter import ttk


win = tk.Tk()
win.title("AIPro Random Pro+")
win.geometry("500x300")

var_radioButton = tk.StringVar(value="A")
var_resul_label = tk.StringVar()
var_filen_entry = tk.StringVar()
var_count_entry = tk.IntVar()
var_peoNu_entry = tk.IntVar()
var_Nloop_entry = tk.IntVar()

count_label = tk.Label(win, text = "参与人数:")
peoNu_label = tk.Label(win, text = "摇号人数:")
Nloop_label = tk.Label(win, text = "重复次数:")
count_entry = tk.Entry(win, textvariable = var_count_entry)
peoNu_entry = tk.Entry(win, textvariable = var_peoNu_entry)
Nloop_entry = tk.Entry(win, textvariable = var_Nloop_entry)

use_num = dict()  # 人数编号字典
final_name = list()  # 人员名单列表
data_list = list() # 保存数据列表
count_num = 0

def random_funcA(count ,peoNum):
    global count_num,result
    for i in range(1,count+1):  # 生成编号字典
        use_num[i] = 0
    data_list.clear()
    result = ""

    while True:
        count_num += 1
        data_dict = dict()
        if peoNum == len(final_name):
            break
        choice_num = random.randint(1,count)
        state_tree.insert("", "end", values=(f"第{count_num}次", choice_num))
        data_dict[f"第{count_num}次"] = choice_num
        data_list.append(data_dict)

        if str(choice_num) in final_name:
            continue
        final_name.append(str(choice_num))

    result = f" ".join(final_name)
    return f"随机结果:"+" ".join(final_name)

def random_funcB(count , peoNum , loop):
    global count_num ,result
    for i in range(1,count+1):  # 生成编号字典
        use_num[i] = 0
    data_list.clear()
    result = ""

    while True:
        count_num += 1
        data_dict = dict()
        if peoNum == len(final_name):
            break
        choice_num = random.randint(1,count)
        state_tree.insert("", "end", values=(f"第{count_num}次", choice_num))
        data_dict[f"第{count_num}次"] = choice_num
        data_list.append(data_dict)

        if use_num[choice_num] != loop:
            use_num[choice_num] += 1

        elif use_num[choice_num] == loop:
            if str(choice_num) in final_name:
                continue
            final_name.append(str(choice_num))

    result = f" ".join(final_name)
    return f"随机结果:"+" ".join(final_name)

def showing_Label():
    if var_radioButton.get() == "A":
        count_label.place(x=10, y=50)
        peoNu_label.place(x=10, y=80)
        count_entry.place(x=80, y=50, width=120)
        peoNu_entry.place(x=80, y=80, width=120)
        Nloop_label.place_forget()
        Nloop_entry.place_forget()

    elif var_radioButton.get() == "B":
        count_label.place(x=10, y=50)
        peoNu_label.place(x=10, y=80)
        Nloop_label.place(x=10, y=110)
        count_entry.place(x=80, y=50,width = 120)
        peoNu_entry.place(x=80, y=80,width = 120)
        Nloop_entry.place(x=80, y=110,width = 120)

showing_Label()

choice_radioA = tk.Radiobutton(win,text = "单次摇号模式",variable = var_radioButton ,value= "A",
                               command=showing_Label).place(x = 10,y = 20)
choice_radioB = tk.Radiobutton(win,text = "多次摇号模式",variable = var_radioButton ,value= "B",
                               command=showing_Label).place(x = 130,y = 20)
result_label = tk.Label(win,textvariable = var_resul_label).place(x = 250 ,y = 50)

def random_start():
    global count_num

    items = state_tree.get_children()
    [state_tree.delete(item) for item in items]

    if var_radioButton.get() == "A":
        if var_count_entry.get() < 1 :
            tk.messagebox.showerror(title="内容错误",message="请重新检查信息是否正确。")
        elif var_peoNu_entry.get() == 0 :
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        elif var_count_entry.get() < var_peoNu_entry.get():
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        else:
            count = var_count_entry.get()
            peoNu = var_peoNu_entry.get()
            var_resul_label.set(random_funcA(count, peoNu))
            final_name.clear()
            use_num.clear()
            count_num = 0

    if var_radioButton.get() == "B":
        if var_count_entry.get() < 1:
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        elif var_peoNu_entry.get() <= 0:
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        elif var_Nloop_entry.get() <= 0:
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        elif var_count_entry.get() < var_peoNu_entry.get():
            tk.messagebox.showerror(title="内容错误", message="请重新检查信息是否正确。")
        else:
            count = var_count_entry.get()
            peoNu = var_peoNu_entry.get()
            Nloop = var_Nloop_entry.get()
            var_resul_label.set(random_funcB(count ,peoNu ,Nloop))
            final_name.clear()
            use_num.clear()
            count_num = 0

def save_data():
    TopLevel = tk.Toplevel(win)
    TopLevel.title("请输入保存名称")
    TopLevel.geometry("300x150")
    name_label = tk.Label(TopLevel,text = "请输入保存文件的名称：")
    name_label.place(x=5,y=10)
    name_entry = tk.Entry(TopLevel,textvariable = var_filen_entry)
    name_entry.place(x=25,y=40)

    def sava_file():
        if var_filen_entry.get() == "":
            tk.messagebox.showerror(title="文件名为空",message="请重新输入文件名！")
        elif len(data_list) == 0:
            tk.messagebox.showerror(title="文件数据为空", message="摇号数据为空！")
        else:
            if var_radioButton.get() == "A":
                try:
                    fp = open(f"{var_filen_entry.get()}.csv", "a+", newline="")
                    writer = csv.writer(fp)
                    writer.writerow(["单次循环摇号模式", ""])
                    writer.writerow(["参与人数:", var_count_entry.get()])
                    writer.writerow(["摇号人数:", var_peoNu_entry.get()])
                    writer.writerow(["摇号结果:", result])
                    writer.writerow([""])
                    writer.writerow(["摇号过程如下:", ""])
                    writer.writerow(["摇号次数", "摇号结果"])
                    for i in data_list:
                        for j in i.items():
                            writer.writerow(j)
                    fp.close()
                except PermissionError:
                    tk.messagebox.showerror(title="文件正在打开中", message="文件打开中，请关闭重试！")

                get_dir = os.getcwd()
                os.startfile(f"{get_dir}")

            elif var_radioButton.get() == "B":
                try:
                    fp = open(f"{var_filen_entry.get()}.csv","a+",newline="")
                    writer = csv.writer(fp)
                    writer.writerow(["多次循环摇号模式",""])
                    writer.writerow(["参与人数:",var_count_entry.get()])
                    writer.writerow(["摇号人数:", var_peoNu_entry.get()])
                    writer.writerow(["循环次数:",var_Nloop_entry.get()])
                    writer.writerow(["摇号结果:",result])
                    writer.writerow([""])
                    writer.writerow(["摇号过程如下:",""])
                    writer.writerow(["摇号次数", "摇号结果"])
                    for i in data_list:
                        for j in i.items():
                            writer.writerow(j)
                    fp.close()
                except PermissionError:
                    tk.messagebox.showerror(title="文件正在打开中",message="文件打开中，请关闭重试！")

                get_dir = os.getcwd()
                os.startfile(f"{get_dir}")

    save_button = tk.Button(TopLevel,text = "保存文件",command = sava_file)
    save_button.place(x = 200,y=80)

start_button = tk.Button(win,text = "开始摇号",command = random_start).place(x = 250 ,y = 110)
savef_button = tk.Button(win,text = "保存数据",command = save_data).place(x = 320 ,y = 110)

def about_use():
    tk.messagebox.showinfo(title="使用说明",message="单次摇号模式：只对区域号数内的人数进行一次选择\n"
                                                "多次摇号模式：对区域号数内进行n次选择，选取最先被摇到n次的号数\n"
                                                "参与人数：参加摇号的总人数。\n摇号人数：摇号结果人数。\n循环次数：重复摇号，直到出现n次才为结果")
def about_messagebox():
    tk.messagebox.showinfo(title='关于', message='关于作者：CAIXYPROMISE')

state_cols = ("选择次数", "选择结果")

state_tree = ttk.Treeview(win, show="headings", columns=state_cols, selectmode=tk.EXTENDED)
state_tree.place(x=5, y=150, height = 20,relwidth=0.98, relheight=0.4)

for state_col in state_cols:
    state_tree.heading(state_col, text=state_col)
    state_tree.column(state_col, width=80, anchor="w")

window_Menu = tk.Menu(win)
Menu_file = tk.Menu(window_Menu, tearoff = 0)
Menu_Show = tk.Menu(window_Menu, tearoff = 0)
window_Menu.add_command(label = "使用说明",command = about_use)
window_Menu.add_command(label = "开始摇号",command = random_start)
window_Menu.add_command(label = "保存数据",command = save_data)
window_Menu.add_command(label = "关于软件",command = about_messagebox)

win.config(menu=window_Menu)
win.mainloop()