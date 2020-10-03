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
        self.parse_tree = None  # tree structure of code

        # read the text
        with open(path, "r", encoding="utf8") as rf:
            self.raw_lines = rf.readlines()

        # skip the blank
        self.lines = [str(line).strip().rstrip() for line in self.raw_lines]

        self.run()

    def get_result(self):
        return Result(self)

    def run(self):
        total = "".join(self.raw_lines)
        in_precompile = False
        in_string = False
        in_block = False
        cache = ""

        for str_index, s in enumerate(total):
            if in_precompile or in_string or in_block:
                if in_precompile is True:
                    # cache += s  # append the char into cache
                    if s is "\n":
                        # test
                        print(f"in_precompile, {cache}, str index:", str_index)
                        in_precompile = False

            else:
                # re-init
                cache = ""
                in_precompile = in_string = in_block = False

                if s is "#":
                    in_precompile = True
                elif s is '"':
                    in_string = True
                elif s in "{":
                    in_block = True

            cache += s

    def build_parse_tree(self):
        pass
