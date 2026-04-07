# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if in order traversal, including null nodes (serialized) string is in another string
        # then we can do it in o(n+m)
        def serialize(node):
            if not node:
                return '#'

            return str(node.val) + ',' +  serialize(node.left) + ',' +  serialize(node.right)

        return serialize(subRoot) in serialize(root)

        # def sameTree(tree, subTree):
        #     if not tree and not subTree:
        #         return True

        #     if tree and not subTree or subTree and not tree:
        #         return False

        #     if tree.val == subTree.val:
        #         return sameTree(tree.left, subTree.left) and sameTree(tree.right, subTree.right)
            
        #     return False

        # if not subRoot:
        #     return True

        # if not root:
        #     return False

        # if sameTree(root, subRoot):
        #     return True 

        # return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoott)
        
        
        
        