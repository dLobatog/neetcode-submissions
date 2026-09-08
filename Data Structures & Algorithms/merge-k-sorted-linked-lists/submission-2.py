# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # max lists, 10k
        # simple solution. 
        # find min head of lists. add it to new list. make original min head head.next 
        # repeat until done
        # we would run min(lists) n times 
        # then k times
        # so at least n * k 
        # perhaps a simpler thing. use a min heap of size len(lists)
        # fill it will first element of all lists
        # reduce all lists size by 1
        # concat all of the heap elements
        # resume until lists are empty
        dummy = ListNode()
        cur = dummy
        h = []

        for l in lists:
            if l:
                heapq.heappush(h, l)

        while h:
            node = heapq.heappop(h)
            cur.next = node
            cur = cur.next 
            if node and node.next:
                heapq.heappush(h, node.next)

        return dummy.next
            


