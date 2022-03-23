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
    count = 0
    for i in range(m, len(s)):
    #    print(i-m, i, squares[i-m:i], d)
        if sum(s[i-m:i]) == d:
            count += 1
        
    print(count) 
    return count

s = [1, 2, 1, 3, 2]
d = 3
m = 2
result = birthday(s, d, m)
