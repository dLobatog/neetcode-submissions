"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        cur = head
        cur_copy = None
        while cur:
            cur_copy = Node(x=cur.val)
            old_to_new[cur] = cur_copy
            cur = cur.next
        # now that we have the copies, we need to start linking
        cur = head
        while cur:
            # print('map', old_to_new[cur].val,  old_to_new[cur].next,  old_to_new[cur].random)
            if cur.next:
                # print("setting next of cur", cur.val)
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                # print("setting random of cur", cur.val)
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
        return old_to_new[head]


        
