#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0

    for i in range(n):
        if arr[i] > 0:
            positives += 1
        elif arr[i] < 0:
            negatives += 1
        else:
            zeros += 1

    print(f'{(positives / n):.6f}\n{(negatives / n):.6f}\n{(zeros / n):.6f}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
