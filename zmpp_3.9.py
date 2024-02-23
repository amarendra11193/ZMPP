def isPalindrome():
    num = int(input('Enter the number: \n'))
    orig = num
    d = 0
    while (num != 0):
        a = num % 10
        print (a, end="")
        d = (d*10)+a
        num //= 10
    
    if (orig==d):
        print('\nIt IS a Palindrome')
    else:
        print('\nIt is NOT a Palindrome')

isPalindrome()