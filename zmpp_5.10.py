# Write a program to find the first and the last occurence of the letter 'o' and character ',' 
# in "Hello, World".

def occur(sentence, letter):
    #occ = 0
    i = 0
    while(sentence[i:]):
        if (letter == sentence[i]):
            print(i)
            i += 1
        else:
            i += 1

sentence = str(input('Enter the sentence: \n'))
letter = str(input('Enter the letter/character to find: \n'))
occur (sentence, letter)