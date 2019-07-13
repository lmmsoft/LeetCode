### [1120\. Maximum Average Subtree](https://leetcode.com/problems/maximum-average-subtree/)
- https://leetcode.com/problems/maximum-average-subtree/
- https://leetcode.com/contest/biweekly-contest-4/problems/maximum-average-subtree/
Difficulty: **Medium**


Given the `root` of a binary tree, find the maximum average value of any subtree of that tree.

(A subtree of a tree is any node of that tree plus all its descendants. The average value of a tree is the sum of its values, divided by the number of nodes.)

**Example 1:**

![](https://assets.leetcode.com/uploads/2019/04/09/1308_example_1.png)

```
Input: [5,6,1]
Output: 6.00000
Explanation: 
For the node with value = 5 we have and average of (5 + 6 + 1) / 3 = 4.
For the node with value = 6 we have and average of 6 / 1 = 6.
For the node with value = 1 we have and average of 1 / 1 = 1.
So the answer is 6 which is the maximum.
```

**Note:**

1.  The number of nodes in the tree is between `1` and `5000`.
2.  Each node will have a value between `0` and `100000`.
3.  Answers will be accepted as correct if they are within `10^-5` of the correct answer.


#### Solution
- dfs 深度搜索二叉树，思路是对的，但是想了一会儿，写得比较慢，这题和高手差距较大 1AC
- 这题要求每个子树中平均数的最大值，用深搜遍历每一颗子树的值即可
- 平均数= 总和/数的个数= (左子树和+右子树和+当前节点的值)/(左子树个数+右子树个数+1)
- 空数 总和和个数都是0
- 这题要return的是两个值sum和size，python比较直观，java和c++可以返回大小为2的数组或者vector来替代，也可以定义一个struct

Language: **Python3**

```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        avg_max = -1
​
        def dfs(n: TreeNode) -> (int, int):
            nonlocal avg_max
            if not n:
                return 0, 0
            lsum, lsize = dfs(n.left)
            rsum, rsize = dfs(n.right)
​
            all_sum = lsum + rsum + n.val
            all_size = lsize + rsize + 1
            avg_max = max(avg_max, all_sum / all_size)
​
            return all_sum, all_size
​
        dfs(root)
​
        return avg_max
```