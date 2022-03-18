#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity -> O(n.log n)
# Space Complexity -> O(1)

def miniMaxSum(arr):
    # array is sorted with time complexity O(n log n)
    arr.sort()
    minValue = arr[0] + arr[1] + arr[2] + arr[3]
    maxValue = arr[len(arr) - 1] + arr[len(arr) - 2] + arr[len(arr) - 3] + arr[len(arr) - 4]
    
    print(str(minValue) + " " + str(maxValue))
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
