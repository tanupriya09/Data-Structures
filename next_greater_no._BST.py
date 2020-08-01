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
root = Node(100)
insert(root,99)
insert(root,96)
insert(root,98)
insert(root,97)
insert(root,102)

def next_greater_num(root,key):
    if root:
        next_greater_num(root.left,key)
        if root.data>key:
            print(root.data)
            exit()
        next_greater_num(root.right,key)
next_greater_num(root,97)

