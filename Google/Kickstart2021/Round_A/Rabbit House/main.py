from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time
start_time = time.time()
"""
Problem
Barbara got really good grades in school last year, so her parents decided to gift her with a pet rabbit. She was so excited that she built a house for the rabbit, which can be seen as a 2D grid with R rows and C columns.

Rabbits love to jump, so Barbara stacked several boxes on several cells of the grid. Each box is a cube with equal dimensions, which match exactly the dimensions of a cell of the grid.

However, Barbara soon realizes that it may be dangerous for the rabbit to make jumps of height greater than 1 box, so she decides to avoid that by making some adjustments to the house. For every pair of adjacent cells, Barbara would like that their absolute difference in height be at most 1 box. Two cells are considered adjacent if they share a common side.

As all the boxes are superglued, Barbara cannot remove any boxes that are there initially, however she can add boxes on top of them. She can add as many boxes as she wants, to as many cells as she wants (which may be zero). Help her determine what is the minimum total number of boxes to be added so that the rabbit's house is safe.

Input
The first line of the input gives the number of test cases, T. T test cases follow.

Each test case begins with a line containing two integers R and C.

Then, R lines follow, each with C integers. The j-th integer on i-th line, Gi,j, represents how many boxes are there initially on the cell located at the i-th row and j-th column of the grid.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the minimum number of boxes to be added so that the rabbit's house is safe.

Limits
Memory limit: 1 GB.
1≤T≤100.
0≤Gi,j≤2⋅106, for all i, j.
Test Set 1
Time limit: 20 seconds.
1≤R,C≤50.
Test Set 2
Time limit: 40 seconds.
1≤R,C≤300.
"""
class Priority_Queue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    def __len__(self):
        return len(self.queue)
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element in the queue
    def append(self, data):
        self.queue.append(data)
  
    # for popping an element based on Priority
    def pop(self):
        try:
            max = 0
            for i in range(len(self.queue)):
                if self.queue[i][1] > self.queue[max][1]:
                    max = i
            item = self.queue[max]
            del self.queue[max]
            return item
        except IndexError:
            print()
            exit()

def insert(lst, tple):
    i = 0
    j = len(lst)- 1
    if len(lst) == 0 or tple[1] <= lst[0][1]:
        lst.insert(0, tple)
        return
    elif tple[1] > lst[-1][1]:
        lst.append(tple)
        return
    while i < j:
        if lst[i][1] > tple[1]:
            lst.insert(i, tple)
            return
        if lst[j][1] < tple[1]:
            lst.insert(j+1, tple)
            return   

        i+=1
        j-=1
    if lst[i][1] > tple[1]:
        lst.insert(i, tple)
    else:
        lst.insert(i+1, tple)
    return


def addBox(boxes, x1, y1, x2, y2):
    ans = 0
    if abs(boxes[x1][y1] - boxes[x2][y2]) >= 2:
        ans = abs(boxes[x2][y2] - boxes[x1][y1]) - 1
        if boxes[x1][y1] > boxes[x2][y2]:
            boxes[x2][y2] = boxes[x2][y2] + ans
        else: 
            boxes[x1][y1] = boxes[x1][y1] + ans
    return ans



def getAnswer2(boxes, R, C):
    G = boxes
    DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = 0
    buckets = defaultdict(set)
    for i in range(R):
        for j in range(C):
            d = 0
            buckets[boxes[i][j]].add((i, j))

    max_G = max(boxes[i][j] for i in range(R) for j in range(C))
    x = max_G-((R-1)+(C-1))+1
    h = max_G
    #print('max: %d min: %d,   DIF: %d' % (h, x, h - x))
    #print('R: %d C: %d' % (R, C))
    while h >= x:
        for i, j in buckets[h]:
            for di, dj in DIRECTIONS:
                ni, nj = di+i, dj+j
                if not (0 <= ni < R and 0 <= nj < C and G[ni][nj] < h-1):
                    continue
                buckets[G[ni][nj]].remove((ni, nj))
                ans += (h-1)-G[ni][nj]
                G[ni][nj] = h-1
                buckets[G[ni][nj]].add((ni, nj))
        h -= 1  
    return ans

def getAnswer(boxes, R, C):
    res_boxes = deepcopy(boxes)
    x = 0
    y = 0
    max = -1
    i = 0
    st = []
    queue = Priority_Queue()
    for i in range(R):
        for j in range(C):
            d = 0
            queue.append([[i, j], boxes[i][j]])
            #insert(st, [[i, j], -boxes[i][j]])
    ans = 0
    visited = []
    #while len(st):
    while len(queue):
        #current = st.pop(0)
        current = queue.pop()
        x = current[0][0]
        y = current[0][1]
        if x > 0:
            if abs(boxes[x - 1][y] - boxes[x][y]) > 1:
                #if [[x-1, y], -boxes[x-1][y]] in st:
                #    st.remove([[x - 1, y], -boxes[x-1][y]])
                ans += addBox(boxes, x, y, x - 1, y)
                #insert(st, [[x-1, y], -boxes[x-1][y]])
        if y > 0:
            if abs(boxes[x][y-1] - boxes[x][y]) > 1:
                #if [[x, y-1], -boxes[x][y-1]] in st:
                #    st.remove([[x, y - 1], -boxes[x][y - 1]])
                ans += addBox(boxes, x, y, x, y - 1)
                #insert(st, [[x, y - 1], -boxes[x][y-1]])
        if x < R - 1:
            if abs(boxes[x + 1][y] - boxes[x][y]) > 1:
                #if [[x+1, y], -boxes[x+1][y]] in st:
                #    st.remove([[x + 1, y], -boxes[x+1][y]])
                ans += addBox(boxes, x, y, x + 1, y)
                #insert(st, [[x+1, y], -boxes[x+1][y]])
        if y < C - 1:
            if abs(boxes[x][y+1] - boxes[x][y]) > 1:
                #if [[x, y+1], -boxes[x][y+1]] in st:
                #    st.remove([[x, y + 1], -boxes[x][y + 1]])
                ans += addBox(boxes, x, y, x, y + 1)
                #insert(st, [[x, y + 1], -boxes[x][y+1]])
        visited.append(current)
    return ans
    for i in range(R):
        for j in range(C):
            h = abs(max - res_boxes[i][j]) - abs(x - i) - abs(y - j)
            ans += abs(max - res_boxes[i][j]) - abs(x - i) - abs(y - j)
            res_boxes[i][j] = res_boxes[i][j] + h
    return ans

dir = os.path.dirname(__file__)
inp = open(os.path.join(dir, 'test_data/test_set_2/ts2_input.txt'),'r')
out = open(os.path.join(dir, 'test_data/test_set_2/ts2_output.txt'),'r')
#inp = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#out = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(inp.readline())

for case in range(t):
    
    tmp = list(inp.readline().strip().split(" "))
    r = int(tmp[0])
    c = int(tmp[1])
    #s = inp.readline()
    boxes = []
    for i in range(r):
        boxes.append(list(map(int, inp.readline().split(" "))))
    
    result = (out.readline())[:-1]
    tmpAns = getAnswer2(boxes, r, c)
    ans = ('Case #%d: %s') % (case+1, tmpAns)
    if ans != result:
        print('Case #%d: Error, %d' % (case+1, tmpAns))
    else:
        print(ans)
print("--- %s seconds ---" % (time.time() - start_time))