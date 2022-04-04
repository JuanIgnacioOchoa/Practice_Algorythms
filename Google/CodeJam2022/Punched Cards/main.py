from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

def line1(R, C):
    line = ""
    for i in range(C * 2 + 1):
        if i % 2 == 0:
            line += "+"
        else:
            line += "-"
    return line

def line2(R, C):
    line = ""
    for i in range(C * 2 + 1):
        if i % 2 == 0:
            line += "|"
        else:
            line += "."
    return line
def drawPunchCard(R, C):
    ans = []
    line = ".."
    for i in range(2, C * 2 + 1):
        if i % 2 == 0:
            line += "+"
        else:
            line += "-"
    ans.append(line)
    line = ".."
    for i in range(2, C * 2 + 1):
        if i % 2 == 0:
            line += "|"
        else:
            line += "."
    ans.append(line)
    for i in range(R - 1):
        ans.append(line1(R, C))
        ans.append(line2(R, C))
    
    ans.append(line1(R, C))
    return ans
dir = os.path.dirname(__file__)


#stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    A = stdin.readline().strip().split(' ')
    R = int(A[0])
    C = int(A[1])
    result = stdout.readline().strip()
    ans = drawPunchCard(R, C)
    print(('Case #%d:') % (case+1))
    for i in range( 2 * R + 1):
        result = stdout.readline().strip()
        print(ans[i])
print("--- %s seconds ---" % (time.time() - start_time))