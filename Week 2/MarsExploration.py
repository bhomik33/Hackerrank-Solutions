#!/bin/python3

import math
import os
import random
import re
import sys

# SOS SOS SOS
# 012 345 678

def marsExploration(s):
    currentIdx = 0
    count = 0
    while currentIdx < len(s) :
        if currentIdx == len(s):
            break
        leftCharacter = s[currentIdx]
        middleCharacter = s[currentIdx + 1]
        rightCharacter = s[currentIdx + 2]
        print(leftCharacter, middleCharacter, rightCharacter)
        if leftCharacter == 'S' and middleCharacter == 'O' and rightCharacter == 'S':
            currentIdx += 3
            continue
        if leftCharacter != 'S':
            count += 1
        if middleCharacter != 'O':
            count += 1
        if rightCharacter!= 'S':
            count += 1
        currentIdx +=3
    return count
 


    return count 
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
