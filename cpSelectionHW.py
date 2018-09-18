#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpSelectionHW.py
#
# Due Date:    Monday October 16 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Comparing threee numbers and retur the middle one and also
#              getting two points on line and one to check if the third point
#              lies on the line return yes or no
#
# Input:       Get three integers from User and also get two (x,y) on the line
#              and one (x,y) coordinate to check if it lies on the line
#
# Output:      Middle value of three integers and reply if the third point
#              lies on the line or not
#
#******************************************************************************

import math

#*******************************************************************************
# middleNumber
#
# description: by the help of three condition we decide which is the number in
#              the middle.
#              
#
# input: N/A
#
# output: N/A
# 
# parameters: a: Integer number, b: Integer Number
#             c: Integer number,        
# 
# returns: Value: Whichever condition evaluates it returns the value of
#          that number.  
#          
#*******************************************************************************
def middleNumber(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c

#*******************************************************************************
# isBetween
#
# description: by the help of equating splope we can calculate if the point
#              is on line or not
#
# input: N/A
#
# output: N/A
# 
# parameters: (x1: Point on line, y1: Point on line)
#             (x2: Point on line, y2: Point on line)
#             (x: Point to check  , y: Point to check)
#       
# 
# returns: True/False: If the condition evaluates its True if not False 
#          
#*******************************************************************************
def isBetween(x1, y1, x2, y2, x, y):
    slope = (y2 - y1) / (x2 - x1)
    boolValue = bool(y - y1 == slope * (x - x1))
    return boolValue

print()
print("Which number is the middle !")
print("Enter three numbers to check which one is in middle: ")
numA = int(input("1: "))
numB = int(input("2: "))
numC = int(input("3: "))
middle = middleNumber(numA,numB,numC)
print("\n[ {} ] is in middle of {}, {} and {}".format(middle,numA,numB,numC))
print()
print("Check if the point lies on the line !")
x1 = int(input("Enter first x - coordinate on the line : "))
y1 = int(input("Enter first y - coordinate on the line : "))
x2 = int(input("Enter second x - coordinate on the line : "))
y2 = int(input("Enter second y - coordinate on the line : "))
x = int(input("Enter x - coordinate of point to check : "))
y = int(input("Enter y - coordinate of point to check : "))
result = isBetween(x1, y1, x2, y2, x, y)
if(result == True):
    print("The point ({},{}) lies on the line !".format(x,y))
else:
    print("The point  ({},{}) doesn't lie on the line!".format(x,y))
print()
