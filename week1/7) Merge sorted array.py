#My approach
class Solution:
    def merge(nums1, m, nums2, n):
        for num in nums2:
            nums1[-n]=num
            n=n-1
        nums1.sort()
#T: O(nlogn)

#Optimal solution
class Solution:
    def merge(nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
#T: O(n) as both the arrays are already sorted, the
#  time complexity should be O(n).

#Note: I still dont understand the optimal version