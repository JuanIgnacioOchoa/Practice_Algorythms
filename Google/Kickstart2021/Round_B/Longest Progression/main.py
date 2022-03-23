from sys import stdin, stdout, maxsize
from copy import deepcopy
from collections import defaultdict
import os
import time
start_time = time.time()

"""
Problem
In Kick Start 2020 Round E (you do not need to know anything about the previous problem to solve this one) Sarasvati learned about arithmetic arrays. An arithmetic array is an array that contains at least two integers and the differences between consecutive integers are equal. For example, [9,10], [3,3,3], and [9,7,5,3] are arithmetic arrays, while [1,3,3,7], [2,1,2], and [1,2,4] are not.

Sarasvati again has an array of N non-negative integers. The i-th integer of the array is Ai. She can replace at most one element in the array with any (possibly negative) integer she wants.

For an array A, Sarasvati defines a subarray as any contiguous part of A. Please help Sarasvati determine the length of the longest possible arithmetic subarray she can create by replacing at most one element in the original array.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integer N. The second line contains N integers. The i-th integer is Ai.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the length of the longest arithmetic subarray.

Limits
Time limit: 30 seconds.
Memory limit: 1 GB.
1≤T≤100
0≤Ai≤109.
Test Set 1
2≤N≤2000.
Test Set 2
2≤N≤3×105 for at most 10 test cases.
For the remaining cases, 2≤N≤2000.
"""
def longest_arithmetic(A, N):
    start = 0
    end = 0
    curr = -1
    start = 0
    start2 = 0
    max = 2
    flag = 0
    tmpV = 0
    i = 1
    while i < len(A):
        diff = A[i-1] - A[i]
        tmpM = 0
        if i - start == 1:
            curr = diff
            end = i
        elif curr == diff:
            end = i
            tmpM = end - start + 1
        else:
            if flag == 0:
                tmpV = A[i]
                A[i] = A[i-1] - curr
                end = i
                start2 = i
                tmpM = end - start + 1
                flag = 1
            elif flag == 1:
                A[start2] = tmpV
                diff = A[i-1] - A[i]
                i = start2 - 1
                tmpV = A[i]
                A[i] = A[start2] + diff
                i -= 1
                start = i
                flag = 2
            elif flag == 2:
                A[start2-1] = tmpV
                diff = A[start2-1] - A[start2]
                tmpV = A[start]
                A[start] = A[start2-1] + diff
                i = start
                flag = 3
            else:
                start = start2 - 1
                i = start
                A[start-1] = tmpV
                flag = 0
        if max < tmpM:
            max = tmpM
        i+=1
    return max

dir = os.path.dirname(__file__)


stdin = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#stdin = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    start_time_1 = time.time()
    N = int(stdin.readline())
    A = list(map(int, stdin.readline().split(" ")))
    result = stdout.readline()[:-1]
    tmpAns = (longest_arithmetic(A, N))
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %d' % (result, (tmpAns)))
        tmpAns = (longest_arithmetic(A, N))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))