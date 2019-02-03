# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalTraversal(self, root: 'TreeNode') -> 'List[List[int]]':
        import collections
        d: dict = collections.defaultdict(list)  # key(x) -> value(y, val)

        def find(n: TreeNode, x: int, y: int):

            d[x].append((y, n.val))

            if not n.left is None:
                find(n.left, x - 1, y + 1)

            if not n.right is None:
                find(n.right, x + 1, y + 1)

        find(root, 0, 0)

        for k in d:
            d[k].sort()

        keys = d.keys()
        keys = sorted(keys)

        res = [[item[1] for item in d[k]] for k in keys]
        # for k in keys:
        #     r = []
        #     for tuple in d[k]:
        #         r.append(tuple[1])
        #     res.append(r)

        return res


def case():
    n0 = TreeNode(3)
    n1 = TreeNode(9)
    n2 = TreeNode(20)
    n0.left = n1
    n0.right = n2

    n3 = TreeNode(15)
    n4 = TreeNode(7)
    n2.left = n3
    n2.right = n4

    print(Solution().verticalTraversal(n0))


if __name__ == '__main__':
    case()
