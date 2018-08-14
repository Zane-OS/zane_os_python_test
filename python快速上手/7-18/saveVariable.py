#! python3 /user/bin/env python3
import os
import shelve
import pprint

# 利用shelve模块，你可以将程序中的变量保存到二进制的shelve文件中
# Windows 上运行下边的代码，将在指定目录中创建 mydata.bak mydata.dat mydata.dir
# OS X 上只会创建 mydata.db

# path = '/Users/zane/Desktop/zane_os_python_test/python快速上手/7-18/regexFindall.py'
# dirname = os.path.dirname(path)
# shelf_file = shelve.open(os.path.join(dirname, 'testchdir/mydata'))
# cats = ['zop', 'poo', 'sim']
# shelf_file['cats'] = cats
# shelf_file.close()

# 可以使用shelve重新打开并读取这些数据，shelf值不必用读或者写模式打开，
# 因为他们打开后既可以读也可以写
# shelf_file = shelve.open(os.path.join(dirname, 'testchdir/mydata'))
#
# print(type(shelf_file))
# print(shelf_file['cats'])
# print(list(shelf_file.keys()))
# print(list(shelf_file.values()))

# ###############################################################################

import myCats
import pprint

print('-----> ppront')
# 使用pprint.pformat()函数保存变量
cats = [{'name': 'zop', 'desc': 'chun'}, {'name': 'poo', 'desc': 'flu'}]
pprint.pprint(cats)
file_obj = open('myCats.py', 'w')
file_obj.write('cats = ' + pprint.pformat(cats) + '\n' )
file_obj.close()


print(myCats.cats)
