#Programme for finding minimum value in ascending order rotated sorted array-

def rotated_array(arr):

    if len(arr)==1:
        return arr[0]

    for i in range(0,len(arr)-1):
        if arr[i]<arr[i+1]:
            pass
        else :
            if arr[i]>arr[i+1]:
             print(arr[i+1])

arr =[3,4,5,1,2]
rotated_array(arr)


