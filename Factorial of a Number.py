def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

a= int(input("Enter the Number: "))
print("The factorial of", a, "is", factorial(a))
