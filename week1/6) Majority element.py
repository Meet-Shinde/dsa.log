#My approach (actually got it right)
class Solution:
    def majorityElement(nums):
        count = {}
        for val in nums:
            count[val] = count.get(val, 0) + 1
        for res in count:
            if count[res] > (len(nums) / 2):
                return res
#T: O(n)
#S: O(n)

#Best approach (Boyer-Moore Algorithm)
class Solution:
    def majorityElement(nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
#T: O(n)
#S: O(1)

#Note: Again for frequencies, use hashmap/dict