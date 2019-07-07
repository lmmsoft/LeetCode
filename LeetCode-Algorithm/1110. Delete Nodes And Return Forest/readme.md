### [1110\. Delete Nodes And Return Forest](https://leetcode.com/problems/delete-nodes-and-return-forest/)

Contest 144 https://leetcode.com/contest/weekly-contest-144/problems/delete-nodes-and-return-forest/

Difficulty: **Medium**


Given the `root` of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in `to_delete`, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/07/01/screen-shot-2019-07-01-at-53836-pm.png)**

```
Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
```

**Constraints:**

*   The number of nodes in the given tree is at most `1000`.
*   Each node has a distinct value between `1` and `1000`.
*   `to_delete.length <= 1000`
*   `to_delete` contains distinct values between `1` and `1000`.


#### Solution

- 比赛时候没想太清楚，直接按照题目要求模拟，一步步的做，最后比赛结束没来得及完全实现
- 赛后看了答案，多想想，发现这题可以大大简化
    - 删除数字的顺序不影响最后的结果 -> 所以可以按照任意顺序删除 -> 所以可以只递归扫描一遍，遇到 要删的数字就删除，不需要反复判断反复扫描
    - 如果上面这种思路，大概需要考虑几种情况
        - 被删除节点的左右子树可以插入森林(如果左右本身不删除的话)
        - 一个节点如果父节点不删除，那就不能插入森林，否则可以插入森林

Language: **Python3**

```python3
from typing import List, Dict
​
​
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None
​
​
class Solution:
    def __init__(self):
        self.p: int = 0
        self.forest: Dict[int, TreeNode] = {}
​
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.forest[self.p] = root
​
        def exist(tree: TreeNode, to_delete: int) -> bool:
            if tree.val == to_delete:
                return True
            if tree.left and exist(tree.left, to_delete):
                return True
            if tree.right and exist(tree.right, to_delete):
                return True
            return False
​
        def split(tree: TreeNode, to_delete: int) -> (bool, List[TreeNode], bool):
            if tree.val == to_delete:
                trees: List[TreeNode] = []
                if tree.left:
                    trees.append(tree.left)
                if tree.right:
                    trees.append(tree.right)
                return True, trees, False
​
            if tree.left:
                if tree.left.val == to_delete:
                    finished, trees, b = split(tree.left, to_delete)
                    tree.left = None
                    return True, trees, True
​
                else:
                    finished, trees, b = split(tree.left, to_delete)
                    if finished:
                        return finished, trees, b
​
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
​
        def delete(to_delete: int) -> None:
            # find
​
            key = 0
            tree = None
            for key1, tree1 in self.forest.items():
                if exist(tree1, to_delete):
                    key = key1
                    tree = tree1
                    break
​
            finished, foreast2, need_root = split(tree, to_delete)
```