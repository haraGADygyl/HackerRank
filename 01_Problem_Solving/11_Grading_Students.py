#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grade = []

    for i in range(grades_count):
        steps = 0
        current_grade = grades[i]
        if current_grade >= 38:
            if current_grade % 5 == 0:
                final_grade.append(current_grade)
            else:
                while current_grade % 5 != 0:
                    current_grade += 1
                    steps += 1

                if steps < 3:
                    final_grade.append(current_grade)
                else:
                    final_grade.append(grades[i])
        else:
            final_grade.append(current_grade)

    return final_grade


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
