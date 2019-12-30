# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        s = 0
        nodes = [root]
        next_nodes = []
        while nodes:
            for n in nodes:
                s += n.val
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            if not next_nodes:
                return s

            nodes = next_nodes
            next_nodes = []
            s = 0

    def deepestLeavesSum_by_lee(self, root):
        l = [root]
        while l:
            pre, l = l, [child for p in l for child in [p.left, p.right] if child]
        return sum(node.val for node in pre)
