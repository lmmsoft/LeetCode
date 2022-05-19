# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        l = self.search(root)
        return l

    def search(self, node: Optional[TreeNode]) -> List[int]:
        l = []

        if node.left:
            ll = self.search(node.left)
            l.extend(ll)

        if node.right:
            lr = self.search(node.right)
            l.extend(lr)

        l.append(node.val)
        return l
