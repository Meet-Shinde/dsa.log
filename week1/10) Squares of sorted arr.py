#My approach: 
class Solution:
    def sortedSquares(nums):
        left=0
        right=len(nums)-1
        arr=[]
        while left<right:
            if abs(nums[left])>abs(nums[right]):
                arr.insert(0, nums[left]**2)
                left+=1
            else:
                arr.insert(0, nums[right]**2)
                right-=1
        if left==right:
            arr.insert(0, nums[right]**2)
        return arr
#T: O(n^2) cuz of repetitive insert()
#S: O(n)

#Optimal way: 
class Solution:
    def sortedSquares(nums):
        left=0
        right=len(nums)-1
        k=right
        arr=[0]*len(nums) #making room as the insertion is from back.
        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                arr[k]=nums[left]**2
                left+=1
                k-=1
            else:
                arr[k]=nums[right]**2
                right-=1
                k-=1
        return arr
#T: O(n)
#S: O(n)

'''Note: Notice how this also follows the same pattern
as Valid palindrome (putting a specific conditioned element
at the end. ---Two-pointers, one at front and one at back.)'''

