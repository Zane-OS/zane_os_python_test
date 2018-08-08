#! python3 /user/bin/env python3
import pprint
# ##################################################################
# theBoard = {
# 	'top-l':'O', 'top-m':'O', 'top-r':'O',
# 	'mid-l':'X', 'mid-m':'X', 'mid-r':' ',
# 	'low-l':' ', 'low-m':' ', 'low-r':'X'
# }

# theBoard = {
# 	'top-l':' ', 'top-m':' ', 'top-r':' ',
# 	'mid-l':' ', 'mid-m':' ', 'mid-r':' ',
# 	'low-l':' ', 'low-m':' ', 'low-r':' '
# }

# def formatBoard(board):
# 	print(board['top-l'] + '|' + board['top-m'] + '|' + board['top-r'])
# 	print('-+-+-')
# 	print(board['mid-l'] + '|' + board['mid-m'] + '|' + board['mid-r'])
# 	print('-+-+-')
# 	print(board['low-l'] + '|' + board['low-m'] + '|' + board['low-r'])

# # formatBoard(theBoard)

# turn = 'X'

# for i in range(9):
# 	formatBoard(theBoard)
# 	print("turn for " + turn + ". move on which space?")
# 	move = input()
# 	theBoard[move] = turn
# 	if turn == 'X':
# 		turn = 'O'
# 	else:
# 		turn = 'X'
# formatBoard(theBoard)

# 这不是一个完整的井字游戏，因为他不能判断输赢，规则逻辑也不完善

# ##################################################################

# allGuests = {
# 	'alice':{
# 		'apple': 2,
# 		'pretzels': 12
# 	},
# 	'bob':{
# 		'sandwiches': 3,
# 		'apple': 3
# 	},
# 	'carol':{
# 		'apple': 4,
# 		'cups': 2
# 	}
# }

# # pprint.pprint(allGuests)

# def totalBrought(guests, item):
# 	numBrounght = 0
# 	for key, value in guests.items():
# 		numBrounght = numBrounght + value.get(item,0)
# 	return numBrounght

# print('number of things being brought:')
# print('- apples '+str(totalBrought(allGuests,'apple')))
# print('- pretzels '+str(totalBrought(allGuests,'pretzels')))
# print('- sandwiches '+str(totalBrought(allGuests,'sandwiches')))
# print('- cups '+str(totalBrought(allGuests,'cups')))

# ##################################################################

stuff = {
	'rope': 1,
	'torch': 6,
	'gold coin': 41,
	'dagger': 1,
	'arrow': 12
}

def displayInventory(inventory):
	print("Inventory:")
	item_total = 0
	for key, value in inventory.items():
		print(str(value) + " " + key)
		item_total += value
	print("total number of items: " + str(item_total))

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
	for value in addedItems:
		inventory.setdefault(value, 0)
		inventory[value] = inventory[value] + 1
	return inventory

stuff = addToInventory(stuff, dragonLoot)

displayInventory(stuff)

# print(addToInventory(stuff, dragonLoot))


