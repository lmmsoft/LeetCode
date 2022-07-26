# [113\. Path Sum II](https://leetcode.com/problems/path-sum-ii/submissions/)

## Description

Difficulty: **Medium**  

Related Topics: [Backtracking](https://leetcode.com/tag/backtracking/), [Tree](https://leetcode.com/tag/tree/), [Depth-First Search](https://leetcode.com/tag/depth-first-search/), [Binary Tree](https://leetcode.com/tag/binary-tree/)


Given the `root` of a binary tree and an integer `targetSum`, return _all **root-to-leaf** paths where the sum of the node values in the path equals_ `targetSum`_. Each path should be returned as a list of the node **values**, not node references_.

A **root-to-leaf** path is a path starting from the root and ending at any leaf node. A **leaf** is a node with no children.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg)

```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg)

```
Input: root = [1,2,3], targetSum = 5
Output: []
```

**Example 3:**

```
Input: root = [1,2], targetSum = 0
Output: []
```

**Constraints:**

*   The number of nodes in the tree is in the range `[0, 5000]`.
*   `-1000 <= Node.val <= 1000`
*   `-1000 <= targetSum <= 1000`


## Solution

做过112,再做113就简单了，把列表加入递归函数就行，注意 li.copy() 列表复制再传递

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.l = []
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def find(root, ts, li):
            
            if not root:
                return
            
            li = li.copy()
            li.append(root.val)
            
            if not root.left and not root.right:
                if root.val == ts:
                    
                    self.l.append(li)
                return 
            
            
            find(root.left, ts-root.val, li)
            find(root.right, ts-root.val, li)
        
        find(root, targetSum, [])
        return self.l
            if not root:
```