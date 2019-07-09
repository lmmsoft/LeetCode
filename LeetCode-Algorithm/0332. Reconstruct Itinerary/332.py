from typing import List


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


if __name__ == '__main__':
    assert Solution().coinChange([1, 2, 5], 11) == 3
    assert Solution().coinChange([2], 3)
