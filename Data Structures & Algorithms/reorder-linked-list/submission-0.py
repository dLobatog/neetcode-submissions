# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # One potential way of doing this, is traversing the list first, then using
        # another data sturcture to reorder it (an array)

        # find halfpoint
        slow = head
        fast = head.next
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse 2nd half
        def reverse(node):
            prev = None
            cur = node
            while cur:
                next_node = cur.next 
                cur.next = prev
                prev = cur 
                cur = next_node 
            return prev 

        second = reverse(second)
        first = head 

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1 
            second = tmp2
        # 1st half = cur
        # 2nd half reversed = cur2
        # new_next = cur.next
        # cur.next = cur2
        # cur2.next = new_next 
        # cur2.next = 