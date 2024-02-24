# Write a program to check if the word 'python' is present in the "welcome to python programming".

def find_letter(sentence, word):
    counter = 0
    i = 0
    sentence = sentence.split()
    print (sentence)
    while (sentence[i:]):
        if (word == sentence[i]):
            counter += 1
            i += 1
        else:
            i += 1
            continue
    if (counter > 0):
        print('The word is present in the sentence')
    else:
        print('The word is NOT present in the sentence')

sentence = str(input('Enter the sentence: \n'))
word = str(input('Enter the word to search: \n'))

find_letter(sentence, word)