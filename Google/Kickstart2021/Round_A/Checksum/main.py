from sys import stdin, stdout, maxsize
from copy import deepcopy
from collections import defaultdict
import os
import time
start_time = time.time()
"""
Problem
Grace and Edsger are constructing a N×N boolean matrix A. The element in i-th row and j-th column is represented by Ai,j. They decide to note down the checksum (defined as bitwise XOR of given list of elements) along each row and column. Checksum of i-th row is represented as Ri. Checksum of j-th column is represented as Cj.

For example, if N=2, A=[1101], then R=[10] and C=[01].

Once they finished the matrix, Edsger stores the matrix in his computer. However, due to a virus, some of the elements in matrix A are replaced with −1 in Edsger's computer. Luckily, Edsger still remembers the checksum values. He would like to restore the matrix, and reaches out to Grace for help. After some investigation, it will take Bi,j hours for Grace to recover the original value of Ai,j from the disk. Given the final matrix A, cost matrix B, and checksums along each row (R) and column (C), can you help Grace decide on the minimum total number of hours needed in order to restore the original matrix A?

Input
The first line of the input gives the number of test cases, T. T test cases follow.

The first line of each test case contains a single integer N.

The next N lines each contain N integers representing the matrix A. j-th element on the i-th line represents Ai,j.

The next N lines each contain N integers representing the matrix B. j-th element on the i-th line represents Bi,j.

The next line contains N integers representing the checksum of the rows. i-th element represents Ri.

The next line contains N integers representing the checksum of the columns. j-th element represents Cj.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of hours to restore matrix A.

Limits
Memory limit: 1 GB.
1≤T≤100.
−1≤Ai,j≤1, for all i,j.
1≤Bi,j≤1000, for i,j where Ai,j=−1, otherwise Bi,j=0.
0≤Ri≤1, for all i.
0≤Cj≤1, for all j.
It is guaranteed that there exist at least one way to replace −1 in A with 0 or 1 such that R and C as satisfied.

Test Set 1
Time limit: 20 seconds.
1≤N≤4.
Test Set 2
Time limit: 35 seconds.
1≤N≤40.
Test Set 3
Time limit: 35 seconds.
1≤N≤500.
"""
class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                    for row in range(vertices)]
 

def checksum(A, B, N):
    adj = [[0]*(2*N) for _ in xrange(2*N)]
    selected = [0] * ((2*N))
    nodes = set()
    maxN = 0
    for i in range(N):
        for j in range(N):
            if A[i][j] == -1:
                adj[i][j+N] = adj[N+j][i] = B[i][j]  # Space: O(N^2)
                nodes.add(i)
                nodes.add(j+N)
                maxN += B[i][j]
    nodes = list(nodes)
    result = 0
    max_e = [0]*len(nodes)
    lookup = [False]*len(nodes)
    for _ in xrange(len(nodes)):
        u = -1
        for v in xrange(len(nodes)):
            if lookup[v]:
                continue
            if u == -1 or max_e[v] > max_e[u]:
                u = v
        lookup[u] = True
        result += max_e[u]
        for v in xrange(len(nodes)):
            if adj[nodes[u]][nodes[v]] > max_e[v]:
                max_e[v] = adj[nodes[u]][nodes[v]]

    return maxN - result

dir = os.path.dirname(__file__)


inp = open(os.path.join(dir, 'test_data/test_set_1/ts1_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())

for case in range(t):
    n = int(inp.readline())
    A = []
    for _ in range(n):
        A.append(list(map(int, inp.readline().split(" "))))
    B = []

    for _ in range(n):
        B.append(list(map(int, inp.readline().split(" "))))
    rows = []
    rows.append(list(map(int, inp.readline().split(" "))))
    cols = []
    cols.append(list(map(int, inp.readline().split(" "))))
    result = (out.readline())[:-1]
    tmpAns = checksum(A, B, n)
    ans = ('Case #%d: %s') % (case+1, tmpAns)
    if ans != result:
        print('Case #%d: Error, %d' % (case+1, tmpAns))
        tmpAns = checksum(A, B, n)
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))