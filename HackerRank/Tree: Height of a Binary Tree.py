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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def maxHeight(node, depth, maxDepth):
    if node == None:
        return depth
    else:
        x1 = maxHeight(node.left, depth+1, maxDepth)
        x2 = maxHeight(node.right, depth+1, maxDepth)
        if x1 > maxDepth:
            maxDepth = x1
        if x2 > maxDepth:
            maxDepth = x2
        return maxDepth
def height(root):
    height = 0
    stack = []
    x = maxHeight(root, -1, 0)
    return 0


tree = BinarySearchTree()
t = 7#int(input())

arr = [3, 5, 2, 1, 4, 6, 7]#list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

print(height(tree.root))
