#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    minimum_sum = sum(sorted(arr)[:-1])
    maximum_sum = sum(sorted(arr)[1:])

    print(f'{minimum_sum} {maximum_sum}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
