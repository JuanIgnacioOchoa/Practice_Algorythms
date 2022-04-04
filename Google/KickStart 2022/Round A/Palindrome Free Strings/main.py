from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

def isPallindrome(S):
    i = 0
    j = len(S) - 1
    while i < j:
        if S[i] != S[j]:
            return False
        i += 1
        j -= 1
    return True
def findAllStrings(index, S, subs):
    while index < len(S):
        if S[index] == '?':
            tmp = S
            tmp1 = deepcopy(tmp)
            tmp1[index] = '0'
            tmp2 = deepcopy(tmp)
            tmp2[index] = '1'
            findAllStrings(index, tmp1, subs)
            findAllStrings(index, tmp2, subs)
            return
        index += 1
    subs.append(S)
def isPallindromePossible(N, S):
    questionMarks = []
    i = 0
    while i < len(S):
        if S[i] == "?":
            questionMarks.append(i)
        i+=1
    subs = []
    findAllStrings(0, list(S), subs) 
    ans = False
    q = 0
    values = [-1] * len(S)
    for s in subs:
        i = 0
        while i < N - 4:
            sub = s[i: i+5]
            res = isPallindrome(sub)
            for q in questionMarks:
                if i <= q < i + 5:
                    if res:
                        if values[q] == -1:
                            values[q] = s[q]
                        elif values[q] != s[q]:
                            return "IMPOSSIBLE"
            
            i+=1
    return 'POSSIBLE'
dir = os.path.dirname(__file__)

stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = int(stdin.readline())
    S = stdin.readline().strip()
    result = stdout.readline().strip()
    tmpAns = isPallindromePossible(N, S)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))