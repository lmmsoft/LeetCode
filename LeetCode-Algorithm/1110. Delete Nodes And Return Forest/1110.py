from typing import List, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


class Solution:
    def __init__(self):
        self.p: int = 0
        self.forest: Dict[int, TreeNode] = {}

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.forest[self.p] = root

        def exist(tree: TreeNode, to_delete: int) -> bool:
            if tree.val == to_delete:
                return True
            if tree.left and exist(tree.left, to_delete):
                return True
            if tree.right and exist(tree.right, to_delete):
                return True
            return False

        def split(tree: TreeNode, to_delete: int) -> (bool, List[TreeNode], bool):
            if tree.val == to_delete:
                trees: List[TreeNode] = []
                if tree.left:
                    trees.append(tree.left)
                if tree.right:
                    trees.append(tree.right)
                return True, trees, False

            if tree.left:
                if tree.left.val == to_delete:
                    finished, trees, b = split(tree.left, to_delete)
                    tree.left = None
                    return True, trees, True

                else:
                    finished, trees, b = split(tree.left, to_delete)
                    if finished:
                        return finished, trees, b

            if tree.right:
                if tree.right.val == to_delete:
                    finished, trees, b = split(tree.right, to_delete)
                    tree.right = None
                    return True, trees, True
                else:
                    finished, trees, b = split(tree.right, to_delete)
                    if finished:
                        return finished, trees, b
            return False, None, None

        def delete(to_delete: int) -> None:
            # find

            key = 0
            tree = None
            for key1, tree1 in self.forest.items():
                if exist(tree1, to_delete):
                    key = key1
                    tree = tree1
                    break

            finished, foreast2, need_root = split(tree, to_delete)
            if not finished:
                return
            if not self.forest.get(key, None):
                self.forest.pop(key)
            if not need_root:
                self.forest.pop(key)
            if foreast2:
                for tree in foreast2:
                    self.p += 1
                    self.forest[self.p] = tree

        for t in to_delete:
            delete(t)

        res = []
        for f in self.forest.values():
            res.append(f)
        return res


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7

    res = Solution().delNodes(t1, [3, 5])#124,6,7
    print(res)

    # t1 = TreeNode(1)
    # Solution().delNodes(t1, [1])

    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)

    t1.left = t2
    t2.left = t4
    t2.right = t3
    to_del = [2, 3]
    Solution().delNodes(t1, to_del)  # 1, 4
