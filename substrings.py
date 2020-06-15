def substring(str):
    for i in range(len(str)):
        for j in range(i+1,len(str)+1):
             a = str[i:j]
             print(a)
substring("python")

