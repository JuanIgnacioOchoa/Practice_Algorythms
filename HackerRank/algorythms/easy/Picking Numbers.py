#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    numbers = dict()
    ans = 0
    for n in a:
        if n not in numbers:
            sumP = 0
            sumM = 0
            j = 0
            while j < len(a):
                if (n - a[j]) <= 1 and (n - a[j]) >= 0:
                    sumM += 1
                if (a[j] - n) <= 1 and (a[j] - n) >= 0:
                    sumP += 1
                j += 1
            numbers[n] = [sumP, sumM]
            if ans < sumP:
                ans = sumP
            if ans < sumM:
                ans = sumM
    return ans


n = 6

a = [1,2,2,3,1,2]

result = pickingNumbers(a)
print(result)