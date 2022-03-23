#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def isAppleIn(s, t, a, apple):
    if apple < 0:
        return 0
    elif (a + apple) >= s and (a + apple) <= t:
        return 1
    
    return 0


def isOrangeIn(s, t, b, orange):
    if orange > 0:
        return 0
    elif (b + orange) >= s and (b + orange) <= t:
        return 1
    
    return 0
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applesIn = 0
    orangesIn = 0
    for apple in apples:
        applesIn += isAppleIn(s, t, a, apple)

    for orange in oranges:
        orangesIn += isOrangeIn(s, t, b, orange)

    return None


s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
apples = [-2,2,1]
oranges = [5, -6]
countApplesAndOranges(s, t, a, b, apples, oranges)
    
