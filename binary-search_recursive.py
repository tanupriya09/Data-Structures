# Python3 Program for recursive binary search. Returns index of x in arr if present, else -1
def binarySearch(arr, left, right, key):
    # Check base case
    if right >= left:

        mid = left + (right - left) // 2

        # If element is present at the middle itself
        if arr[mid] == key:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > key:
            return binarySearch(arr, left, mid - 1, key)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, right, key)

    else:
        # Element is not present in the array
        return -1


# Driver Code
arr = [2, 3, 4, 10, 40]
x = 11

# Function call
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")