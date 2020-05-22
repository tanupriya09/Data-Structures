
def partition(arr,left,right):
    i = left - 1
    pivot = arr[right]
    for j in range(left,right):
        if arr[j]<pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[right]=arr[right],arr[i+1]
    return i+1
def quick_sort(arr,left,right):
    if left<=right:
        pi = partition(arr,left,right)
        quick_sort(arr,left,pi-1)
        quick_sort(arr,pi+1,right)
arr =  [1,0,2,0,1,2,0,2,1,2,0,1,1,0,2,2]
quick_sort(arr,0,len(arr)-1)
print(arr)
