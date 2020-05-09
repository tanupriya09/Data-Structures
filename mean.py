def mean(arr):
    sum = 0
    for element in arr:
        sum = sum+element
    return sum/len(arr)

arr = [10,20,30,40]
result = mean(arr)
print(result)