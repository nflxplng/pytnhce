def factorial(n):
    res = 1
    for i in range (1,n+1):
        res=res*i
    return res
n=int(input("Enter the value for N:  "))
r=int(input("Enter the value for R:  "))
ncr=factorial(n)/(factorial(r)*factorial(n-r))
print("The value of nCr is", ncr)
