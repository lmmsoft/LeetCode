# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeNode:
    def __init__(self, x):
        self.val: int = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


## 把数组转换为完全二叉树

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


import queue


class Solution:
    def __init__(self):
        self.height_to_node_value = {}

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS， mid,right, left with height
        if not root:
            return []

        q = queue.Queue()
        q.put((root, 0))
        while not q.empty():
            node, height = q.get()
            if height not in self.height_to_node_value:
                self.height_to_node_value[height] = node.val

            if node.right:
                q.put((node.right, height + 1))
            if node.left:
                q.put((node.left, height + 1))

        li = sorted([(height, value) for height, value in self.height_to_node_value.items()], key=lambda x: x[0])
        return [x[1] for x in li]


if __name__ == '__main__':
    root = array_to_tree_nodel([1, 2, 3, None, 5, None, 4])
    l = Solution().rightSideView(root)
    assert l == [1, 3, 4]
