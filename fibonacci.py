
# Fibonacci series till nth term -

n = int(input("Enter the nth number :"))
def fibonacci_series(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci_series(n-1) + fibonacci_series(n-2)
for i in range(1,n+1):
        print(fibonacci_series(i))