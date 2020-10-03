# -*- coding: utf-8 -*-
# @Time: 2020/9/9 14:59
# @Author: Rollbear
# @Filename: test_parser.py

import unittest

from service.parser import Parser


class TestParser(unittest.TestCase):
    """unit test of cpp parser"""
    def test_file_io(self):
        file_path = "files/test.cpp"
        res = Parser(file_path).get_result()
        # res.save("./files/lines_without_blanks.cpp")

        print(res.lines)


if __name__ == '__main__':
    unittest.main()
