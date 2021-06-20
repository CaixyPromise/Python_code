# -*- coding:utf-8 -*-

"""
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

"""
import csv
import tkinter as tk
from tkinter import messagebox, EXTENDED
from tkinter import ttk
import pickle
import os
import threading
import win32api

users_name =""
users_password =""
homework_list = list()
savedata_dict = dict()

win = tk.Tk()
win.title("登录_Version_2.0")
win.geometry("500x300")
win.resizable(width=False, height=False)

canvas = tk.Canvas(win, height=200, width=500)
image_file = tk.PhotoImage(file="img/welcome.png")
canvas.create_image(0, 0, anchor="nw", image=image_file)
canvas.pack(side="top")


def forget_win():
    win.withdraw()


def quit_system():
    mess = tk.messagebox.askokcancel(title="是否确认退出？", message="系统即将退出，请确认题目已保存！")
    if mess:
        win.quit()

def quit_system1():
    win.quit()

# Label
tk.Label(win, text="账号：").place(x=50, y=150)
tk.Label(win, text="密码：").place(x=50, y=190)
tk.Label(win, text="请选择您的身份").place(x=50, y=120)

# Class
var_username = tk.StringVar()
var_password = tk.StringVar()
var_signName = tk.StringVar()
var_signPassword = tk.StringVar()
var_confirm = tk.StringVar()
var_radioButton = tk.StringVar(value="A")
var_radioButton_login = tk.StringVar(value="student")
var_teacher_entry = tk.StringVar()
var_family_entry = tk.StringVar()
var_question_entry = tk.StringVar()
var_answer_entry = tk.StringVar()
var_workName_entry = tk.StringVar()
var_getdatetime_entry = tk.StringVar()

# Entry

textbox_uesrname = tk.Entry(win, textvariable=var_username)
textbox_uesrname.place(x=160, y=150)
textbox_password = tk.Entry(win, textvariable=var_password, show="*")
textbox_password.place(x=160, y=190)

# Choice
# 开始登录界面
choice_student = tk.Radiobutton(win, text="学 生", variable=var_radioButton, value="A")
choice_student.place(x=150, y=120)
choice_teacher = tk.Radiobutton(win, text="老 师", variable=var_radioButton, value="B")
choice_teacher.place(x=220, y=120)
choice_family = tk.Radiobutton(win, text="家 长", variable=var_radioButton, value="C")
choice_family.place(x=290, y=120)


