#My approach:
#Couldnt formulate an approach.

#Best way:
class Solution:
    def search(nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2 
            if target>nums[mid]:
                left=mid+1
            elif target<nums[mid]:
                right=mid-1
            else:
                return mid
        return -1
#T: O(log n)
#S: O(1)

'''Note: Two-pointers are applied in lots of problems.
Master it properly.'''