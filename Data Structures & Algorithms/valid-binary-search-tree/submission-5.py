# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower_bound, higher_bound):
            if not node:
                return True

            if lower_bound < node.val < higher_bound:
               left_res = dfs(node.left, lower_bound, node.val) 
               right_res = dfs(node.right, node.val, higher_bound)
               return left_res and right_res
            
            return False

        return dfs(root, -float('inf'), float('inf'))
        
