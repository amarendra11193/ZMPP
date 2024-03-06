# Write a python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(),(),('',),('a','b'),('a','b','c'),('d')]
# Expected Output: [('',),('a','b'),('a','b','c'),('d')]

# This code is not working as expected & has flaws. Looking for the fix.
# Code is correct as per the online articles though!

def remove_empty(tupList):
    for i in tupList:
        if(i == ()):
            tupList.remove(i)
    return tupList

tupList = [(),(),(),('',),('a','b'),('a','b','c'),('d')]
print(remove_empty(tupList))