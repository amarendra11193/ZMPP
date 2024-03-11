# Write a python program to create a set difference.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

def set_diff(set1, set2):
    a = {}
    a = set1 - set2
    return a

print('Set 1 is: \n', s1)
print('Set 2 is: \n', s2)
print('Set Difference is: \n', set_diff(s1, s2))