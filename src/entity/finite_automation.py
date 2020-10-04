# -*- coding: utf-8 -*-
# @Time: 2020/10/3 15:59
# @Author: Rollbear
# @Filename: finite_automation.py

from resource.symbols import operators, other_symbols, keywords

LABELS = []
BUFFER = ""


def finite_automation_handler(raw_string):
    """有穷自动机"""
    global BUFFER, LABELS
    BUFFER = ""
    LABELS = []
    case0_root(raw_string, 0)  # 跳转到状态0
    return LABELS  # 改行的词法分析结果返回调用处


def is_letter(char):
    return ord("z") >= ord(char) >= ord("A")


def is_digit(char):
    return ord("9") >= ord(char) >= ord("0")


def case0_root(raw_string, str_index):
    """状态0：关键字"""
    global BUFFER, LABELS
    cur_char = raw_string[str_index]

    if is_letter(cur_char):  # 判断英文字母
        BUFFER += cur_char
        case0_root(raw_string, str_index + 1)  # 字符指针前进一个字符，在状态0循环，直到不是英文字母
        return

    if cur_char == '"':
        # 识别为字符串
        BUFFER += cur_char
        case3_string(raw_string, str_index + 1)
        return

    if is_digit(cur_char):
        # 识别为数值
        BUFFER += cur_char
        if str_index + 1 == len(raw_string):
            LABELS.append((BUFFER, "数值"))
            return
        case2_digit(raw_string, str_index + 1)  # 跳转到状态2：数值
        return

    if cur_char in other_symbols or cur_char in operators or \
            cur_char == " " or cur_char == "\t":
        # 识别为特殊符号
        if BUFFER != "":
            if BUFFER in keywords:
                # 识别为关键字
                LABELS.append((BUFFER, "关键字"))
                BUFFER = ""  # 清空buffer
            else:
                # 识别为标识符
                LABELS.append((BUFFER, "标识符"))
                BUFFER = ""
        if cur_char in other_symbols:
            LABELS.append((cur_char, "特殊符号"))
        elif cur_char in operators:
            # 跳转到状态4，处理操作符和注释
            BUFFER += cur_char
            if str_index + 1 == len(raw_string):
                LABELS.append((BUFFER, "操作符"))
                return
            case4_operator_and_comment(raw_string, str_index+1)
            return
        if str_index + 1 == len(raw_string):
            return
        case0_root(raw_string, str_index + 1)
        return


def case1_identifier(raw_string, str_index):
    """状态1：标识符"""
    global BUFFER, LABELS
    cur_char = raw_string[str_index]
    if is_digit(cur_char) or cur_char == "_" or is_letter(cur_char):
        BUFFER += cur_char
        if str_index + 1 == len(raw_string):
            LABELS.append((BUFFER, "标识符"))
            return
        case1_identifier(raw_string, str_index + 1)
        return
    else:
        LABELS.append((BUFFER, "标识符"))
        case0_root(raw_string, str_index)  # 字符指针不前进，跳转回状态0
        return


def case2_digit(raw_string, str_index):
    """状态2：数值"""
    global BUFFER, LABELS
    cur_char = raw_string[str_index]
    if is_digit(cur_char):
        BUFFER += cur_char
        if str_index + 1 == len(raw_string):
            LABELS.append((BUFFER, "数值"))
            return
        case2_digit(raw_string, str_index + 1)  # 当前字符仍是数值，则指针前进，返回状态2
        return
    else:
        LABELS.append((BUFFER, "数值"))
        BUFFER = ""  # 清空buffer
        case0_root(raw_string, str_index)  # 指针不前进，返回状态1
        return


def case3_string(raw_string, str_index):
    """状态3：字符串"""
    global BUFFER, LABELS
    cur_char = raw_string[str_index]
    if cur_char == '"' and BUFFER[-1] != "\\":
        # 识别到第二个引号且不是转义时，退出状态3，返回状态0
        BUFFER += cur_char
        LABELS.append((BUFFER, "字符串"))
        BUFFER = ""  # 清空buffer
        if str_index + 1 == len(raw_string):
            return
        case0_root(raw_string, str_index + 1)  # 字符指针前进，返回状态0
        return
    else:
        # 否则继续填充字符串，在状态3中循环
        BUFFER += cur_char
        if str_index + 1 == len(raw_string):
            LABELS.append((BUFFER, "非法字符"))
            return
        case3_string(raw_string, str_index + 1)
        return


def case4_operator_and_comment(raw_string, str_index):
    """状态4：操作符与注释"""
    global BUFFER, LABELS
    cur_char = raw_string[str_index]

    if BUFFER + cur_char in operators:
        LABELS.append((BUFFER + cur_char, "操作符"))
        BUFFER = ""  # 清空buffer
        case0_root(raw_string, str_index+1)
        return
    elif BUFFER + cur_char == "//":
        # 单行注释，本行结束，解析退出
        LABELS.append((raw_string[raw_string.index(BUFFER):], "注释"))
        return
    else:
        LABELS.append((BUFFER, "操作符"))
        BUFFER = ""  # 清空buffer
        case0_root(raw_string, str_index)  # 字符指针不前进，跳转回状态0
        return
