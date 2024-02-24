# Write a program to find the length of the string "Programming" without using len function.

def get_Len(strng):
    counter = 0
    for i in strng:
        counter += 1
    print('The length of',strng, ' = ',counter)

strng = str(input('Enter the string: \n'))
get_Len(strng)