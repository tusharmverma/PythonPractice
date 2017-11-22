import os.path
# open yearlyRainfall.txt for writing
myOutput = open("yearlyRainfall.txt", "a")

# verify rainfall.txt exists and can be opened
if (os.path.isfile("rainfall.txt")):
    # open rainfall.txt for reading
    myInput = open("rainfall.txt","r")
    # read and convert each line from rainfall.txt
    count = 0
    total = 0
    day = 0
    largestRainfall = 0
    while (count < 365):
        a = myInput.readline()
        if (a != ""):
            inputLine = float(a)
            total = total + inputLine
            if(largestRainfall <inputLine):
                largestRainfall = inputLine
                day = count
            if(inputLine != 0):
                rainDays = 1
                rainDays = rainDays + 1
            count = count + 1
 
    myOutput.write("{}\n".format(total))
    # close file
    myInput.close()
    myOutput.close()
    print("Higest Rain was {} on {} Day".format(highestRain,day))
    print("The number of Days it rained : {}".format(rainDays))
    print("Total rain: {:.2f}".format(total))
    
else:
    print("Unable to open rainfall.txt.")
    
