# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        def dfs(node, height):
            nonlocal balanced 

            if not node:
                return height

            leftHeight = dfs(node.left, height + 1)
            rightHeight = dfs(node.right, height + 1)
            if abs(rightHeight - leftHeight) > 1:
                balanced = False
                return height

            return max(leftHeight, rightHeight)

        
        dfs(root, 0)
        return balanced


        