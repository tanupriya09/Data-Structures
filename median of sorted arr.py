
def median(arr):
    mid = len(arr)//2

    if len(arr)%2==1:
        return arr[mid]
    else:
        return (arr[mid-1]+arr[mid])/2

arr = [45,66,70,92]
print(median(arr))
