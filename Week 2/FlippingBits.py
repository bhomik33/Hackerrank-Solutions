# Its purpose is to define the location of interpreter
#!/bin/python3

import math
import os
import random
import re
import sys



# 2 ^ 32 -1 =  4,294,967,295        Note: -1 because we are not dealing with the sign bit in it

def flippingBits(n):
# just calculate the difference between base10 value of 32 bits and the given integer
    return (pow(2,32) - 1 - n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
