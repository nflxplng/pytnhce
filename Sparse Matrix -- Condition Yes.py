a=[
     [0, 1, 0],
     [0, 5, 0],
     [0, 1, 0]
     ]
print("The Matrix is:")
print("a= \n[[0, 1, 0], \n[0, 5, 0], \n[0, 1, 0]]\n")
count=0
rows=len(a)
cols=len(a)
size=rows*cols
for i in range(0, rows):
    for j in range(0, cols):
        if(a[i][j]==0):
            count=count+1
if (count>(size/2)):
    print("Given Matrix is a Sparse Matrix")
else:
    print("The Given Matrix is not a Sparse Matrix")
