arr = [-2,1,-3,4,-1,2,1,-5,4]
sub = []
for i in range(len(arr)):
    for j in range(i+1,len(arr)+1):
        a = arr[i:j]
        sub.append(a)
print(sub)
a = max(sub,key=sum)
print(a)

















