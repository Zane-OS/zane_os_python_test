#! python3 /user/bin/env python3
# this project did extract the phone number and email address.

# 需求：
# 1、从剪贴板获取文本
# 2、找出文本中的电话号码和email地址
# 3、将他们粘贴到剪贴板

# 分析：
# 1、使用pyperclip模块复制粘贴字符串
# 2、创建正则表达式，分别匹配电话号码和邮箱地址
# 3、找到所有匹配的字符串
# 4、将匹配的字符串整理好，放到一个字符串中用于粘贴
# 5、如果找不到现实提示信息

import pyperclip, re

# TODO: Creat phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    \d{3}               # first 3digits
    (\s|-|\.)           # separator
    \d{4}               # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension 
    )''', re.VERBOSE)

# TODO: Creat email address regex
emailRegex = re.compile(r'''
    [a-zA-Z0-9._%+-]+   # username
    @                   # @
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    ''', re.VERBOSE)

# TODO: Find matches in clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email address found.')