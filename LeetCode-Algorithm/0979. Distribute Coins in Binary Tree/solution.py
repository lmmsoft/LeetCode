# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeNode2:

    def __init__(self, val, left, right, sum_node, sum_coin, in_move, out_move):
        self.val = val
        self.left = left
        self.right = right
        self.sum_node = sum_node
        self.sum_coin = sum_coin
        self.in_move = in_move
        self.out_move = out_move


class Solution:
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        root2 = TreeNode2(0, None, None, 0, 0, 0, 0)
        self.copyTrees(root, root2)

        self.calc2(root2)
        return root2.in_move

    def copyTrees(self, node1, node2):
        """
        :type node1: TreeNode
        :type node2: TreeNode2
        """
        node2.val = node1.val

        if node1.left is None:
            node2.left = None
        else:
            node2.left = TreeNode2(0, None, None, 0, 0, 0, 0)
            self.copyTrees(node1.left, node2.left)

        if node1.right is None:
            node2.right = None
        else:
            node2.right = TreeNode2(0, None, None, 0, 0, 0, 0)
            self.copyTrees(node1.right, node2.right)

    def calc2(self, node: TreeNode2):
        if node.left is None:
            l = TreeNode2(0, None, None, 0, 0, 0, 0)
        else:
            self.calc2(node.left)
            l = node.left

        if node.right is None:
            r = TreeNode2(0, None, None, 0, 0, 0, 0)
        else:
            self.calc2(node.right)
            r = node.right

        node.sum_node = l.sum_node + r.sum_node + 1
        node.sum_coin = l.sum_coin + r.sum_coin + node.val
        node.in_move = l.in_move + l.out_move + r.in_move + r.out_move
        node.out_move = abs(node.sum_node - node.sum_coin)


def case1():
    root = TreeNode(3)
    node1 = TreeNode(0)
    node2 = TreeNode(0)
    root.left = node1
    root.right = node2

    ans = Solution().distributeCoins(root)
    print(ans)
    assert ans == 2


def case2():
    root = TreeNode(0)
    node1 = TreeNode(3)
    node2 = TreeNode(0)
    root.left = node1
    root.right = node2

    ans = Solution().distributeCoins(root)
    print(ans)
    assert ans == 3


def case3():
    root = TreeNode(1)
    node1 = TreeNode(0)
    node2 = TreeNode(2)
    root.left = node1
    root.right = node2

    ans = Solution().distributeCoins(root)
    print(ans)
    assert ans == 2


def case4():
    root = TreeNode(3)
    node1 = TreeNode(0)
    node2 = TreeNode(0)
    node4 = TreeNode(3)
    root.left = node1
    root.right = node2
    node2.right = node4

    ans = Solution().distributeCoins(root)
    print(ans)
    assert ans == 4


if __name__ == '__main__':
    case1()
    case2()
    case3()
    case4()
