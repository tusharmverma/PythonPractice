#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpIntroHW2ReverseNum.py
#
# Due Date:    Monday September 18 2017 
#
# Instructor:  Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Reverse number 
#
# Input:       N/A
#
# Output:      Print the reverse number
#
#*******************************************************************************

number = 357916
num = number

digit1 = str(num % 10)
num//= 10
digit2 = str(num % 10)
num//= 10
digit3 = str(num % 10)
num//= 10
digit4 = str(num % 10)
num//= 10
digit5 = str(num % 10)
num//= 10
digit6 = str(num % 10)

reverseNum = int(digit1+digit2+digit3+digit4+digit5+digit6)
reverseNumSpaces = str(digit1 + ' ' + digit2 + ' ' + digit3 + ' ' + digit4 +\
                       ' ' + digit5 + ' ' + digit6)

print("The number to reverse: {:<20n}" .format(number))
print("The digits, in order, are: {:}".format(reverseNumSpaces))
print("The number in reverse: {:}".format(reverseNum))

     
