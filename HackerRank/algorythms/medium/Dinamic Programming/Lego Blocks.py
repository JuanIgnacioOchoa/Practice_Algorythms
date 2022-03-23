#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
MOD=10**9+7

def oneRow(w):
    ans = []
    arr = []
    i = 0
    startIndex = i
    while i < len(legos):
        if legos[i][2] <= w - sum(arr):
            arr.append(legos[i][2])
            i-=1
        elif sum(arr) == w:
            i = startIndex
            startIndex+=1
            ans.append(arr)
            arr = []
        i+=1
    return ans
def legoBlocks(h, w):
    tmpW = 0
    ans = []
    arr = []
    i = 0
    startIndex = i
    while i < len(legos):
        if legos[i][2] <= w - sum(arr):
            arr.append(legos[i][2])
            i-=1
        elif sum(arr) == w:
            i = startIndex
            startIndex+=1
            ans.append(arr)
            arr = []
        i+=1
    return ans


result = legoBlocks(1, 2)
print(result)