print("Matrix Addition B/W 3x3 and 4x4 Matrices")
print("Enter Values for 3x3 Matrix:")
a11=int(input("Enter value for a11:  "))
a12=int(input("Enter value for a12:  "))
a13=int(input("Enter value for a13:  "))
a21=int(input("Enter value for a21:  "))
a22=int(input("Enter value for a22:  "))
a23=int(input("Enter value for a23:  "))
a31=int(input("Enter value for a31:  "))
a32=int(input("Enter value for a32:  "))
a33=int(input("Enter value for a33:  "))
print("Enter Values for 3x4 Matrix:")
a11=int(input("Enter value for a11:  "))
a12=int(input("Enter value for a12:  "))
a13=int(input("Enter value for a13:  "))
a14=int(input("Enter value for a14:  "))
a21=int(input("Enter value for a21:  "))
a22=int(input("Enter value for a22:  "))
a23=int(input("Enter value for a23:  "))
a24=int(input("Enter value for a24:  "))
a31=int(input("Enter value for a31:  "))
a32=int(input("Enter value for a32:  "))
a33=int(input("Enter value for a33:  "))
a34=int(input("Enter value for a34:  "))
A= [[a11, a12, a13],
       [a21, a22, a23],
       [a31, a32, a33]]

B= [[a11, a12, a13, a14],
       [a21, a22, a23, a24],
       [a31, a32, a33, a34]]

result = [[0, 0, 0, 0],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]]

for i in range(len(A)):
    for j in range(len(B)):
        result[i][j] += A[i][j] + B[i][j]

print("The Addition of given Matrix is\n")
for r in result:
    print(r)
