from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        s = sum(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(amount + 1 - c):
                if dp[i]:
                    dp[i + c] += dp[i]
        return dp[amount]


if __name__ == '__main__':
    assert Solution().change(5, [1, 2, 5]) == 4
    assert Solution().change(3, [2]) == 0
    assert Solution().change(10, [10]) == 1
