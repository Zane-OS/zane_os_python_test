#! /user/bin/env python3

# 字符串操作

# ###########################################################
# 字符串可以以‘’单引号开始或结尾。
string0 = 'jhfsadjkajkjjkajkkakladlfl'
# 如果要在字符串中输入单引号，可以以“”双引号开始或结尾。
string1 = "That is Alice's cat."
# 也可以使用\反斜杠，在字符串中输入单引号和双引号
string2 = 'That is Alice\'s cat.'
string3 = 'That is Alice\'s \"cat\".'

print(string0 + "\n" + string1 + "\n" + string2 + "\n" + string3)

# 转义字符

#####################
#  \'  #  单引号     #
#####################
#  \"  #  双引号     #
#####################
#  \t  #  制表符     #
#####################
#  \n  #  换行符     #
#####################
#  \\  #  倒斜杠     #
#####################

# 原始字符串 在字符串前加r
print(r'That is Carol\'s cat.')
# That is Carol\'s cat.

# 用三重引号的多行字符串
more_line_str = '''
	Dear Alice,
		Eve's has been arrested for catnapping, cat burglary, and extortion.
													Sincerely, Bob
'''

print(more_line_str)
# ###########################################################
"""
 这是多行注释的方式
"""
# ###########################################################
"""
#  字符串下标和切片
"""
spam = "Hello world!"
print(spam)
print(spam[5]) # []
print(spam[0:5]) # Hello
print(spam[:5]) # Hello
print(spam[6:]) # world!
print(spam[-1]) # !
# ###########################################################
"""
#  字符串的 in 和 not in
"""
temp = "ello"
print(temp in spam)
print(temp not in spam)
# ###########################################################
"""
#  有用的字符串方法 
# upper()  lower()  isupper()  islower()
"""
upstr = spam.upper()
lowstr = spam.lower()
print(upstr+"\n"+lowstr)
# 注意这些方法不是改变原有的字符串，而是返回一个新的字符串
# 如果要改变原来的字符串，只需要重新赋值即可
# spam = spam.upper()

# 这些方法在忽略大小写判断用户输入的时候很好用
"""
print('How are you!')
feeling = input("what are your feeling:")
if feeling.lower() == "great":
	print("I'm feel great too!")
else:
	print("I hope the rest day of your day is good!")
"""
print("Hello".upper().isupper())
print("Hello".lower().islower())

# isX() 方法
# isalpha() 字符串只包含字母并且非空
# isalnum() 字符串只包含字母和数字并且非空
# isdecimal() 字符串只包含数字字符并且非空
# isspace() 字符串只包含制表符、空格和换行并且非空
# istitle() 字符串仅包含大写字母开头后边都是小写字母的单词并且非空
# 如果要验证用户输入isX是很有用的
"""
while True:
	print("Enter your age:")
	age = input(":")
	if age.isdecimal():
		break
	print("Please enter a number of your age!")

while True:
	print("Select a new password (letters and numbers only):")
	password = input(":")
	if password.isalnum():
		break
	print('Passwords can only have letters and numbers!')
"""
# 字符串方法startswith()和endswith()
print("Hello world!".startswith("Hello"))
print("Hello world!".endswith("d!"))
# 字符串方法join()和split()
print(",".join(['1','2','3']))
print("Hello world!".split())
print("Hello world!".split('o'))
# 字符串方法rjust()\ljust()\center()
print('Hello'.rjust(20))
print("Hello".ljust(20))
print('Hello'.center(20))
print('Hello'.center(20,"="))
"""
['Hello', 'world!']
['Hell', ' w', 'rld!']
               Hello
Hello
       Hello
"""
# eg.
def printPicnic(itemsDic, leftWidth, rightWidth):
	print('PICNIC ITEMS'.center(leftWidth+rightWidth, '-'))
	for key, value in itemsDic.items():
		print(key.ljust(leftWidth, '.')+str(value).rjust(rightWidth, '.'))
picnicItems = {'sandwiches':20,
			   'apples':321,
			   'cups':44,
			   'cookies':77
			  }
printPicnic(picnicItems, 12, 12)
"""
------PICNIC ITEMS------
sandwiches............20
apples...............321
cups..................44
cookies...............77
"""
# 字符串方法
# strip()-->在字符串首尾删除指定字符默认删除空白字符（空格、换行、制表符）
# rstrip()-->在字符串右侧删除指定字符串默认删除空白字符（空格、换行、制表符）
# lstrip()-->在字符串左侧删除指定字符串默认删除空白字符（空格、换行、制表符）
spam = " Hello world! "
print(spam.strip()) # "Hello world!"
print(spam.lstrip()) # "Hello world! "
print(spam.rstrip()[:2]) # " H"
print(spam.strip(' H')) # ello world!

# ###########################################################

