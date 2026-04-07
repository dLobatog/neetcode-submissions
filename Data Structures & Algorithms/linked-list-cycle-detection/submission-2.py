# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        oneStep, twoStep = head, head

        index = 0
        while twoStep and twoStep.next:  
            oneStep = oneStep.next
            twoStep = twoStep.next.next
            
            if oneStep == twoStep:
                return True

        return False