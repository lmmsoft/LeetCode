### [653\. Two Sum IV - Input is a BST](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/)

Difficulty: **Easy**


Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

**Example 1:**

```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
```

**Example 2:**

```
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
```


#### Solution
- Easy 水题，用O(N)空间储存已有的值，然后BFS DFS都行

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
​
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        d = set()
        found = False
        
        def dfs(n:TreeNode):
            nonlocal d
            nonlocal found
            if not n:
                return
            if found:
                return
            if (k - n.val) in d:
                found = True
            else:
                d.add(n.val)
            dfs(n.left)
            dfs(n.right)
            
            
        
        dfs(root)
        return found
```

## Link
- https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
- https://leetcode.com/submissions/detail/247839167/