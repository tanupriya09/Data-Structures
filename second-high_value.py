def second_highest(arr):
    if len(arr) < 2:
        return "No element found"

    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
    else:
        second = arr[0]
        first = arr[1]

    for i in range(2, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif second < arr[i] < first:
            second = first
        else:
            pass
    return second


arr = [12, 30, 10, 72]
# arr = [-1, -2, 2, -3]
# arr = [2, 2]
# arr = [2]
result = second_highest(arr)
print(result)
# elm < second

# elm > second  and elm < first
#     second = ele
# ele > first
#     second = first
#     first = ele