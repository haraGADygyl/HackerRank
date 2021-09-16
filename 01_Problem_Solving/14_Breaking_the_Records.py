#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    minimum = scores[0]
    maximum = scores[0]

    minimum_count = 0
    maximum_count = 0

    for i in range(1, len(scores)):
        if scores[i] < minimum:
            minimum = scores[i]
            minimum_count += 1
        elif scores[i] > maximum:
            maximum = scores[i]
            maximum_count += 1

    return [maximum_count, minimum_count]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    # print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
