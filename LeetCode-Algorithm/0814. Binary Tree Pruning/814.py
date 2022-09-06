# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



from typing import Optional

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        root_has_1 = self.has_1(root)
        if not root_has_1:
            return None

        return root

    def has_1(self, node: Optional[TreeNode]):
        # node is empty
        if not node:
            return False

        left_has_1 = self.has_1(node.left)
        if not left_has_1:
            node.left = None

        right_has_1 = self.has_1(node.right)
        if not right_has_1:
            node.right = None

        if node.val == 1 or left_has_1 or right_has_1:
            return True
        return False





