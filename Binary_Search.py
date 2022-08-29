def BinarySearch(list,key):
    low=0
    high=len(list)-1
    Found = False
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list[mid]:
            Found = True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid+1
    if (Found==True):
        print("Key is Found!")
    else:
        print("Key is not Found..")
num=int(input("How many numbers do you want to enter?"))
list=[int(input("Enter a number: ")) for x in range(num)]
list.sort()
print(list)
key=int(input("Enter the key Element: "))
BinarySearch(list,key)
