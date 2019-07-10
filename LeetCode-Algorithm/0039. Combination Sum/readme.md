### [39\. Combination SumCopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/combination-sum/)

Difficulty: **Medium**


Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

The **same** repeated number may be chosen from `candidates` unlimited number of times.

**Note:**

*   All numbers (including `target`) will be positive integers.
*   The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
```

**Example 2:**

```
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```


#### Solution
- 完全背包，具体解放见注释，用三维数组记录所有方案

Language: **Python3**

```python3
from typing import List
​
​
class Solution1:
    def combinationSum(self, nums: List[int], target: int) -> List:
        dp2: dict = {0: [[]]}
​
        for n in nums:
            for i in range(n, target + 1):
                if (i - n) in dp2:
                    li: list = dp2[i - n]
                    li2 = [l + [n] for l in li]
                    if i in dp2:
                        dp2[i] = dp2[i] + li2
                    else:
                        dp2[i] = li2
​
        if target in dp2:
            return dp2[target]
        return []
​
​
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> int:
        # 保存方案，使用三维数组
        # 第一维： dp:List 表示和为不同数时的方案
        # 第二维： dp[s]:List 表示和i的方案列表
        # 第三维 每种具体的方案都是数组， dp[s][j]:List 表示和为s的第j个方案的数组
        dp: list = [[[]]] + [[] for i in range(
            target)]  # 初始化 eg: [[[]], [], [], [], [], []]， 保证和为0有一种方案 [], 完全背包需要恰好装满的时候，dp[0] 必须初始化为0
​
        for n in nums:  # 对于每个数
            for s in range(n, target + 1):  # 完全背包，从小到大
                li = [l + [n] for l in dp[s - n]]  # 对于把和为s-n的每种方案，添加数字n, 就变成一种新的 和为s的方案
                dp[s] += li  # 把新方案添加到 原来和为s的方案里
        return dp[target]
​
​
if __name__ == '__main__':
    assert Solution().combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert Solution().combinationSum([2, 3, 5], 8) == [
        [2, 2, 2, 2],
        [2, 3, 3],
        [3, 5]
    ]
    assert Solution().combinationSum([2], 1) == []
​
```