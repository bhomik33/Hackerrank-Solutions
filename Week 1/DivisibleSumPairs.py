#!/bin/python3

import math
import os
import random
import re
import sys

# Time complexity -> O(n ^ 2)
# Space complexity -> O(1)

def divisibleSumPairs(n, k, ar):
    # Write your code here
    pairCount = 0

    for i in range(0, n):
        for j in range(0, n):
            if i < j:
                if((ar[i] + ar[j]) % k == 0):
                    pairCount +=1
                
    return pairCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
