#Write a Python program to exchange the value of two variables.

#Using 3rd variable
a = 2
b = 5
c = a
a = b
b = c
print ('value of a = ',a)
print ('value of b = ',b)

#Using only two variables
a = a+b
b = a-b
a = a-b
print ('value of a now = ',a)
print ('value of b now = ',b)