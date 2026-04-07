# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        oneStep, twoStep = head, head

        index = 0
        while oneStep and twoStep:                
            if oneStep:
                oneStep = oneStep.next
            if twoStep:
                twoStep = twoStep.next
                if twoStep:
                    twoStep = twoStep.next
            if oneStep is not None and oneStep == twoStep:
                return True

        return False