def distanceInKm():
    km = float(input('Enter the distance in KM: \n'))
    m = 1000*km
    ft = float(3280.84*km)
    inc = float(39370.1*km)
    cm = 100000*km
    print ('Distance in Meters = ', m)
    print ('Distance in Feet = ', ft)
    print ('Distance in Inches = ', inc)
    print ('Distance in Centimeters = ', cm)
    return 0

distanceInKm()