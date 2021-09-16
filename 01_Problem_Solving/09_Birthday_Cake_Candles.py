#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    tallest_candles = 1
    candles_sorted = list(reversed(sorted(candles)))

    for i in range(candles_count - 1):
        if candles_sorted[i] == candles_sorted[i + 1]:
            tallest_candles += 1
        else:
            break

    return tallest_candles


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
