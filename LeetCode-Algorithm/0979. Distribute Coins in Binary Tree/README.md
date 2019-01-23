# Link
- Problem
    - https://leetcode.com/problems/longest-turbulent-subarray/
    - https://leetcode-cn.com/problems/longest-turbulent-subarray/
- Contest
    - https://leetcode.com/contest/weekly-contest-120/problems/distribute-coins-in-binary-tree/
    - https://leetcode-cn.com/contest/weekly-contest-120/problems/distribute-coins-in-binary-tree/
- Official solution
    - 
    
# Description
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4
 

Note:

1<= N <= 100
0 <= node.val <= N
# Solution
- 又是一道赛后AC的题
- 自己对题目推理的过程基本对了，但不够简化
    - 导致深搜过程中需要保存的变量太多
    - 于是又构造了有更多数据的TreeNode2，先复制一遍树再计算
- 其实不需要保存这么多过程的变量的
    - 看了官方的解放，思路差不多，但并不要保存过程中的数据，每次累加就行了
    - def dfs()也直接写到def distributeCoins()的内部
    - 比赛中快的选手不到十分钟就写出来的，代码肯定不会长
    - 以后自己也要尽可能把思路简化，把代码写短，这样思路会更清晰，容易调试，不容易出错，遇到以后的比赛或面试也会更容易应对

```python
class Solution(object):
    def distributeCoins(self, root):
        self.ans = 0

        def dfs(node):
            if not node: return 0
            L, R = dfs(node.left), dfs(node.right)
            self.ans += abs(L) + abs(R)
            return node.val + L + R - 1

        dfs(root)
        return self.ans
```