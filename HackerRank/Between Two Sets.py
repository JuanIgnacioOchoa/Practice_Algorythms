#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    result = []
    for i in range(a[0], b[-1] + 1):
        if all(i%x==0 for x in a) and all(x%i==0 for x in b):
            result.append(i)
    return None

arr = [2, 4]
brr = [16, 32, 96]
total = getTotalX(arr, brr)