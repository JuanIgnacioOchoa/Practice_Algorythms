from sys import stdin, stdout
import os
import time
from collections import defaultdict
start_time = time.time()

class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def silly_substitutions(S):
    tail = head = Node(S[0])
    lookup = defaultdict(set)
    cnt = 0
    for i in xrange(1, len(S)):
        node = Node(S[i], left=tail)
        node.left.right = node
        if (int(tail.val)+1)%10 == node.val:
            lookup[tail.val].add(tail)
            cnt += 1
        tail = node
    i = 0
    while cnt:
        while lookup[i]:
            node = lookup[i].pop()
            cnt -= 1
            if node.left and node.left in lookup[node.left.val]:
                lookup[node.left.val].remove(node.left)
                cnt -= 1
            if node.right in lookup[node.right.val]:
                lookup[node.right.val].remove(node.right)
                cnt -= 1
            node = Node((i+2)%10, left=node.left, right=node.right.right)
            if node.left:
                node.left.right = node
            else:
                head = node
            if node.right:
                node.right.left = node
            # the number of inital nodes of interest is at most O(N).
            # we will remove at most O(N) nodes.
            # for each remove, at most 2 nodes of interest are added.
            # the total number of added nodes of interest will be at most O(3N)
            if node.left and (node.left.val+1)%10 == node.val and node.right and (node.val+1)%10 == node.right.val:
                x1 = 0
            if node.left and (node.left.val+1)%10 == node.val:
                lookup[node.left.val].add(node.left)
                cnt += 1
            if node.right and (node.val+1)%10 == node.right.val:
                lookup[node.val].add(node)
                cnt += 1
        i = (i+1)%10
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.right
    return "".join(result)
def silly_substitutions2(S):
    tail = head = Node(S[0])
    lookup = defaultdict(set)
    cnt = 0
    for i in xrange(1, len(S)):
        node = Node(S[i], left=tail)
        node.left.right = node
        if (tail.val+1)%10 == node.val:
            lookup[tail.val].add(tail)
            cnt += 1
        tail = node
    i = 0
    while cnt:
        while lookup[i]:
            node = lookup[i].pop()
            cnt -= 1
            if node.left and node.left in lookup[node.left.val]:
                lookup[node.left.val].remove(node.left)
                cnt -= 1
            if node.right in lookup[node.right.val]:
                lookup[node.right.val].remove(node.right)
                cnt -= 1
            node = Node((i+2)%10, left=node.left, right=node.right.right)
            if node.left:
                node.left.right = node
            else:
                head = node
            if node.right:
                node.right.left = node
            # the number of inital nodes of interest is at most O(N).
            # we will remove at most O(N) nodes.
            # for each remove, at most 1 node of interest is needed to add.
            # the total number of added nodes of interest will be at most O(2N)
            if node.left and (node.left.val+1)%10 == node.val and \
               (not node.left.left or (node.left.left.val+1)%10 != node.left.val):
                # assume current replace is (01), and both two possible interests (12) and (23) exist
                # - (^|[1-9])1(01)3 => (^|[1-9])1(2)3,
                #   since (12) is prior to (23), (^|[1-9])(1(2))3 => (^|[1-9])(3)3,
                #   only need to mark (12) as interest
                # - 01(01)3 => 01(2)3,
                #   since (01) is prior to (12) and (23), (01)(2)3 => (2)(2)3,
                #   only need to mark (23) as interest
                lookup[node.left.val].add(node.left)
                cnt += 1
            elif node.right and (node.val+1)%10 == node.right.val:
                lookup[node.val].add(node)
                cnt += 1
        i = (i+1)%10
    result = []
    curr = head
    while curr:
        result.append(str(curr.val))
        curr = curr.right
    return "".join(result)

def changeContinous(s, x):
    if x >= len(s) - 1 or s[x+1] == '\n':
        if s[x+1] == '\n':
            return x - 1
        return x + 1
    x1 = int(s[x+1])
    x2 = int(s[x])
    a1 = 10 - abs(x1 - x2)
    a2 = abs(x1 - x2)
    while x < len(s) - 1 and s[x+2] != '\n' and (a1 == 2 or a2 == 2):
        x+=1
        x1 = int(s[x+1])
        x2 = int(s[x])
        a1 = 10 - abs(x1 - x2)
        a2 = abs(x1 - x2)
    if s[x] == '\n':
        return x
    return x + 1
def subs(s):
    ans = s
    i = 0
    prev = ""
    while prev != s:
        prev = s
        while "01" in s:
            i = s.find("01")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("01", "2")
        while "12" in s:
            i = s.find("12")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("12", "3")
        while "23" in s:
            i = s.find("23")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("23", "4")
        while "34" in s:
            i = s.find("34")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("34", "5")
        while "45" in s:
            i = s.find("45")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("45", "6")
        while "56" in s:
            i = s.find("56")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("56", "7")
        while "67" in s:
            i = s.find("67")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("67", "8")
        while "78" in s:
            i = s.find("78")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("78", "9")
        while "89" in s:
            i = s.find("89")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("89", "0")
        while "90" in s:
            i = s.find("90")
            x = changeContinous(s, i + 1)
            if i + 2 < x:
                tmp = str(int(s[x-1]) + 1)
                tmp2 = s[i: x]
                s = s.replace(tmp2, tmp)
            else :
                s = s.replace("90", "1")
    if s[-1] == "\n":
        s = s[:-1]
    return(s)
dir = os.path.dirname(__file__)

inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())


for case in range(t):
    
    n = int(inp.readline())
    s = map(int, list(inp.readline().strip()))
    #s = inp.readline()
    result = (out.readline())[:-1]
    if case == 7:
        p = 0
    ans = ('Case #%d: %s') % (case+1, silly_substitutions(s))
    if ans != result:
        print 'Case #%d: Error' % (case+1)
    #else:
        
        #print 'Case #%d: %s' % (case+1, ans)


print("--- %s seconds ---" % (time.time() - start_time))