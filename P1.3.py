def results():
    sub1 = int(input('Marks obtained in Subject 1: \n'))
    if (sub1 < 0 or sub1 > 100):
        print('Enter a value between 0 to 100')
    else:
        sub2 = int(input('Marks obtained in Subject 2: \n'))
        if (sub2 < 0 or sub2 > 100):
            print('Enter a value between 0 to 100')
        else:
            sub3 = int(input('Marks obtained in Subject 3: \n'))
            if (sub3 < 0 or sub3 > 100):
                print('Enter a value between 0 to 100')
            else:
                sub4 = int(input('Marks obtained in Subject 4: \n'))
                if (sub1 < 0 or sub1 > 100):
                    print('Enter a value between 0 to 100')
                else:
                    sub5 = int(input('Marks obtained in Subject 5: \n'))
                    if (sub1 < 0 or sub1 > 100):
                        print('Enter a value between 0 to 100')
                    else:
                        total = sub1+sub2+sub3+sub4+sub5
                        percentage = (total/5)
                        print ('Agrregate Marks = ',total)
                        print ('Percentage Marks = ', percentage)
                        return 0

results()