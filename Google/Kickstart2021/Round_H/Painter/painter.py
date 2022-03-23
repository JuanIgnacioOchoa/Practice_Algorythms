from sys import stdin, stdout
import os
import time
start_time = time.time()

def paint(paints, colors, primaryColors):
    ans = 0
    i = 0
    blocks = dict()
    while i < len(paints) and paints[i] != '\n':
        blocks[i] = []
        i+=1
    i = 0 
    while i < len(paints) and paints[i] != '\n':
        p = paints[i]
        if len(blocks[i]) != len(colors[p]):
            if p in primaryColors:
                j = i
                while paints[j] != '\n' and p in colors[paints[j]] and p not in blocks[j]:
                    blocks[j].append(p)
                    j+=1
            else :
                j = i + 1
                while paints[j] != '\n' :
                    if paints[j] in primaryColors:
                        if paints[j] in colors[p] and paints[j] not in blocks[i]:
                            break
                    j+=1
                if j < len(paints) and paints[j] != '\n':
                    pr = paints[j]
                    j = i
                    while paints[j] != '\n' and pr not in blocks[j] and pr in colors[paints[j]]:
                        blocks[j].append(pr)
                        j+=1
                    i-=1
                else :
                    ans -= 1
                    while len(blocks[i]) != len(colors[p]):
                        pr = ''
                        if 'R' in colors[p] and 'R' not in blocks[i]:
                            pr = 'R'
                        if 'B' in colors[p] and 'B' not in blocks[i]:
                            pr = 'B'
                        if 'Y' in colors[p] and 'Y' not in blocks[i]:
                            pr = 'Y'
                        j = i
                        while paints[j] != '\n' and pr not in blocks[j] and pr in colors[paints[j]]:
                            blocks[j].append(pr)
                            j+=1
                        ans += 1
            ans+=1
        i+=1
                
    return ans

dir = os.path.dirname(__file__)

inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())

colors = dict()
colors['U'] = []
colors['R'] = ['R']
colors['Y'] = ['Y']
colors['B'] = ['B']
colors['O'] = ['R', 'Y']
colors['P'] = ['R', 'B']
colors['G'] = ['Y', 'B']
colors['A'] = ['R', 'Y', 'B']

primaryColors = ['R', 'Y', 'B']

for case in range(t):
    n = int(inp.readline())
    p = inp.readline()
    result = int(out.readline().split(':')[1])
    ans = (paint(p, colors, primaryColors))
    if ans != result:
        print 'Case #%d: Error' % (case+1)
    else:
        print 'Case #%d: %s' % (case+1, ans)


print("--- %s seconds ---" % (time.time() - start_time))