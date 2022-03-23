#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):

    i = 0
    j = len(s)-1
    while i < len(s) / 2:
        if s[i] != s[j]:
            if s[i] == s[j-1]:
                return j
            elif s[i+1] == s[j]:
                return i
        j -= 1
        i += 1
    return -1


s = "hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh"
res = palindromeIndex(s)
n = len(s)
x = s[res]
x3 = s[0 : res : ] + s[res + 1 : :]
x1 = x3[ :len(s)/2 + 1]
x2 = x3[len(s)/2 - 1: ]
x2 = x2[::-1]
p = 1


