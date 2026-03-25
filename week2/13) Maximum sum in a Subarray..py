#My approach:
#Couldnt find any, Medium problem :[

#Optimal Solution: (Kadane's Algorithm)
class Solution:
    def maxSubArray(nums):
        max_sum=min(nums)
        curr_sum=0
        for val in nums:
            curr_sum+=val
            if curr_sum>max_sum:
                max_sum=curr_sum
            if curr_sum<0:
                curr_sum=0
        return max_sum
#T: O(n)
#S: O(1)