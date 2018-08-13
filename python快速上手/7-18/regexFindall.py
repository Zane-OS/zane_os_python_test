#! python3 /user/bin/env python3

import re

phone_number_regex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phone_number_regex.search('Cell:028-451-4632,work:264-544-9632')
print(mo.group())

# 没有分组的情况下findall返回，匹配到的字符串数组
# 有分组的情况下返回，匹配到的分组元组数组

moo = phone_number_regex.findall('Cell:028-451-4632,work:264-544-9632')
print('--->没有分组')
print(moo)

phone_number_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
moo = phone_number_regex.findall('Cell:028-451-4632,work:264-544-9632')
print('--->分组')
print(moo)

# 字符分类
"""
----------------------------------------
|   \d    |    0~9字符                  |
++++++++++++++++++++++++++++++++++++++++
|   \D    |    除0～9其他                |
++++++++++++++++++++++++++++++++++++++++
|   \w    |    任意字母、数字或下划线      |
++++++++++++++++++++++++++++++++++++++++
|   \W    |    除字母、数字和下划线其他    |
++++++++++++++++++++++++++++++++++++++++
|   \s    |    空格、制表符或换行         |
++++++++++++++++++++++++++++++++++++++++
|   \S    |    除空格、制表符和换行其他    |
----------------------------------------
"""
# 字符串分类对缩短正则表达式很有用，比如[0-5]表示匹配数字0～5，这比输入(0|1|2|3|4|5)要简便很多。
xmasRegex = re.compile(r'\d+\s\w+')
fi = xmasRegex.findall('12 docx, 13 css, 15 cust, 22 vvc, 9 oop')
print('--->字符分类')
print(fi)

# 建立自己的字符分类
# 有时候你想匹配一组字符，但是缩写的转义字符太宽泛，你可以使用[]定义自己的字符串分类
vouelRegex = re.compile(r'[aeiouAEIOU]')
vo = vouelRegex.findall('Robocop eats baby food. BABY FOOD.')
print('--->元音字符')
print(vo)

# 也可以使用-表示字母和数字的范围[a-z0-9A-Z],它表示匹配所有的大小写字母和数字
# 这意味着你不需要添加到斜杠转义、*、{}、？
# 你也可以在方括号后架上[^ 表示非字符类，[^aeiouAEIOU]就表示非元音字符

# 插入字符^和结尾字符$,可以同时使用表示字符串必须匹配正则
beginWithHello = re.compile(r'^Hello')
be = beginWithHello.findall('Hello world!')
print('--->hello 开头')
print(be)

endWithWorld = re.compile(r'world!$')
en = endWithWorld.findall('Hello world!')
print('--->world！结尾')
print(en)

staticString = re.compile(r'^\d+$')
st1 = staticString.findall('123233565665')
st2 = staticString.findall('5454dadasda5444545')
print('--->强制正则完全匹配')
print(st1)
print(st2)

# 通配字符 ',' 和 '.' ，通配符匹配除了空格外的所有字符
atRegex = re.compile(r'.at')
at = atRegex.findall('the cat in the hat on the flat mat.')
print('--->通配字符')
print(at)

# 用 '.*' 匹配所有字符
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
na = nameRegex.search('First Name: zanewangwangwangwangwnagwangwangwang Last Name: xx1234567890xx')
print('---> all in')
print(na.group())

# '.*' 默认贪心，尽量匹配多的内容。
# 如果使用非贪心匹配写法如下
nongreedyRegex = re.compile(r'<.*?>')
greedyRegex = re.compile(r'.*')
non = nongreedyRegex.search('<To save man> for dinner.>')
gre = greedyRegex.search('<To save man> for dinner.>')
print('---> 通配符的贪心和非贪心')
print(non.group())
print(gre.group())

# 通配符是不识别换行的，那如何让它识别呢？
# 这需要re.compile()传入第二个参数re.DOTALL
newlineRegex = re.compile(r'.*', re.DOTALL)
new = newlineRegex.search('Serve the public trust.\nPortect the innocent.')
neww = greedyRegex.search('Serve the public trust.\nPortect the innocent.')
print('--->通配符识别换行')
print(new.group())
print(neww.group())

"""
正则表达是复习
* ? 匹配零次或者一次前面的分组
* * 匹配零次或者多次前面的分组
* + 匹配一次或者多次前面的分组
* {n}匹配n次前面的分组
* {n,}匹配n次或者多次前面的分组
* {,m}匹配零次到m次前面的分组
* {n,m}匹配至少n次、至多m次前面的分组
* {n,m}?或者*?或者+?对前面的分组进行贪心匹配
* ^spam意味着字符串必须以spam开头
* spam$意味着字符串必须以spam结尾
* . 匹配所有字符串，换行符除外
* [abc]匹配方括号内的任意字符（诸如a、b、c）
* [^abc]匹配不再方括号内的字符
"""

# 不区分大小写的匹配
robocop = re.compile(r'robocop', re.I)
rob = robocop.search('Robocop is part man, part machine, all cop.').group()
print('--->不区分大小写的匹配')
print(rob)

# 用sub()方法替换字符串
# 正则表达式不仅能找到文本模式，而且可以使用新的文本替换掉这些模式
# Regex对象的 sub() 方法有两个参数，第一个参数是字符串，用于取代发现的匹配，第二个参数字符串，即正则表达式
namesRegex = re.compile(r'Agent \w+')
name_sub = namesRegex.sub('Zane', 'Agent Alice gave the secret documents to Agent Bob.')
print('--->替换字符串')
print(name_sub)
# 有时候你希望匹配的文本本身，作为替换的一部分
# 可以使用 (\1)(\2)(\3)... 表示'替换输入分组1、2、3...的文本'
agentNamesRegex = re.compile(r'Agent (\w)\w')
agentNames = agentNamesRegex.sub(r'\1*****', 'Agent Alice gave the secret documents to Agent Bob.')
print(agentNames)

# 管理复杂的正则表达式
# 如果要匹配的文本很简单，那很好
# 但如果匹配的文本很浮在，那我们需要对正则表达式放在多行并添加注释
# 我们需要给re.compile()方法传入re.VERBOSE作为第二个参数
phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# 写成如下形式并加注释
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # area code
    (\s|-|\.)?          # separator
    \d{3}               # first 3digits
    (\s|-|\.)           # separator
    \d{4}               # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})? # extension 
    )''', re.VERBOSE)
