# Write a python program to print a specified list after removing the 0th,4th &5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def new_list(n):
	entList = [ ]
	print('Enter the items of the list - sepatated by Enter:')
	for i in range (0, n):
		a = input()
		entList.append(a)
	return entList

def rem_list(newList):
	a = newList[0]
	b = newList[4]
	c = newList[5]
	newList.remove(a)
	newList.remove(b)
	newList.remove(c)
	return newList

n=int(input('Enter the number of elements: \n'))
if (n < 6):
	print('ERROR! Please Enter a digit greater than 6')
else:
	temp = new_list(n)
	print('The list entered is: \n', temp)
	print('The updated list is: \n', rem_list(temp))