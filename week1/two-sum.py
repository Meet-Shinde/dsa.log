#My approach (brute force)
class Solution:
    def twoSum(self, nums, target):
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if target==nums[i]+nums[j]:
                        output=[i,j]
                        return output
#Best solution
class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for index, value in enumerate(nums):
            rest = target - value
            if rest in seen:
                return [seen[rest], index]
            seen[value] = index
        return None