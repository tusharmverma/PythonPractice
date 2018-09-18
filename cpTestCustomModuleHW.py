#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpTestCustomModuleHW
#
# Due Date:    Friday October 12 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Using the geometry.py to test the functions inside the module.
#
# Input:       N/A
#
# Output:      Printing the Tested values from functions in module geometry.py 
#
#*******************************************************************************

import geometry

print("{} {} {}".format('='*45,"Testing Geometry Module",'='*49))
print()
print("{:<20} {:>20} {:>20} {:>20} {:>20} ".format("Triangle","Side A","Side B","Side C","Area"))
print("{:>20} {:>20} {:>20} {:>20} {:>20,.1f}".format("Test 1:","3","4","5",geometry.areaOfTriangle(3,4,5)))
print("{:>20} {:>20} {:>20} {:>20} {:>20,.1f}".format("Test 2:","10.2","12.6","13.2",geometry.areaOfTriangle(10.2,12.6,13.2)))
print("{:>20} {:>20} {:>20} {:>20} {:>20,.1f}".format("Test 3:","8.29","11.61","14.79",geometry.areaOfTriangle(8.29,11.61,14.79)))
print()
print("{:<20} {:>20} {:>20} ".format("Circle","Radius","Area"))
print("{:>20} {:>20} {:>20,.1f}".format("Test 1:","5",geometry.areaOfCircle(5)))
print("{:>20} {:>20} {:>20,.1f}".format("Test 2:","12.6",geometry.areaOfCircle(12.6)))
print("{:>20} {:>20} {:>20,.1f}".format("Test 3:","28.49",geometry.areaOfCircle(28.49)))
print()
print("{:<20} {:>20} {:>20} {:>20} ".format("Right Triangle","Width","Height","Area"))
print("{:>20} {:>20} {:>20} {:>20,.2f}".format("Test 1:","5","7",geometry.areaOfRTriangle(5,7)))
print("{:>20} {:>20} {:>20} {:>20,.2f}".format("Test 2:","18.8","21.7",geometry.areaOfRTriangle(18.8,21.7)))
print("{:>20} {:>20} {:>20} {:>20,.2f}".format("Test 3:","25.67","27.77",geometry.areaOfRTriangle(25.67,27.77)))
print()
print("{:<20} {:>20} {:>20} {:>20} ".format("Distance b/w points","Point A","Point B","Distance"))
print("{:>20} {:>20} {:>20} {:>20,.1f}".format("Test 1:","(3,4)","(6,9)",geometry.distanceOfPoints(3,4,6,9)))
print("{:>20} {:>20} {:>20} {:>20,.1f}".format("Test 2:","(5.6,7.8)","(12.7,13.4)",geometry.distanceOfPoints(5.6,7.8,12.7,13.4)))
print("{:>20} {:>20} {:>20} {:>20,.1f}".format("Test 3:","(8.52,12.33)","(-11.73,-9.43)",geometry.distanceOfPoints(8.52,12.33,-11.73,-9.43)))
print()
print('='*120)
print()

