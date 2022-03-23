#!/bin/python3

import math
import os
import random
import re
import sys
import time
start_time = time.time()

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def insert(val, arr):
    i = 0
    j = len(arr) - 1
    while i < len(arr) and arr[i] < val:
        if arr[j] < val:
            i = j
            break
        if arr[i] > val:
            break
        i+=1
        j-=1
    arr.insert(i, val) 
def cookies(k, A):
    arr = A
    arr.sort()
    ans = 0
    while (min(arr) < k) and len(arr) >= 2:
        c1 = arr.pop(0)
        c2 = arr.pop(0)
        c = (c1 * 1) + (c2*2)
        insert(c, arr)
        ans += 1
    if min(arr) < k:
        return -1
    return ans


dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'input.txt'),'r')

first_multiple_input = inp.readline().rstrip().split()

n = int(first_multiple_input[0])

#k = int(first_multiple_input[1])

#A = list(map(int, inp.readline().rstrip().split()))
k = 9
A = [1, 2, 3, 9, 10, 12]
result = cookies(k, A)
print("--- %s seconds ---" % (time.time() - start_time))