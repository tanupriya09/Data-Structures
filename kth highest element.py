def partition(arr,low,high):
    i = low - 1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<pivot:
            i += 1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
k = int(input("Enter value of k"))
def kth_highest(arr,low,high,k):
    if low<=high:
        pivot = partition(arr,low,high,)
        if k<pivot:
            return kth_highest(arr,low,pivot-1,k)
        elif k==pivot:
            return arr[pivot]
        else:
            return kth_highest(arr,pivot+1,high,k)
#arr = [3, 9, 5, 7, 1, 0]
arr = [20,-12,0,-14,22]
arr = [-34,0,54,23,11,0,11]
arr = [54,-12,90,-33,10,-48]
arr = [0,1,2,3,4,5,6]
arr = [1,0,2,0,1,2,0,1]
print(kth_highest(arr,0,len(arr)-1,len(arr)-k))


