# Write a program to check if the letter 'e' is present in the word 'welcome'

def find_letter(word, letter):
    counter = 0
    for i in word:
        if (letter == i):
            counter += 1 
        else:
            continue
    if (counter > 0):
        print('The letter is present in the word')
    else:
        print('The letter is NOT present in the word')

word = str(input('Enter the word: \n'))
letter = str(input('Enter the letter to search: \n'))

find_letter(word,letter)