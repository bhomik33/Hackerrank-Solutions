#!/bin/python3

import math
import os
import random
import re
import sys


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    
    array = [0]* 4
    numOfCharacterToAdd = 0
    
    # Time complexity -> O (n)
    # Space complexity -> O(1)
    for chr in password:
        if chr in numbers:
            array[0] = array[0] + 1
        elif chr in lower_case:
            array[1] = array[1] + 1
        elif chr in upper_case:
            array[2] = array[2] + 1
        else:
            array[3] = array[3] + 1
    print(array)
    
    for num in array:
        if num == 0:
            numOfCharacterToAdd += 1

    if len(password) + numOfCharacterToAdd < 6:
        numOfCharacterToAdd += 6 - (len(password) + numOfCharacterToAdd)
    
    return numOfCharacterToAdd
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
