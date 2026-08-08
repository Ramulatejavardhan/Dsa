class Solution(object):
    def moveZeroes(self, nums):
        left=0
        for right in range(0,len(nums)):
            if nums[right]!=0:
                temp=nums[right]
                nums[right]=nums[left]
                nums[left]=temp
                left=left+1
obj=Solution()