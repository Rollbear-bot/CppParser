# -*- coding: utf-8 -*-
# @Time: 2020/9/9 15:13
# @Author: Rollbear
# @Filename: parser.py

from entity.result import Result


keywords = ["asm", "else", "new", "this", "auto", "enum",
            "operator", "throw", "bool", "explicit", "private",
            "true", "break", "export", "protected", "try",
            "case", "extern", "public", "typedef", "catch",
            "false", "register", "typeid", "char", "float",
            "reinterpret_cast", "typename", "class", "for",
            "return", "union", "const", "friend", "short",
            "unsigned", "const_cast", "goto", "signed",
            "using", "continue", "if", "sizeof", "virtual",
            "default", "inline", "static", "void", "delete",
            "int", "static_cast", "volatile", "do", "long",
            "struct", "wchar_t", "double", "mutable", "switch",
            "while", "dynamic_cast", "template"]

operators = ["+", "-", "*", "/", "%", "++", "--", "==", "!=",
             "<", ">", "<=", ">=", "&&", "||", "!", "&", "|",
             "^", "~", "<<", ">>", "=", "+=", "-=", "*=", "/=",
             "%=", "<<=", ">>=", "&=", "^=", "|=", "?"]

other_symbols = [".", "{", "}", "[", "]", ";"]


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

        # self.run()
        self.result = self.run_version3()

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

    def run_version2(self):
        """有穷自动机的概念，使用状态转换思想"""
        for char in self.raw_str:
            # la(char)
            pass
        cases = {

        }

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
                # todo::其他情况
                buffer = ""
                for char in row:
                    if ord("Z") >= ord(char) >= ord("a"):  # 判断英文字母
                        buffer += char
                    elif buffer in keywords:
                        result_message += f"(行{row_id+1}, 字符{row.index(char)+1}, 关键字)"

            if result_message != "":
                result.append(result_message)

        return result

    def build_parse_tree(self):
        pass
