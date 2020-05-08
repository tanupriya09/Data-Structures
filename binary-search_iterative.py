def binary_search(arr, left, right, key):
    mid = left + (right - left) // 2
    if right >= left:
        if key == arr[mid]:
            return mid
        elif key > arr[mid]:
            return binary_search(arr, mid + 1, right, key)
        else:
            return binary_search(arr, left, mid - 1, key)
    else:
        return -1


arr = [10, 14, 19, 27, 33, 35, 42, 44]
key = 10
# left = 0
# right = len(arr) - 1

result = binary_search(arr, 0, len(arr) - 1, 33)
print(result)

keys = [10, 33, -1, -1100, 1000, 35]
for key in keys:
    result = binary_search(arr, 0, len(arr) - 1, key)
    print(result)

# left = 0
# right =  7
# mid = 3 , arr[mid] = 27
# if key ==  arr[mid]:
#     return

# if key > arr[mid]:
# right side
# mid + 1: right

# if key < arr[mid]:
# left side
# left :   mid- 1
# mid =