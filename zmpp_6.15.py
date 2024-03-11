# Write a Python program to find the length of a set.

s2 = {1, 2, 3, 4, 5, 6, 7}

def set_length(set1):
    count = 0
    for item in set1:
        count += 1
    return count

print('Length of the set is: ', set_length(s2))