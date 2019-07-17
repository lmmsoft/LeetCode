# Definition for a binary tree node.
from typing import Dict, List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lcaDeepestLeaves1(self, root: TreeNode) -> TreeNode:
        self.parent: Dict[TreeNode, TreeNode] = {}
        self.deep_list: Dict[int, List[TreeNode]] = {}

        def dfs(n: TreeNode, deep: int):
            if deep in self.deep_list:
                self.deep_list[deep].append(n)
            else:
                self.deep_list[deep] = [n]

            if n.left:
                self.parent[n.left] = n
                dfs(n.left, deep + 1)
            if n.right:
                self.parent[n.right] = n
                dfs(n.right, deep + 1)

        dfs(root, 0)
        max_deep: int = max(self.deep_list.keys())

        leaves: list = self.deep_list[max_deep]
        while True:
            s = set()
            for l in leaves:
                s.add(l)
            if len(s) == 1:
                return list(s)[0]
            else:
                leaves = [self.parent[leaf] for leaf in leaves]

        return None

    # rank 11 superluminal
    # 类似的思路，使用 BFS 实现
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        parent = {}
        queue = set([root])
        while True:
            next_queue = set()
            for node in queue:
                for child in (node.left, node.right):
                    if child:
                        parent[child] = node
                        next_queue.add(child)
            if not next_queue:
                break
            queue = next_queue
        # 此时的queue就是所有的叶子节点，因为他们的next_queue是空的
        while len(queue) > 1:
            queue = set(parent[n] for n in queue)
        for node in queue:
            return node


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    assert Solution().lcaDeepestLeaves(n1) == n1

    n2.left = n4
    assert Solution().lcaDeepestLeaves(n1) == n4

    n2.right = n5
    assert Solution().lcaDeepestLeaves(n1) == n2
