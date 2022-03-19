#!/bin/python3

import math
import os
import random
import re
import sys


# Time complexity -> O(n) we are looping once over the array elements
# Space complexity -> O(1)

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    travellingValley = False
    numberOfValleyWalkedCount = 0
    for i in range(0, len(path)):
        if path[i] == 'D': altitude -= 1
        else: altitude += 1
        
        if altitude >= 0 : travellingValley = False
        else:
            if travellingValley == False:
                numberOfValleyWalkedCount += 1
                travellingValley = True
    return numberOfValleyWalkedCount
                
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
