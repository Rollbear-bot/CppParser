# -*- coding: utf-8 -*-
# @Time: 2020/9/9 15:15
# @Author: Rollbear
# @Filename: result.py


class Result:
    """parsing result obj"""
    def __init__(self, parser_obj):
        self.lines = parser_obj.lines
        self.raw_lines = parser_obj.raw_lines

    def save(self, output_path):
        # with open(output_path, "w", encoding="utf8") as wf:
        #     wf.writelines(self.lines)
        pass

    def get_concise(self):
        return Concise(self)

    def get_text(self):
        return self.lines


class Concise(Result):
    """the most concise cpp source file"""
    def __init__(self, parser_obj):
        super().__init__(parser_obj)
        # todo::去除注释，以及任何不必要的空白字符
