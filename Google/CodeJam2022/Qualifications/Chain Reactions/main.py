
from re import I
from sys import stdin, stdout
from collections import defaultdict
from copy import deepcopy
import os
import time
import itertools
from unittest import result

start_time = time.time()


def getInitiators(P):
    indicators = []
    modules = set()
    for i in range(len(P)):
        modules.add(P[i])

    for i in range(len(P)):
        if (i + 1) not in modules:
            indicators.append(i)
    return indicators

## TEST 1
def getFun3(F, P, res, curr, triggered, dic):
    
    while not (curr in triggered or curr[0] == -1):
        res.append(curr)
        triggered.append(curr)
        curr = dic[curr[0]]

def getAllCombinations(ini):
    res = []
    for comb in itertools.permutations(ini, len(ini)):
        res.append(comb)
    return res

def getFun2(N, F, P):   
    ini = getInitiators(P)
    comb = getAllCombinations(ini)
    ans = 0
    for var in comb:
        triggered = []
        
        tmp = 0
        for v in var:
            res = []
            getFun3(F, P, res, v, triggered)
            tmp += max(res)
        if tmp > ans:
            ans = tmp
    return ans


# TEST 2
def getScore(N, F, P):
    ini = getInitiators(P)
    score = 0
    for i in ini:
        curr = i
        prev = curr
        while curr != -1:
            
            father = P[curr] - 1
            if father == -1:
                score += F[curr]
                F[curr] = F[prev]
            else:
                if F[curr] > F[father]:
                    F[father], F[curr] = F[curr], F[father]
            prev = curr
            curr = father
    return score
dir = os.path.dirname(__file__)


#stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = int(stdin.readline().strip())
    F = list(map(int, stdin.readline().split()))
    P = list(map(int, stdin.readline().split()))
    score = getScore(N, F, P)
    res = stdout.readline().strip()
    ans = ('Case #%d: %s') % (case+1, score)
    if ans != res:
        print('Case #%d: Error, %d' % (case+1, score))
        print(res)
        #tmpAns = checksum(A, B, n)
    else:
        print(ans)
    #print(('Case #%d: %s') % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))