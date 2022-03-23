from sys import stdin, stdout
from copy import deepcopy
from collections import defaultdict
import os
import time

start_time = time.time()

class Vertex:
    def __init__(self, node):
        self.id = node
        self.limit = {}
        self.toll = {}
        self.bestN = None
        self.bestW = None
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, l=0, t=0):
        self.limit[neighbor] = l
        self.toll[neighbor] = t

    def get_connections(self):
        return self.limit.keys()  

    def get_id(self):
        return self.id

    def get_limit(self, neighbor):
        return self.limit[neighbor]

    def get_toll(self, neighbor):
        return self.toll[neighbor]

    def set_best(self, neighbor, weight):
        if self.bestN == None or weight < self.bestW:
            self.bestN = neighbor
            self.bestW = weight

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, limit = 0, toll = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], limit, toll)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], limit, toll)

    def get_vertices(self):
        return self.vert_dict.keys()
    
    def resetWeigths(self):
        for i in self.get_vertices():
            focus = self.get_vertex(i)
            focus.bestN = None
            focus.bestW = None

class Node:
    def __init__(self, id):
        self.id = id
        self.limit = {}
        self.toll = {}
        self.children = []
        self.parent = None

class Edge:
    def __init__(self, x, y, limit, charge):
        self.x = x
        self.y = y
        self.limit  = limit
        self.charge = charge

class Query:
    def __init__(self, city, weight, index):
        self.city = city
        self.weight = weight
        self.index = index
class Tree:
    def __init__(self, root):
        self.root = root
        self.nodes = {}
        self.adj = defaultdict(list)
        self.sub = defaultdict(set)
        self.parent = defaultdict(list)
    def add_edge(self, x, y):

        self.adj[x].append(y)
        self.adj[y].append(x)
    #def addChild(self, node):
    def bfs(self, start):
        q = [start]
        explored = [start]
        sub_tree = []
        while len(q):
            c = q.pop(0)
            for e in self.adj[c]:
                if e not in explored:
                    q.append(e)
            explored.append(c)
            sub_tree.append(c)
        return sub_tree
    def createSubs(self, start, explored):
        self.parent[1] = 0
        q = [start]
        sub_tree = []
        local_explored = [start]
        while len(q):
            c = q.pop(0)
            for e in self.adj[c]:
                if e not in explored and e not in local_explored:
                    q.append(e)
            local_explored.append(c)
            sub_tree.append(c)
        return sub_tree

    def createTreeWithSubTree(self, start, explored):
        self.parent[start] = 0
        q = [start]
        sub_tree = []
        leafs = []
        c = q.pop(0)
        while True:
            parent = c
            leaf = True
            for e in self.adj[c]:
                if e not in explored:
                    q.append(e)
                    self.parent[e] = c
                    leaf = False
            if leaf:
                leafs.append(c)
            explored.append(c)
            sub_tree.append(c)
            if(len(q) == 0):
                break
            c = q.pop(0)
            #self.sub[parent].append(self.createTreeWithSubTree(c, explored))
        explored = [1]
        for leaf in leafs:
            self.sub[leaf].add(leaf)
            child = leaf
            parent = self.parent[leaf]

            while parent != 0:
                self.sub[parent] |= self.sub[child] 
                child = parent
                parent = self.parent[child]
                self.sub[parent].add(parent)
                
        ##for i in range(1, len(sub_tree)):
        ##    self.sub[sub_tree[i]] = self.createSubs(sub_tree[i], explored)
        ##    explored.append(sub_tree[i])
        #self.sub[1] = sub_tree
        return sub_tree
    def createTree(self, edges):
        current = self.root
        open = [G.get_vertex(1)]
        while len(open):
            vert = open.pop(0)
            current = self.nodes[vert.id]
            adj = vert.get_connections()
            for a in adj:
                node = None
                if a.id in self.nodes:
                    continue
                    node = self.nodes[a.id]
                else:
                    node = Node(a.id)
                    self.nodes[a.id] = node 
                current.children.append(node)
                current.limit[node] = vert.get_limit(a)
                current.toll[node] = vert.get_toll(a)
                if node not in nodes:
                    nodes.append(node)
                node.parent = current
                open.append(a)
        return self


def getCommonDivisor(x1, x2):
    while x2 != 0 and x1 != 0:
        if x1 > x2:
            x1 -= x2 * (int(x1/x2))
        else:
            x2 -= x1 * (int(x2/x1))
    return x1 if x2 == 0 else x2
def getAmountPaid2(start, tree, W, queries, edges):
    #return ["1", "2"]
    queries.sort(key = lambda x: x.weight)
    edges.sort(key = lambda x: x.limit)
    ans = [-1] * len(queries)
    e = 0
    GCP = {}
    for q in queries:
        while e < len(edges) and edges[e].limit <= q.weight:
            depth1 = tree.sub[edges[e].x]
            depth2 = tree.sub[edges[e].y]
            parent = edges[e].x if len(depth1) > len(depth2) else edges[e].y
            child = edges[e].x if len(depth1) < len(depth2) else edges[e].y
            parentArr = depth2 if len(depth1) > len(depth2) else depth1
            for c in parentArr:
                if c not in GCP:
                    GCP[c] = 0
                GCP[c] = getCommonDivisor(GCP[c], edges[e].charge)
            e+=1
        if q.city not in GCP:
            GCP[q.city] = 0
        ans[q.index] = str(GCP[q.city])
    
    return ans
dir = os.path.dirname(__file__)


stdin  = open(os.path.join(dir, 'test_data/test_set_1/ts1_input.txt'),'r')
stdout = open(os.path.join(dir, 'test_data/test_set_1/ts1_output.txt'),'r')
#stdin  = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_input.txt'),'r')
#stdout = open(os.path.join(dir, 'test_data/sample_test_set_1/sample_ts1_output.txt'),'r')

t = int(stdin.readline())

for case in range(t):
    start_time_1 = time.time()
    rd = list(map(int, stdin.readline().split(" ")))
    N = rd[0]
    Q = rd[1]
    edges = []    
    queries = []
    tree = Tree(1)
    for _ in range(N-1):
        val = list(map(int, stdin.readline().split(" ")))
        x = val[0]
        y = val[1]
        l = val[2]
        t = val[3]
        edges.append(Edge(x, y, l, t))
        tree.add_edge(x, y)
    #tree.printTree()
    #tree.createTree(edges)
    start_time_1 = time.time()
    tree.createTreeWithSubTree(1, [])
    #print("1--- %s seconds ---" % (time.time() - start_time_1))
    ans = []   
    for i in range(Q):
        q = (list(map(int, stdin.readline().split(" "))))
        c = q[0]
        w = q[1]
        queries.append(Query(c, w, i))
        
    start_time_1 = time.time()
    tmpAns = getAmountPaid2(c, tree, w, queries, edges)
    #print("2--- %s seconds ---" % (time.time() - start_time_1))
    result = stdout.readline().strip()
    ans = ('Case #%d: %s') % (case+1, (" ".join(tmpAns)))
    if ans != result:
        print('%s, Incorrect: %d' % (result, (tmpAns)))
        #tmpAns = (longest_arithmetic(A, N))
        pass
    else:
        print(ans)

print("--- %s seconds ---" % (time.time() - start_time))