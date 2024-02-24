# Write a program to print every character of a string entered by user in a new line using loop.

def char_Print(char):
    for i in char:
        print(i)

char = str(input('Enter the string: \n'))
char_Print(char)