# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # for each node, I need the max value traversing down
        # if max_value > node.val - not good node, else, good node
        def traverseWithMax(node, max_value):
            if not node:
                return 0

            currentGoodNode = 1 if max_value <= node.val else 0
            leftGoodNodes = traverseWithMax(node.left, max(max_value, node.val)) 
            rightGoodNodes = traverseWithMax(node.right, max(max_value, node.val))
            return currentGoodNode + leftGoodNodes + rightGoodNodes

        return traverseWithMax(root, float('-inf')) 
        