class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None
def view_list(head):
    count=0
    temp = head
    while temp:
        print(temp.data, end=" ")
        count+=1
        temp = temp.next
    print("\n")
def insert(head, value):
    new_node = Node(value)
    if head is None:
         head = new_node
         return head
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head
def length(head):
    count = 0
    temp = head
    while temp:
        count += 1
        temp = temp.next
    return count
list1 = linked_list()
list1.head = insert(list1.head, 0)
list1.head = insert(list1.head, 3)
list1.head = insert(list1.head, 4)
list1.head = insert(list1.head, 9)
view_list(list1.head)
n1=length(list1.head)

list2 = linked_list()
list2.head = insert(list2.head, 2)
list2.head = insert(list2.head, 4)
list2.head = insert(list2.head, 5)
list2.head = insert(list2.head, 8)
list2.head = insert(list2.head, 12)
view_list(list2.head)
n2=length(list2.head)

def merge_lists():
    list3=linked_list()
    i=list1.head
    j=list2.head
    if i.data<j.data:
        node=Node(i.data)
        i=i.next
    else:
        node=Node(j.data)
        j=j.next
    list3.head=node
    k=node
    p1,p2=0,0
    while p1<n1 and p2<n2 and i and j:
        if i.data<j.data:
            node=Node(i.data)
            i=i.next
            p1+=1
        else:
            node=Node(j.data)
            j=j.next
            p2+=1
        k.next=node
        k=k.next
    while p1<n1 and i:
        node = Node(i.data)
        i = i.next
        p1+=1
    while p2<n2 and j:
        node = Node(j.data)
        j = j.next
        p2+=1
    k.next = node
    k = k.next
    view_list(list3.head)
merge_lists()


