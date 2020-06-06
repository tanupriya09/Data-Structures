# QUEUE -

queue = ["1","2","3","4","5"]

# add elements
def Enqueue(elements):
    queue.insert(0,elements)
Enqueue(6)
print(queue)

# remove elements
def Dequeue(elements):
    if len(queue)>0:
        queue.pop(elements)
    else :print("Empty")
Dequeue(0)
print(queue)

# display elements
def display():
    for i in range(len(queue)):
        print(queue[i])
display()





