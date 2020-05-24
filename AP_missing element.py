def missing_element(arr):
        left = 0
        right = len(arr)-1
        d = (arr[right]-arr[left])/len(arr)
        print(d)
        while right>=left:
                if arr[left+1]==arr[left]+d:
                        left+=1
                else:
                        print(arr[left]+d)
                        break
                if arr[right-1]==arr[right]-d:
                        right-=1
                else:
                        print(arr[right]-d)
                        break
#arr = [2,6,8,10]                 4
#arr = [1,4,7,13,16]              10
#arr = [8,5,2,-4]                 -1
#arr = [-10,0,20,30,40]           10
#arr = [-5,-10,-15,-25]           -20
#arr = [-12,-7,-2,8,13]            3
arr = [20,14,8,2,-10]             #-4
missing_element(arr)
