# -*- coding: utf-8 -*-
# @Time: 2020/10/3 10:37
# @Author: Rollbear
# @Filename: main_gui.py

import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from src.entity.parser import Parser

# 根面板
root = Tk()  # 创建窗口对象的背景色
root.geometry("600x400")

# 初始化文本
CPP_PATH = ""
file_path_str_obj = StringVar()
file_path_str_obj.set("当前选择的文件：\nnone")

# 初始化组件
label_file_path = Label(root, textvariable=file_path_str_obj)

# 创建滚动条
scroll = tkinter.Scrollbar()
# 创建展示解析结果的文本框
text = tkinter.Text(root)


def get_file_path():
    global CPP_PATH
    CPP_PATH = filedialog.askopenfilename()
    while not str(CPP_PATH).endswith('.cpp'):
        messagebox.askokcancel("确认",
                               f"{CPP_PATH}不是一个cpp文件，请重新选择")
        CPP_PATH = filedialog.askopenfilename()

    # 动态更新面板的文本
    file_path_str_obj.set("当前选择的文件：\n" + CPP_PATH)


def run():
    """链接"""
    if not file_path_str_obj.get().endswith(".cpp"):
        messagebox.askokcancel("确认",
                               f"你还没有选择cpp文件")
    else:
        res_text = Parser(path=CPP_PATH).get_result().get_result_text()
        # 清空文本框并刷新
        text.delete(0.0, END)
        text.insert('insert', res_text)
        pass


if __name__ == '__main__':
    label_file_path.pack()

    # 获取cpp文件路径的按钮
    button_get_file_path = Button(root, command=get_file_path, text="选择文件")
    button_get_file_path.pack()

    # 开始解析的按钮
    button_run = Button(root, command=run, text="开始解析")
    button_run.pack()

    # 将滚动条填充
    scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
    text.pack()
    # 将滚动条与文本框关联
    scroll.config(command=text.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
    text.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框

    root.mainloop()
