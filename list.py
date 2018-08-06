# username = input("plase input your name:")

# password = input("password:")

# if username == "zzw" and password == "123" :

# 	print(username)

# else:

# 	print(password)

# spam = 0
# while spam < 5:
#     print("spam<5,spam=",spam)
#     spam = spam + 1
	
# name = ""
# while name != "your name":
#     print("Please type your name")
#     name = input()
# print("thank you!")
# for i in range(12,-1,-2):
# 	print(i)

import random,sys

##########################################################

# for i in range(5):
# 	print(random.randint(1,10))
# 	if i==3:
# 		sys.exit()

# if True:
#     print("True")
# else:
# 	print("False")
# spam = input("Please input a number:")

# if int(spam) == 1:
# 	print("Hello")
# elif int(spam) == 2:
# 	print("Hane")
# else:
# 	print("Other")

# while True:
# 	print("cont!!")


# for i in range(1,11):
# 	print(i)

# y=1
# while y<11:
# 	print(y)
# 	y=y+1


##########################################################

# def hello(name):
	# print("hello,"+name+"!")

# hello("zzw")

# def game1():
# 	print("gass some number btown 1～10")
# 	ansow = random.randint(1,10)
# 	pl_str = "Please input a gass number:"
# 	user_input = input(pl_str)

# 	while int(user_input) != ansow:
# 		if int(user_input)<ansow:
# 			print("small!!")
# 			user_input = input(pl_str)
# 		else:
# 			print("big!!")
# 			user_input = input(pl_str)
# 	print("you are right!!")

# game1()


##########################################################

# # this func just return the calculation results
# def collatz(number):
# 	if number%2 == 0:
# 		print(str(number//2))
# 		return number//2
# 	else:
# 		print(str(3*number+1))
# 		return 3*number+1
# # get and try except the value of user input
# # repeat if value type isequal str or equal zero.
# def getInput():
# 	try:
# 		str_value = input("number:")
# 		if int(str_value) == 0:
# 			print("Please input a value that's not zero !!")
# 			return getInput()
# 		return int(str_value)
# 	except Exception as e:
# 		print("Please enter a numeric type value !!")
# 		return getInput()
# # start 
# print("Please input a number:")
# int_value = getInput()
# result = collatz(int_value)
# # return when the result equal 1.
# while result != 1:
# 	result = collatz(result)

##########################################################

# list base
spam = ["ss","sss","ssss","sssss","ssssss"]
sss = [1,2,3,"4",None,4,5]
print(spam)
print(spam[0])
print(spam[-1])
print(sss+spam)
ddd = sss+spam 
# append()和insert()没有返回值， 直接修改原值
ddd.append("1111")
ddd.insert(1,"22222")
print(ddd)
print(ddd[1:4])
del ddd[0]
# remove()如果要删除的值在list不存在将会报错
ddd.remove("1111")
# sort() 方法将列表中的值进行排序，直接操作原来的list无返回值,
# 也可以指定reverse为true，实现逆序
# 不能对既有数字又有str的混序list排序
# sort()对str排序是按ascii排序因此大写字母在小写字母之后，因此如果需要普通的排序要设置key=str.lower
ll = [1,3,-4,9,6,4,5,-3]
ll.sort() 
ll
# [-4,-3,1,3,4,5,6,9]
ll = ["d","c","f","c","a"]
ll.sort()
ll
# ["a","c","c","d","f"]\

# 类似于list， str可以看成是单字符列表，很多list语法操作对str也是适用的
name = "zzw"
name[0]
# "z"
name[0:2]
# "zz"
"z" in name
# true
for i in name:
	print("*****"+i+"*****")
# *****z*****
# *****z*****
# *****w*****

# 但是列表和字符串有一个重要的不同，那就是list是可变的，str是不可变的，list可以修改（增删改）元素
# str只读

# 下边介绍的是另外一只不可变类型的列表（元组tuple）
# 元组与数据类型几乎与列表数据类型一样，只是元组输入（）而不是【】

eggs = ('hello',42,0.5)
eggs[0]
# 'hello'
eggs[1:3]
# (42,0.5)
len(eggs)
# 3

# 如果元组中只有一个值，你需要在结束时输入“，”告诉python这是一个元组否则它会认为这只是一个带括号的值
type(('hello',))
# <class 'tuple'>
type(('hello'))
# <class 'str'>
# 你可以使用元组告诉读代码的人这个序列的值是不可被修改的

# list()和tuple()
list(eggs) #元组转化list
tuple(ll) #list转化为元组

# 引用
spam = 45
chese = spam
spam = 100
spam
# 100
chese
# 45
# 这类似深copy而，
spam = [1,2,3,4,5]
chese = spam
chese[1] = "hello"
spam
# [1,"hello",3,4,5]
chese
# [1,"hello",3,4,5]
# 这类似于浅copy

# 传递引用
def eggs(params):
	params.append("hello")

spam = [1,2,3]
eggs(spam)
print(spam)

# 以上的方法修改了spam的元素值，这是浅 copy导致的

# 以下我们来介绍copy()和deepcopy(),深copy
# 如果列表作为方法的参数，方法内修改了列表的值这是很可怕的事情
spam = ["a","b","c"]
cheese = copy.copy(spam)
cheese[1] = "hello"
spam
# ["a","b","c"]
# 注意如果spam元素包含list，那就需要deepcopy()


##########################################################

mypots=["cat","dog","chani","eleph"]
name = input("Please input a pot type:")

if name not in mypots:
	mypots = mypots+[name]
	print(mypots)
else:
	print("you had a pot type in array !!")



