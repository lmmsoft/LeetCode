# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        avg_max = -1

        def dfs(n: TreeNode) -> (int, int):
            nonlocal avg_max
            if not n:
                return 0, 0
            lsum, lsize = dfs(n.left)
            rsum, rsize = dfs(n.right)

            all_sum = lsum + rsum + n.val
            all_size = lsize + rsize + 1
            avg_max = max(avg_max, all_sum / all_size)

            return all_sum, all_size

        dfs(root)

        return avg_max


if __name__ == '__main__':
    n1: TreeNode = TreeNode(5)
    n2: TreeNode = TreeNode(6)
    n3: TreeNode = TreeNode(1)
    n1.left = n2
    n1.right = n3

    assert Solution().maximumAverageSubtree(n1) == 6

    n1: TreeNode = TreeNode(10)
    n2: TreeNode = TreeNode(1)
    n3: TreeNode = TreeNode(1)
    n1.left = n2
    n1.right = n3

    assert Solution().maximumAverageSubtree(n1) == 4
