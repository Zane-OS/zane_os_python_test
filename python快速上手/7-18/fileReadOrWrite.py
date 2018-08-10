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
os.makedirs(os.getcwd()+'/testchdir/xxx/xx/x') # 成功在当前工作目录创建文件夹

# os.path模块
# os.path模块包含了很多于文件名称相关的函数，比如上边使用的os.path.join()来构建所有操作系统上都有效的路径
# ⚠️：在这之后的很多测试都需要导入os

# 处理绝对路径和相对路径
