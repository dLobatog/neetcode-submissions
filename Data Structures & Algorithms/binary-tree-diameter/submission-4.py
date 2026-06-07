# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node):
            nonlocal diameter 
            if not node:
                return 0

            leftSubtree = dfs(node.left)
            rightSubtree = dfs(node.right)
            diameter = max(
                diameter,
                leftSubtree + rightSubtree, 
            )

            return max(leftSubtree, rightSubtree) + 1

        dfs(root)
        return diameter

                