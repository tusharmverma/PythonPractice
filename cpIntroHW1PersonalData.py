#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpIntroHW1PersonalData.py
#
# Due Date:    Fridat September 15 2017 
#
# Instructor:  Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Personal Info Program 
#
# Input:       N/A
#
# Output:      Print Personal Info
#
#*******************************************************************************

NAME = "Jane Doe"
AGE = 55
WEIGHT = 145.40
SALARY = 163000.00
convertToKilo = WEIGHT * 0.45392022
decades = AGE//10
yearsFromDecade = 10-(AGE-((AGE//10)*10))
#payCheckEveryTwoWeeks = SALARY / 26
print ("Data for {:}".format(NAME))
print ("{:} is {:} years of age.  That means that {:} has seen {:}"
       " decades and is {:} years from another."
       .format(NAME,AGE,NAME,decades,yearsFromDecade))
print ("Jane Doe weighs {:} pounds which is {:,.1f} kilograms."
       .format(WEIGHT,convertToKilo))
print ("Jane Doe earns an annual salary of {:,.2f} which"
       "translates to a paycheck of {:,.2f} every two weeks."
       .format(SALARY,SALARY / 26))
