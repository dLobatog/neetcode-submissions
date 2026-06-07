# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        # if both p and q are > current node, then search on right
        # if both are < current node, then search on left
        # if both are = to current node, return it
        # if p > current node and q < current node or viceverse, return it

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val == root.val or q.val == root.val:
            return root
        elif (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
            return root

        # [2,1,3,4,5,7,8,9]

        