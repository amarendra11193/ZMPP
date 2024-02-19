def simpleInterest(p,t,r):
    print ('The principle amount is ', p)
    print ('The time period is ', t)
    print ('The rate of interest is ', r)
    
    si = p*t*r/100

    print ('The simple ineterst is', si)
    return si

simpleInterest (8,6,8)