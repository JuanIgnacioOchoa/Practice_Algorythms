#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    k1 = x1
    k2 = x2
    while k1 != k2:
        if (v2 > v1 and k2 > k1) or (v1 > v2 and k1 > k2) or (v2 == v1 and k1 != k2):
            return "NO"
        k1 += v1
        k2 += v2
        
    return "YES"
x1 = 0
v1 = 2
x2 = 5
v2 = 3
kangaroo(x1, v1, x2, v2)
