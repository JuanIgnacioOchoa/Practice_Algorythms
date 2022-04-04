from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

def getArray(N, C):
    if N > C:
        return 'IMPOSSIBLE'
    worstArr = [i+1 for i in reversed(range(N))]

    return " "
dir = os.path.dirname(__file__)

#stdin = open(os.path.join(dir,  'test_data/test_set_2/ts2_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    A = stdin.readline().split(' ')
    N = int(A[0])
    C = int(A[1])
    result = stdout.readline().strip()
    tmpAns = getArray(N, C)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))