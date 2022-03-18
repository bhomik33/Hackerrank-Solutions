#!/bin/python3

import math
import os
import random
import re
import sys

# Time complexity -> O(n) - we are traversing over the array elements
# Space complexity -> O(1) - we are modifying the array in place

def gradingStudents(grades):
    # Write your code here
    for i in range(0, len(grades)):
        if grades[i] < 38:
            continue
        difference = grades[i] % 5
        if 5 - difference < 3:
            grades[i] = grades[i] + 5 - difference
        else:
            continue
    return grades
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
