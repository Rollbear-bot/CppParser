# -*- coding: utf-8 -*-
# @Time: 2020/9/9 15:13
# @Author: Rollbear
# @Filename: parser.py

from src.entity.result import Result
from src.entity.finite_automation import finite_automation_handler


class Parser:
    """parser obj"""
    def __init__(self, path):
        self.path = path
        self.raw_lines = None
        self.lines = None
        self.raw_str = None
        self.parse_tree = None  # tree structure of code
        self.result = None

        # read the text
        with open(path, "r", encoding="utf8") as rf:
            self.raw_lines = rf.readlines()
            self.raw_str = rf.read()

        # skip the blank
        self.lines = [str(line).strip().rstrip() for line in self.raw_lines]

        self.result = self.run_version3()

    def get_result(self):
        return Result(self)

    # def run(self):
    #     total = "".join(self.raw_lines)
    #     in_precompile = False
    #     in_string = False
    #     in_block = False
    #     cache = ""
    #
    #     for str_index, s in enumerate(total):
    #         if in_precompile or in_string or in_block:
    #             if in_precompile is True:
    #                 # cache += s  # append the char into cache
    #                 if s is "\n":
    #                     # test
    #                     print(f"in_precompile, {cache}, str index:", str_index)
    #                     in_precompile = False
    #
    #         else:
    #             # re-init
    #             cache = ""
    #             in_precompile = in_string = in_block = False
    #
    #             if s is "#":
    #                 in_precompile = True
    #             elif s is '"':
    #                 in_string = True
    #             elif s in "{":
    #                 in_block = True
    #
    #         cache += s

    def run_version3(self):
        result = []
        for row_id, raw_row in enumerate(self.raw_lines):
            result_message = ""
            row = raw_row.strip().rstrip()
            if row.rstrip() == "":
                result_message += f"行{row_id+1}, 空行"
            elif row.startswith("#"):
                # todo::进一步处理预处理语句
                result_message += f"行{row_id+1}, 预处理语句"
            else:
                # 其他情况
                # 交给有穷自动机处理
                res = finite_automation_handler(row)
                result_message = f"行{row_id+1}: \n"
                for syb in res:
                    result_message += f"{syb[0]}\t{syb[1]}\n"

            if result_message != "":
                result.append(result_message)

        return result
