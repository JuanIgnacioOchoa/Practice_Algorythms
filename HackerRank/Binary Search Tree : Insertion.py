class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (str(root.info) + " ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        #Enter you code here.
        node = Node(val)
        if self.root == None:
            self.root = node
            return
        current = self.root
        prev = None
        while current != None:
            prev = current
            if current.info > val:
                current = current.left
            else:
                current = current.right
        if prev.info > val:
            prev.left = node
        else:
            prev.right = node
        return 

tree = BinarySearchTree()
t = 6#int(input())

arr = list(map(int, "4 2 3 1 7 6".split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
