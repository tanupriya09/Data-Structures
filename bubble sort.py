
#    #> array[6]: array[5], array[6] = array[6], array[5]

# print(array)
# a = 13
# b = 23
# print(a)
# print(b)
#
# # temp = a
# # a = b
# # b = temp
# # print(a)
# # print(b)
#
# a, b = b, a
# print(a)
# print(b)
# print(array)
# if array[0] > array[1]:
#     array[0], array[1] = array[1], array[0]
#
# if array[1] > array[2]:
#     array[1], array[2] = array[2], array[1]
#
# if array[2] > array[3]:
#     array[2], array[3] = array[3], array[2]
# # .....
#
# if array[5]

# for item in array:
#     print(item)

array_1 = [85, 23, 76, 98, 12, 102, 8]




 le_sort(array):
    arr_len = len(array)
    total_iteration = 0
    for outer_index in range(arr_len - 1):
        # print("outer index: ", outer_index)
        for inner_index in range(arr_len - 1 - outer_index):
            total_iteration += 1
            # print("inner_index: ", inner_index)
            if array[inner_index] > array[inner_index + 1]:
                array[inner_index], array[inner_index + 1] = array[inner_index + 1], array[inner_index]

    print(total_iteration)
    print(array)


def bubble_sort_v2(array):
    arr_len = len(array)
    total_iteration = 0
    for outer_index in range(arr_len - 1):
        # print("outer index: ", outer_index)
        for inner_index in range(arr_len - 1):
            total_iteration += 1
            # print("inner_index: ", inner_index)
            if array[inner_index] > array[inner_index + 1]:
                array[inner_index], array[inner_index + 1] = array[inner_index + 1], array[inner_index]

    print(total_iteration)
    print(array)


bubble sort(array_1)
bubble_sort_v2(array_1)

bubble_sort(array_2)
bubble_sort_v2(array_2)