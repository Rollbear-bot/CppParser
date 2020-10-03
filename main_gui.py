# -*- coding: utf-8 -*-
# @Time: 2020/10/3 10:37
# @Author: Rollbear
# @Filename: main_gui.py

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

from entity.parser import Parser

# 根面板
root = Tk()  # 创建窗口对象的背景色

# 初始化文本
CPP_PATH = ""
file_path_str_obj = StringVar()
file_path_str_obj.set("当前选择的文件：\nnone")
result_str_obj = StringVar()
result_str_obj.set("解析结果：\nnone")

# 初始化组件
label_file_path = Label(root, textvariable=file_path_str_obj)
text_result = Label(root, textvariable=result_str_obj)


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
        res_text = Parser(path=CPP_PATH).get_result().get_text()
        result_str_obj.set(f"解析结果：\n{res_text}")
        pass


if __name__ == '__main__':
    label_file_path.pack()

    # 获取cpp文件路径的按钮
    button_get_file_path = Button(root, command=get_file_path, text="选择文件")
    button_get_file_path.pack()

    # 开始解析的按钮
    button_run = Button(root, command=run, text="开始解析")
    button_run.pack()

    # 展示解析结果的面板
    text_result.pack()

    root.mainloop()
