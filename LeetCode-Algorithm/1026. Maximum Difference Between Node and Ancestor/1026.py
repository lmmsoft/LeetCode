from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution_in_contest:
    h = []
    h_max = []

    mmax = 0

    cmin = None
    cmax = None

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.search(root)
        return self.mmax

    def search(self, node: TreeNode):
        if node != None:
            self.h.append(node.val)
            self.check(node.val)

            self.search(node.left)
            self.search(node.right)

            self.h.pop(len(self.h) - 1)

            if node.val == self.cmin:
                self.cmin = None
            elif node.val == self.cmax:
                self.cmax = None

    def check(self, v: int):
        self.cmin = tmin = self.cmin if self.cmin and v >= self.cmin else self.findmin()
        self.cmax = tmax = self.cmax if self.cmax and v <= self.cmax else self.findmax()

        if tmax - tmin > self.mmax:
            self.mmax = tmax - tmin

    def findmin(self):
        m = None
        for i in self.h:
            if m == None:
                m = i
            elif i < m:
                m = i
        return m

    def findmax(self):
        m = None
        for i in self.h:
            if m == None:
                m = i
            elif i > m:
                m = i
        return m


class Solution:
    def maxAncestorDiff_2(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, Min, Max):
            if not node:
                return Max - Min
            if node.val < Min:
                l = dfs(node.left, node.val, Max)
                r = dfs(node.right, node.val, Max)
            elif node.val > Max:
                l = dfs(node.left, Min, node.val)
                r = dfs(node.right, Min, node.val)
            else:
                l = dfs(node.left, Min, Max)
                r = dfs(node.right, Min, Max)
            return max(l, r)

        return dfs(root, root.val, root.val)  # 这种写法不能 给Min Max默认参数，是因为 if node.val < Min时，Max传入的不是正确的值

    def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(
            self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)),
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))
        ) if root else mx - mn


def array_to_tree_nodel(l: List[int]) -> Optional[TreeNode]:
    head: Optional[TreeNode] = None
    tree_node_list: List[Optional[TreeNode]] = [None] * len(l)

    for idx, val in enumerate(l):
        if val is None:
            continue
        node = TreeNode(val)
        if idx == 0:
            head = node
        else:
            parent_idx = (idx + 1) // 2 - 1
            if tree_node_list[parent_idx]:
                if idx % 2:  # left tree
                    tree_node_list[parent_idx].left = node
                else:
                    tree_node_list[parent_idx].right = node

        tree_node_list[idx] = node

    return head


if __name__ == '__main__':
    root: TreeNode = TreeNode(8)
    l1: TreeNode = TreeNode(3)
    r1: TreeNode = TreeNode(10)
    l21: TreeNode = TreeNode(1)
    l22: TreeNode = TreeNode(6)
    r22: TreeNode = TreeNode(14)
    l33: TreeNode = TreeNode(4)
    l34: TreeNode = TreeNode(7)
    r31: TreeNode = TreeNode(13)

    root.left = l1
    root.right = r1
    l1.left = l21
    l1.right = l22
    l22.left = l33
    l22.right = l34

    r1.right = r22
    r22.left = r31

    print(Solution().maxAncestorDiff(root))

    assert Solution().maxAncestorDiff(array_to_tree_nodel([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 7
