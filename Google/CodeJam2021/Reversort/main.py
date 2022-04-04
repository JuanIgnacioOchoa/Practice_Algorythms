from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

def costReversort(N, L):
    i = 0
    cost = 0
    while i < N - 1:
        sub = L[i:N]
        j = sub.index(min(sub))
        #L[i], L[m] = L[m], L[i]
        sub = L[i: i + j + 1]
        sub.reverse()
        L = L[0: i] + sub + L[i + j + 1: N]
        xi = i + 1
        xj = j + i + 1
        c = xj - xi + 1
        cost = cost + c
        i+=1
    return cost
dir = os.path.dirname(__file__)

stdin = open(os.path.join(dir,  'test_data/test_set_2/ts2_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = int(stdin.readline().strip())
    L = list(map(int, stdin.readline().split(' ')))
    result = stdout.readline().strip()
    tmpAns = costReversort(N, L)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
        tmpAns = costReversort(N, L)
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))