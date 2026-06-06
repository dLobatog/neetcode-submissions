# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower_bound, upper_bound):
            if not node:
                return True
            
            if node.val <= lower_bound or node.val >= upper_bound:
                return False

            
            leftBST = dfs(node.left, lower_bound, node.val)
            rightBST = dfs(node.right, node.val, upper_bound)

            return leftBST and rightBST 
        
        return dfs(root, float('-inf'), float('inf'))

        
