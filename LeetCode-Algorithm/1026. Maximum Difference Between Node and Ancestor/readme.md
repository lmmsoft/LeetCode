### [1026\. Maximum Difference Between Node and Ancestor](https://leetcode.com/contest/weekly-contest-132/problems/maximum-difference-between-node-and-ancestor/)

Difficulty: **Medium**

Given the `root` of a binary tree, find the maximum value `V` for which there exists **different** nodes `A` and `B` where `V = |A.val - B.val|` and `A` is an ancestor of `B`.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

**Example 1:**

![](http://i68.tinypic.com/2whqcep.jpg)

```
Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
```

**Note:**

1.  The number of nodes in the tree is between `2` and `5000`.
2.  Each node will have value between `0` and `100000`.

#### Solution
- https://leetcode.com/contest/weekly-contest-132/ranking/
- 题意： 求最大的 祖先节点与子节点 的差值绝对值
- 深搜，保存 max min， 搜到叶子节点计算差值即可
- 写解题报告时顺便测试自己的array_to_tree_nodel辅助函数，好用

Language: **Python3**

```python3
from typing import List, Optional
​
​
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
​
​
class Solution_in_contest:
    h = []
    h_max = []
​
    mmax = 0
​
    cmin = None
    cmax = None
​
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.search(root)
        return self.mmax
​
    def search(self, node: TreeNode):
        if node != None:
            self.h.append(node.val)
            self.check(node.val)
​
            self.search(node.left)
            self.search(node.right)
​
            self.h.pop(len(self.h) - 1)
​
            if node.val == self.cmin:
                self.cmin = None
            elif node.val == self.cmax:
                self.cmax = None
​
    def check(self, v: int):
        self.cmin = tmin = self.cmin if self.cmin and v >= self.cmin else self.findmin()
        self.cmax = tmax = self.cmax if self.cmax and v <= self.cmax else self.findmax()
​
        if tmax - tmin > self.mmax:
            self.mmax = tmax - tmin
​
    def findmin(self):
        m = None
        for i in self.h:
            if m == None:
                m = i
            elif i < m:
                m = i
        return m
​
    def findmax(self):
        m = None
        for i in self.h:
            if m == None:
                m = i
            elif i > m:
                m = i
        return m
​
​
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, Min=100001, Max=-1):
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
​
        return dfs(root, root.val, root.val)
​
​
def array_to_tree_nodel(l: List[int]) -> Optional[TreeNode]:
    head: Optional[TreeNode] = None
    tree_node_list: List[Optional[TreeNode]] = [None] * len(l)
​
    for idx, val in enumerate(l):
        if val is None:
            continue
        node = TreeNode(val)
        if idx == 0:
            head = node
        else:
            parent_idx = (idx + 1) // 2 - 1
            if tree_node_list[parent_idx]:
                if idx % 2:  # left tree
                    tree_node_list[parent_idx].left = node
                else:
                    tree_node_list[parent_idx].right = node
​
        tree_node_list[idx] = node
​
    return head
​
​
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
​
    root.left = l1
    root.right = r1
    l1.left = l21
    l1.right = l22
    l22.left = l33
    l22.right = l34
​
    r1.right = r22
    r22.left = r31
​
    print(Solution().maxAncestorDiff(root))
​
    assert Solution().maxAncestorDiff(array_to_tree_nodel([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])) == 7
​
```