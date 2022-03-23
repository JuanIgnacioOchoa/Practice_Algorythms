from sys import stdin, stdout
import os
import time
start_time = time.time()
"""
Problem
Download the Starter Code!
Jorge is a physicist who has published many research papers and wants to know how much impact they have had in the academic community. To measure impact, he has developed a metric, H-index, to score each of his papers based on the number of times it has been cited by other papers. Specifically, the H-index score of a researcher is the largest integer H such that the researcher has H papers with at least H citations each.

Jorge has written N papers in his lifetime. The i-th paper has Ci citations. Each paper was written sequentially in the order provided, and the number of citations that each paper has will never change. Please help Jorge determine his H-index score after each paper he wrote.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing N, the number of papers Jorge wrote. The second line contains N integers. The i-th integer is Ci, the number of citations that the i-th paper has.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a space-separated list of N integers. The i-th integer is Jorge's H-index score after writing his i-th paper.

Limits
Time limit: 50 seconds.
Memory limit: 1 GB.
1≤T≤100
1≤Ci≤105
Test Set 1
1≤N≤1000
Test Set 2
1≤N≤105.
"""

def getHIndex(n, citations):
    ans = []
    if len(citations) <= 0:
        return [0]
    i = 0
    dp = [0] * (max(citations) + 1)
    idx = 1
    s = 0
    while i < len(citations):
        j = 0
        c = citations[i]
        dp[c] += 1
        if c > idx:
            s += 1
        if s > idx:
            idx += 1
            s -= dp[idx]
        ans.append(idx)
        i+=1
    return ans

dir = os.path.dirname(__file__)

inp = open(os.path.join(dir, 'input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')

t = int(inp.readline())


for case in range(t):
    n = int(inp.readline().strip())
    citations = list(map(int, inp.readline().split()))
    index = getHIndex(n, citations)
    ans =('Case #%d: %s') % (case+1, index)
    
    #print(ans)

print("--- %s seconds ---" % (time.time() - start_time))