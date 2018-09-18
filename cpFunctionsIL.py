#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpFunctionsIL.py
#
# Due Date:    Monday September 02 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Calculate distance and mid point between two cartesian points 
#
# Input:       Two points on Cartesian Plane
#
# Output:      Print the Mid point and Distance between two points
#
#*******************************************************************************

import math
def displayInfo():
    print("Tushar Verma\n")
    print("This Program tests multiple cartesian points for \n"
          "midpoints and distance between them also it asks \n"
          "user for a input of two points to calculate the midpoints\n"
          "and distance between the two points\n")

def displayExit():
    print("\n\nEnd of Script. Existing...\n\n")

def calculateDistance(x1,y1,x2,y2):
    temp = ((x2-x1)**2)+((y2-y1)**2)
    distance = math.sqrt(temp)
    return distance

def calculateMid(x1,y1,x2,y2):
    midX = (x1+x2)/2
    midY = (y1+y2)/2
    distance = calculateDistance(x1,y1,x2,y2)
    print("The mid point of the two points ({},{}) and ({},{}) \n"
          "is ({},{}). The distance between the two points is {:.4f}"
          .format(x1,y1,x2,y2,midX,midY,distance))

displayInfo()
print("Input points are (6,1) and (2,5)")
calculateMid(6,1,2,5)
print()
print("Input points are (-5,-3) and (8,10)")
calculateMid(-5,-3,8,10)
print()
print("Input points are (-4,-1) and (-12,-10)")
calculateMid(-4,-1,-12,-10)
print()
print("Input points are (5.3,7) and (4.3,9.1)")
calculateMid(5.3,7,4.3,9.1)
print()
x1 = float(input("Enter point x1 : "))
y1 = float(input("Enter point y1 : "))
x2 = float(input("Enter point x2 : "))
y2 = float(input("Enter point y2 : "))
print("Input points are ({},{}) and ({},{})".format(x1,y1,x2,y2))
calculateMid(x1,y1,x2,y2)
displayExit()


    
