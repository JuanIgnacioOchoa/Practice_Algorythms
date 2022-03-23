import math
import os
import random
import re
import sys

class Node:
    def __init__(self, info, value): 
        self.edge = info 
        self.value = value 
        self.edges = []
        self.level = None 

def createTree(c, edges):
    values = dict()
    i = 0
    for a, b in edges:
        left = None
        right = None
        if a in values:
            left = values[a]
        else:
            left = Node(a, c[i])
            values[a] = left
            i+=1
        if b in values:
            right = values[b]
        else:
            right = Node(b, c[i])
            values[b] = right
            i+=1
        
        left.edges.append(right)
    return values[edges[0][0]]

def balancedForest(c, edges):
    root = createTree(c, edges)
    return None


q = 2
n = 5
c = [1, 2, 2, 1, 1]
edges = [
    [1, 2],
    [1, 3],
    [3, 5],
    [1, 4]
]

result = balancedForest(c, edges)