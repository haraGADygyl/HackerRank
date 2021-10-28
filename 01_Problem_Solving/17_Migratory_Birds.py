#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    types = {}

    for i in range(arr_count):
        if arr[i] not in types:
            types[arr[i]] = 1
        else:
            types[arr[i]] += 1

    types_sorted = sorted(types.items(), key=lambda kv: (kv[1], -kv[0]), reverse=True)

    return types_sorted[0][0]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)

    fptr.write(str(result) + '\n')
    
    fptr.close()
