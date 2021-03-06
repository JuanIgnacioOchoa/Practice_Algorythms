class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def postOrder(root):
    values = ""
    stack = []
    current = root
    while current != None or len(stack):
        if current == None:
            current = stack.pop()
            if len(stack) > 0 and stack[-1] == current.right:
                tmp = stack.pop()
                stack.append(current)
                current = tmp
            else:
                values += str(current.info) + " "
                current = None
        else:
            if current.right:
                stack.append(current.right)
            stack.append(current)
            current = current.left
    print(values)


tree = BinarySearchTree()
t = 6#int(input())

arr = [1, 2, 5, 3, 6, 4]#list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

postOrder(tree.root)