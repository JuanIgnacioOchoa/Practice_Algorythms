#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))
arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
result = migratoryBirds(arr)