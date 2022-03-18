#!/bin/python3

import math
import os
import random
import re
import sys

# Matrix representation
# 00 01 02 
# 10 11 12 
# 20 21 22


# Time complexity O(len(matrix))
# Space complexity O(1)

def diagonalDifference(arr):
    # Write your code here
    leftToRightDiagonal = 0
    rightToLeftDiagonal = 0
    
    for i in range(0, len(arr[0])):
        leftToRightDiagonal += arr[i][i] 
        rightToLeftDiagonal += arr[i][len(arr) - i -1] 
    return abs(leftToRightDiagonal - rightToLeftDiagonal)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
