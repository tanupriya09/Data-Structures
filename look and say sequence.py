def seq(n):
    if n==1:
        return "1"
    a = seq(n - 1)
    count = 1
    ans = ""
    for i in range(len(a)):
        if i == len(a) - 1:
            ans = ans + str(count) + a[i]
        elif a[i] == a[i + 1]:
            count += 1
        else:
            ans = str(ans) + str(count) + a[i]
            count = 1
    return ans
print(seq(5))