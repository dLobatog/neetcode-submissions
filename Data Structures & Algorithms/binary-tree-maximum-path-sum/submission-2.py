# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        totalMax = float('-inf')

        def dfs(node):
            nonlocal totalMax

            if not node:
                return 0
            
            leftSubtree = dfs(node.left)
            rightSubtree = dfs(node.right)
            totalMax = max(
                totalMax, 
                node.val, 
                leftSubtree + node.val,
                rightSubtree + node.val,
                leftSubtree + rightSubtree + node.val
            )
            maxPath = max(
                leftSubtree + node.val,
                rightSubtree + node.val,
                node.val
            )
            return maxPath

        dfs(root)
        return totalMax