#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpFunctionsTempConvert.py
#
# Due Date:    Monday October 04 2017 
#
# Instructor:  Ms. Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Getting the input of Celcius, Fahrenheit, Kevin and convert each
#              temperature in to the other two temperature scales
#
# Input:       Get three temperatures from user in Celcius, Fahrenheit, Kelvin 
#
# Output:      Printing the table of Temperatures on the screen 
#
#*******************************************************************************


# celciusToFah
#
# description: Converting temperature from Celcius to Fahrenheit
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperature in Celcius 
#             
# returns: result - Temperature in Fahrenheit 
#          

def celciusToFah(temp):
    result = (temp * 1.8) + 32 #formula to convert celcius to Fahrenheit
    return result 

# celciusToKel
#
# description: Convert the temperature from Celcius to Kelvin             
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperature in Celcius
#             
# returns: Temperature in Kelvin 
#          

def celciusToKel(temp):
    result = temp + 273.15 #formula to convert form Celcius to kelvin
    return result 

# fahToCelcius
#
# description: Convert the temperature from Celcius to Kelvin
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperature in Celcius
#             
# returns: Temperature in Celcius 
#          

def fahToCelcius(temp):
    result = (temp - 32)/1.8 #formula to convert from
                             #fahrenheit to celcius
    return result 

# kelToCelcius
#
# description: From the temperature in Kevin convert it
#              to Celcius
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperature in Kelvin
#             
# returns: Temperature in Celcius 
#          

def kelToCelcius(temp):
    result = temp - 273.15 #formuala to convert
                           #from kelvin to celcius
    return result 

# fahToKelvin
#
# description: We convert fahrenheit to kelvin by first 
#              converting from Fahrenheit to celcius then
#              calling fahToCelciius function for converting to kelvin
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperatur in Fahrenheit
#             
# returns: result - Temperature in Kelvin
#          

def fahToKelvin(temp):
    tempresult = fahToCelcius(temp) #Calling function to to get
                                    #value from fahreheit to celcius
    result = celciusToKel(tempresult) #Calling function to get
                                      #celcius converted to kelvin  
    return result 

# kelvinToFah
#
# description: Converting the temperature from kelvin to fahrenheit
#
# input: N/A  
#
# output: N/A
# 
# parameters: temp - Temperature in Kelvin               
#             
# returns: result - Temperature in Fahrenheit 
#          

def kelvinToFah(temp):
    result = (temp * (9/5)) - 459.67 #formula to convert into Fahrenheit
    return result

tempInCelcius = float(input("Enter the temperature in Celcius: "))
tempInFah = float(input("Enter the temperature in Fahrenheit: "))
tempInKel = float(input("Enter the temperature in Kelvin: "))

print("{:>10} {:>15} {:>15}".format("Celcius","Fahrenheit","Kelvin"))

print("{:>10,.2f} {:>15,.2f} {:>15,.2f}".
      format(tempInCelcius,celciusToFah(tempInCelcius),celciusToKel(tempInCelcius)))

print("{:>10,.2f} {:>15,.2f} {:>15,.2f}"
      .format(fahToCelcius(tempInFah),tempInFah,fahToKelvin(tempInFah)))

print("{:>10,.2f} {:>15,.2f} {:>15,.2f}"
      .format(kelToCelcius(tempInKel),kelvinToFah(tempInKel),tempInKel))
