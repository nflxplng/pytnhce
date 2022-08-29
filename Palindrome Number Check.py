a=int(input("Enter a Value:"))
temp=a
r=0
while(a>0):
    d=a%10
    r=r*10+d
    a=a//10
if(temp==r):
    print("The entered value is a Palindrome Number!")
else:
    print("It is not a Palindrome Number..")
