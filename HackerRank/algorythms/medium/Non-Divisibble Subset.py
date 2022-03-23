#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#
def nonDivisibleSubset(k, s):
    ans = 0
    h = dict()

    for i in range(len(s)):
        m = s[i] % k
        if m not in h:
            h[m] = 0
        h[m] += 1

    i = 1
    j = k -1
    if 0 in h:
        ans += 1
    if k%2 == 0 and k/2 in h:
        ans+=1
    while i < j:
        if i not in h and j not in h:
            i+=1
            j-=1
            continue
        if i not in h:
            ans += h[j]
        elif j not in h:
            ans += h[i]
        else:
            if h[i] > h[j]:
                ans+=h[i]
            else:
                ans+=h[j]
        i+=1
        j-=1
            

    return ans

n = 4#int(first_multiple_input[0])

k = 4

s = list(map(int, "1 2 3 4 5 6 7 8 9 10".rstrip().split()))

result = nonDivisibleSubset(k, s)
print('a')
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = 4#int(first_multiple_input[0])

    k = 4

    s = [19,10,12,10,24,25,22]

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
"""