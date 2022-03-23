

class Node:
    def __init__(self, info): 
        self.info = info  
        self.edges = []
        self.level = None 

    def __str__(self):
        return str(self.info) 

def createTree(edges):
    values = dict()
    for a, b in edges:
        left = None
        right = None
        if a in values:
            left = values[a]
        else:
            left = Node(a)
            values[a] = left

        if b in values:
            right = values[b]
        else:
            right = Node(b)
            values[b] = right
        
        left.edges.append(right)
        right.edges.append(left)
    return values

def getNodePairs(query):
    result = []
    i = 0
    j = 0
    if len(query) == 1:
        result.append([query[0], query[0]])
    while i < len(query) - 1:
        j = i + 1
        while j < len(query):
            result.append([query[i], query[j]])
            j+=1
        i+=1

    return result

def getDistanceBetweenNodes(node1, node2):
    visited = []
    parents = []
    current = node1
    stack = []
    dist = 0
    while current != node2:
        a = False
        for c in current.edges:
            if c not in visited:
                stack.append(c)
                a = True
        if a:
            parents.append(current)
            visited.append(current)
            current = stack.pop()
            dist+=1
        else:
            dist-=1
            visited.append(current)
            current = parents.pop()
        

    return dist
def kittysTree(edges, queries):
    tree = createTree(edges)
    result = []
    i = 0
    for q in queries:
        result.append(0)
        pairs = getNodePairs(q)
        for a, b in pairs:
            dist = getDistanceBetweenNodes(tree[a], tree[b])
            result[i] += a * b * dist
        result[i] = result[i] % ((10**9)+7)
        i+=1
    return result
        
        
edges = [[1, 2], [1, 3], [1, 4], [3, 5], [3, 6], [3, 7]]
queries = [[2, 4], [5], [2, 4, 5]]

kittysTree(edges, queries)