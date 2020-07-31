class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
def insert(root,data):
    if root is None:
        root = Node(data)
    else:
        if root.data>data:
            if root.left == None:
                root.left = Node(data)
            else:
                insert(root.left,data)
        else:
            if root.right == None:
                root.right = Node(data)
            else:
                insert(root.right,data)
root = Node(4)
insert(root,5)
insert(root,6)
insert(root,7)
insert(root,1)
insert(root,2)
insert(root,3)

def kth_largest(root,k,count):
    if root:
        kth_largest(root.right, k,count)
        count[0]+=1
        if count[0]==k:
          print(root.data)
        kth_largest(root.left,k,count)
kth_largest(root,7,count=[0])

def kth_smallest(root,k,count):
    if root:
        kth_smallest(root.left, k,count)
        count[0]+=1
        if count[0]==k:
          print(root.data)
        kth_smallest(root.right,k,count)
kth_smallest(root,7,count=[0])