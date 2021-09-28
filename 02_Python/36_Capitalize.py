#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(name):
    result_as_string = ""
    list_of_words = name.split(' ')

    for elem in list_of_words:
        if len(result_as_string) > 0:
            result_as_string = result_as_string + " " + elem.capitalize()
        else:
            result_as_string = elem.capitalize()

    if not result_as_string:
        return name
    else:
        return result_as_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    # print(result)

    fptr.write(result + '\n')

    fptr.close()
