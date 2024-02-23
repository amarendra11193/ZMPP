# Write a program to calculate the area of circle where radius of circle will be entered through the keyboard.

def circleArea():
    rad = float(input('Enter the radius of the circle: \n'))
    area = 3.14*(rad**2)
    print ('The radius of the circle will be: ', area)
    return area

circleArea()