
from sys import stdin, stdout
from collections import defaultdict
from copy import deepcopy
import os
import time
import itertools

start_time = time.time()

def sortInitiators(F, ini):
    res = []
    tmp = []
    for i in ini:
        x = [i, F[i]]
        tmp.append(x)
    tmp.sort(key = lambda x: x[1])
    return tmp
        
def getInitiators(P):
    indicators = []
    modules = set()
    for i in range(len(P)):
        modules.add(P[i])

    for i in range(len(P)):
        if (i + 1) not in modules:
            indicators.append(i)
    return indicators

def getOveralFun(F, current, adj, lst, res):
    if len(adj[current]) == 0:
        lst.append(F[current])
        return max(lst)
    elif len(adj[current]) > 1 and current == -1:
        tmpLst = []
        for x in adj[current]:
            tmp = getOveralFun(F, x, adj, [], res)
            if tmp != None:
                tmpLst.append(tmp)
        #tmpLst.remove(min(tmpLst))
        for t in tmpLst:
            res.append(t)
        x = 0
    elif len(adj[current]) > 1:
        tmpLst = []
        for x in adj[current]:
            tmp = getOveralFun(F, x, adj, [], res)
            if tmp != None:
                tmpLst.append(tmp)
        tmpLst.append(F[current])
        tmpLst.remove(min(tmpLst))
        for t in tmpLst:
            res.append(t)
        x = 0
    elif current != -1:
        lst.append(F[current])
        return getOveralFun(F, adj[current][0], adj, lst, res)
    else:
        return getOveralFun(F, adj[current][0], adj, lst, res)


def getFun(N, F, P):
    adj = defaultdict(list)

    dic = {}
    for i in range(N):
        if P[i] == 0:
            dic[i] = [-1, -1]
        else:
            dic[i] = [P[i] - 1, F[P[i] - 1]]
        adj[P[i] - 1].append(i)
    res = []
    ini = getInitiators(P)
    sortIni = sortInitiators(F, ini)
    triggered = []
    tmp = 0
    i = 0
    while i < len(sortIni):
        res = []
        t1 = deepcopy(triggered)
        getFun3(F, P, res, sortIni[i], t1, dic)
        res1 = []
        t2 = deepcopy(triggered)
        if i + 1 < len(sortIni):
            getFun3(F, P, res1, sortIni[i + 1], t2, dic)
            res.sort(key = lambda x: x[1], reverse=True)
            res1.sort(key = lambda x: x[1], reverse=True)
            j = 0
            while res[j] in res1:
                j+=1
            if res[j][1] > res[j][1]:
                triggered = deepcopy(t2)
                tmp += (res1[0][1])
            else:
                triggered = deepcopy(t1)
                tmp += (res[0][1])
        else:

            res.sort(key = lambda x: x[1], reverse=True)
            tmp += res[0][1]
        i+=1
    return tmp
    #while len(res) > len(ini):
    #    res.remove(min(res))
    #return sum(res)

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
    ans = getFun(N, F, P)
    print(('Case #%d: %s') % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))