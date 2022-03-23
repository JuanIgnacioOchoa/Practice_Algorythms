#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#


def dayOfProgrammer(year):
    day = 0
    if year == 1918 
        day = 26
    elif year > 1918:
        x = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)
        day = 256 - x
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            day -= 1
    else:
        x = (31 + 28 + 31 + 30 + 31 + 30 + 31 + 31)
        day = 256 - x
        if year % 4 == 0:
            day -= 1
    return str(day) + ".09." + str(year)


year = 1800

result = dayOfProgrammer(year)
