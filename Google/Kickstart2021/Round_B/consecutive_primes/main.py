from sys import stdin, stdout, maxsize
from copy import deepcopy
from collections import defaultdict
import os
import time
import math
"""
Problem
Ada has bought a secret present for her friend John. In order to open the present, Ada wants John to crack a secret code. She decides to give him a hint to make things simple for him. She tells him that the secret code is a number that can be formed by taking the product of two consecutive prime numbers, such that it is the largest number that is smaller than or equal to Z. Given the value of Z, help John to determine the secret code.

Formally, let the order of prime numbers 2,3,5,7,11, ... be denoted by p1,p2,p3,p4,p5, ... and so on. Consider Ri to be the product of two consecutive primes pi and pi+1. The secret code is the largest Rj such that Rj≤Z.

Input
The first line of the input gives the number of test cases, T. T lines follow.
Each line contains a single integer Z, representing the number provided by Ada as part of the hint.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the secret code - the largest number less than or equal to Z that is the product of two consecutive prime numbers.

Limits
Time limit: 15 seconds.
Memory limit: 1 GB.
1≤T≤100.
Test Set 1
6≤Z≤2021.
Test Set 2
6≤Z≤109.
Test Set 3
6≤Z≤1018.
"""
start_time = time.time()

def is_prime(n):
    if n == 1 or n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    N = n//2
    while i < N:
        if n % i == 0:
            return False
        N = n / i
        i+=2
    return True
def consecutive_number(N):
    ans = 0
    prime1 = 2
    prime2 = 3
    prev = current = 2 * 3
    for i in range(5, N - 1, 2):
        if is_prime(i):
            prime1 = prime2
            prime2 = i
            current = prime1 * prime2
            if current > N:
                return prev
            prev = current
    return current

def consecutive_number_2(N):
    ans = 0
    root = int(math.ceil(math.sqrt(N)))
    primesTop = 0
    primesBottom = []
    top = root + 1
    bottom = root
    top_f = False
    while bottom > 0:
        if not top_f and is_prime(top):
            top_f = True
            primesTop = top
        if is_prime(bottom):
            if len(primesBottom) == 2:
                curr = primesBottom[0] * primesBottom[1]
                if curr <= N:
                    return curr
            else:
                primesBottom.append(bottom)
                if len(primesBottom) == 2:
                    curr = primesBottom[0] * primesBottom[1]
                    if curr <= N:
                        return curr
                elif len(primesBottom) == 1 and primesTop != 0:
                    curr = primesBottom[0] * primesTop
                    if curr <= N:
                        return curr
        top+=1
        bottom-=1

    return ans

dir = os.path.dirname(__file__)


stdin = open(os.path.join(dir,  'test_data/test_set_2/ts2_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#stdin = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = int(stdin.readline())
    result = stdout.readline()[:-1]
    tmpAns = consecutive_number_2(N)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %d' % (result, (tmpAns)))
        tmpAns = (consecutive_number_2( N))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))