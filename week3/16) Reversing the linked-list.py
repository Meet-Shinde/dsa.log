#My approach: (optimal)
class Solution:
    def reverseList(head):
        curr=head
        prev=None
        nexts=None
        if head==None or head.next==None:
            return head
        while curr != None:
            nexts=curr.next
            curr.next=prev
            prev=curr
            curr=nexts
        head=prev
        return head
#T: O(n)
#S: O(1)

#Optimal solution: (a bit cleaner)
class Solution:
    def reverseList(head):
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev
#T: O(n)
#S: O(1)

'''Note: After finishing the code, think on whether
it could be optimized in any way.'''