def user_Login(event=None):
    global users_name, users_password
    # 选择学生身份登录
    if var_radioButton.get() == "A":
        users_name = var_username.get()
        users_password = var_password.get()
        try:
            with open("data/user_data/users_students_info.pickle", "rb") as users_file:
                users_info = pickle.load(users_file)
        except FileNotFoundError:
            with open("data/user_data/users_students_info.pickle", "wb") as users_file:
                users_info = {"admin": "admin"}
                pickle.dump(users_info, users_file)
        if users_name in users_info:
            if users_password == users_info[users_name]:
                win.withdraw()
                tk.messagebox.showinfo(title="欢迎", message=f"欢迎回来,{users_name}")
                win_studentUI = tk.Toplevel(win)
                win_studentUI.geometry("550x280")
                win_studentUI.resizable(width=False, height=False)
                win_studentUI.title("学生系统")
                Hello_label = tk.Label(win_studentUI, text="算你牛——学生系统")
                Hello_label.place(x=100, y=5)
                homework_label = tk.Label(win_studentUI, text = "作业列表")
                homework_label.place(x=410,y=5)
                student_label = tk.Label(win_studentUI, text=f"你好,{users_name}:")
                student_label.place(x=20, y=35)
                up_label = tk.Label(win_studentUI, text="\t千里之行始于足下，今天也要继续加油噢！")
                up_label.place(x=20, y=70)

                state_cols = ("作业名称", "完成状态")
                state_tree = ttk.Treeview(win_studentUI, show="headings", columns=state_cols, selectmode=EXTENDED)
                state_tree.place(x=340, y=35,width =200)

                def get_data():
                    step_dir = os.listdir("data/work_data")
                    name = ""

                    for i in step_dir:
                        if users_name in i:
                            word = i.split("_")
                            for identity in word[1:]:
                                if identity ==users_name:
                                    for result in word[2:]:
                                        if result == ".csv":
                                            break
                                        name += result
                                    fp = open(f"data/work_data/{i}", "r", encoding="utf-8")
                                    data = fp.read()
                                    if "Done" in data:
                                        s = state_tree.insert("", "end", values=(name, "待批阅"))
                                        savedata_dict[s] = i
                                    elif "reading" in data:
                                        s = state_tree.insert("", "end", values=(name, "已批阅"))
                                        savedata_dict[s] = i
                                    else:
                                        s = state_tree.insert("", "end", values=(name, "未完成"))
                                        savedata_dict[s] = i
                                    fp.close()
                                name = ""

                def thread():
                    t = threading.Thread(target=get_data)
                    t.daemon = True
                    t.start()
                thread()

                for state_col in state_cols:
                    state_tree.heading(state_col, text=state_col)
                    state_tree.column(state_col, width=80, anchor="w")

                def go_information():
                    # get_dir = os.getcwd()
                    # os.startfile(f"{get_dir}/data/excute_data/{users_name}_data.csv")  # 打开文件
                    if var_family_entry.get() == "":
                        tk.messagebox.showerror("请重新输入", message="账号为空，无法查询")
                    else:
                        information_name = var_family_entry.get()
                        data_path = "data/excute_data"
                        filename = ""
                        for root_dirs, dirs, filename in os.walk(data_path):
                            pass
                        if f"{information_name}_data.dat" in filename:
                            get_dir = os.getcwd()
                            os.startfile(f"{get_dir}/data/excute_data/{information_name}_data.csv")  # 打开文件
                        else:
                            tk.messagebox.showerror(title="请重新输入", message="账号错误，请重新核对后输入!")
                def do_homework():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    set_question = list()
                    with open(f"{get_dir}/data/work_data/{get_file}","r",encoding="utf-8") as fp:
                        default = fp.read()
                        if "Done" in default:
                            tk.messagebox.showinfo(title="该作业已完成",message="该作业已经完成啦！")
                        elif "reading" in default:
                            tk.messagebox.showinfo(title="该作业已完成", message="该作业已经完成啦！")
                        else:
                            with open(f"{get_dir}/data/work_data/{get_file}","r",encoding="utf-8") as data_read:
                                fp_key = csv.reader(data_read)
                                for csv_key in fp_key:
                                    csv_reader = csv.DictReader(data_read, fieldnames=csv_key)
                                    for row in csv_reader:
                                        set_question.append(row)
                            forget_studentUI()
                            main(1,set_question,data)
                def reading_homework():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    with open(f"{get_dir}/data/work_data/{get_file}", "r", encoding="utf-8") as fp:
                        default = fp.read()
                        if "reading" in default:
                            os.startfile(f"{get_dir}/data/excute_data/{get_file}")
                def forget_studentUI():
                    win_studentUI.withdraw()
                go_challenge_button = tk.Button(win_studentUI, text="开始答题", command=lambda: [forget_win(),forget_studentUI(),main(0)])
                go_challenge_button.place(x=120, y=130)
                go_homework_button = tk.Button(win_studentUI,text = "开始作业",command = lambda :[do_homework()])
                go_homework_button.place(x=220,y=130)
                go_information_button = tk.Button(win_studentUI, text="查看成绩", command=go_information)
                go_information_button.place(x=120, y=170)
                quit_system_button = tk.Button(win_studentUI,text = "退出系统",command = quit_system1)
                quit_system_button.place(x=120,y=210)
                reading_homework_button = tk.Button(win_studentUI,text = "查看作业",command = reading_homework)
                reading_homework_button.place(x=220,y=170)
            elif users_password != users_info[users_name]:
                tk.messagebox.showerror(title="密码错误", message="密码错误，请重新输入！")
        else:
            is_sign_up = tk.messagebox.askyesno("请重新输入", "账号不存在或密码错误，是否需要注册？")
            if is_sign_up:
                user_SignUp()
    # 选择老师身份登录
    elif var_radioButton.get() == "B":
        users_name = var_username.get()
        users_password = var_password.get()
        try:
            with open("data/user_data/users_teacher_info.pickle", "rb") as users_file:
                users_info = pickle.load(users_file)
        except FileNotFoundError:
            with open("data/user_data/users_teacher_info.pickle", "wb") as users_file:
                users_info = {"admin": "admin"}
                pickle.dump(users_info, users_file)
        if users_name in users_info:
            if users_password == users_info[users_name]:
                win.withdraw()
                tk.messagebox.showinfo(title="欢迎", message="你好，" + users_name)
                win_teacherUI = tk.Toplevel(win)
                win_teacherUI.geometry("550x280")
                win_teacherUI.resizable(width=False, height=False)
                win_teacherUI.title("教师系统")
                Hello_label = tk.Label(win_teacherUI, text="算你牛——教师系统")
                Hello_label.place(x=100, y=5)
                input_label = tk.Label(win_teacherUI, text="请输入您的学生账号")
                input_label.place(x=20, y=35)
                homework_label = tk.Label(win_teacherUI, text="已布置作业列表")
                homework_label.place(x=390, y=5)
                input_entry = tk.Entry(win_teacherUI, textvariable=var_teacher_entry)
                input_entry.place(x=20, y=60)

                state_cols = ("作业名称", "完成状态")
                state_tree = ttk.Treeview(win_teacherUI, show="headings", columns=state_cols, selectmode=EXTENDED)
                state_tree.place(x=340, y=35,width =200)


                for state_col in state_cols:
                    state_tree.heading(state_col, text=state_col)
                    state_tree.column(state_col, width=80, anchor="w")

                def get_data():
                    step_dir = os.listdir("data/work_data")
                    name = ""
                    for i in step_dir:
                        if users_name in i:
                            word = i.split("_")
                            if word[1] == "t":
                                for result in word[2:]:
                                    if result == ".csv":
                                        break
                                    name += result
                                fp = open(f"data/work_data/{i}", "r", encoding="utf-8")
                                data = fp.read()

                                if "Done" in data:
                                    s = state_tree.insert("", "end", values=(name, "完成"))
                                    savedata_dict[s] = i
                                elif "reading" in data:
                                    s = state_tree.insert("", "end", values=(name, "已批阅"))
                                    savedata_dict[s] = i
                                else:
                                    s = state_tree.insert("", "end", values=(name, "未完成"))
                                    savedata_dict[s] = i

                                fp.close()
                            name = ""

                get_data()

                def restart():
                    restart_data = state_tree.get_children()
                    for restart in restart_data:
                        state_tree.delete(restart)

                def finish_work():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    with open(f"{get_dir}/data/work_data/{get_file}", "w", encoding="utf-8") as fp:
                        writer = csv.writer(fp)
                        writer.writerow(["reading"])

                def read_data():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    with open(f"{get_dir}/data/work_data/{get_file}", "r", encoding="utf-8") as fp:
                        default = fp.read()
                        if "reading" in default:
                            os.startfile(f"{get_dir}/data/excute_data/{get_file}")
                        else:
                            os.startfile(f"{get_dir}/data/work_data/{get_file}")

                def go_information():
                    if var_teacher_entry.get() == "":
                        tk.messagebox.showerror("请重新输入", message="账号为空，无法查询")
                    else:
                        information_name = var_teacher_entry.get()
                        data_path = "data/excute_data"
                        filename = ""
                        for root_dirs, dirs, filename in os.walk(data_path):
                            pass
                        if f"{information_name}_data.dat" in filename:
                            get_dir = os.getcwd()
                            os.startfile(f"{get_dir}/data/excute_data/{information_name}_data.csv")  # 打开文件
                        else:
                            tk.messagebox.showerror(title="请重新输入", message="账号错误，请重新核对后输入!")
                def forget_teacherUI():
                    win_teacherUI.withdraw()
                def update():
                    if var_teacher_entry.get() == "":
                        tk.messagebox.showerror("请重新输入", message="账号为空，无法指定学生出题")
                    else:
                        information_name = var_teacher_entry.get()
                        with open("data/user_data/users_students_info.pickle", "rb") as users_file:
                            users_info = pickle.load(users_file)
                        if f"{information_name}" in users_info:
                            forget_win()
                            forget_teacherUI()
                            update_teacherUI = tk.Toplevel(win)
                            update_teacherUI.title("布置作业")
                            update_teacherUI.geometry("700x500")

                            # 表格
                            cols = ("题目", "答案")

                            tree = ttk.Treeview(update_teacherUI, show="headings", columns=cols, selectmode=EXTENDED)
                            tree.place(x=5, y=250, relwidth=0.98, relheight=0.4)

                            state_cols = ("作业名称", "完成状态")
                            state_tree = ttk.Treeview(update_teacherUI, show="headings", columns=state_cols, selectmode=EXTENDED)
                            state_tree.place(x=475,y=10,width = 210)
                            def get_data():
                                step_dir = os.listdir("data/work_data")
                                name = ""
                                for i in step_dir:
                                    if users_name in i:
                                        word = i.split("_")
                                        if word[1] == "t":
                                            for result in word[2:]:
                                                if result == ".csv":
                                                    break
                                                name += result
                                            fp = open(f"data/work_data/{i}","r",encoding="utf-8")
                                            data = fp.read()

                                            if "Done" in data:
                                                s = state_tree.insert("", "end",values=(name, "完成"))
                                                savedata_dict[s] = i
                                            elif "reading" in data:
                                                s = state_tree.insert("","end",values = (name, "已批阅"))
                                                savedata_dict[s] = i
                                            else:
                                                s = state_tree.insert("", "end", values=(name, "未完成"))
                                                savedata_dict[s] = i

                                            fp.close()
                                        name = ""
                            get_data()
                            def restart():
                                restart_data = state_tree.get_children()
                                for restart in restart_data:
                                    state_tree.delete(restart)

                            for col in cols:
                                tree.heading(col, text=col)
                                tree.column(col, width=80, anchor="w")

                            for state_col in state_cols:
                                state_tree.heading(state_col,text=state_col)
                                state_tree.column(state_col,width=80,anchor="w")

                            num_label = tk.Label(update_teacherUI,text = f"正在给 {information_name} 出题",font =10)
                            num_label.place(x=10,y=20)

                            work_label = tk.Label(update_teacherUI,text = "作业名称:",font=10)
                            work_label.place(x=10,y=60)
                            work_entry = tk.Entry(update_teacherUI,textvariable = var_workName_entry)
                            work_entry.place(x=90,y=60)

                            que_label = tk.Label(update_teacherUI,text = "该题题目:",font =10)
                            que_label.place(x=10,y=90)
                            que_entry = tk.Entry(update_teacherUI,textvariable = var_question_entry)
                            que_entry.place(x=90,y=90)

                            ans_label = tk.Label(update_teacherUI, text="该题答案:",font =10)
                            ans_label.place(x=10, y=120)
                            ans_entry = tk.Entry(update_teacherUI, textvariable=var_answer_entry)
                            ans_entry.place(x=90, y=120)

                            def add_question(event=None):
                                if var_question_entry.get() == "" and var_answer_entry.get() == "":
                                    tk.messagebox.showerror(title="输入错误",message="题目或答案为空，请重新输入！")
                                else:
                                    if " " in var_answer_entry.get():
                                        tk.messagebox.showerror(title="输入错误", message="答案格式错误，请重新输入！")
                                    else:
                                        tree.insert("", "end", values=(var_question_entry.get(), var_answer_entry.get()))
                                        data_dict = dict()
                                        data_dict[var_question_entry.get()] = var_answer_entry.get()
                                        homework_list.append(data_dict)


                            def delete_question():
                                item = tree.focus()
                                try:
                                    tree.delete(item)
                                except:
                                    pass

                            def set_cell_value(event):
                                global cn, rn
                                for item in tree.selection():
                                    item_text = tree.item(item, "values")
                                column = tree.identify_column(event.x)  # 列
                                row = tree.identify_row(event.y)  # 行
                                try:
                                    cn = int(str(column).replace("#", ""))
                                    rn = int(str(row).replace("I", ""))
                                except:
                                    pass
                                entryedit = tk.Text(update_teacherUI, width=10 , height=1)
                                entryedit.place(x=70 + (cn - 1) * 330, y=255 + rn * 20)

                                def saveedit():
                                    tree.set(item, column=column, value=entryedit.get(0.0, "end"))
                                    entryedit.destroy()
                                    okb.destroy()

                                okb = ttk.Button(update_teacherUI, text="保存", width=4, command=saveedit)
                                okb.place(x=170 + (cn - 1) * 330, y=255 + rn * 20)

                            def create_work():
                                if f"{users_name}_t_{var_teacher_entry.get()}_{var_workName_entry.get()}_.csv" \
                                        in os.listdir("data/work_data"):
                                    tk.messagebox.showerror(title="作业名称错误",message="该作业名称已存在，请重新输入！")
                                else:
                                    fp = open(f"data/work_data/{users_name}_t_{var_teacher_entry.get()}_{var_workName_entry.get()}_.csv",
                                              "a+",encoding="utf-8", newline="")
                                    writer = csv.writer(fp)
                                    writer.writerow(["题目", "答案"])
                                    for i in homework_list:
                                        for j in i.items():
                                            writer.writerow(j)
                                    fp.close()
                                    tk.messagebox.showinfo(title="生成题目完成",message=f"题目制作完成，共出{len(homework_list)}道题"
                                                                                  f"给到学生{information_name}\n"
                                                                                  f"学生完成后将收到答题结果，感谢您为孩子的倾情付出！")
                            def read_data():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                with open(f"{get_dir}/data/work_data/{get_file}", "r", encoding="utf-8") as fp:
                                    default = fp.read()
                                    if "reading" in default:
                                        os.startfile(f"{get_dir}/data/excute_data/{get_file}")
                                    else:
                                        os.startfile(f"{get_dir}/data/work_data/{get_file}")
                            def delete_data():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                mess = tk.messagebox.askyesno(title="是否确认结束作业？",message="结束以后将会删除作业")
                                if mess:
                                    state_tree.delete(data)
                                    os.remove(f"{get_dir}/data/work_data/{get_file}")
                                    os.remove(f"{get_dir}/data/excute_data/{get_file}")

                            def finish_work():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                with open(f"{get_dir}/data/work_data/{get_file}","w",encoding="utf-8") as fp:
                                    writer = csv.writer(fp)
                                    writer.writerow(["reading"])
                            update_teacherUI.bind("<Return>",add_question)
                            add_button = tk.Button(update_teacherUI,text="添加题目",command = add_question)
                            add_button.place(x=300, y=105)
                            delete_button = tk.Button(update_teacherUI,text="删除题目",command = delete_question)
                            delete_button.place(x=370, y=105)
                            homework_button = tk.Button(update_teacherUI,text="生成作业",command = lambda :[create_work(),restart(),get_data()])
                            homework_button.place(x=300,y=145)
                            readwork_button = tk.Button(update_teacherUI,text="批阅作业",command = read_data)
                            readwork_button.place(x=370,y=145)
                            deletework_button = tk.Button(update_teacherUI,text="结束作业",command = lambda :[delete_data(),restart(),get_data()])
                            deletework_button.place(x=370,y=185)
                            finishwork_button = tk.Button(update_teacherUI,text="完成作业",command = lambda :[finish_work(),restart(),get_data()])
                            finishwork_button.place(x=300,y=185)
                            quit_button = tk.Button(update_teacherUI,text="退出系统",command=quit_system)
                            quit_button.place(x=230,y=185)

                            tree.bind("<Double-1>", set_cell_value)

                        else:
                            tk.messagebox.showerror(title="请重新输入", message="账号错误，请重新核对后输入!")

                go_information_button = tk.Button(win_teacherUI, text="查看成绩", command=go_information)
                go_information_button.place(x=170, y=130)
                go_challenge_button = tk.Button(win_teacherUI, text="答题系统", command=lambda: [forget_win(),forget_teacherUI(),main(0)])
                go_challenge_button.place(x=70, y=130)
                go_updateQuestion_button = tk.Button(win_teacherUI,text="作业系统",command =update)
                go_updateQuestion_button.place(x=270, y=130)
                quit_system_button = tk.Button(win_teacherUI, text="退出系统", command=quit_system1)
                quit_system_button.place(x=70, y=170)
                read_homework_button = tk.Button(win_teacherUI,text="批阅作业",command = read_data)
                read_homework_button.place(x=170,y=170)
                finish_homework_button = tk.Button(win_teacherUI,text = "完成作业",command = lambda :[finish_work(),restart(),get_data()])
                finish_homework_button.place(x=270,y=170)
            elif users_password != users_info[users_name]:
                tk.messagebox.showerror(title="密码错误", message="密码错误，请重新输入！")
        else:
            is_sign_up = tk.messagebox.askyesno("请重新输入", "账号不存在或密码错误，是否需要注册？")
            if is_sign_up:
                user_SignUp()

    # 选择家长身份登录
    elif var_radioButton.get() == "C":
        users_name = var_username.get()
        users_password = var_password.get()
        try:
            with open("data/user_data/users_family_info.pickle", "rb") as users_file:
                users_info = pickle.load(users_file)
        except FileNotFoundError:
            with open("data/user_data/users_family_info.pickle", "wb") as users_file:
                users_info = {"admin": "admin"}
                pickle.dump(users_info, users_file)
        if users_name in users_info:
            if users_password == users_info[users_name]:
                win.withdraw()
                tk.messagebox.showinfo(title="欢迎", message="你好，" + users_name)
                win_familyUI = tk.Toplevel(win)
                win_familyUI.geometry("550x280")
                win_familyUI.resizable(width=False, height=False)
                win_familyUI.title("家长系统")
                Hello_label = tk.Label(win_familyUI, text="算你牛——家长系统")
                Hello_label.place(x=100, y=5)
                input_label = tk.Label(win_familyUI, text="请输入您的孩子账号")
                input_label.place(x=20, y=35)
                homework_label = tk.Label(win_familyUI, text="已布置作业列表")
                homework_label.place(x=390, y=5)
                input_entry = tk.Entry(win_familyUI, textvariable=var_family_entry)
                input_entry.place(x=20, y=60)

                state_cols = ("作业名称", "完成状态")
                state_tree = ttk.Treeview(win_familyUI, show="headings", columns=state_cols, selectmode=EXTENDED)
                state_tree.place(x=340, y=35, width=200)

                for state_col in state_cols:
                    state_tree.heading(state_col, text=state_col)
                    state_tree.column(state_col, width=80, anchor="w")
                def get_data():
                    step_dir = os.listdir("data/work_data")
                    name = ""
                    for i in step_dir:
                        if users_name in i:
                            word = i.split("_")
                            if word[1] == "f":
                                for result in word[2:]:
                                    if result == ".csv":
                                        break
                                    name += result
                                fp = open(f"data/work_data/{i}", "r", encoding="utf-8")
                                data = fp.read()

                                if "Done" in data:
                                    s = state_tree.insert("", "end", values=(name, "完成"))
                                    savedata_dict[s] = i
                                elif "reading" in data:
                                    s = state_tree.insert("", "end", values=(name, "已批阅"))
                                    savedata_dict[s] = i
                                else:
                                    s = state_tree.insert("", "end", values=(name, "未完成"))
                                    savedata_dict[s] = i

                                fp.close()
                            name = ""
                get_data()

                def read_data():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    with open(f"{get_dir}/data/work_data/{get_file}", "r", encoding="utf-8") as fp:
                        default = fp.read()
                        if "reading" in default:
                            os.startfile(f"{get_dir}/data/excute_data/{get_file}")
                        else:
                            os.startfile(f"{get_dir}/data/work_data/{get_file}")
                def restart():
                    restart_data = state_tree.get_children()
                    for restart in restart_data:
                        state_tree.delete(restart)
                def finish_work():
                    data = state_tree.focus()
                    get_file = savedata_dict[data]
                    get_dir = os.getcwd()
                    with open(f"{get_dir}/data/work_data/{get_file}", "w", encoding="utf-8") as fp:
                        writer = csv.writer(fp)
                        writer.writerow(["reading"])
                def go_information():
                    if var_family_entry.get() == "":
                        tk.messagebox.showerror("请重新输入", message="账号为空，无法查询")
                    else:
                        information_name = var_family_entry.get()
                        data_path = "data/excute_data"
                        filename = ""
                        for root_dirs, dirs, filename in os.walk(data_path):
                            pass
                        if f"{information_name}_data.dat" in filename:
                            get_dir = os.getcwd()
                            os.startfile(f"{get_dir}/data/excute_data/{information_name}_data.csv")  # 打开文件
                        else:
                            tk.messagebox.showerror(title="请重新输入", message="账号错误，请重新核对后输入!")
                def forget_familyUI():
                    win_familyUI.withdraw()

                def update():
                    if var_family_entry.get() == "":
                        tk.messagebox.showerror("请重新输入", message="账号为空，无法指定出题")
                    else:
                        information_name = var_family_entry.get()
                        with open("data/user_data/users_students_info.pickle", "rb") as users_file:
                            users_info = pickle.load(users_file)
                        if f"{information_name}" in users_info:
                            forget_win()
                            forget_familyUI()
                            update_familyUI = tk.Toplevel(win)
                            update_familyUI.title("布置作业")
                            update_familyUI.geometry("700x500")

                            # 表格
                            cols = ("题目", "答案")

                            tree = ttk.Treeview(update_familyUI, show="headings", columns=cols, selectmode=EXTENDED)
                            tree.place(x=5, y=250, relwidth=0.98, relheight=0.4)

                            state_cols = ("作业名称", "完成状态")
                            state_tree = ttk.Treeview(update_familyUI, show="headings", columns=state_cols,
                                                      selectmode=EXTENDED)
                            state_tree.place(x=475, y=10, width=210)

                            def get_data():
                                step_dir = os.listdir("data/work_data")
                                name = ""
                                for i in step_dir:
                                    if users_name in i:
                                        word = i.split("_")

                                        for result in word[2:]:
                                            if result == ".csv":
                                                break
                                            if word[1] == "t":
                                                name += "老师布置的"
                                            name += result
                                        fp = open(f"data/work_data/{i}", "r", encoding="utf-8")
                                        data = fp.read()

                                        if "Done" in data:
                                            s = state_tree.insert("", "end", values=(name, "完成"))
                                            savedata_dict[s] = i
                                        elif "reading" in data:
                                            s = state_tree.insert("", "end", values=(name, "已批阅"))
                                            savedata_dict[s] = i
                                        else:
                                            s = state_tree.insert("", "end", values=(name, "未完成"))
                                            savedata_dict[s] = i

                                        fp.close()
                                    name = ""
                            get_data()
                            def restart():
                                restart_data = state_tree.get_children()
                                for restart in restart_data:
                                    state_tree.delete(restart)

                            for col in cols:
                                tree.heading(col, text=col)
                                tree.column(col, width=80, anchor="w")

                            for state_col in state_cols:
                                state_tree.heading(state_col, text=state_col)
                                state_tree.column(state_col, width=80, anchor="w")

                            num_label = tk.Label(update_familyUI, text=f"正在给 {information_name} 出题", font=10)
                            num_label.place(x=10, y=20)

                            work_label = tk.Label(update_familyUI, text="作业名称:", font=10)
                            work_label.place(x=10, y=60)
                            work_entry = tk.Entry(update_familyUI, textvariable=var_workName_entry)
                            work_entry.place(x=90, y=60)

                            que_label = tk.Label(update_familyUI, text="该题题目:", font=10)
                            que_label.place(x=10, y=90)
                            que_entry = tk.Entry(update_familyUI, textvariable=var_question_entry)
                            que_entry.place(x=90, y=90)

                            ans_label = tk.Label(update_familyUI, text="该题答案:", font=10)
                            ans_label.place(x=10, y=120)
                            ans_entry = tk.Entry(update_familyUI, textvariable=var_answer_entry)
                            ans_entry.place(x=90, y=120)

                            def add_question(event=None):
                                if var_question_entry.get() == "" and var_answer_entry.get() == "":
                                    tk.messagebox.showerror(title="输入错误", message="题目或答案为空，请重新输入！")
                                else:
                                    if " " in var_answer_entry.get():
                                        tk.messagebox.showerror(title="输入错误", message="答案格式错误，请重新输入！")
                                    else:
                                        tree.insert("", "end",
                                                    values=(var_question_entry.get(), var_answer_entry.get()))
                                        data_dict = dict()
                                        data_dict[var_question_entry.get()] = var_answer_entry.get()
                                        homework_list.append(data_dict)

                            def delete_question():
                                item = tree.focus()
                                try:
                                    tree.delete(item)
                                except:
                                    pass

                            def set_cell_value(event):
                                global cn, rn
                                for item in tree.selection():
                                    item_text = tree.item(item, "values")
                                column = tree.identify_column(event.x)  # 列
                                row = tree.identify_row(event.y)  # 行
                                try:
                                    cn = int(str(column).replace("#", ""))
                                    rn = int(str(row).replace("I", ""))
                                except:
                                    pass
                                entryedit = tk.Text(update_familyUI, width=10, height=1)
                                entryedit.place(x=70 + (cn - 1) * 330, y=255 + rn * 20)

                                def saveedit():
                                    tree.set(item, column=column, value=entryedit.get(0.0, "end"))
                                    entryedit.destroy()
                                    okb.destroy()

                                okb = ttk.Button(update_familyUI, text="保存", width=4, command=saveedit)
                                okb.place(x=170 + (cn - 1) * 330, y=255 + rn * 20)

                            def create_work():
                                if f"{users_name}_f_{var_family_entry.get()}_{var_workName_entry.get()}_.csv" \
                                        in os.listdir("data/work_data"):
                                    tk.messagebox.showerror(title="作业名称错误", message="该作业名称已存在，请重新输入！")
                                else:
                                    fp = open(
                                        f"data/work_data/{users_name}_f_{var_family_entry.get()}_{var_workName_entry.get()}_.csv",
                                        "a+", encoding="utf-8", newline="")
                                    writer = csv.writer(fp)
                                    writer.writerow(["题目", "答案"])
                                    for i in homework_list:
                                        for j in i.items():
                                            writer.writerow(j)
                                    fp.close()
                                    tk.messagebox.showinfo(title="生成题目完成", message=f"题目制作完成，共出{len(homework_list)}道题"
                                                                                   f"给到孩子{information_name}\n"
                                                                                   f"孩子完成后将收到答题结果，感谢您为孩子的倾情付出！")

                            def read_data():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                with open(f"{get_dir}/data/work_data/{get_file}", "r", encoding="utf-8") as fp:
                                    default = fp.read()
                                    if "reading" in default:
                                        os.startfile(f"{get_dir}/data/excute_data/{get_file}")
                                    else:
                                        os.startfile(f"{get_dir}/data/work_data/{get_file}")

                            def delete_data():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                mess = tk.messagebox.askyesno(title="是否确认结束作业？", message="结束以后将会删除作业")
                                if mess:
                                    state_tree.delete(data)
                                    os.remove(f"{get_dir}/data/work_data/{get_file}")
                                    os.remove(f"{get_dir}/data/excute_data/{get_file}")
                            def finish_work():
                                data = state_tree.focus()
                                get_file = savedata_dict[data]
                                get_dir = os.getcwd()
                                with open(f"{get_dir}/data/work_data/{get_file}", "w", encoding="utf-8") as fp:
                                    writer = csv.writer(fp)
                                    writer.writerow(["reading"])
                            update_familyUI.bind("<Return>", add_question)
                            add_button = tk.Button(update_familyUI, text="添加题目", command=add_question)
                            add_button.place(x=300, y=105)
                            delete_button = tk.Button(update_familyUI, text="删除题目", command=delete_question)
                            delete_button.place(x=370, y=105)
                            homework_button = tk.Button(update_familyUI, text="生成作业",
                                                        command=lambda: [create_work(), restart(), get_data()])
                            homework_button.place(x=300, y=145)
                            readwork_button = tk.Button(update_familyUI, text="批阅作业", command=read_data)
                            readwork_button.place(x=370, y=145)
                            deletework_button = tk.Button(update_familyUI, text="结束作业",
                                                          command=lambda: [delete_data(), restart(), get_data()])
                            deletework_button.place(x=370, y=185)
                            finishwork_button = tk.Button(update_familyUI, text="完成作业",
                                                          command=lambda: [finish_work(), restart(), get_data()])
                            finishwork_button.place(x=300, y=185)
                            quit_button = tk.Button(update_familyUI, text="退出系统", command=quit_system)
                            quit_button.place(x=230, y=185)

                            tree.bind("<Double-1>", set_cell_value)
                go_information_button = tk.Button(win_familyUI, text="查看成绩", command=go_information)
                go_information_button.place(x=170, y=130)
                go_challenge_button = tk.Button(win_familyUI, text="答题系统", command=lambda: [forget_win(),forget_familyUI(),main(0)])
                go_challenge_button.place(x=70, y=130)
                go_updateQuestion_button = tk.Button(win_familyUI, text="作业系统", command=update)
                go_updateQuestion_button.place(x=270, y=130)
                quit_system_button = tk.Button(win_familyUI, text="退出系统", command=quit_system1)
                quit_system_button.place(x=70, y=170)
                read_homework_button = tk.Button(win_familyUI, text="批阅作业", command=read_data)
                read_homework_button.place(x=170, y=170)
                finish_homework_button = tk.Button(win_familyUI, text="完成作业",
                                                   command=lambda: [finish_work(), restart(), get_data()])
                finish_homework_button.place(x=270, y=170)
            elif users_password != users_info[users_name]:
                tk.messagebox.showerror(title="密码错误", message="密码错误，请重新输入！")
        else:

            is_sign_up = tk.messagebox.askyesno("请重新输入", "账号不存在或密码错误，是否需要注册？")
            if is_sign_up:
                user_SignUp()


