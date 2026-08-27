# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # simplest way would be to gather all 
        l1_num = 0
        if l1:
            cur = l1
            l1_num = ''
            while cur: 
                l1_num += str(cur.val)
                cur = cur.next
            l1_num = l1_num[::-1]
            l1_num = int(l1_num)
        if l2:
            cur = l2
            l2_num = ''
            while cur: 
                l2_num += str(cur.val)
                cur = cur.next
            l2_num = l2_num[::-1]
            l2_num = int(l2_num)

        final = str(l1_num + l2_num)[::-1]
        start = ListNode(val=final[0])
        cur = start
        for i in range(1, len(final)):
            cur.next = ListNode(val=int(final[i]))
            cur = cur.next 

        return start

