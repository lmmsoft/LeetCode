### [1155\. Number of Dice Rolls With Target Sum](https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/)
- https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
- https://leetcode.com/contest/weekly-contest-149/problems/number-of-dice-rolls-with-target-sum/

Difficulty: **Medium**


You have `d` dice, and each die has `f` faces numbered `1, 2, ..., f`.

Return the number of possible ways (out of `f<sup>d</sup>` total ways) **modulo `10^9 + 7`** to roll the dice so the sum of the face up numbers equals `target`.

**Example 1:**

```
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
```

**Example 2:**

```
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

**Example 3:**

```
Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
```

**Example 4:**

```
Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
```

**Example 5:**

```
Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
```

**Constraints:**

*   `1 <= d, f <= 30`
*   `1 <= target <= 1000`


#### Solution
- 不是很难的一道递推dp题，我却想来很久，最后二维数组初始化还耽误了不少时间，不应该啊
- 思路是从第一个，到第n个骰子，递推
- 递推公式是 dp[Dice][Sum + Face] += dp[Dice-1][Sum]
- Dice的骰子的个数，外层循环
- Sum是当前骰子总和，由前一层的总和加当前层的骰子数目
- Face是1-f，所有可能的情况
- 初始化 dp[0][0]=1，然后三层循环即可

Language: **Python3**

```python3
from collections import defaultdict
​
​
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > f * d:
            return 0
​
        dp = [{0: 1}]
        # dp[0][0] = 1
        for n in range(1, d + 1):
            li = list(dp[n - 1].keys())
            dp.append(defaultdict(int))
            for s in li:
                for ff in range(1, f + 1):
                    dp[n][s + ff] += dp[n - 1][s]
​
        return dp[d][target]%1000000007
​
​
if __name__ == '__main__':
    assert Solution().numRollsToTarget(d=1, f=6, target=3) == 1
    assert Solution().numRollsToTarget(d=2, f=6, target=7) == 6
    assert Solution().numRollsToTarget(d=2, f=5, target=10) == 1
    assert Solution().numRollsToTarget(d=1, f=2, target=3) == 0
    assert Solution().numRollsToTarget(d=30, f=30, target=500) == 222616187
​
```