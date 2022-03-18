#!/bin/python3

import math
import os
import random
import re
import sys



# Time complexity -> O(n)
# Space complexity -> O(n)

def timeConversion(s):

    if s[8] == 'A':
        if s[0:2] == '12':
           newString = s.replace(s[0], '0' , 1)
           newString = newString.replace(newString[1], '0', 1)
           return newString[0:8]
        else:
            return s[0:8]
    else:
        if s[0:2] == "12": return s[0:8]
        else:
            number = int(s[0:2]) + 12
            numberString = str(number)
            newString = s.replace(s[0],numberString[0] , 1)
            newString = newString.replace(newString[1], numberString[1], 1)
            return newString[0:8]
             
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
