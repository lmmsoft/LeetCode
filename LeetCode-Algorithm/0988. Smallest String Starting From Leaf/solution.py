# 1 最短
# 2 最短里字符最小的

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self.min_s = 'z' * 100
        self.min_h = 1001

    def smallestFromLeaf(self, root: 'TreeNode') -> 'str':

        def find(n: TreeNode, height: int, s: str):
            ch = chr(97 + n.val)
            s2 = ch + s

            if n.left == None and n.right == None:
                self.min_s = min(s2, self.min_s)
                self.min_h = min(height, self.min_h)

            # if height == self.min_h:
            #     return

            if not n.left == None:
                find(n.left, height + 1, s2)
            if not n.right == None:
                find(n.right, height + 1, s2)
            return

        find(root, 1, "")
        # print(self.min_s)
        return self.min_s


def case1():
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(3)
    n6 = TreeNode(4)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    print(Solution().smallestFromLeaf(n0))


def case2():
    n0 = TreeNode(25)
    n1 = TreeNode(1)
    n2 = TreeNode(3)
    n3 = TreeNode(1)
    n4 = TreeNode(3)
    n5 = TreeNode(0)
    n6 = TreeNode(2)
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n2.left = n5
    n2.right = n6
    print(Solution().smallestFromLeaf(n0))


def case3():
    n0 = TreeNode(2)
    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n0.left = n1
    n0.right = n2

    n3 = TreeNode(1)
    n4 = TreeNode(0)
    n1.right = n3
    n3.left = n4

    n5 = TreeNode(0)
    n2.left = n5

    print(Solution().smallestFromLeaf(n0))


def case4():
    n0 = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n0.left = n1
    n0.right = n2

    n3 = TreeNode(15)
    n4 = TreeNode(7)
    n2.left = n3
    n2.right = n4

    print(Solution().smallestFromLeaf(n0))


if __name__ == '__main__':
    case1()
    case2()
    case3()
    case4()
