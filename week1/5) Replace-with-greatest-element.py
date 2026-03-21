#My approach
#Couldnt find an approach

#Best way
class Solution:
    def replaceElements(arr):
        right_max=-1
        for i in range(len(arr)-1, -1, -1):
            current=arr[i]
            arr[i]=right_max
            right_max=max(right_max, current)
        return arr

#Note: Try to visualize the transfers.