arr = [0]
arr = [1,0,0,0,0]
arr = [1,2,3,4,5]
arr = [9,7,6,9,0]
arr = [3,4,5,8,9]
arr = [1,2,9,9,9]
arr = [9,9,9,9]
arr = [0,0,0,9,9,9,9]
arr = [6,4,9,9,0]

if arr==[9]*len(arr):
    b=[1]
    for i in range(len(arr)):
        b.append(0*i)
    print(b)
    exit()
for i in reversed(range(0,len(arr))):
    if arr[i]<9 and arr[i]>=0:
        arr[i] = arr[i]+1
        break
    else :
        if arr[i]==9:
            arr[i]=0
            i-=1
        else:
            arr[i]=arr[i]+1
            break
print(arr)






