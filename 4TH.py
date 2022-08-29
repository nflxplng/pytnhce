a=input("what shape do you want to calculate the area of?")
if a=="square":
    b=input("what is the side of the square?")
    print("The area of the figure is" , b*b)

elif a=="circle":
    c=int(input("what is the radius of the circle?"))
    print("the area of the figure is" , 3.14*c*c)

elif a=="triangle":
    d=int(input("what is the height of the triangle?"))
    e=int(input("what is the base of the triangle?"))
    print("the area of the figure is" , 0.5*e*d)

else:
    print("error")
