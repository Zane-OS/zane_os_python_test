#! python3 /user/bin/env python3

# 当程序运行的时候，变量是保存数据的好方法。
# 但是如果希望程序结束数据仍然保持，就需要把数据保存到文件中

# 文件与文件路径
# 路径指明了文件在计算机上的位置
# 文件名分两部分.前为文件名称.后为文件后缀（扩展名），指定文件的类型

# 在Windows上文件路径书写使用\，而在OS X和Linux上是/，如果想写的程序在不同的操作系统上运行就需要处理这种情况
# 好在，用os.path.join()函数来做这件事情，他会返回一个当前操作系统正确的路径

import os

path = os.path.join('users', 'zane', 'desktop', 'zane_os_python_test')
print('--->返回正确的路径')
print(path)

myFiles = ['account.txt', 'details.csv', 'invite.docx']
for fileName in myFiles:
    print(os.path.join('users', 'zane', 'desktop', 'zane_os_python_test', fileName))

# 当前工作目录
print(os.getcwd())
# 切换当前工作目录
# os.chdir(os.getcwd()+'/testchdir') 路径需存在，这里暂时没有正确路径不注释会报错

# 绝对路径和相对路径
# 绝对路径：总是从跟文件夹开始
# 相对路径：它相对于程序的当前工作目录
# '.'和'..'文件夹，不是真正的文件夹，而是可以在路径中使用的特殊符号，
# 前者用作文件夹名称是当前文件夹
# 后者表示父文件夹
"""
Mac OS 中的相对路径有待查询
                                             相对路径               绝对路径
「__」/Users                                  
  |
   -> 「__」/zane
        |
         -> 「__」/Desktop
              |
               -> 「__」/zane_os_python_test
"""

# 创建文件夹
# 执行os.makedirs() 会创建所有必要的中间文件夹以保证完整路径的存在
# os.makedirs(os.getcwd()+'/testchdir/xxx/xx/x') # 成功在当前工作目录创建文件夹

# os.path模块

# os.path模块包含了很多于文件名称相关的函数，比如上边使用的os.path.join()来构建所有操作系统上都有效的路径
# ⚠️：在这之后的很多测试都需要导入os

# 处理绝对路径和相对路径
# abspath('path')将返回参数的绝对路径
# isabs('path')如果参数是绝对路径就返回True否则返回False
# relpath('path')返回参数的相对路径
abp = os.path.abspath('./regexFindall.py')
isabp = os.path.isabs(abp)
print('--->绝对路径')
print(abp)
print(isabp)
relp = os.path.relpath('./regexFindall.py')
print('--->相对路径')
print(relp)

# dirname()返回一个包含path中最后一个斜杠之前的内容
# basename()返回一个包含path中最后一个斜杠之后的内容
path = '/Users/zane/Desktop/zane_os_python_test/python快速上手/7-18/regexFindall.py'
dirname = os.path.dirname(path)
basename = os.path.basename('./regexFindall.py')
print('--->文件所在位置，文件名')
print(dirname + '\n' + basename)

# 如果想同时获取文件明和目录名需使用split(),该方法不会返回每个文件夹的字符串列表，
# 请使用split()字符串方法，并根据os.path.sep中的字符串进行分割
spname = os.path.split(path)
splname = path.split(os.path.sep)
print(spname)
print(splname)

# 查看文件的大小和文件夹的内容
# 一旦有办法处理文件路径，就可以开始搜集特定文件和文件夹信息
# os.path模块提供了一些函数，用于查看文件字节数和给定文件夹的文件和子文件
psize = os.path.getsize(path) # 返回path下文件的字节数
print('--->文件大小')
print(psize)
listdir = os.listdir(dirname)
print('--->文件列表')
print(listdir)

total_size = 0
for name in listdir:
    total_size = total_size + os.path.getsize(os.path.join(dirname, name))
print(str(total_size))

# 检查路径的有效性
# 如果你提供的文件路径不存在，python会崩溃报错
# os.path模块也提供了函数用于检测文件路径是否存在，以及它是文件还是文件夹。
a = os.path.exists(path) # 也可以用于检测闪存或者DVD当前的连接状态
b = os.path.isfile(path)
c = os.path.isdir(path)
print(a, b, c)

# 文件的读写过程
# 在熟悉了处理文件和相对路径后，你就可以指定文件的位置，进行读写
# 以下介绍的几个函数适用于纯文本文件
# 在 python 中读写文件的步骤
# 1、调用open()函数，返回file对象
# 2、调用file对象的read()、write()方法
# 3、调用file对象的close()方法关闭该文件
join_path = os.path.join(dirname, 'testchdir/test.txt')
print('------->' + dirname)
print(join_path)
# TODO: OPEN FILE
test_txt = open(os.path.join(dirname, 'testchdir/test.txt'))
sonnet_file = open(os.path.join(dirname, 'testchdir/sonnet29.txt'))
# TODO: READ
# 读文件
content_txt = test_txt.read()
content_txt_line = sonnet_file.readline()
print('read-->' + content_txt)
print('readline--->' + '\n')
print(sonnet_file.readlines())
# TODO: WRITE
# 写文件
# python允许你将内容写入文件，方式与print()函数将字符串'写'到屏幕上是类似的
# 但是如果是以读的方式打开就不能写
# 你需要以写入纯文本或者添加纯文本模式打开
# 写模式将覆写原有的文件，从头开始 'w'作为open()的第二个参数
# 添加模式是在已有文件末尾添加文本 'r'作为open()的第二个参数
# 如果传入的文件名不存在，写模式和添加模式都会创建一个新的空文件
# 在读写结束必须close才能重新open
bacon = open(os.path.join(dirname, 'testchdir/bacon.txt'), 'w')
bacon.write('hello world!\n')
bacon.close()

bacon = open(os.path.join(dirname, 'testchdir/bacon.txt'), 'a')
bacon.write('bacon is not a vegetable')
bacon.close()

content = open(os.path.join(dirname, 'testchdir/bacon.txt'))
print('---> racontent')
print(content)
# ⚠️：write方法不会在字符串末尾假如换行，因此要手动加入'\n'

# TODO: CLOSE FILE
test_txt.close()
sonnet_file.close()