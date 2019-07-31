# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        found = False

        def dfs(n: TreeNode):
            nonlocal d
            nonlocal found
            if not n:
                return
            if found:
                return
            if (k - n.val) in d:
                found = True
            else:
                d.add(n.val)
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return found
