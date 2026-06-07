# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        res = []
        def dfs(node):
            nonlocal res 

            if not node:
               res.append("N")
               return 

            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right) 

        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 0:
            return 
        encoded_tree = iter(data.split(','))

        def dfs():
            val = next(encoded_tree)

            if val == "N":
                return None

            node = TreeNode(val=int(val))
            node.left = dfs()
            node.right = dfs()
        
            return node
        
        return dfs()

        

