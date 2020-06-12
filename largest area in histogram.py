a = [6,2,5,4,5,1,6]                #12
a = [1,1,1,1]                      #4
a = [1,2,3,4,5,3]                  #12
a = [4,7,9,12,3,0]                 #21
a = [10,8,6,4,2,0]                 #18
a = [1,3,5,7,9]                    #15
a = [5,5,5,5,5]                    #25
a = [8,5,10,3,7,2]                 #15
area = 0
for i in range(len(a)):
    start = 0
    for j in range(len(a)):
        if a[j]>=a[i] and j!= len(a)-1:
            j+=1
        else:
            if a[j]>=a[i] and j==len(a)-1:
                end = j
            else:
                end = j-1
            current_area = a[i] * (end - start + 1)
            if current_area>area:
                area = current_area
            new_start = j + 1
            start = new_start
print("Max area is :",area)




















