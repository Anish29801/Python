# Write an expression that calculates the average of 23, 32 and 64
# Place the expression in this print statement

import math

def calculateBill(bill1, bill2,bill3):
    return math.ceil(((bill1 + bill2 + bill3)/3))

avgBill = str(calculateBill(23,32,64))
print("Your bill: $"+avgBill)