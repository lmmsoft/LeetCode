# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
