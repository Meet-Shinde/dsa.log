#My approach (modified two-sum I): 
class Solution: 
    def twoSum(numbers, target):
        dic={} 
        for index, num in enumerate(numbers): 
            res=target-num 
            if res in dic: 
                return (dic[res]+1, index+1) 
            dic[num]=index 
            return None
#T: O(n)
#S: O(n)

#My second approach (fails in some cases): 
class Solution:
    def twoSum(numbers, target):
        first=0
        next=1
        while first<len(numbers)-1:
            if numbers[first]+numbers[next]==target:
                return [first+1, next+1]
            next+=1
            if numbers[first]+numbers[next]==target:
                return [first+1, next+1]
            first+=1
        return None

#Optimal way: 
class Solution:
    def twoSum(numbers, target):
        left=0
        right=len(numbers)-1
        while left<=right:
            if numbers[left]+numbers[right]==target:
                return [left +1, right+1]
            if numbers[left]+numbers[right]<target:
                left+=1
            if numbers[left]+numbers[right]>target: 
                right-=1
        return None
#T: O(n)
#S: O(1)

'''Note: When array is sorted and you need a pair sum:
        start at both ends
        not at neighboring indices'''