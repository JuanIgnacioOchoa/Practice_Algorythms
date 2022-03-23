#!/bin/python3

import math
import os
import random
import re
import sys




    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
def delete(s, k):
    return s[:-k]
def add(s, k):
    return s + k
tests = 8#int(input())
s = ""
queries = [
    [1, 'abc'],
    [3, 3],
    [2, 3],
    [1, 'xy'],
    [3, 2],
    [4],
    [4],
    [3, 1],

]
prev = []
for tests_itr in range(tests):
    q = queries[tests_itr]
    action = q[0]
    
    if action == 1:
        prev.append([1, len(q[1])])
        s = add(s, q[1])
    elif action == 2:
        tmp = s[len(s) - q[1]: len(s)]
        prev.append([2, tmp])
        s = delete(s, q[1])
    elif action == 3:
        print(s[q[1]-1])
    elif action == 4:
        if len(prev) > 0:
            tmp = prev.pop()
            if tmp[0] == 1:
                s = delete(s, tmp[1])
            elif tmp[0] == 2:
                s = add(s, tmp[1])
                
            
        #fptr.write(str(result) + '\n')

    #fptr.close()

    