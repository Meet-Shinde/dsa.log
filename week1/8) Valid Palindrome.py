#My approach: 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        lst=[]
        lst2=[]
        for char in s:
            if char.isalnum():
                lst.append(char)
        for i in range(len(lst)-1, -1, -1):
            lst2.append(lst[i])
        return lst==lst2
#T: O(n)
#S: O(n) cuz of creation of 2 lists

#Optimal Solution: 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
#T: O(n)
#S: O(1)

'''Note: for problems having:
        compare both front and back
        symmetric structures
        palindromes
    Try going for two-pointer approach.'''