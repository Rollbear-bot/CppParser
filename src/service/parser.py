# -*- coding: utf-8 -*-
# @Time: 2020/9/9 15:13
# @Author: Rollbear
# @Filename: parser.py

from entity.result import Result


class Parser:
    """parser obj"""
    def __init__(self, path):
        self.path = path
        self.raw_lines = None
        self.lines = None

        # read the text
        with open(path, "r", encoding="utf8") as rf:
            self.raw_lines = rf.readlines()

        # skip the blank
        self.lines = [str(line).strip().rstrip() for line in self.raw_lines]

    def get_result(self):
        return Result(self)
