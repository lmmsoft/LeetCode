### [518\. Coin Change 2Copy for Markdown](https://leetcode.com/problems/coin-change-2/)

Difficulty: **Medium**


You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

**Example 1:**

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2:**

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3:**

```
Input: amount = 10, coins = [10] 
Output: 1
```

**Note:**

You can assume that

*   0 <= amount <= 5000
*   1 <= coin <= 5000
*   the number of coins is less than 500
*   the answer is guaranteed to fit into signed 32-bit integer


#### Solution
- 完全背包方法数，降空间到一维需要从小到大扫描
Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        s = sum(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
​
        for c in coins:
            for i in range(amount + 1-c):                
                dp[i + c] += dp[i]
        return dp[amount]
​
​
if __name__ == '__main__':
    assert Solution().change(5, [1, 2, 5]) == 4
    assert Solution().change(3, [2]) == 0
    assert Solution().change(10, [10]) == 1
​
```