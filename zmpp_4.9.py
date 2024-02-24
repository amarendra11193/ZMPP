# Write a program to define a function that takes entered number as parameter and count and print its 
# number of digits.

def length(num):
    d=0
    while (num != 0):
        a = num % 10
        d = d+1
        num //= 10
    print ('The total number of digits: ', d)

num = int(input('Enter a number : \n'))
if (num < 0):
    print ('Enter a valid Number')
else:
    length(num)