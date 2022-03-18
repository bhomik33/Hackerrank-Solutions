#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity -> O(n)
# Space Complexity -> O(1)

def plusMinus(arr):
    numberOfPositiveElements = 0
    numberOfNegativeElements = 0
    numberOfZeroElements = 0
    
    for i in range(0,len(arr)):
        if arr[i]> 0: numberOfPositiveElements +=1
        elif arr[i] < 0 : numberOfNegativeElements +=1
        else: numberOfZeroElements += 1
        
    print(round(numberOfPositiveElements/len(arr), 6))
    print(round(numberOfNegativeElements/len(arr), 6))
    print(round(numberOfZeroElements/len(arr), 6))    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
