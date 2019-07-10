### [216\. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

Difficulty: **Medium**


Find all possible combinations of _**k**_ numbers that add up to a number _**n**_, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**

*   All numbers will be positive integers.
*   The solution set must not contain duplicate combinations.

**Example 1:**

```
Input: k = 3, n = 7
Output: [[1,2,4]]
```

**Example 2:**

```
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```


#### Solution

- 01backpackm, use Combination Sum II code and add check len(res)==k 

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        candidates = list(range(1, 10))
        dp: List[List[List]] = [[[]]] + [[] for i in range(target)]
        for num in candidates:
            for s in range(target, num - 1, -1):
                # 不需要 and dp[s - num], 因为dp[0] 是[[]] ，可以推倒，做 [] + [num]，而 dp[1] to dp[target] 初始化都是[]，不能推倒
                if (s - num) >= 0:  # 如果加上 and dp[s - num]，会快一点，减少一些无效推倒， if [] 为False, if [[]] 为True
                    li = [l + [num] for l in dp[s - num]]
                    dp[s] += li
        # 结果去重
        res = [list(t) for t in set(tuple(li) for li in dp[target])]  # 这一行很精妙
        res = [r for r in res if len(r) == k]
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().combinationSum3(3, 7) == [[1, 2, 4]]
    assert Solution().combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
​
```

- One Line code from discuss use combinations, beautiful
- https://leetcode.com/problems/combination-sum-iii/discuss/60624/Clean-167-liners-(AC)
```python3
from itertools import combinations

class Solution:
    def combinationSum3(self, k, n):
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
```