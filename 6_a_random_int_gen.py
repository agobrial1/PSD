# Second modification
# First commit

import random
# method to generate a list with random numbers

class Random:

    def __init__(self, amount, minRange, maxRange):
        
        # array container
        self.randomList = []
        # amount of random numbers to generate
        for i in range(amount):
            # generate random number
            self.randomList.append(random.randint(minRange, maxRange))
        # print array
        print(self.randomList) 

# create object

amount = int(input("Enter the amount of random numbers: "))
minRange = int(input("Enter the minimum range: "))
maxRange = int(input("Enter the maximum range: "))

Random(amount, minRange, maxRange)

'''
Pre-Conditions - amount input must be integer above 1, and minRange cannot equal maxRange.
Post-Conditions - The program will print an array of random numbers, and returned values are integers.
'''
