# test the count of character count
import pprint
message = "it was a bright cold day in april, and the clocks were striking thirteen."
count = {}
for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1
pprint.pprint(count)
# 使用pprint 漂亮的打印，根据值大小排序
# 如果字典本身包含嵌套列表或字典，pprint()函数就特别有用。
# 如果希望得到漂亮的打印，而不是简单的显示在屏幕上那就调用pprint.pformat(),以下代码是等价的
pprint.pprint(message)
print(pprint.pformat(message))

