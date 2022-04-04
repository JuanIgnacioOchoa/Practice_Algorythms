from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
import math

start_time = time.time()

dir = os.path.dirname(__file__)

def findNine(N):
    ans = 0
    i = 0
    number_to_add = 0
    if int(N) % 9 == 0:
        return int(N[:1] + str(0) +  N[1:])
    else:
        number_to_add = 9 - int(N) % 9
    while i < len(N):
        if int(N[i]) > number_to_add:
            s = int(N[:i] + str(number_to_add) +  N[i:])
            return int(N[:i] + str(number_to_add) +  N[i:])
        i+=1
    s = int(N + str(number_to_add))
    return int(N + str(number_to_add))
stdin = open(os.path.join(dir,  'test_data/test_set_1/ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    N = (stdin.readline().strip())
    result = stdout.readline().strip()
    tmpAns = findNine(N)
    ans = ('Case #%d: %s') % (case+1, (tmpAns))
    if ans != result:
        print('%s, Incorrect: %s' % (result, (tmpAns)))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))