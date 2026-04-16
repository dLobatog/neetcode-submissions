# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we find p in left  , q in right - this is the lowestCommonAncestor
        # we find q in left, p in right, this is the lowestCommonAncestor
        # we find p in left, q in left... this can't be. 
        result = None

        def dfs(node):
            nonlocal result, p, q  
            if node is None:
                return False

            # print("node.val", node.val, p.val, q.val)
            if p.val <= node.val and q.val >= node.val: 
                return node
            elif p.val >= node.val and q.val <= node.val: 
                return node
            elif p.val < node.val and q.val < node.val:
                return dfs(node.left)
            elif p.val > node.val and q.val > node.val:
                return dfs(node.right)
            
        return dfs(root)