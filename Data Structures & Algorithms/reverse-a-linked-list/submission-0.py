# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        '[null <-0<-1 2->3]'
        while cur:
            nxt = cur.next #1, 2
            cur.next = prev #reversed 0 pointer to the left - null, 0
            prev = cur #0,1
            cur = nxt #1,2
        return prev
        


