#My approach (weird one)
class Solution: 
    def isAnagram(s, t): 
        r=s+t 
        r_set=set(r) 
        return len(s)==len(r_set)
#This fails for more than 2 duplicates of a character

#The most optimal solution
class Solution:
    def isAnagram(s, t):
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            count[ch] = count.get(ch, 0) - 1
        for val in count.values():
            if val != 0:
                return False
        return True

#Another optimal solution (using counter function)
from collections import Counter
class Solution:
    def isAnagram(s,t):
        return Counter(s)==Counter(t)

'''Note: Set = who exists
    Dict/Counter = how many exist'''