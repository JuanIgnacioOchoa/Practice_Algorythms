
from collections import defaultdict
from copy import deepcopy
from sys import stdin, stdout
import os
import time
import itertools


start_time = time.time()

class Node():
    def __init__(self, n, w):
        self.n = n
        self.w = w
        self.children = []
        self.father = None

    def addChild(self, child):
        child.father = self.n
        self.children.append(child)

    def dfs(self):
        global score
        if len(self.children) == 0:
            return self.w
        childAnswer = []
        for n in self.children:
            childAnswer.append(n.dfs())
        childAnswer.sort()
        for i in range(1, len(self.children)):
            score+=childAnswer[i]
        
        return max(self.w, childAnswer[0])

def getScore(nodes, P):
    ans = 0
    ini = getInitiators(P)
    res = []
    N = len(P)
    
    while N > 0:
        while N not in ini and N > 0:
            N -= 1
        curr = nodes[N]
        
        childAnswers = []
        for n in curr.children:
            childAnswers.append(n.w)
        childAnswers.sort()
        for i in range(1, len(childAnswers)):
            res.append(childAnswers[i])
            ans += childAnswers[i]
        if len(childAnswers):
            curr.w = max(curr.w, childAnswers[0])
        if curr.father == 0:
            ans += curr.w
            N-=1
            continue
        ini[curr.father] = False
        N-=1
        #ini.sort()
    return ans

def getInitiators(P):
    indicators = {}
    modules = set()
    for i in range(len(P)):
        modules.add(P[i])

    for i in range(len(P)):
        if (i + 1) not in modules:
            indicators[i + 1] = False
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


def buildTree(nodes, F, P):
    nodes[0] = Node(0, -1)
    n = len(F)
    for i in range(n):
        nodes[i + 1] = Node(i + 1, F[i])
        nodes[P[i]].addChild(nodes[i + 1])
    return
dir = os.path.dirname(__file__)

#stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    score = 0
    N = int(stdin.readline().strip())
    F = list(map(int, stdin.readline().split()))
    P = list(map(int, stdin.readline().split()))
    nodes = [None] * (N + 1)
    buildTree(nodes, F, P)
    score = getScore(nodes, P)
    
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