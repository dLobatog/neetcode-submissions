# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        
        while cur is not None:
            orig_next = cur.next
            cur.next = prev
            prev = cur 
            cur = orig_next
           
        return prev

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        prev = dummy
        pos = 1
        
        #1. Reach the beginning of the section
        while pos < left:
            prev = cur
            cur = cur.next
            pos += 1 
        
        # pos == left
        before = prev
        start  = cur 
        prev   = None
        
        # 2. Reverse the section (isolated)
        while pos <= right:
            orig_next = cur.next
            cur.next = prev
            prev = cur 
            cur = orig_next
            pos += 1

        # connect beginning of section 
        before.next = prev 
        # connect end of section
        start.next = cur
           
        return dummy.next

        
        