#My approach: 
'''(move all non zeroes to left and zeroes to the right.)
But this is not the right solution as the order messes up.'''
class Solution:
    def moveZeroes(nums):
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]==0 and nums[right]!=0:
                nums[left], nums[right]=nums[right], nums[left]
                left+=1
                right-=1
            elif nums[left]==0 and nums[right]==0:
                right-=1
            else:
                left+=1

#Optimal Solution: 
class Solution:
    def moveZeroes(nums):
        left=0
        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left], nums[right]=nums[right], nums[left]
                #interchanged them
                left+=1

'''Note: As the order was supposed to be preserved, 
back-pointer swapping fails.
Try to imagine different approaches.'''