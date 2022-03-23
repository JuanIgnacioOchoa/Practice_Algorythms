#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5
    liked = int(shared/2)
    result = liked
    for _ in range(1, n):
        shared = liked * 3
        liked = int(shared/2)
        result += liked
    return result

n=3
result = viralAdvertising(n)
