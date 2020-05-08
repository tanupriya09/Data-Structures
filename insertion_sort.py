array = [1, 3, 4, 5, 2]
# 0, 1, 2, 3, 4

# temp = array[4]
# array[4] = array[3]
# array[3] = array[2]
# array[2] = array[1]
# array[1] = temp

# print(array)
# # [1, 3, 3, 4, 5]
# # [1, 5, 3, 4, 5]

index = len(array) - 1
key = array[index]

while index >= 2:
    print(index)
    array[index] = array[index - 1]
    index -= 1
array[index] = key
print(array)