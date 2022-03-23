from sys import stdin, stdout
import os
import time
start_time = time.time()

def transform(s, f):
    ans = 0
    alph_size = 26
    i = 0
    dist = dict()
    while i < len(s) and ord(s[i]) != 10:
        m = alph_size
        if s[i] not in dist:
            j = 0
            while j < len(f) and ord(f[j]) != 10 and m > 0:
                x1 = alph_size - abs(ord(s[i]) - ord(f[j]))
                x2 = abs (ord(f[j]) - ord(s[i]))
                if x1 < x2 and x1 < m:
                    m = x1
                elif x2 < m:
                    m = x2
                j+=1
            dist[s[i]] = m
        ans += dist[s[i]]
        i+=1
    return ans



dir = os.path.dirname(__file__)

x = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
output = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#f = open('test_data/sample_test_set_2/sample_ts2_input.txt','r')

t = int(x.readline())

for case in range(t):
    s = x.readline()
    f = x.readline()
    result = int(output.readline().split(':')[1])
    ans = (transform(s, f))
    if ans != result:
        print('Case #%d: Error' % (case+1))
    else:
        print('Case #%d: %s' % (case+1, ans))
print("--- %s seconds ---" % (time.time() - start_time))