def sort(nums,size):
    for i in range(size):
        min=1
        for j in range(i+1,size):
            if nums[j]<nums[min]:
                min=j
                temp=nums[i]
                nums[i]=nums[min]
                nums[min]=temp
                print(nums)
nums=[5,3,8,6,7,2]
print("The given array is [5,3,8,6,7,2]\n")
size=len(nums)

print("The output of the array is \n")
sort(nums,size)

print(nums)
