# Write a program to make a new string with all the consonants deleted from the string
# "Hello, have a good day".

def listToString(lst):
    strng = ""
    for l in lst:
        strng += l
    return strng

def no_Consonant(sentence):
    sentence = list(sentence)
#    print(sentence)
    newlist = []
    for item in sentence:
        if (item != 'a' and item != 'e' and item != 'i' and item != 'o' and item != 'u' and item != ' '
            and item != '.' and item != ',' and item != '?'):
            newlist.append(item)
        else:
            continue
#    print (newlist)
    result = [i for i in sentence if i not in newlist]
    return listToString(result)

sentence = str(input('Enter the string: \n'))
print('The string without consonants is: \n',no_Consonant(sentence))