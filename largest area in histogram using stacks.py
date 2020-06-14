a=[1,2,3]
a=[1,2,3,4,5 ]           #9
a=[9,8]                  #16
a=[9,8,7]                #21
a=[1,2,3,4,5,4,3,2,1]    #15
a=[1,1,1,1]              #4
a=[6,2,5,4,5,1,6]        #12
max_area=0
i=0
stack =[]
while i<len(a):
    if len(stack)==0:
        stack.append(i)
        i+=1
    elif len(stack)!=0 and a[stack[-1]]<=a[i]:
        stack.append(i)
        i += 1
    elif a[stack[-1]]>a[i]:
        highest_value=a[stack.pop()]
        if len(stack)!=0:
            area = highest_value * (i - stack[-1] - 1)
        else:area =highest_value*(i)
        max_area=max(area,max_area)
while len(stack) != 0:
    highest_value=a[stack.pop()]
    if len(stack)!=0:
        area = highest_value * (i - stack[-1] - 1)
    else:
        area = highest_value * (i)
    max_area = max(area, max_area)
print(max_area)