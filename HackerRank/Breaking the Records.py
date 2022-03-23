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
    h = scores[0]
    l = scores[0]
    result = [0, 0]
    for i in range(1, len(scores)):
        score = scores[i]
        if score < l:
            l = score
            result[1]+=1
        elif score > h:
            h = score
            result[0] += 1
    return result

scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
result = breakingRecords(scores)
