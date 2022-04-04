from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

dir = os.path.dirname(__file__)

def getNumberOfDice(N, S):
    ans = 0
    S.sort()
    for i in range(N):
        if S[i] > ans:
            ans += 1
    return ans

#stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = int(stdin.readline().strip())
    S = list(map(int, stdin.readline().split()))
    ans = getNumberOfDice(N, S)
    print(('Case #%d: %s') % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))