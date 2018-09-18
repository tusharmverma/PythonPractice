#*******************************************************************************
# geometry.py
#       Returning the value of area of Triangle, area of Circle
#       area of Right Triangle and distance between points
#       prompted by user.
#
# Tushar Verma
# October 12 2017
#*******************************************************************************

import math

# Function:    areaOfTriangle
# Description: Purpose of this function is to calculate area of Triangle.
# Input:       none
# Output:      none
# Parameters:  a - Side of Triangle 
#              b - Side of Triangle
#              c - Side of Triangle
# Returns:     area - Area calculated by the formula
def areaOfTriangle(a,b,c):   
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    return area

# Function:    areaOfCircle
# Description: Purpose of this function is to calculate area of Circle.
# Input:       none
# Output:      none
# Parameters:  radius - radius of the circle
# Returns:     area - Area calculated by the formula
def areaOfCircle(radius):
    area = (math.pi)*radius**2
    return area

# Function:    areaOfRTriangle
# Description: Purpose of this function is to calculate area of Right Triangle.
# Input:       none
# Output:      none
# Parameters:  width - Base length of Triangle
#              height - Height of Triangle
# Returns:     area - Area calculated by the formula
def areaOfRTriangle(width,height):
    area = 0.5 * width * height
    return area

# Function:    distanceOfPoints
# Description: Purpose of this function is to calculate distance between two points.
# Input:       none
# Output:      none
# Parameters:  x1 - X Intercept of point A
#              y1 - Y Intercept of point A
#              x2 - X Intercept of point B
#              y2 - Y Intercept of point B
# Returns:     area - Area calculated by the formula
def distanceOfPoints(x1,y1,x2,y2):
    distance = math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )
    return distance
