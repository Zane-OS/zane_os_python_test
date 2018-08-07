###############################################################

# 字典 一种灵活的数据访问和组织方式
myCat = {'size':"fat",'color':"gray",'disposition':"loud"}

print(myCat)

print(myCat['size'])

# python 中的字典可以以任意数字作为key，并像数组那样取值

myCat = {123:"123",456:"456"}

print(myCat)

print(myCat[123])

# 字典与列表的对比
# 字典中的表项是无序排序的
spam = ["2","1","3"]
bacon = ["3","1","2"]
spam = bacon
# False

eggs = {"name":"zzw","age":"16"}
ham = {"age":"16","name":"zzw"}
eggs = ham
# True
# 由于字典是无序的，所以不能像list那样切片
# 尝试访问不存在的key将导致carsh
# print(spam["color"]) 
# carsh like that
# traceback (most recent call last):
# 、、、
# KeyError: "color"

###############################################################

# 尽管字典无序，正因为（你可以使用任意值作为key）这一点，能让你以这种强大的方式组织数据

# birthdays = {"alice":"apr 1","bob":"dec 12","carol":"mar 4","zzw":"teb 3"}

# while True:
# 	print("please enter a name:")
# 	name = input()
# 	if name == "":
# 		break
# 	if name in birthdays:
# 		print(name + "'s" + " birthday is " + birthdays[name])
# 	else:
# 		print("i dont't have birthday information for " + name);

# 当程序终止的时候我们所输入的内容将会消失，以后我们将学习如何将数据保存在硬盘文件中

###############################################################

# keys()、values()、items()
# items() 遍历得到的是包含键值的元组

spam = {"color": "red", "age": 42}
for v in spam.values():
	print("value:"+str(v))

for k in spam.keys():
	print("key:"+k)

for i in spam.items():
	print(i) # 遍历值类型toupe
	print(list(i)) # 遍历值从元组转化为list
# 也可直接便利key和value
for key,value in spam.items():
	print("value: "+ str(value) + "\n" + "key: " + str(key))

# 用 in 来检查字典中是否存在键值，得到True or False

# get()
# 访问不存在的键值导致崩溃,因此，我们可以通过get()来访问，该方法有两个参数，
# param1: 要取得key
# param2: 不存在返回的默认值
print(spam.get("color", "str"))
print(spam.get("other", "def"))

# setdefault() 
# 我们需要为字典中的某个键设置一个默认值，当该键没有任何值时返回它（show me code）
spam = {"name": "pooka", "age": "56"}
if "color" not in spam:
	spam["color"] = "withe"
# setdefault()方法帮助我们快速实现这个功能（like this）
spam = {"name": "pooka", "age": "56"}
spam.setdefault("color","withe")