def user_SignUp():
    def sign_in():
        # 选择学生身份注册
        if var_radioButton_login.get() == "student":
            sign_Name = textbox_signName.get()
            sign_Password = textbox_signPassword.get()
            sign_confirm_Password = textbox_confirm_signPassword.get()
            with open("data/user_data/users_students_info.pickle", "rb") as users_file:
                loading_user_info = pickle.load(users_file)

            if sign_Password != sign_confirm_Password:
                tk.messagebox.showerror("请重新输入", message="两次密码输入不一致")
            elif sign_Name in loading_user_info:
                tk.messagebox.showerror("请重新输入", message="该用户已注册，请重新输入！")
            elif sign_Name == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            elif sign_Password == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            else:
                loading_user_info[sign_Name] = sign_Password
                with open("data/user_data/users_students_info.pickle", "wb") as users_file:
                    pickle.dump(loading_user_info, users_file)
                tk.messagebox.showinfo("注册成功", message="注册成功，欢迎回来！")
                win_signUp.destroy()

        # 选择老师身份注册
        elif var_radioButton_login.get() == "teacher":
            sign_Name = textbox_signName.get()
            sign_Password = textbox_signPassword.get()
            sign_confirm_Password = textbox_confirm_signPassword.get()
            with open("data/user_data/users_teacher_info.pickle", "rb") as users_file:
                loading_user_info = pickle.load(users_file)

            if sign_Password != sign_confirm_Password:
                tk.messagebox.showerror("请重新输入", message="两次密码输入不一致")
            elif sign_Name in loading_user_info:
                tk.messagebox.showerror("请重新输入", message="该用户已注册，请重新输入！")
            elif sign_Name == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            elif sign_Password == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            else:
                loading_user_info[sign_Name] = sign_Password
                with open("data/user_data/users_teacher_info.pickle", "wb") as users_file:
                    pickle.dump(loading_user_info, users_file)
                tk.messagebox.showinfo("注册成功", message="注册成功，欢迎回来！")
                win_signUp.destroy()

        # 选择家长身份注册
        elif var_radioButton_login.get() == "family":
            sign_Name = textbox_signName.get()
            sign_Password = textbox_signPassword.get()
            sign_confirm_Password = textbox_confirm_signPassword.get()
            with open("data/user_data/users_family_info.pickle", "rb") as users_file:
                loading_user_info = pickle.load(users_file)

            if sign_Password != sign_confirm_Password:
                tk.messagebox.showerror("请重新输入", message="两次密码输入不一致")
            elif sign_Name in loading_user_info:
                tk.messagebox.showerror("请重新输入", message="该用户已注册，请重新输入！")
            elif sign_Name == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            elif sign_Password == "":
                tk.messagebox.showerror("请重新输入", message="账号或密码为空，请重新输入")
            else:
                loading_user_info[sign_Name] = sign_Password
                with open("data/user_data/users_family_info.pickle", "wb") as users_file:
                    pickle.dump(loading_user_info, users_file)
                tk.messagebox.showinfo("注册成功", message="注册成功，欢迎回来！")
                win_signUp.destroy()

    win_signUp = tk.Toplevel(win)
    win_signUp.geometry("350x200")
    win_signUp.title("注册")
    win_signUp.resizable(width=False, height=False)

    choice_status = tk.Label(win_signUp, text="请选择您的身份：")
    choice_status.place(x=10, y=5)
    login_student_button = tk.Radiobutton(win_signUp, text="学 生", variable=var_radioButton_login, value="student")
    login_student_button.place(x=150, y=5)
    login_teacher_button = tk.Radiobutton(win_signUp, text="老 师", variable=var_radioButton_login, value="teacher")
    login_teacher_button.place(x=210, y=5)
    login_family_button = tk.Radiobutton(win_signUp, text="家 长", variable=var_radioButton_login, value="family")
    login_family_button.place(x=270, y=5)

    login_usename = tk.Label(win_signUp, text="账号：")
    login_usename.place(x=10, y=40)
    textbox_signName = tk.Entry(win_signUp, textvariable=var_signName)
    textbox_signName.place(x=150, y=40)

    login_password = tk.Label(win_signUp, text="密码：")
    login_password.place(x=10, y=80)
    textbox_signPassword = tk.Entry(win_signUp, textvariable=var_signPassword, show="*")
    textbox_signPassword.place(x=150, y=80)

    login_confirpassword = tk.Label(win_signUp, text="再次输入您的密码：")
    login_confirpassword.place(x=10, y=120)
    textbox_confirm_signPassword = tk.Entry(win_signUp, textvariable=var_confirm, show="*")
    textbox_confirm_signPassword.place(x=150, y=120)

    button_confirm_SignUp = tk.Button(win_signUp, text="注册", command=sign_in)
    button_confirm_SignUp.place(x=150, y=150)


tk.Button(win, text="登录", command=user_Login).place(x=170, y=250)  # button_Login
tk.Button(win, text="注册", command=user_SignUp).place(x=270, y=250)  # button_SignUp
win.bind("<Return>", user_Login)

if __name__ == '__main__':
    win.mainloop()