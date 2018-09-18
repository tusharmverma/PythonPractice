#**************************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpFilesHWdigitSum.py
#
# Due Date:    Tuesday November 7 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Getting series of numbers from different line until the
#              sentinal (-1) reached and then using the function to
#              add up every digit from each number in the line then write the
#              output of every number addition in a different file.
#
# Input:       Reading a file to get the different numbers to calculate the
#              sum of digits
#              
# Output:      Getting value from the reading the file and then writing
#              the output in the different file
#
#**************************************************************************************
import os.path

# digit_sum
#
# description: gettiing the number and then breaking it down to
#              calculate the sum of digits.
#
# input: N/A 
#
# output: N/A
# 
# parameters: n - the number to calculate the sum of digits 
#             
# returns: total - The total of the digit of the number
#
def digit_sum(n):
    n = abs(n)
    total = 0
    while n >= 1:
        total += (n % 10)
        n = n // 10
    return total

if (os.path.isfile("cpFilesHWdigitSum.txt")):
    count = 0
    file = open("cpFilesHWdigitSum.txt","r")
    writeFile = open("cpFilesHWoutput.txt","w")
    while (count >= 0):
        line = int(file.readline())
        if(line != -1):
            num = digit_sum(line)
            writeFile.writelines("{}:{}\n".format(line,num))
            count = count + 1 
        else:
            count = -1
    writeFile.close()
    file.close()
else:
    print("Unable to open cpFilesHWdigitSum.txt for reading. ")

