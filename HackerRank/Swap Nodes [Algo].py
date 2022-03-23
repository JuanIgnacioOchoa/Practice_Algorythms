#!/bin/python3

import math
import os
import random
import re
import sys

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def inorder(root):
     
    stack = []
    result = ""
    current = root
    while len(stack) or current != None:
        

        if current != None:
            stack.append(current)
            current = current.left
        elif len(stack):
            current = stack.pop()

            result += str(current.info) + " "

            current = current.right
    return result

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

def createTree(indexes):
    head = Node(-1)
    stack = []
    root = Node(1)
    root.level = 1
    head.left = root
    i = 0
    current = head.left
    while len(indexes) > 0:
        index = indexes.pop(0)
        lvl = current.level
        if index[0] != -1:
            current.left = Node(index[0])
            current.left.level = lvl + 1
            stack.append(current.left)
        if index[1] != -1:
            current.right = Node(index[1])
            current.right.level = lvl + 1
            stack.append(current.right)
        if len(stack):
            current = stack.pop(0)
    return head.left

def swapNodes(indexes, queries):
    # Write your code here
    head = Node(-1)
    root = createTree(indexes)
    head.left = root
    result = []
    i = 0
    for q in queries:
        current = head.left
        stack = []
        result.append([])
        while current != None or len(stack) > 0:
            if current != None and current.level%q == 0:
                tmp = current.left
                current.left = current.right
                current.right = tmp
            if current != None:
                stack.append(current)
                current = current.left
            elif len(stack):
                current = stack.pop()
                result[i].append(current.info)
                current = current.right
        #result.append(inorder(head.left))
        i+=1

    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = 11
    #n = int(input().strip())

    indexes = []
    inp = ["2 3", "4 -1", "5 -1", "6 -1", "7 8", "-1 9", "-1 -1", "10 11", "-1 -1", "-1 -1", "-1 -1"]
    for i in range(n):
        #indexes.append(list(map(int, input().rstrip().split())))
        indexes.append(list(map(int, inp[i].split())))

    queries_count = 2
    #queries_count = int(input().strip())

    queries = []
    inp = ["2", "4"]
    for i in range(queries_count):
        #queries_item = int(input().strip())
        queries_item = int(inp[i])
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    print(result)
    #fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    #fptr.write('\n')

    #fptr.close()
