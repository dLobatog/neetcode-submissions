# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # same structure would come from same in order and post order traversal
        def iot(node: Optional[TreeNode]):
            if not node:
                return '-'
            return iot(node.left) + str(node.val) + iot(node.right)

        def pot(node: Optional[TreeNode]):
            if not node:
                return '-'
            return str(node.val) + pot(node.left) + pot(node.right) 


        return iot(p) == iot(q) and pot(p) == pot(q)

        