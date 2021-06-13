# -*- coding:utf-8 -*-

'''
CODE >>> SINCE IN CAIXYPROMISE.
STRIVE FOR EXCELLENT.
CONSTANTLY STRIVING FOR SELF-IMPROVEMENT.

'''

from tkinter import *
# 导入ttk
from tkinter import ttk
# 导入filedialog
from tkinter import filedialog


class App:
    def __init__(self, master):
        self.master = master
        self.initWidgets()

    def initWidgets(self):
        # 创建7个按钮，并为之绑定事件处理方法
        ttk.Button(self.master, text='打开单个文件', command=self.open_file).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='打开多个文件', command=self.open_files).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='获取单个打开文件的文件名', command=self.open_filename).pack(side=LEFT, ipadx=5, ipady=5,
                                                                                      padx=10)
        ttk.Button(self.master, text='获取多个打开文件的文件名', command=self.open_filenames).pack(side=LEFT, ipadx=5, ipady=5,
                                                                                       padx=10)
        ttk.Button(self.master, text='获取保存文件', command=self.save_file).pack(side=LEFT, ipadx=5, ipady=5, padx=10)
        ttk.Button(self.master, text='获取保存文件的文件名', command=self.save_filename).pack(side=LEFT, ipadx=5, ipady=5,
                                                                                    padx=10)
        ttk.Button(self.master, text='打开目录', command=self.open_directory).pack(side=LEFT, ipadx=5, ipady=5, padx=10)

    def open_file(self):
        # 调用askopenfile方法获取单个打开的文件
        print(filedialog.askopenfile(title='打开单个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],  # 只处理的文件类型
                                     initialdir='d:/'))  # 初始目录

    def open_files(self):
        # 调用askopenfiles方法获取多个打开的文件
        print(filedialog.askopenfiles(title='打开多个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],  # 只处理的文件类型
                                      initialdir='d:/'))  # 初始目录

    def open_filename(self):
        # 调用askopenfilename方法获取单个文件的文件名
        print(filedialog.askopenfilename(title='打开单个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                         # 只处理的文件类型
                                         initialdir='d:/'))  # 初始目录

    def open_filenames(self):
        # 调用askopenfilenames方法获取多个文件的文件名
        print(filedialog.askopenfilenames(title='打开多个文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                          # 只处理的文件类型
                                          initialdir='d:/'))  # 初始目录

    def save_file(self):
        # 调用asksaveasfile方法保存文件
        print(filedialog.asksaveasfile(title='保存文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],  # 只处理的文件类型
                                       initialdir='d:/'))  # 初始目录

    def save_filename(self):
        # 调用asksaveasfilename方法获取保存文件的文件名
        print(filedialog.asksaveasfilename(title='保存文件', filetypes=[('文本文件', '*.txt'), ('Python源文件', '*.py')],
                                           # 只处理的文件类型
                                           initialdir='d:/'))  # 初始目录

    def open_directory(self):
        # 调用askdirectory方法打开目录
        print(filedialog.askdirectory(title='打开目录',
                                      initialdir='d:/'))  # 初始目录


root = Tk()
root.title('文件对话框测试')
App(root)
root.mainloop()


# NOT UI

# import win32ui

# dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
# dlg.SetOFNInitialDir('E:/Python')  # 设置打开文件对话框中的初始显示目录
# dlg.DoModal()
# filename = dlg.GetPathName()