# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        res = []

        def search(node:TreeNode):
            if not node:
                return
            res.append(node.val)
            if node.left:
                search(node.left)
            if node.right:
                search(node.right)

        search(root1)
        search(root2)
        return sorted(res)
