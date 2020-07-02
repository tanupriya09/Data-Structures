class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linked_list:
    def __init__(self):
        self.head = None

def view_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
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

list1 = linked_list()
list1.head = insert(list1.head, 2)
list1.head = insert(list1.head, 3)
list1.head = insert(list1.head, 7)
list1.head = insert(list1.head, 9)
view_list(list1.head)

list2 = linked_list()
list2.head = insert(list2.head, 3)
list2.head = insert(list2.head, 2)
list2.head = insert(list2.head, 6)
list2.head = insert(list2.head, 5)
view_list(list2.head)

def add_lists():
    list3 = linked_list()
    temp1 = list1.head
    temp2 = list2.head
    value = temp1.data + temp2.data
    carry=value//10
    node1=Node(value%10)
    list3.head=node1
    result=node1
    temp1=temp1.next
    temp2=temp2.next
    while temp1 and temp2:
        value= temp1.data + temp2.data + carry
        result.next=Node(value % 10)
        carry=value//10
        result=result.next
        temp1=temp1.next
        temp2=temp2.next
    while temp1:
        value= temp1.data + carry
        result=Node(value % 10)
        carry=value//10
        result=result.next
        temp1=temp1.next
    while temp2:
        value=temp2.data+carry
        result = Node(value % 10)
        carry = value // 10
        result = result.next
        temp2 = temp2.next
    if carry>0:
        result.next=Node(carry)
    view_list(list3.head)
add_lists()




