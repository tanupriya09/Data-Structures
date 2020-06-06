# STACKS -

stack = ["a","b","c","d","e"]

#check if stack is empty -
def ifempty(stack):
    if stack==[]:
        print("True")
    else:
        print("False")
ifempty(stack)

# addition in stack -
def Push(stack):
    stack.append("f")
    print(stack)
Push(stack)

# deletion in stack -
def Pop(stack):
        if len(stack)==0: # check if empty
            print("None")
        else:
            print(stack.pop())
Pop(stack)

# display elements in stack -
def display(stack):
    if stack==[]:
        print("Empty")
    else:
        for i in range(len(stack)-1,-1,-1):
            print(stack[i])
display(stack)


