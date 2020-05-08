def reverse_array(arr):
    if len(arr)==0:
        print("Invalid Input")
    for i in range(0,len(arr)//2):
        arr[i],arr[len(arr)-1-i] =arr[len(arr)-1-i],arr[i]



arr = [34,55,10,63,80]
reverse_array(arr)
print(arr)