# Write a program to define a function that takes entered number as a parameter and returns true if
# number is Armstrong number and false if number is not Armstrong number.

def arm(num):
    s = 0
    cube = num
    print(cube)
    while (cube != 0):
        a = cube % 10
        s += a**3
        cube //= 10
    return s

user = int(input('Enter the number: \n'))
print('The number is ', user)
print('Comparison: ', arm(user))
if (user == arm(user)):
    print ('True')
else:
    print ('False')