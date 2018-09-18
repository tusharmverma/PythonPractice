HALF_DOLLAR = 0.5
QUARTERS = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01
noOfHalfDollar = 10
noOfQuarters = 11
noOfDime = 12
noOfNickel = 13
noOfPenny = 14
totalHalfDollar = noOfHalfDollar*HALF_DOLLAR 
totalQuarter = noOfQuarters*QUARTERS
totalDime = noOfDime*DIME
totalNickel = noOfNickel*NICKEL
totalPenny = noOfPenny*PENNY
totalNoOfCoins = noOfHalfDollar + noOfQuarters + noOfDime + noOfNickel + noOfPenny
totalAmountOfCoins = totalHalfDollar + totalQuarter + totalDime + totalNickel + totalPenny
print("No. of Half Dollar {:.2f}".format(noOfHalfDollar))
print("Amount of Half Dollar : ${:.2f}".format(totalHalfDollar))
print("No. of Quarters {:.2f}".format(noOfQuarters))
print("Amount of Quarters : ${:.2f}".format(totalQuarter))
print("No. of Dime {:.2f}".format(noOfDime))
print("Amount of Dime : ${:.2f}".format(totalDime))
print("No. of Nickel {:.2f}".format(noOfNickel))
print("Amount of Nickel : ${:.2f}".format(totalNickel))
print("No. of Penny {:.2f}".format(noOfPenny))
print("Amount of Penny : ${:.2f}".format(totalPenny))
print("Total number of coins: ",totalNoOfCoins)
print("Total value : ${:.2f}".format(totalAmountOfCoins))
print("Half Dollars: {:5} {:30}".format(noOfHalfDollar,"      ${:<.2f}".format(totalHalfDollar)))


