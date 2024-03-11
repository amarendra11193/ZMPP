# Write a python program to issubset and isseuperset

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3, 4, 5, 6, 7}

def issubset(s1, s2):
    if (s1 <= s2):
        return True
    else:
        return False
    
def issuperset(s1, s2):
    if (s1 >= s2):
        return True
    else:
        return False

print('Is Subset?: \n', issubset(s1, s2))
print('Is Superset?: \n', issubset(s1, s2))