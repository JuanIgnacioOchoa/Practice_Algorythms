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

def getWays2(n, c, coins, ans, ans2):
    ans1 = []
    for i in range(len(ans)):
        ans1.append(ans[i])
    if c :
        ans1.append(c)
    if n == 0:
        return ans2.append(ans1)
    elif n < 0:
        return 
    
    for c in coins:
        getWays2(n - c, c, coins, ans1, ans2)
    
def getWays1(n, coins):
    ans2 = []
    getWays2(n, None, coins, [], ans2)
    ans = []
    for i in ans2:
        i.sort()
        if i not in ans:
            ans.append(i)
    return len(ans)

def getWays(n, coins):
    ans = 0
    dp = dict()
    dp = [1] + [0] * n
    for c in coins:
        for i in range(c, n+1):
            dp[i] += dp[i-c]
        

    return ans[len(ans) -1 ]

first_multiple_input = "100 3".strip().split(" ")

coins = list(map(int, "1 99 100".rstrip().split()))

result = getWays(int(first_multiple_input[0]), coins)
print(result)