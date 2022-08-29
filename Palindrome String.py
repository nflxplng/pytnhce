string=input(("Enter a String to check if it is a palindrome or not: "))
if(string==string[::-1]):
    print("The entered string is a Palindrome!")
else:
    print("The entered string is not a Palindrome...")
