def grossSalary ():
    bs = float(input('Enter the base Salary: \n'))
    da = bs*0.4
    hra = bs*0.2
    gs = bs + da + hra
    print ('Gross Salary is', gs)
    return gs

grossSalary()