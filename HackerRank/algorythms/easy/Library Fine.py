#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

def libraryFine(d1, m1, y1, d2, m2, y2):
    ans = 0
    x1 = '%d-%d-%d' % (y1, m1, d1)
    x2 = '%d-%d-%d' % (y2, m2, d2)
    days = days_between(x1, x2)
    if y1 > y2:
        ans = 10000*days
    elif m1 > m2:
        ans = 500*days
    elif d1 > d2:
        ans = 15 * days
    print(ans)
    return ans

libraryFine(2, 7, 1014, 1, 1, 1014)