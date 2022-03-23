from sys import stdin, stdout, maxsize
from copy import deepcopy
from collections import defaultdict
import os
import time
start_time = time.time()
"""
Problem
Your friend John just came back from vacation, and he would like to share with you a new property that he learned about strings.

John learned that a string C of length L consisting of uppercase English characters is strictly increasing if, for every pair of indices i and j such that 1≤i<j≤L (1-based), the character at position i is smaller than the character at position j.

For example, the strings ABC and ADF are strictly increasing, however the strings ACC and FDA are not.

Now that he taught you this new exciting property, John decided to challenge you: given a string S of length N, you have to find out, for every position 1≤i≤N, what is the length of the longest strictly increasing substring that ends at position i.

Input
The first line of the input gives the number of test cases, T. T test cases follow.

Each test case consists of two lines.

The first line contains an integer N, representing the length of the string.

The second line contains a string S of length N, consisting of uppercase English characters.

Output
For each test case, output one line containing Case #x: y1 y2 ... yn, where x is the test case number (starting from 1) and yi is the length of the longest strictly increasing substring that ends at position i.

Limits
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
Time limit: 20 seconds.
1≤N≤100.
Test Set 2
Time limit: 40 seconds.
1≤N≤2×105.
"""

def increase_subs(S, N):
    ans = []
    res = 0
    prev = -1
    for s in S:
        if prev == -1 or prev >= s:
            res = 1
        else:
            res+=1
        prev = s
        ans.append(str(res))
    return " ".join(ans)
dir = os.path.dirname(__file__)


inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())

for case in range(t):
    N = int(inp.readline())
    S = inp.readline().strip()
    result = out.readline()[:-1]
    tmpAns = (increase_subs(S, N))
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('Case #%d: Error, %d' % (case+1, (tmpAns)))
        tmpAns = increase_subs(A, B, n)
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))