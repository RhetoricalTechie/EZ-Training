def factorial(n):
    if n==1:
        return 1
    a = n*factorial(n-1)
    return a
n=int(input("Enter the factorial: "))
b=factorial(n)
print(b) 