#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    colors = dict()
    ans = 0
    for c in ar:
        if c not in colors:
            colors[c] = 1
        else :
            colors[c] += 1
    for key in colors:
        ans += int(colors[key]/2)
    return ans
n = 9

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

result = sockMerchant(n, ar)
print(result)
