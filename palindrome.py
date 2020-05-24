 # check whether given number is palindrome or not -

 # 1.

str = "12321"
str1= str[::-1]
if str==str1:
    print("YES,it is a pallindrome")
else:
    print("NO,it is not a pallindrome")

# 2.

def pallindrome(arr):
    n = len(arr)
    for i in range(n//2):
        if arr[i]!=arr[n-1-i]:
            return False
        else:
            return True
arr = [1,2,3,2,1]
print(pallindrome(arr))


