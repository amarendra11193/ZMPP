def printPalindrome():
    for num in range(100, 201):
        init = num
        rev = 0
        while (num != 0):
            a = num % 10
            #print(a, end="")
            rev = (rev*10)+a
            num //= 10
        if (init == rev):
            print(rev)
        else:
            continue

printPalindrome()