#My approach
class Solution:
    def containsDuplicate(nums):
        nums_t=set(nums)
        if(len(nums_t)==len(nums)):
            return True
        else:
            return False

#A bit cleaner version
class Solution:
    def containsDuplicate(nums):
        return len(set(nums)) != len(nums)