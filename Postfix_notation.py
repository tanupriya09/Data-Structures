def push(stk,ele):
    stk.append(ele)
eqn = "24+46+*"
eqn = "90-34*/"
eqn = "25*34+-"
def postfix(eqn):
    stk = []
    operator = ["+", "-", "/","*"]
    for ele in eqn:
        if ele not in operator:
            push(stk,ele)
        else:
            a = int(stk.pop())
            b = int(stk.pop())
            if ele=="+":
                push(stk,b+a)
            elif ele=="-":
                push(stk,b-a)
            elif ele=="*":
                push(stk,b*a)
            elif ele=="/":
                push(stk,b/a)
            else:
                print("Invalid Input")
    print(stk)
postfix(eqn)

