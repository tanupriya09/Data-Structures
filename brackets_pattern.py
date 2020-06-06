stk = []
def Push(stk,element):
    stk.append(element)
def Pop(stk):
    stk.pop()
pattern = "((()))))"
pattern = "((((("
pattern = "))))"
pattern = "(())"
for element in pattern:
    if element=="(":
        Push(stk,element)
    else:
        if len(stk)==0:
            print("Invalid Pattern")
            exit()
        else:
            Pop(stk)
if len(stk)==0:
    print("Valid Pattern")
else:
    print("Invalid Pattern")






