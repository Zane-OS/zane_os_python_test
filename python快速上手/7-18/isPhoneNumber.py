#! python3 /user/bin/env python3

"""
def is_phone_number(test_str):
    if len(test_str) != 12:
        return False
    for i in range(0, 3):
        if not test_str[i].isdecimal():
            return False
    if test_str[3] != '-':
        return False
    for i in range(4, 7):
        if not test_str[i].isdecimal():
            return False
    if test_str[7] != '-':
        return False
    for i in range(8, 12):
        if not test_str[i].isdecimal():
            return False
    return True


print('055-824-5515 is a phone number:')
print(is_phone_number('055-824-5515'))


message = 'Call me at 055-824-5515 tomorrow. 055-824-5515 is my phone number.'
for i in range(len(message)):
    chunk = message[i: i + 12]
    if is_phone_number(chunk):
        print('phone number found: ' + chunk)
"""
import re

phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_number_regex.search('Call me at 055-824-5515 tomorrow. 055-824-5515 is my phone number.')
print('phone number found: ' + mo.group())
# 正则匹配电话号码

# 分离区号的操作
# 正则添加（）将会对正则表达式分组，
# 通过对group传递参数0/[不传]，返回整体匹配结果
# 传递1～... 获取对应分组结果
regex1 = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mo1 = regex1.search('Call me at 055-824-5515 tomorrow. 055-824-5515 is my phone number.')
print('phone number found: ' + mo1.group(0) + '\n' + mo1.group(1) + '\n' + mo1.group(2) + '\n' + mo1.group(3))
area_num, mid_num, last_num = mo1.groups()
# groups()不包含整体匹配结果
print('phone num: '+'\n'+'area_num: '+area_num+'\n'+'mid_num: '+mid_num+'\n'+'last_num: '+last_num)

# 正则表达式匹配复习
# 1、使用 import re 导入正则表达式模块
# 2、使用re.compile()函数创建一个Regex对象（记得使用原始字符串）
# 3、向Regex对象的search()方法传递想要查询的字符串，返回一个Match对象
# 4、调用Match的group()/groups()方法，返回实际匹配文本的字符串
# 5、通过对group传递参数0/[不传]，返回整体匹配结果，传递1～... 获取对应分组结果
# 6、groups()返回匹配到的分组
