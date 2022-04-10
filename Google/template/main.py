from sys import stdin, stdout
import os
import time

start_time = time.time()

#dir = os.path.dirname(__file__)


#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = 1#int(stdin.readline())

for case in range(t):

    #result = stdout.readline().strip()
    ans = 0#inkUsage(ink)
    print(('Case #%d: %s') % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))