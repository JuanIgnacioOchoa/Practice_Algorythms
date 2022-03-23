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

def grade(grade):
    if grade < 38:
        return grade
    elif grade % 5 == 0:
        return grade
    else:
        x = grade % 5
        if x >= 3:
            return grade + (5 - x)
        else:
            return grade

def gradingStudents(grades):
    result = []
    for g in grades:
        result.append(grade(g))
    return result

#if __name__ == '__main__':
#fptr = open(os.environ['OUTPUT_PATH'], 'w')

grades_count = 4#int(input().strip())

grades = [73, 67, 38, 33]

#for _ in range(grades_count):
#    grades_item = int(input().strip())
#    grades.append(grades_item)

result = gradingStudents(grades)
print(result)
