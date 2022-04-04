from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()
inkSize = pow(10, 6)
def inkUsage(inks):
    for i in inks:
        if sum(i) < inkSize:
            return 'IMPOSSIBLE'
    C = min([inks[0][0], inks[1][0], inks[2][0]])
    M = min([inks[0][1], inks[1][1], inks[2][1]])
    Y = min([inks[0][2], inks[1][2], inks[2][2]])
    K = min([inks[0][3], inks[1][3], inks[2][3]])
    minInks = [C, M, Y, K]
    totalInk = sum(minInks)
    if totalInk < inkSize:
        return 'IMPOSSIBLE'
    else:
        diff = totalInk - inkSize
        if diff != 0:
            i = 0
            while diff != 0 and i < len(minInks):
                if (minInks[i] - diff) < 0:
                    diff -= minInks[i]
                    minInks[i] = 0
                else: 
                    minInks[i] = minInks[i] - diff
                    diff = 0
                i += 1
            if i > len(minInks) and diff != 0:
                return 'IMPOSSIBLE'
    return "" + str(minInks[0]) + " " + str(minInks[1]) + " " + str(minInks[2]) + " " + str(minInks[3])
dir = os.path.dirname(__file__)


#stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    ink = []
    for _ in range(3):
        ink.append(list(map(int, stdin.readline().split())))

    result = stdout.readline().strip()
    ans = inkUsage(ink)
    print(('Case #%d: %s') % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))