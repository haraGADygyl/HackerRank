#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    alice_points = 0
    bob_points = 0

    if a[0] > b[0]:
        alice_points += 1
    elif a[0] < b[0]:
        bob_points += 1

    if a[1] > b[1]:
        alice_points += 1
    elif a[1] < b[1]:
        bob_points += 1

    if a[2] > b[2]:
        alice_points += 1
    elif a[2] < b[2]:
        bob_points += 1

    return f'{alice_points}{bob_points}'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
