# Write a python program to convert a tuple to a string.

def new_tuple(n):
	lst = [ ]
	print('Enter the items - separated by ENTER: \n')
	for i in range(0, n):
		a = input()
		lst.append(a)
	tup = tuple(lst)
	return tup

n = int(input('Enter the number of items: \n'))
temp = new_tuple(n)
print ("Here's the tuple: \n", temp)

def tup_to_str(tup):
	str = ' '
	for i in tup:
		# To add space between two items when converted to string, have used the below expression instead of (str += i)
		str = str + i + ' '
	return str

print ('Tuple to String : \n', tup_to_str(temp))