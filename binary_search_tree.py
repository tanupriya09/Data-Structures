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
root = Node(15)
insert(root,10)
insert(root,6)
insert(root,20)
insert(root,5)
insert(root,18)
insert(root,12)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)
inorder(root)

def find(root,data):
    if root is None:
        return "Invalid"
    if root.data==data :
        return root
    if root.data>data:
        return find(root.left,data)
    if root.data<data:
        return find(root.right,data)
print(find(root,20))


