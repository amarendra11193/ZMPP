# Write a python program to sum all the items in a list.

def new_list(n):
	newList = [ ]
	print('Enter the items of the list - only integers - separated by ENTER \n')
	for i in range (0, n):
		a = int(input())
		newList.append(a)
	return newList

def sum_list(newList):
	sum = 0
	for i in newList:
		sum += i
	return sum

n = int(input('Enter the number of items in the list: \n'))
temp = new_list(n)
print('The list is: \n', temp)
print('The sum of the items in the list is: \n', sum_list(temp))