# Write a program to define a function that takes entered number as parameter and returns
# its reverse number.

def rev_num(num):
    rev = 0
    while (num > 0):
        a = int(num % 10)
        rev = (rev*10) + a
        num = int(num / 10)
    return rev

n = int(input('Enter the number which you want to reverse: \n'))
print('The reverse of the entered number is: \n',rev_num(n))