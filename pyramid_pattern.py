n = int(input("Enter the number"))
def pattern(n):
    for i in range(1,n+1):
        a = (n-i)*" "
        for j in range(0,i):
            a = a + str(j+1)
        for k in reversed(range(1,j+1)):
            a = a + str(k)
        print(a)
pattern(n)





