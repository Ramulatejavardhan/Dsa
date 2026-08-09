nums=[0,1,0,11,23,0]
left=0
for right in range(0,len(nums)):
    if nums[right]!=0:
        temp=nums[right]
        nums[right]=nums[left]
        nums[left]=temp
        left=left+1
print(nums)
# Time Complexity → O(N)
# Space Complexity → O(1)