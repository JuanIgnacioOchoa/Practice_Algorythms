#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAYs s as parameter.
#
def isMagicSquare(s):
    n = len(s)
    magicNumber = (n*((n**2)+1))/2
    x = 0
    
    for i in range(n):
        x = 0
        for j in range(n):
            x += s[i][j]
        if x != magicNumber:
            return False
    for i in range(n):
        x = 0
        for j in range(n):
            x += s[j][i]
        if x != magicNumber:
            return False
    
    x = 0
    for i in range(n):
        x += s[i][i]
    if x != magicNumber:
        return False
    x = 0
    for i in range(n):
        x += s[i][n-i-1]
    if x != magicNumber:
        return False

    return True

def allMagicSquares():
    orig = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    all_squares = [orig]
    all_squares.append(orig[::-1])
    all_squares.append([i[::-1] for i in orig])
    all_squares.append(all_squares[2][::-1])
    all_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
    all_squares.append(all_squares[4][::-1])
    all_squares.append([i[::-1] for i in all_squares[4]])
    all_squares.append(all_squares[6][::-1])
    return all_squares

def diff(s1, s2):
    diff = 0
    for i in range(len(s1)):
        for j in range(len(s1)):
            diff += abs(s1[i][j] - s2[i][j])
    return diff
def formingMagicSquare(s):
    allSquares = allMagicSquares()
    result = diff(allSquares[0], s)
    for i in range(1, len(allSquares)):
        tmp = diff(allSquares[i], s)
        if tmp < result:
            result = tmp
    return result
s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
result = formingMagicSquare(s)
orig = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
all_squares = [orig]
all_squares.append(orig[::-1])
all_squares.append([i[::-1] for i in orig])
all_squares.append(all_squares[2][::-1])
all_squares.append([[4, 3, 8], [9, 5, 1], [2, 7, 6]])
all_squares.append(all_squares[4][::-1])
all_squares.append([i[::-1] for i in all_squares[4]])
all_squares.append(all_squares[6][::-1])