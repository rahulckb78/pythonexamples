#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getSecondLargestFromList' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY inputArray as parameter.
#

def getSecondLargestFromList(inputArray):
    # Write your code here
    return sorted(list(set(inputArray)))

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    inputArray_count = int(input().strip())

    inputArray = []

    for _ in range(inputArray_count):
        inputArray_item = int(input().strip())
        inputArray.append(inputArray_item)

    result = getSecondLargestFromList(inputArray)

    fptr.write(str(result) + '\n')

    fptr.close()
