# -*- coding: utf-8 -*-
# @Time: 2020/9/9 11:46
# @Author: Rollbear
# @Filename: main.py

import sys


def main(argv: list):
    """
    :param argv: [cpp file path]
    :return: none
    """
    # print the params.
    for row in argv:
        print(row)

    # the first arg received is the path of the cpp file
    file_path = argv[1]

    # parse the .cpp / .h files only
    if not (str(file_path).endswith(".h") or
            str(file_path).endswith(".cpp")):
        print("unsupported files!")
        sys.exit(0)

    with open(file_path, "r", encoding="utf8") as file_in:
        lines = file_in.readlines()

    print(lines)


if __name__ == '__main__':
    main(sys.argv)
