#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total = sum(bill)
    anna = (total - bill[k])/2
    return "Bon Appetit" if anna >= b else b - anna
n = 4

k = 1

bill = [3,10,2,9]

b = 12

bonAppetit(bill, k, b)
