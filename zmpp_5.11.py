# Write the string after the first occurence of ',' and the string after the last occurence of ','
# in the string "Hello, Good, Morning, World".

def occur_firstLast (sentence):
    sentence = sentence.split(", ")
    print (sentence)
    print(sentence[1])
    print(sentence[-1])


sentence = str(input('Enter the sentence: \n'))
occur_firstLast(sentence)