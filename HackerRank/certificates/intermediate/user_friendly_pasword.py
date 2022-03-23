#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'authEvents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY events as parameter.
#
def hashFuntion(f, p):
    return f*131**(p)
def getCode(s):
    res = 0
    i = 0
    while i < len(s):
        x = hashFuntion(ord(s[i]), len(s) - i - 1)
        res += x
        i += 1
    res = res % ((10**9) + 7)
    return str(res)
def authEvents(events):
    codePswd = ""
    pswd = ""
    result = []
    otherPossible = dict()
    for action, s in events:
        if action == 'setPassword':
            pswd = s
            codePswd = getCode(s)
        elif action == "authorize":
            if codePswd == s:
                result.append(1)
            else:
                first = int(getCode(pswd+chr(0)))
                final = int(getCode(pswd+chr(127)))
                tmp = int((s))
                if tmp >= first and tmp <= final:
                    result.append(1)
                else:
                    result.append(0)
                p = 0
    return result 


events = [['setPassword', '000A'], ['authorize', '108738450'], ['authorize', '108738449'], ['authorize', '244736787']]
#events = [
#    ["setPassword", "1"],
#    ["setPassword", "2"],
#    ["setPassword", "4"],
#    ["authorize", "49"],
#    ["authorize", "50"]
#]
authEvents(events)
