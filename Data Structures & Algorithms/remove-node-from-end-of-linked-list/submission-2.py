# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if we remove the nth node from the end, we need to know where the end Lies 
        #. a simple way: send 2 pointers with nth difference
        if not head:
            return None

        current = head
        start_plus = head


        for i in range(n):
            start_plus = start_plus.next 

        if not start_plus:
            return head.next

        while start_plus.next:
            start_plus = start_plus.next
            current = current.next

        # print('finished', start_plus, current.val) 


        current.next = current.next.next
        return head
