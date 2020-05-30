arr1 = [1,4]
arr2 = [1,4]
answer =0
for j in reversed(range(len(arr2))):
    for i in range(len(arr1)):
        ans_arr = (arr2[j] * (10 ** (len(arr2) - 1 - j))) * (arr1[i] * (10 ** (len(arr1) - 1 - i)))
        answer= answer + ans_arr
ans_arr=[]
while answer!=0:
    ans_arr.insert(0,answer%10)
    answer=answer//10
print(ans_arr)












