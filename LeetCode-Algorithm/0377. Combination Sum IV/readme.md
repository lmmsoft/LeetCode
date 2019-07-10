### [377\. Combination Sum IVCopy for MarkdownCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/combination-sum-iv/)

Difficulty: **Medium**


Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

**Example:**

```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

**Follow up:**  
What if negative numbers are allowed in the given array?  
How does it change the problem?  
What limitation we need to add to the question to allow negative numbers?


#### Solution
- 完全背包，最后求排列数和组合数的方法是不同的
    - 如果是组合数，那么先foreach nums，再foreach sum 保证同一个数字只考虑一次（出现在结果里是连在一起的）
    - 如果是组合数，先foreach sum, 再foreach nums， 同一个数字会在不同位置考虑（出现在结果里是不连续的）
Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    # 这种按照题意，求排列数个数
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp: List = [1] + [0] * target
​
        for s in range(0, target + 1):  # 完全背包，从小到大
            for n in nums:  # 对于每个数
                if s - n >= 0:
                    dp[s] += dp[s - n]
        return dp[target]
​
    # 这种前两行交换，求组合数个数
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        dp: List = [1] + [0] * target
​
        for s in range(0, target + 1):  # 完全背包，从小到大
            for n in nums:  # 对于每个数
                if s - n >= 0:
                    dp[s] += dp[s - n]
        return dp[target]
​
​
if __name__ == '__main__':
    assert Solution().combinationSum4([1, 2, 3], 4) == 7
    assert Solution().combinationSum4([4, 2, 1], 32) == 39882198
​
```