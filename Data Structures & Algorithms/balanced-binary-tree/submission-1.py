# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return [True, 0]

            leftBalanced, leftHeight = dfs(node.left)
            rightBalanced, rightHeight = dfs(node.right)

            if not rightBalanced or not leftBalanced:
                return [False, 0]

            if abs(rightHeight - leftHeight) > 1:
                balanced = False
                return [False, 0]

            return [True, max(leftHeight, rightHeight) + 1]

        balanced, height = dfs(root)
        return balanced


        