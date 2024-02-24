# Write a program to design simple calculator performing arithmetic functions like addition,
# substraction, multiplication and division with the input given by user.

def add(a, b):
    x = a+b
    print('The sum of the two numbers is: ',x)

def sub(a, b):
    x = a-b
    print('The difference of the two numbers is: ',x)

def mul(a, b):
    x = a*b
    print('The product of the two numbers is: ',x)

def div(a, b):
    x = a/b
    print('The divison of the two numbers is: ',x)

a = int(input('Enter the first number: \n'))
b = int(input('Enter the first number: \n'))
c = str(input('Enter one of the operations - Add, Substract, Multiply or Divide: \n'))

if (c == "Add"):
    add(a,b)
elif (c == "Substract"):
    sub(a,b)
elif (c == "Multiply"):
    mul(a,b)
elif (c == "Divide"):
    div(a,b)
else:
    print('Enter a valid operation!')