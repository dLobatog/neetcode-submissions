# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
          return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # both children: hang the left subtree under the smallest node on the right
            node = root.right
            while node.left:
                node = node.left
            # smallest on node.right - make root.left hang there
            node.left = root.left
            # now root.right contains previous root.left, no "val'
            return root.right
        return root

            