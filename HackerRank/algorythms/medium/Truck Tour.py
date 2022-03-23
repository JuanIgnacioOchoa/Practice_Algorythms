#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#

def truckTour(petrolpumps):
    ans = -1
    i = 0
    n = len(petrolpumps)
    pumps = [len(petrolpumps)+1] * len(petrolpumps)
    print(pumps)
    while i < n:
        p1 = petrolpumps[i]
        curr= p1[0] - p1[1]
        if curr < 0:
            i+=1
            continue
        j = 0
        while j < n - 1:
            k = (i + j+ 1) % n
            p2 = petrolpumps[k]
            curr += p2[0]
            curr -= p2[1]
            
            if curr < 0:
                j = n
                continue
            j+=1
        if i > ans:
            ans = i
            break
        i+=1
    return ans

if __name__ == '__main__':
    n = 3

    petrolpumps = [
        [4, 6], 
        [7, 3],
        [4, 5],
        [6, 5]]


    result = truckTour(petrolpumps)

