#**************************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpRepetitionHW.py
#
# Due Date:    Monday October 30 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Guessing a number game, calculating a factorial, sum of
#              positive and negative numbers and multplication by addition 
#
# Input:       Get value data for each different problem
#              
#
# Output:      Guessing Game, Factorial, Sum of Positive and negative numbers and
#              multoply by Addition
#              total Interest
#
#**************************************************************************************
import random

# guessingGame
#
# description: Generating random number and guessing if the input number is same
#
# input: Getting number from user  
#
# output: Letting user know if number is equal to random or not equal
# 
# parameters: N/A 
#             
# returns: N/A
# 
def guessingGame():
    secretNum = random.randint(1,100)
    print("\t\tGuessing Game!")
    guessedNum = float(input("\nGuess a Number (Enter -1 to stop) : "))
    while(guessedNum != secretNum and guessedNum != -1):
        print("Inncorrect guess!")
        guessedNum = float(input("\nGuess a Number(Enter -1 to stop) : "))
    if(guessedNum == -1):
        print()
    else:
        print("Congratulations! You guessed the right number ")
        
# factorial
#
# description: Calculating factorial of number
#
# input: N/A  
#
# output: N/A
# 
# parameters: num - Number to calculate factorial 
#             
# returns: result - Value of Factorial 
#    
def factorial(num):
    result = 1
    if (num <= 0):
        result = 0
    else:
        while(num != 1):
            result = result*num
            num = num - 1
    return result

# sumPositiveOrNegative
#
# description: Getting multiple numbers and calculating sum of positive
#              and negative numbers
#
# input: Getting integers negative or positive  
#
# output: The sum of postive and negative numbers
# 
# parameters: N/A 
#             
# returns: N/A 
# 
def sumPositiveOrNegative():
    num = 1
    i = 99
    totalPositive = 0
    totalNegative = 0
    print("\n\t\tSum of all Postive and Negative numbers!\n")
    num = int(input("Enter a Positive or Negative number (Enter 0 to Stop) : "))
    while (num > 0 and num != 0):
        temp = int(num)
        totalPositive += temp
        num = int(input("Enter a Positive or Negative number (Enter 0 to Stop) : "))
    while (num < 0 and num != 0):
        temp2 = int(num)
        totalNegative = totalNegative + num
        num = int(input("Enter a Positive or Negative number (Enter 0 to Stop) : "))
    print("\nThe Positive Total of the entered Values is : {} ".format(totalPositive))
    print("The Negative Total of the entered Values is : {} ".format(totalNegative))
    
# multiplyByAddition
#
# description: Calculating multiplication by addition
#
# input: Geting two integers to multiply  
#
# output: Returning the multiplication of two numbers 
# 
# parameters: N/A 
#             
# returns: N/A
# 
def multiplyByAddition():
    print("\n\t\tMultipling two integers using repeated addition.")
    firstInterger = 1
    secondInteger = 1
    while (firstInterger >= 0 and secondInteger >= 0):
        firstInteger = int(input("\nEnter the first Integer(Input -1 to Exit): "))
        if(firstInteger == -1):
            print("")
            firstInteger = -1
            secondInteger = -1
        else:
            secondInteger = int(input("Enter the second Integer: "))
            if(firstInteger < 0 or secondInteger < 0):
                print("You entered First or Second or Both as Negative !!")
                firstInteger = 1
                secondInteger = 1
            else:
                check = 1
                answer = 0
                outputString =""
                print("{} X {} = ".format(firstInteger,secondInteger),end= "")
                while (check <= secondInteger):
                    if (check == secondInteger and firstInteger != 0):
                       outputString = outputString + "{} = ".format(firstInteger)
                    elif(firstInteger != 0):
                        outputString = outputString + "{} + ".format(firstInteger)          
                    answer = answer + firstInteger
                    check = check + 1
                print(outputString,end= "")
                print(answer)
    print()


guessingGame()
print()
print("\t\tCalculate Factorial of a number!\n")
num = int(input("Input a number : "))
result = factorial(num)
print("Factorial of {} is {}".format(num,result))
sumPositiveOrNegative()
multiplyByAddition()
print("Program Exit ...")
