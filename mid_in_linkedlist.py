class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
llist = LinkedList()
node1 = Node(1)
llist.head = node1
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5
node6 = Node(6)
node5.next = node6
def mid():
    slow = llist.head
    fast = llist.head
    while fast.next and fast:
        fast = fast.next.next
        if fast :
            slow=slow.next
        if fast is None:
            break
    return slow.data
print(mid())