def sorted(arr):
    left = 0
    right = len(arr) - 1
    while right>left:
        if arr[left]==0:
            left += 1
        elif arr[right]==1:
            right -= 1
        else:
            arr[left],arr[right]=arr[right],arr[left]
            left += 1
            right -= 1
arr = [0, 1, 0, 1, 1, 0, 1, 1, 0]
sorted(arr)
print(arr)
