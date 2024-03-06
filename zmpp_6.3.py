# Write a python program to find the repeated items of a tuple.
# NOT PERFECT --> Needs re-work for more efficiency.
# Not using the count python module.

def new_tuple(n):
    lst = [ ]
    for i in range(0, n):
        a = input()
        lst.append(a)
        tup = tuple(lst)
    return tup

def repeat_item(tup):
    i = 1
    while (tup[i:]):
        j = 0
        while (tup[j:]):
            if (i != j):
                if (tup[i] == tup[j]):
                    print(tup[j])
                else:
                    pass
            else:
                pass
            j += 1
        i += 1

# Example:
tup = (1,1,3,3,4,4,5,6)
repeat_item(tup)