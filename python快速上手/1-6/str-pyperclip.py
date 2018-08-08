#! python3 /user/bin/env python3
# import pyperclip
#
# pyperclip.copy('Hello world!')
# print(pyperclip.paste())

# Final practice

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def get_str_max_width(data_list):
    max_width = 0
    # global max_width
    for arr in data_list:
        if max_width < len(arr[0]):
            max_width = len(arr[0])
        elif max_width < len(arr[1]):
            max_width = len(arr[1])
        elif max_width < len(arr[2]):
            max_width = len(arr[2])
        elif max_width < len(arr[3]):
            max_width = len(arr[3])
    return max_width


def format_print_list(data_list):
    le = len(data_list[0])
    max_width = get_str_max_width(data_list) + 4
    for i in range(le):
        print(data_list[0][i].rjust(max_width) + data_list[1][i].center(max_width) + data_list[2][i].ljust(max_width))


format_print_list(tableData)
