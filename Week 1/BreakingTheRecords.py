#!/bin/python3

import math
import os
import random
import re
import sys

# Time Complexity -> O(n)
# Space Complexity -> O(1)

def breakingRecords(scores):

    minScore = scores[0]
    maxScore = scores[0]
    minCount = 0
    maxCount = 0

    for i in range(1, len(scores)):
        if scores[i] < minScore:
            minScore = scores[i]
            minCount +=1
        elif scores[i] > maxScore:
            maxScore = scores[i]
            maxCount += 1
        else:
            continue
    return [maxCount, minCount]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
