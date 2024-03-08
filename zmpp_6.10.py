# Write a python script to add a key to a dictonary.
# Sample Dictonary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

def new_dict(n):
    newDict = { }
    for i in range(0, n):
        a = input('Enter the key: \n')
        newDict[a] = input('Enter the value: \n')
    return newDict

def add_dict(dict1, dict2):
    for i in dict2.keys():
        dict1[i] = dict2[i]
    return dict1

oldDict = {0: 10, 1: 20}
# n = int(input('Enter the number of key-value pairs: \n'))
temp = new_dict(1)
print("Here's the Dictonary you entered: \n", temp)
temp = add_dict(oldDict, temp)
print("Here's the Dictonary you expect: \n", temp)