#*******************************************************************************
# cin.py
# Returning the value of int, float and string prompted by user
#
# Tushar Verma
# October126 2017
#*******************************************************************************

# Function:    test
# Description: This purpose of this function is to provide a means of testing the cin module.
# Input:       none
# Output:      A test message is displayed on the screen.
# Parameters:  none
# Returns:     none
def test():
    print("Hello from cin module!")

# Function:    readint
# Description: This function will read and return an int from the keyboard.
# Input:       The user is expected to enter a whole number.
# Output:      A message is displayed explaining what is expected from the user.
# Parameters:  prompt - message to display to user
# Returns:     user's input of data type int 
def readint(prompt):
    num = int(input(prompt))
    return num

# Function:    readfloat
# Description: This function will read and return a float from keyboard.
# Input:       The user is expected to enter a floating-point number.
# Output:      A message is displayed explaining what is expected from the user.
# Parameters:  prompt - message to display to user
# Returns:     user's input of data type float 
def readfloat(prompt):
    num = float(input(prompt))
    return num

# Function:    readln
# Description: This function will read a line (as a string) from the keyboard.
# Input:       The user is expected to enter a series of one or more characters.
# Output:      A message is displayed explaining what is expected from the user.
# Parameters:  prompt - message to display to user
# Returns:     user's input of data type str 
def readln(prompt):
    string = input(prompt)
    return string
