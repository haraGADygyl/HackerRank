#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour, minutes, seconds = s.split(':')

    if seconds.endswith('AM'):
        if hour != '12':
            return f'{hour}:{minutes}:{seconds[:2]}'
        else:
            return f'00:{minutes}:{seconds[:2]}'
    else:
        if hour != '12':
            return f'{int(hour) + 12}:{minutes}:{seconds[:2]}'
        else:
            return f'12:{minutes}:{seconds[:2]}'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
