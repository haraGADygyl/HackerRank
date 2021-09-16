#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#


def birthday(s, d, m):
    blocks_count = 0

    try:
        for i in range(n):
            temp = 0
            for j in range(m):
                temp += s[i + j]

            if temp == d:
                blocks_count += 1

        return blocks_count

    except IndexError:
        return blocks_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
