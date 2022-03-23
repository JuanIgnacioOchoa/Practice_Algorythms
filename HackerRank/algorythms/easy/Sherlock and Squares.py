import math
import os
import random
import re
import sys

def squares(a, b):
    ans = 0
    x = (math.sqrt(a))
    x = math.ceil(x)
    sq = x**2
    while sq <= b:
        x+=1
        sq = x**2
        ans +=1
    return ans


squares(17, 24)