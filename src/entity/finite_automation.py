# -*- coding: utf-8 -*-
# @Time: 2020/10/3 15:59
# @Author: Rollbear
# @Filename: finite_automation.py

LABELS = []


def fa(raw_string, str_index, cur_case=0):
    """有穷自动机"""
    {
        0: case0,
        1: case1,
        2: case2,
        3: case3
    }[cur_case](raw_string, str_index)


def case0(raw_string, str_index):
    """判断预处理、空行和函数块三种模式，并进行状态跳转"""
    cur_char = raw_string[str_index]
    if cur_char == "#":
        LABELS.append((str_index, "预处理语句起始符"))
    elif str_index+3 < len(raw_string) and cur_char == "i":
        pass


def case1(raw_string, str_index):
    pass


def case2(raw_string, str_index):
    pass


def case3(raw_string, str_index):
    pass
