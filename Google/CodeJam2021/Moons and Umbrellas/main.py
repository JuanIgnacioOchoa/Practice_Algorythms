from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

def jamal(X, Y, S):
    ans = 0
    N = len(S)
    i = 0
    while i < N:
        s = S[i]
        if s == '?':
            j = i
            sj = S[j]
            while sj == '?' and j < N - 1:

                j += 1
                sj = S[j]
            if sj == '?' and j == N - 1 and i != j:
                pass
            elif i != j:
                j -= 1
            
            
            if i != 0 and j != N - 1:
                if S[i - 1] == S[j + 1]:
                    pass
                else:
                    cost1 = None
                    cost2 = None
                    if S[i-1] == 'C':
                        cost1 = X
                    elif S[i - 1] == 'J':
                        cost1 = Y
                    if S[j + 1] == 'J':
                        cost2 = X
                    elif S[j + 1] == 'C':
                        cost2 = Y
                    ans += min(cost1, cost2)
            i = j
        elif i < N - 1:
            if s == 'C' and S[i+1] == 'J':
                ans += X
            elif s == 'J' and S[i+1] == 'C':
                ans += Y
        i+=1
    return ans
dir = os.path.dirname(__file__)

stdin = open(os.path.join(dir,  'test_data/test_set_3/ts3_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_3/ts3_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    A = stdin.readline().split(' ')
    X = int(A[0])
    Y = int(A[1])
    S = A[2].strip()
    result = stdout.readline().strip()
    tmpAns = jamal(X, Y, S)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
        tmpAns = jamal(X, Y, S)
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))