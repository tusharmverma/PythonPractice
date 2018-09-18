#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpFunctionsSurfaceArea.py
#
# Due Date:F   friday October 06 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: This program calculates the area of prism by the help of
#              of two functions one to calculate the area of triangle
#              with herons formula and then use the area of triangle with
#              herons formula to calculate the area of top and bottom triangles
#              and then calculate rest of area by adding area of sides by area
#              of rectangle formula
#
# Input:       get the 3 sides and height of prism 
#
# Output:      Printing the data about prism and the area 
#
#*******************************************************************************

import math

# calcAreaHeronFormula
#
# description: gettig the sides of triangle and
#              calculating the area by herons formulas
#
# input: N/A  
#
# output: N/A
# 
# parameters: a,b,c - Sides of Triangle 
#             
# returns: area - Area of Triangle 
#          

def calcAreaHeronFormula(a,b,c):
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

# calcSurfaceAreaRightPrism
#
# description: getting the sides and height using calcAreaHeronFormula
#              get the are of two triangles and use the area of
#              rectangle formuala for area of sides
#
# input: N/A  
#
# output: N/A
# 
# parameters: a,b,c - Sides of Triangle, h - Height of prism 
#             
# returns: area - Area of right prism 
#          

def calcSurfaceAreaRightPrism(a,b,c,h):
    baseArea = calcAreaHeronFormula(a,b,c)
    topArea = calcAreaHeronFormula(a,b,c)
    sideArea = (b*h) + (a*h) + (c*h) #using are of rectangle for area of each side
    area = baseArea + topArea + sideArea
    return area

a = float(input("Enter prism side A: "))
b = float(input("Enter prism side B: "))
c = float(input("Enter prism side C: "))
h = float(input("Enter prism side H: "))
#print("The area of Triangle is {}".format(calcAreaHeronFormula(3,4,3)))
print("The Right Triangular Prism with\nSide A: {} \nSide B: {} \nSide C: {} \nHeight: {} \nArea: {:.2f}".format(a,b,c,h,calcSurfaceAreaRightPrism(4,5,6,3)))

