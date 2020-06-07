list = ["5","-2","4","C","-4","9","+","+"]            # -27
list = [10, 5, 2, 'C', 'D', '+']                      # 40
list = [10, 20, 'D', 'D', 'D', '+']                   # 550
list =  [10, 20, 'D', 'D', 'D', '+', 'C', 'C']        # 150
list  = [10, 20, 'C', 'D', 'C', '+', 'D', 10]         # Invalid Input
list  = [5, 2, 'C', 'D', '+']                         # 30
def push(stk,ele):
    stk.append(ele)
stk = []
ops = ["C","D","+"]
for ele in list:
    if ele not in ops:
        push(stk,int(ele))
    elif ele=="C":
        if len(stk)!=0 :
            stk.pop()
        else:
            print("Invalid Input")
            exit()
    elif ele=="D":
        if  len(stk)!=0:
            push(stk,int(stk[-1])*2)
        else:
            print("Invalid Input")
            exit()
    else:
        if ele=="+" and len(stk)>1:
            push(stk,int(stk[-1])+int(stk[-2]))
        else:
            print("Invalid Input")
            exit()
print(stk)
print("Total Points :",sum((stk)))

