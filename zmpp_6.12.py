# Write a program to remove an item from a set if it is present in the set.

s1 = set([1, 2, 3, 4, 5, 6])
s1 = list(s1)
print(s1)
rem  = input('Enter the item to be removed: \n')
i = 0
while (s1[i:]):
    temp1 = s1[i]
    if (str(temp1) == str(rem)):
        s1.remove(temp1)
    else:
        pass
    i += 1
print('The updated set: \n', set(s1))

''' LEARNING - We need to keep the data type in mind (int, str, etc.). If we do not 
consider the data type, the condition will always return as False. Line Number 10! '''