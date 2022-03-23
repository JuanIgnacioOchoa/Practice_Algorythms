#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#

def divisibleSumPairs(n, k, ar):
    result = 0
    for i in range(len(ar)-1):
        for j in range(i+1, len(ar)):
            if (ar[i] + ar[j]) % k == 0:
                result+=1
    return result

n = 6
k = 3
ar = [1, 3, 2, 6, 1, 2]
result = divisibleSumPairs(n, k, ar)