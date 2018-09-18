#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpCustomModuleIL
#
# Due Date:    Friday October 6 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Using the module cin to read better int,float and string value
#
# Input:       Getting int,float and string from user
#
# Output:      Printing the values from functions in module cin.py 
#
#*******************************************************************************


import cin        # my custom input module

cin.test()        # verify access to the cin module
num = cin.readint("Enter a Interger: ")
print("You entered: {} and the type is {}"
      .format(num,type (num)))

decnum = cin.readfloat("Enter a floating-point number: ")
print("You entered: {} and the type is <class 'float'>"
      .format(decnum, type (decnum)))

string = cin.readln("What is your name? ")
print("You entered: {} and the type is <class 'str'>"
      .format(string,type (string))) 
