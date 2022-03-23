#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'taskOfPairing' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY freq as parameter.
#
def maxPairs(freq):
    if freq == None or len(freq) == 0:
        return 0
    count = 0
    for i in range(1, len(freq) - 1):
        pairs1 = min(freq[i-1], freq[i])
        pairs2 = min(freq[i], freq[i + 1])
        if pairs1 >= pairs2:
            count += pairs1
            freq[i] -= pairs1
            freq[i-1] -= pairs1
        else:
            count += pairs2
            freq[i] -= pairs2
            freq[i-1] -= pairs2
    for j in range(len(freq)):
        pairs = int(freq[j] / 2)
        count+= pairs
        freq[j] = 0 if freq[j] % 2 == 0 else 1
        if i > 0 and freq[j - 1] == 1 and freq[j] == 1:
            count+=1
            freq[j - 1] = 0
            freq[j] = 0
    return count


def taskOfPairingJI(freq):
    result1 = 0
    result2 = 0
    weigths = dict()
    subW = dict()
    for i in range(0, len(freq)):
        weigths[i+1] = freq[i]
        subW[i+1] = 0
    tmpW = weigths
    tmpSub = subW
    for key in tmpW:
        subW[key] = tmpW[key] % 2
        result1 += int(tmpW[key] / 2)
    i = 1
    print(subW)
    while i < len(subW) - 1:
        if subW[i+1] > 0:
            if subW[i] > 0:
                result1+=1
                subW[i] -= 1
                subW[i+1] -= 1
            elif subW[i + 2] > 0:
                result1 +=  1
                subW[i+2] -= 1
                subW[i+1] -= 1
        i+=1

    print(subW)
    for key in tmpW:
        tmpSub[key] = tmpW[key] % 2
        result2 += int(tmpW[key] / 2)
    i = 1
    print(tmpSub)
    while i < len(tmpSub) - 1:
        if tmpSub[i+1] > 0:
            if tmpSub[i] > 0:
                result2+=1
                tmpSub[i] -= 1
                tmpSub[i+1] -= 1
            elif tmpSub[i + 2] > 0:
                result2 +=  1
                tmpSub[i+2] -= 1
                tmpSub[i+1] -= 1
        i+=1

    print(tmpSub)
    return result1 if result1 > result2 else result2

def taskOfPairing1(freq):
    ans = 0
    rem = 0
    for i in range(len(freq)):
        if freq[i] != 0:
            ans += (freq[i] + rem) / 2
            rem = (freq[i] + rem) % 2
        else:
            rem = 0
    return ans



freq_count = 3

freq =  [1,1,5,1,1,2,1,1,1,7,1,1,1]
freq1 = [1,1,5,1,1,2,1,1,1,7,1,1,1]
freq2 = [1,1,5,1,1,2,1,1,1,7,1,1,1]
result1 = taskOfPairing1(freq)#taskOfPairing(freq)
result2 = maxPairs(freq1)#taskOfPairing(freq)
result3 = taskOfPairingJI(freq2)#taskOfPairing(freq)
print(result1)
print(result2)
print(result3)
a = 0
