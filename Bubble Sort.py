def bsort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
               temp=nums[j]
               nums[j]=nums[j+1]
               nums[j+1]=temp
nums=[5,1,8,3,2,7]

print("The given array is [5,1,8,3,2,7]\n")

bsort(nums)

print(nums)
