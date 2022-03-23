#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix)/2
    v = 0
    for i in range(n):
        for j in range(n):
            l = []
            k = 2 * n - 1
            l.append(matrix[i][j]) # current matrix
            l.append(matrix[k - i][j])  # bottom left
            l.append(matrix[i][k - j]) # top right
            l.append(matrix[k - i][k - j]) # bottom right
    
            maxv = max(l)
            
            v += maxv
    return v
m = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
flippingMatrix(m)
