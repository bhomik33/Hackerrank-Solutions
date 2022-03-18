#!/bin/python3

import math
import os
import random
import re
import sys


# Time complexity -> O(n log n)
# Space complexity -> O(1)


def lonelyinteger(array):
    array.sort()
    currentIdx = 0
    uniqueElement = 0
    while currentIdx < len(array):
        if currentIdx == len(array) - 1:
            uniqueElement = array[currentIdx]
            break
        if array[currentIdx] == array[currentIdx+1]:
            currentIdx = currentIdx + 2
        else:
            uniqueElement = array[currentIdx]
            break
    return uniqueElement
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
