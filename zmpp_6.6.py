# Write a python program to get the largest number from a list.

def new_list(n):
    newList = [ ]
    print('Enter the items in the list - integer only - separated by ENTER:')
    for i in range (0, n):
        a = int(input())
        newList.append(a)
    return newList

def large_list(newList):
    lar = newList[0]
    i = 1
    while (newList[i:]):
        if(lar < newList[i]):
            lar = newList[i]
        else:
            pass
        i +=1
    return lar

n = int(input('Enter the number of items in the list: \n'))
temp = new_list(n)
print('The list entered is : \n', temp)
print('The largest entry in the list is: \n', large_list(temp))