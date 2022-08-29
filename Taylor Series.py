#Taylor Series program
import sys
import math
x=float(input("Enter the degree"))   #read degree
x=x*(3.142/180)  #convert degree to radian
term=x
sinx=term
n=3 # Number of trems
while(term>sys.float_info.epsilon):  #epsilon is a identifier to overcome too short input error
   fact=2*n*(2+n)
   term=term*x*x/fact
   sinx=sinx+term
   n=n+1
print("the value of sinx",sinx) # sinx without library function
print("the value of sinx value using library function",math.sin(x))  #sinx value with library function
