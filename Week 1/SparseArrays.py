#!/bin/python3

import math
import os
import random
import re
import sys


# Time complexity -> O(n ^ 2)
# Space complexity -> O(1)

def matchingStrings(strings, queries):
    # Write your code here
    result = []
    for i in range(0,len(queries)):
        count = 0
        for j in range(0,len(strings)):
            if queries[i] == strings[j]:
                count += 1
        result.append(count)
    return result
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
