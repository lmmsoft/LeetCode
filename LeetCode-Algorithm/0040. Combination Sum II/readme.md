### [40\. Combination Sum IICopy for MarkdownCopy for MarkdownCopy for MarkdownCopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/combination-sum-ii/)

Difficulty: **Medium**


Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.

Each number in `candidates` may only be used **once** in the combination.

**Note:**

*   All numbers (including `target`) will be positive integers.
*   The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```

**Example 2:**

```
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```


#### Solution
- 01背包，详见注释，在0039完全背包的基础上，从大到小判断，同时注意去重
Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)  # 对结果没影响，帮助assert
        dp: List[List[List]] = [[[]]] + [[] for i in range(target)]
        for num in candidates:
            for s in range(target, num - 1, -1):
                # 不需要 and dp[s - num], 因为dp[0] 是[[]] ，可以推倒，做 [] + [num]，而 dp[1] to dp[target] 初始化都是[]，不能推倒
                if (s - num) >= 0: # 如果加上 and dp[s - num]，会快一点，减少一些无效推倒， if [] 为False, if [[]] 为True
                    li = [l + [num] for l in dp[s - num]]
                    dp[s] += li
        # 结果去重
        res = [list(t) for t in set(tuple(li) for li in dp[target])]  # 这一行很精妙
        res.sort(key=dp[target].index)  # 这句话对结果在影响，是按照dp[target]里面的先后顺序，重新排序res，帮助本地assert
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [
        [1, 2, 5],
        [1, 1, 6],
        [2, 6],
        [1, 7],
    ]
    assert Solution().combinationSum2([2, 5, 2, 1, 2], 5) == [
        [1, 2, 2],
        [5]
    ]
​
```