from sys import stdin, stdout
import os
import time
start_time = time.time()
"""
Problem
Given a grid of R rows and C columns each cell in the grid is either 0 or 1.

A segment is a nonempty sequence of consecutive cells such that all cells are in the same row or the same column. We define the length of a segment as number of cells in the sequence.

A segment is called "good" if all the cells in the segment contain only 1s.

An "L-shape" is defined as an unordered pair of segments, which has all the following properties:

Each of the segments must be a "good" segment.
The two segments must be perpendicular to each other.
The segments must share one cell that is an endpoint of both segments.
Segments must have length at least 2.
The length of the longer segment is twice the length of the shorter segment.
We need to count the number of L-shapes in the grid.

Below you can find two examples of correct L-shapes,

Examples of valid L-shapes.
and three examples of invalid L-shapes.

Examples of invalid L-shapes.
Note that in the shape on the left, two segments do not share a common endpoint. The next two shapes do not meet the last requirement, as in the middle shape both segments have the same length, and in the last shape the longer segment is longer than twice the length of the shorter one.

Input
The first line of the input contains the number of test cases, T. T test cases follow.

The first line of each testcase contains two integers R and C.

Then, R lines follow, each line with C integers representing the cells of the grid.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of L-shapes.

Limits
Time limit: 60 seconds.
Memory limit: 1 GB.
1≤T≤100.
Grid consists of 0s and 1s only.
Test Set 1
1≤R≤40.
1≤C≤40.
Test Set 2
1≤R≤1000 and 1≤C≤1000 for at most 5 test cases.
For the remaining cases, 1≤R≤40 and 1≤C≤40.
"""
def getnumberOfL(sizes):
    x0 = sizes[0]
    x1 = sizes[1]
    ans = 0
    while x1 >= 2:
        if (x1*2) <= x0:
            ans += 1
        x1-=1
    x1 = sizes[1]
    while x0 >= 2:
        if (x0*2) <= x1:
            ans+=1
        x0-=1
    return ans
def findTotalL(grid):
    ans = 0
    i = 0
    while i < len(grid):
        j = 0
        while j < len(grid[i]):

            if grid[i][j] == 1:
                x = 0
                size = [[0,0],[0,0],[0,0],[0,0]]
                if ( (i-x-1 >= 0 and j+x+1 < len(grid[i]) and grid[i-x-1][j] and grid[i][j+x+1])  or 
                        (i+x+1 < len(grid) and j+x+1 < len(grid[i]) and grid[i][j+x+1] and grid[i+x+1][j]) or 
                        (i+x+1 < len(grid) and j-x-1 >= 0 and grid[i+x+1][j] and grid[i][j-x-1]) or 
                        (i-x-1 >= 0 and j-x-1 >= 0 and grid[i][j-x-1] and grid[i-x-1][j])):
                    
                    x = 0
                    while  (i-x >= 0 and grid[i-x][j]) or (j+x < len(grid[i])  and grid[i][j+x]):
                        if (i-x >= 0 and grid[i-x][j]):
                            size[0][0] += 1
                        if (j+x < len(grid[i]) and grid[i][j+x]):
                            size[0][1] += 1
                        x+=1
                    x = 0
                    while  (j+x  < len(grid[i]) and grid[i][j+x]) or (i+x < len(grid)  and grid[i+x][j]):
                        if j+x < len(grid[i]) and grid[i][j+x]:
                            size[1][0] += 1
                        if i+x < len(grid) and grid[i+x][j]:
                            size[1][1] += 1
                        x+=1
                    
                    x = 0
                    while  (i+x  < len(grid) and grid[i+x][j]) or (j-x >= 0  and grid[i][j-x]):
                        if i+x  < len(grid) and grid[i+x][j]:
                            size[2][0] += 1
                        if j-x >= 0  and grid[i][j-x]:
                            size[2][1] += 1
                        x+=1
                    x = 0
                    while  (j-x >= 0  and grid[i][j-x]) or (i-x >= 0 and grid[i-x][j]):
                        if j-x >= 0  and grid[i][j-x]:
                            size[3][0] += 1
                        if i-x >= 0 and grid[i-x][j]:
                            size[3][1] += 1
                        x+=1
                    tmp = 0
                    for s in size:
                        tmp+=getnumberOfL(s)
                    ans+=tmp
                    """
                    if (i-x-1 > 0 and j+x+1 < len(grid[i]) and grid[i-x-1][j] and grid[i][j+x+1]) :
                        
                        size[0][0] = x + 2
                        size[0][1] = x + 2
                    if (i+x+1 < len(grid) and j+x+1 < len(grid[i]) and grid[i][j+x+1] and grid[i+x+1][j]):
                        size[1] = x + 2
                    if (i+x+1 < len(grid) and j-x-1 > 0 and grid[i+x+1][j] and grid[i][j-x-1]):
                        size[2] = x + 2
                    if (i-x-1 > 0 and j-x-1 > 0 and grid[i][j-x-1] and grid[i-x-1][j]):
                        size[3] = x + 2
                    """   

                #Top right
                #if grid[i-1][j] and grid[i][j+1]: 
                #Bottom Right
                #if grid[i][j+1] and grid[i+1][j]:
                #Bottom Left 
                #if grid[i+1][j] and grid[i][j-1]: 
                #Top Left
                #if grid[i][j-1] and grid[i-1][j]: 
            j+=1
        i+=1
    return ans
def count(x, y):
    return max((min(x//2, y)-1) + (min(x, y//2)-1), 0)

def gridd(G, i, j):
    return G[i][j] if len(G) > len(G[0]) else G[j][i]

def l_shaped_plots(R, C, G):

    result = 0
    for direction in (lambda x: x, reversed):
        dp = [0]*min(R, C)
        for i in direction(xrange(max(R, C))):
            print('i-' + str(i))
            for direction in (lambda x:x, reversed):
                curr = 0
                for j in direction(xrange(min(R, C))):
                    print('j-' + str(j))
                    if not gridd(G, i, j):
                        dp[j] = 0
                        curr = 0
                        continue
                    dp[j] += 1
                    curr += 1
                    if count(curr, (dp[j]+1)//2) :
                        print('a')
                    result += count(curr, (dp[j]+1)//2)
    return result

def l_shaped_plots_2(R, C, G):
    ans = 0
    i = 0
    j = 0
    cnt = []
    while i < R:
        cnt.append([0] * C)
        j = 0
        c = 0
        while j < C:
            c+=G[i][j]
            cnt[i][j] = c
            j+=1
        i+=1
    i = 0
    while i < R:
        j = 0
        while j < C:
            if G[i][j]:
                print("X")
        i+=1
    return ans

def flipV(grid, r, c):
    print(grid)
    tempm = grid
    for i in range(0,len(tempm),1):
        tempm[i].reverse()
    return(tempm)

def flipH(grid, r, c):
    print(grid)
    tempm = grid
    tempm.reverse()
    return(tempm)

dir = os.path.dirname(__file__)
#inp = open(os.path.join(dir, 'test_data/test_set_1/ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())


for case in range(t):
    
    tmp = list(inp.readline().strip().split(" "))
    
    r = int(tmp[0])
    c = int(tmp[1])
    grid = [map(int, inp.readline().strip().split()) for _ in xrange(r)]
    result = (out.readline())[:-1]
    tmpAns = l_shaped_plots_2(r,c,grid)
    ans = ('Case #%d: %s') % (case+1, tmpAns)
    
    if ans != result:
        print('Case #%d: Error %d' % (case+1, tmpAns))
    #else:
        
        #print(ans)
print("--- %s seconds ---" % (time.time() - start_time))