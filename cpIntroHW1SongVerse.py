#*******************************************************************************
#
# Computer Science 1114
#
# Fall 2017
#
# Assignment:  cpIntroHW1SongVerse.py
#
# Due Date:    Friday September 15 2017 
#
# Instructor:  Nancy Draganjac
#
# Programmer:  Tushar Verma
#
# Description: Verse of a Song 
#
# Input:       N/A
#
# Output:      Print verse of a Song
#
#*******************************************************************************

numOfBuckets = 99
print ("{:} buckets of bits on the bus,".format(numOfBuckets))
print ("{:} buckets of bits,".format(numOfBuckets))
print ("Take one down, short it to ground,")
print ("{:} buckets of bits on the bus.".format(numOfBuckets-1))
print()
print ("{:} buckets of bits on th bus,\n{:} buckets of bits,"
       "\nTake one down, short it to ground,"
       "\n{:} buckets of bits on the bus.".format(numOfBuckets,numOfBuckets,
                                           numOfBuckets-1))
print()
print('''{:} buckets of bits on the bus,
{:} buckets of bits,
Take one down,short it to ground,
{:} buckets of bits on the bus'''
      .format(numOfBuckets,numOfBuckets,numOfBuckets-1))
