from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

dir = os.path.dirname(__file__)

def deleteLetters(I, P):
    ans = 0
    i = 0
    while len(P) > len(I) and I != P:
        if i > len(I) - 1 or P[i] != I[i]:
            if i == 0:
                P = P[1:]
            else:
                P = P[:i] +  P[i+1:]
            ans += 1
            i-=1
        i+=1
    if len(I) >= len(P) and I != P:
        return 'IMPOSSIBLE'
    return ans
stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    I = stdin.readline().strip()
    P = stdin.readline().strip()
    result = stdout.readline().strip()
    tmpAns = deleteLetters(I, P)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
        tmpAns = deleteLetters(I, P)
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))