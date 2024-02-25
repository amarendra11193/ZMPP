# Write a program to get a string from a given string where all occurences of its first char have
# been changed to '$', except the first char itself.

def listToString(lst):
    strng = ""
    for l in lst:
        strng += l
    return strng

def change_Char(sentence):
    sentence = list(sentence)
    print(sentence)
    first = sentence[0]
    i=1
    while (sentence[i:]):
        if(sentence[i] == first):
            sentence[i] = '$'
            i += 1
        else:
            i += 1
    return listToString(sentence)

sentence = str(input('Enter the sentence: \n'))
print(change_Char(sentence))