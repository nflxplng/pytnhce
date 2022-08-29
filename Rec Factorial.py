def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
a= int(input("Enter the Number: "))
if a<0:
    print("There can be no Negative Factorial")
elif a==0:
    print("The Factorial of 0 is 1")
else:
    print("The factorial of", a, "is",recur_factorial(a))

