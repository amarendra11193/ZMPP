# Write a python program to convert a list of characters into a string

# Not adding in space between the two items of the liat while converting them to a string.

def new_list(n):
	entList = [ ]
	print('Enter the items in the list - separated by ENTER:')
	for i in range(0, n):
		a = input()
		entList.append(a)
	return entList

def list_string(newList):
	strng = " "
	for i in newList:
		strng += i
# If we need a space, we can try:
#	 strng = strng + " " + i
	return strng

n=int(input('Enter the number of items in the list: \n'))
temp = new_list(n)
print('The list you entered is: \n', temp)
print('The converted list is: \n', list_string(temp))