def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
n=int(input("Enter the factorial: "))
b=factorial(n)
print(f"The factorial of {n} is: {b}") 
