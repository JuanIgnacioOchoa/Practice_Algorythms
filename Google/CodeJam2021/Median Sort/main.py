import sys
from copy import deepcopy
from collections import defaultdict
import os
import time
import math
import random

start_time = time.time()

q = 0
def getMedian(a, b, c):
    if a > b:
        if a < c:
            median = a
        elif b > c:
            median = b
        else:
            median = c
    else:
        if a > c:
            median = a
        elif b < c:
            median = b
        else:
            median = c
    return median

def getJudgeMedian(a, b, c):
    #global q
    #q += 1
    #return getMedian(a, b, c)
    print(str(a) + " " + str(b) + " " + str(c))
    median = input()
    if median == "-1":
        sys.exit(0)
    return int(median)
def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in range(0, len(l), n))

def getExtremes(arr):
    if len(arr) == 1:
        return [arr[0]]
    elif len(arr) == 2:
        return [arr[0], arr[1]]
    middles = set()
    x = 0
    y = 1
    z = 2
    i = 0
    while len(middles) + 2 != len(arr):
        if not (x == y or x == z or y == z):
            middles.add(getJudgeMedian(arr[x], arr[y], arr[z]))
        if i % 3 == 0:
            z = (z + 1) % len(arr)
        elif i % 3 == 1:
            y = (y + 1) % len(arr)
        elif i % 3 == 2:
            x = (x + 1) % len(arr)
        i+=1
    extremes = []
    for x in arr:
        if x not in middles:
            #arr.remove(x)
            extremes.append(x)
    return extremes
def resize(arr):
    subArray = []
    i = 0
    while i < len(arr) - 5:
        subArray.append(arr[i: i + 5])
        i += 5
    subArray.append(arr[i: len(arr)])
    return subArray
def getExtremesAll(subArr):
    extremes = []
    for a in subArr:
        extremes.append(getExtremes(a))
    fullExtremes = []
    if len(extremes) == 1:
        return extremes[0]
    for e in extremes:
        fullExtremes = fullExtremes + e
    sub = resize(fullExtremes)
    return getExtremesAll(sub)
    
def sort(arr, N):
    sortedArr = [0] * N 
    extremes = []
    while len(arr):
        sub = resize(arr)
        tmp = getExtremesAll(sub)
        for t in tmp:
            arr.remove(t)
        extremes.append(tmp)
    back = int(N / 2) - 1
    front = int(N / 2)
    
    e1 = extremes[len(extremes) - 1]
    e2 = extremes[len(extremes) - 2]
    if len(e1) == 2:

        sortedArr[back] = e1[0]
        sortedArr[front] = e1[1]
        m = getJudgeMedian(e2[0], e1[0], e1[1])
        if sortedArr[back] == m:
            sortedArr[back-1] = e2[0]
            sortedArr[front+1] = e2[1]
        else:
            sortedArr[back-1] = e2[1]
            sortedArr[front+1] = e2[0]
        back -= 2
        front += 2
    else:
        sortedArr[back] = e1[0]
        back -= 1
        sortedArr[back] = e2[0]
        sortedArr[front] = e2[1]
        front += 1
        back -= 1
    for i in reversed(range(len(extremes) - 1)):
        if back < 0 or front >= N:
            continue
        e1 = extremes[i]
        e2 = extremes[i - 1]
        m = getJudgeMedian(e2[0], e1[0], e1[1])
        if sortedArr[back + 1] == m:
            sortedArr[back] = e2[0]
            sortedArr[front] = e2[1]
        else:
            sortedArr[back] = e2[1]
            sortedArr[front] = e2[0]
        back -= 1
        front += 1
        
    return sortedArr

T, N, K = map(int, input().split())
#T = 1
#N = 10
#arr = [i+1 for i in (range(N))]
for case in range(T):
    arr = [i+1 for i in (range(N))]
    a = sort(arr, N)
    print(' '.join(map(str,a)))
    input()
    ans = input()
    if ans == '-1':
        break

#print("--- %s seconds ---" % (time.time() - start_time))