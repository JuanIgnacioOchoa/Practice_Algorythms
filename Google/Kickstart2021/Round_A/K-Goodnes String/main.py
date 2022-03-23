from sys import stdin, stdout
import os
import time
start_time = time.time()
"""
Problem
Charles defines the goodness score of a string as the number of indices i such that Si≠SN−i+1 where 1≤i≤N/2 (1-indexed). For example, the string CABABC has a goodness score of 2 since S2≠S5 and S3≠S4.

Charles gave Ada a string S of length N, consisting of uppercase letters and asked her to convert it into a string with a goodness score of K. In one operation, Ada can change any character in the string to any uppercase letter. Could you help Ada find the minimum number of operations required to transform the given string into a string with goodness score equal to K?

Input
The first line of the input gives the number of test cases, T. T test cases follow.

The first line of each test case contains two integers N and K. The second line of each test case contains a string S of length N, consisting of uppercase letters.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of operations required to transform the given string S into a string with goodness score equal to K.

Limits
Memory limit: 1 GB.
1≤T≤100.
0≤K≤N/2.
Test Set 1
Time limit: 20 seconds.
1≤N≤100.
Test Set 2
Time limit: 40 seconds.
1≤N≤2×105 for at most 10 test cases.
For the remaining cases, 1≤N≤100.
"""
def getGoodnes(s, k):
    ans = 0
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            ans += 1
        i+=1
        j-=1
    return abs(ans-k)


dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())


for case in range(t):
    
    tmp = list(inp.readline().strip().split(" "))
    n = int(tmp[0])
    k = int(tmp[1])
    s = inp.readline().strip()
    #s = inp.readline()
    result = (out.readline())[:-1]
    tmpAns = getGoodnes(s, k)
    ans = ('Case #%d: %s') % (case+1, tmpAns)
    if ans != result:
        print('Case #%d: Error' % (case+1))
    #else:
        
        #print(ans)
print("--- %s seconds ---" % (time.time() - start_time))