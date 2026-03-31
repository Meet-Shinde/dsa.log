#My approach: (Loads of errors in cases)
class Solution:
    def hasCycle(head):
        fast=head
        slow=head
        if head==None or head.next==None:
            return False
        while (fast.next != None) or (fast.next.next!=None):
            if slow==fast:
                break
            slow=slow.next
            fast=fast.next.next
        return slow==fast

#Optimal Solution: (Floyd's Algorithm)
class Solution:
    def hasCycle(head):
        fast=head
        slow=head
        if head==None or head.next==None:
            return False
        while (fast!=None) and (fast.next != None):
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False
#T: O(n)
#S: O(1)

'''Note: Try to take cases and see how the 
code gives the output.'''