# Write a python program to count the number of strings where the string length is 2 or
# more and the first & last character are same from a given list of strings.
# Sample List : ['abc','xyz','aba','1221']
# Expected Result : 2

def check_req(newList):
    for item in newList:
        if(len(item) > 2):
            temp = list(item)
            a = 1
            