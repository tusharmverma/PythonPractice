#**************************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpFilesHWmultTable.py
#
# Due Date:    Thursday November 9 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Generating a 10 x 10 multiplication table
#              beginning with integers input by the user
#              and then writing the formatted table to a file
#
# Input:       Getting two numbers one going left to right and one going
#              top to bottom for Generating a 10 x 10 multiplication table
#              
# Output:      Writing the generated 10 x 10 multiplication table to a file 
#
#**************************************************************************************

import os.path

# numDigits
#
# description: Calculating the number of digits in the number
#              by floor division
#
# input: N/A 
#
# output: N/A
# 
# parameters: numDown - The number in Multiplication Table going top to bottom
#             numRight - The number in Multiplication Table going Left to Right
#             
# returns: count - The total number of digits
#
def numDigits(numDown,numRight):
    n = (numDown+10)*(numRight+10)
    count = 0
    while (n != 0):
        n = n // 10
        count = count + 1
    return count

# topLine
#
# description: Printing the first line which represents the number from
#              left to right
#
# input: N/A 
#
# output: Writing the first line to the file
# 
# parameters: numDown - The number in Multiplication Table going top to bottom
#             numRight - The number in Multiplication Table going Left to Right
#             
# returns: N/A
#
def topLine(numDown,numRight):
    myOutput = open("cpFilesHWmultTable.txt", "a")
    totalDash = numDigits(numDown,numRight)
    x = 0
    count = numRight
    myOutput.write("\n")
    myOutput.write(" {:<3}".format(""))
    while(count < numRight + 10):
        myOutput.write("{:>{}}".format(numRight+x,totalDash+3))
        x = x + 1
        count = count + 1
    myOutput.write("\n")
    myOutput.close()

# printLine
#
# description: Wrtingt the multiplication table of each number from top to
#              bottom
#
# input: N/A
#
# output: Printing each line of multiplication table from top to bottom
# 
# parameters: numDown - The number in Multiplication Table going top to bottom
#             numRight - The number in Multiplication Table going Left to Right
#             
# returns: N/A
#
def printLine(numDown, numRight):
    myOutput = open("cpFilesHWmultTable.txt", "a")
    totalDash = numDigits(numDown,numRight)
    x = 0
    count = numRight
    myOutput.write("{:<3}|".format(numDown))
    while (count < numRight+10):
        myOutput.write("{:>{:}}".format(numDown*(numRight+x),totalDash+3))
        x = x+ 1
        count = count + 1
    myOutput.write("\n")
    myOutput.close()
    
# dashLine
#
# description: Printing the dashed line under the top line for
#              multiplication table
#
# input: N/A 
#
# output: Writing to the file the dashed line under the top line
# 
# parameters: numDown - The number in Multiplication Table going top to bottom
#             numRight - The number in Multiplication Table going Left to Right
#             
# returns: N/A
#
def dashLine(numDown, numRight):
    myOutput = open("cpFilesHWmultTable.txt", "a")
    totalDash = numDigits(numDown,numRight) 
    myOutput.write(" {:}   ".format(""))
    myOutput.write("_"*((totalDash+3)*10))
    myOutput.write("\n")
    myOutput.close()   

myOutput = open("cpFilesHWmultTable.txt", "a")
print("-- Multiplication Table --")
numDown = int(input("Enter a Number Down: "))
numRight = int(input("Enter a Number Right: "))
topLine(numDown,numRight)
dashLine(numDown,numRight)
count = numDown
x = 0
while (count < numDown+10):
    printLine(numDown+x,numRight)
    count = count + 1
    x = x + 1
    
myOutput.write("\n")


