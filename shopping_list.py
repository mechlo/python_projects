import os

def clear():
	os.system("cls" if os.name == "nt" else "clear")

shopping_list = []

# add items to the list
# quit program with 'DONE'
# print list when quit

def help():
	clear()
	print("""
HELP - list of commands
SHOW - show the current list
DONE - complete list
		""")

def show():
	clear()
	print("Your current list:")

	index = 1
	for new_item in shopping_list:
		print("{}. {}".format(index, new_item))
		index += 1
	print("-"*10)

def add():
	show()
	if len(shopping_list):
		position = input("Where should I enter {}?\n"
											"Press enter to add to the end of list\n"
											"> ".format(item))
	else:
		position = 0

	try:
		position = abs(int(position))
	except ValueError:
		position = None
	if position is not None:
		shopping_list.insert(position-1, new_item)

	shopping_list.append(new_item)
	print("Added! List has {} item(s).".format(len(shopping_list)))


# print("What would you like to add?")
# print("Type DONE to quit")
help()

while True:

	#ask for things to add
	new_item = input('> ')

	if new_item.upper() == 'HELP':
		help()
		continue

	elif new_item.upper() == 'SHOW':
		show()
		continue

	elif new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
		break



print("Here is your list")
show()

