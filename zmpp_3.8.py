# Write a program to find the entered number is prime or not.

def isPrime():
    num = int(input('Enter the number: \n'))
    if (num <= 0):
        print('NOT a Prime Number')
    else:
        n = int(num/2)
        for i in range (2,n):
            if((num % i) == 0):
                print ('NOT a Prime Number')
                break
            else:
                print ('It IS a Prime Number')
                break

isPrime()