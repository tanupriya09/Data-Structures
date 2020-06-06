stk = []
def Push(stk,element):
    stk.append(element)
def isvalid(element1,element2):
    if element2=="(" and element1==")":
        pass
    elif element2=="{" and element1=="}":
        pass
    else:element2=="[" and element1=="]"
    pass
pattern = "[{()}]"
pattern = "{(}(})({}"
pattern = "(([[{([[("
pattern = "[[{}(){()}]]"
for element1 in pattern:
    if element1 == "[" or element1== "{" or element1== "(":
        Push(stk, element1)
    else:
        if len(stk)==0:
            print("Invalid Pattern")
            exit()
        else:element2 = stk.pop()
        isvalid(element1,element2)
if len(stk)==0:
    print("Valid Pattern")
else:print("Invalid Pattern")





