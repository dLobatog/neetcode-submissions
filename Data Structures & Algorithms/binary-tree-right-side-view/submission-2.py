# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do a level order traversal and return the latest node
        if not root:
            return []
        level_traversal = []
        prev_level = -1
        q = deque()
        q.append((root, 0))

        while q:
            node, level = q.popleft()

            if level != prev_level:
                level_traversal.append([node.val])
            else:
                level_traversal[-1].append(node.val)

            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

            prev_level = level
        
        result = [level[-1] for level in level_traversal] # rightmost
        return result
