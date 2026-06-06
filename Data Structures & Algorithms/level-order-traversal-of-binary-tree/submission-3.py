# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        prev_level = -1
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if level != prev_level:
                result.append([node.val])
            else:
                result[-1].append(node.val)
            
            if node.left is not None:
                q.append((node.left, level + 1))
            if node.right is not None:
                q.append((node.right, level + 1))
            
            prev_level = level

        return result
            



        