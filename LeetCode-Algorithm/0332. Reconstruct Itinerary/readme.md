### [322\. Coin Change](https://leetcode.com/problems/coin-change/)

Difficulty: **Medium**


You are given coins of different denominations and a total amount of money _amount_. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

**Example 1:**

```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```

**Example 2:**

```
Input: coins = [2], amount = 3
Output: -1
```

**Note**:  
You may assume that you have an infinite number of each kind of coin.


#### Solution
- 完全背包问题
    - 因为要恰好达到amount，所以从小到大递推
    - 因为求最小个数，且要恰好amont个，所以初始化为+inf，dp[0]=0
Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = 99999999999
        dp: List = [inf] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for a in range(c, amount + 1):
                dp[a] = min(dp[a], dp[a - c] + 1)
        if dp[amount] < inf:
            return dp[amount]
        return -1
​
​
if __name__ == '__main__':
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3)
```