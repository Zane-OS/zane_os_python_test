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
# ###################################################################################

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
# 6、groups()返回匹配到的分组，以元组的形式返回

# ###################################################################################

# 用管道匹配多个分组
# | 符号称为管道，希望匹配多个表达式时使用它，如果管道对象都出现，
# 那么，第一次出现的将作为Match的返回对象。
# ⚠️ 注意️：可以使用findall()返回所有匹配到的结果，这在后边讲解

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

# mo3 = heroRegex.search('Tina Fey and Batman.')
# print(mo3.findall())

# 假如你想匹配'Batman\Batmobile\Batcopter、Batbar'，中的任意一个，
# 由于这些字符串都是'Bat'开头，所以只指定一次前缀就很方便了。

batRegex = re.compile(r'Bat(man|mobile|copter|bar)')
mo = batRegex.search('Batman lost a wheel.')
print(mo.group())
print(mo.group(1))

# 用 ？实现可选匹配，就是无论（）？括号内的字符存在不存在都匹配出来
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('the adv of Batman')
mo1 = batRegex.search('the adv of Batwoman and Batman')
print(mo.group())
print(mo1.groups())

# 用 * 匹配零次或多次，没有就匹配0次，匹配不上就返回None
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('the adv of Batman')
mo1 = batRegex.search('the adv of Batwowowowoman and Batwowowoman')
print('*'+mo.group())
print('*'+mo1.group())

# 用 + 号匹配一次或多次，没有匹配结果为None，有就匹配
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('the adv of Batman')
mo1 = batRegex.search('the adv of Batwoman and Batwowowoman')
mo2 = batRegex.search('the adv of Batwowowowoman and Batwowowoman')
print('++++++++++++')
print(mo == None)
print(mo1.group())
print(mo2.group())

# 用 + 号匹配一次或多次，没有匹配结果为None，有就匹配
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('the adv of Batman')
mo1 = batRegex.search('the adv of Batwoman and Batwowowoman')
mo2 = batRegex.search('the adv of Batwowowowoman and Batwowowoman')
print('++++++++++++')
print(mo == None)
print(mo1.group())
print(mo2.group())

# 用 {} 号匹配特定次数
batRegex = re.compile(r'Bat(wo){3}man')
mo = batRegex.search('the adv of Batman')
mo1 = batRegex.search('the adv of Batwowowoman and Batwowowoman')
print('{}{}{}{}{}{}')
print(mo == None)
print(mo1.group())

# 贪心匹配，有二意的情况下尽可能匹配长的
greetRegex = re.compile(r'(wo){3,5}')
moo1 = greetRegex.search('wowowo')
moo2 = greetRegex.search('wowowowowo')
print('贪心匹配')
print(moo1 == None)
print(moo2.group())

# 非贪心匹配，有二意的情况下尽可能匹配短的
# ⚠️ 注意：？在正则匹配中有二意性，声明非贪心匹配和表示可选匹配，二者无关
greetRegex = re.compile(r'(wo){3,5}?')
moo1 = greetRegex.search('wowowo')
moo2 = greetRegex.search('wowowowowo')
print('非贪心匹配')
print(moo1 == None)
print(moo2.group())