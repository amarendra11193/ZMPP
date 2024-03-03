# Write a python program to convert a list to a tuple.

def listToTuple(lst):
	tup = tuple(lst)
	return tup

def inputList(n, lst):
	print('Enter the items for the list - press enter after each entry')
	for i in range(0, n):
		a = input()
		lst.append(a)
		i += 1
	return lst

n = int(input('Enter the number of items in the list: \n'))
lst = [ ]
print('The list entered is : \n', inputList(n, lst))

print('Converting it to a tuple, we get the output: \n', listToTuple(lst))