# Wrint a program that takes your full name as input and displays the abbreviations of the first and
# middle names except the last name which is displayed as it is. For Example, if your name is Mahendra
# Singh Dhoni, then the output should be M.S. Dhoni

def abb_Name(Name):
    Name = Name.split()
    print(Name)
    Last = Name[-1]
    print(Last)
    Name = Name[:-1]
    print(Name)
    for i in Name:
        abb = list(i)
        print(abb[0],'. ', end="")
    print(Last, end="")


Name = str(input('Enter Name: \n'))
abb_Name(Name)