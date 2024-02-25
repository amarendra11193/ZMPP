# Write a program to find the number of vowels, consonents, digits and white space characters in a string

def vcdw(strng):
    strng = list(strng)
    v = c = d = w = i = 0
    while (strng[i:]):
        if (strng[i] == "a" or strng[i] == "e" or strng[i] == "i" or strng[i] == "o" or strng[i] == "u"):
            v += 1
            i += 1
        elif (strng[i] == '0' or strng[i] == '1' or strng[i] == '2' or strng[i] == '3' or strng[i] == '4' 
              or strng[i] == '5' or strng[i] == '6' or strng[i] == '7' or strng[i] == '8' or strng[i] == '9'):
            d += 1
            i += 1
        elif (strng[i] == " "):
            w += 1
            i += 1
        else:
            c += 1
            i += 1
    print('Number of vowels: ', v)
    print('Number of consonants: ', c)
    print('Number of digits: ', d)
    print('Number of white spaces: ', w)

strng = str(input('Enter the string: \n'))
vcdw(strng)