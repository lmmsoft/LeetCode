# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        d: dict = {}
        x_node: TreeNode = None

        def dfs(n: TreeNode):
            nonlocal x_node

            if not n:
                return 0
            else:
                if n.val == x:
                    x_node = n

                num = dfs(n.left) + dfs(n.right) + 1
                d[n.val] = num
                return num

        dfs(root)

        # check_left
        if x_node.left:
            num1 = d[x_node.left.val]
            num2 = n - num1
            if num1 > num2:
                return True
        # check right
        if x_node.right:
            num1 = d[x_node.right.val]
            num2 = n - num1
            if num1 > num2:
                return True
        # check parent
        num2 = d[x_node.val]
        num1 = n - num2
        if num1 > num2:
            return True

        return False


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t9 = TreeNode(9)
    t10 = TreeNode(10)
    t11 = TreeNode(11)

    t1.left, t1.right = t2, t3
    t2.left, t2.right = t4, t5
    t3.left, t3.right = t6, t7
    t4.left, t4.right = t8, t8
    t5.left, t5.right = t10, t11

    assert Solution().btreeGameWinningMove(t1, 11, 3)
