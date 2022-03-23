#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    max = -1
    keyboards.sort()
    drives.sort()
    vali = 0
    valj = 0
    i = 0
    j = 0
    for i in keyboards:
        for j in drives:
            sum = i+j
            if sum<=s:
                if sum>max:
                    max = sum
    return max

        

n = 3
m = 6
result = getMoneySpent([4], [4], 5)
print(result)