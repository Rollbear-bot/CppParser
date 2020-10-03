# -*- coding: utf-8 -*-
# @Time: 2020/10/3 10:37
# @Author: Rollbear
# @Filename: main_gui.py

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

CPP_PATH = ""
TEXT = "none"

root = Tk()  # 创建窗口对象的背景色

file_path_str_obj = StringVar()
file_path_str_obj.set("当前选择的文件：\nnone")
cur_text = Label(root, textvariable=file_path_str_obj)


def get_file_path():
    global CPP_PATH
    CPP_PATH = filedialog.askopenfilename()
    while not str(CPP_PATH).endswith('.cpp'):
        messagebox.askokcancel("确认",
                               f"{CPP_PATH}不是一个cpp文件，请重新选择")
        CPP_PATH = filedialog.askopenfilename()

    # 动态更新面板的文本
    file_path_str_obj.set("当前选择的文件：\n" + CPP_PATH)


if __name__ == '__main__':
    cur_text.pack()

    # 获取cpp文件路径的按钮
    button_get_file_path = Button(root, command=get_file_path, text="选择文件")
    button_get_file_path.pack()

    root.mainloop()
