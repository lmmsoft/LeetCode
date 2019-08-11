from collections import defaultdict


class Solution:
    def numRollsToTarget1(self, d: int, f: int, target: int) -> int:
        if target < d or target > f * d:
            return 0

        dp = [{0: 1}]
        # dp[0][0] = 1
        for n in range(1, d + 1):
            li = list(dp[n - 1].keys())
            dp.append(defaultdict(int))
            for s in li:
                for ff in range(1, f + 1):
                    dp[n][s + ff] += dp[n - 1][s]

        return dp[d][target] % 1000000007

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        # dp = [[0] * (target + f + 1)] * (d + 1)  # 这样初始化不行，dp里每个数组都是同样的引用，即总是 dp[0] == dp[1] ==dp[2]
        dp = [[0] * (target + f + 1) for _ in range(d + 1)]
        dp[0][0] = 1
        for n in range(1, d + 1):
            for s in range(0, target + 1):
                for ff in range(1, f + 1):
                    dp[n][s + ff] += dp[n - 1][s]

        return dp[d][target] % 1000000007


if __name__ == '__main__':
    assert Solution().numRollsToTarget(d=1, f=6, target=3) == 1
    assert Solution().numRollsToTarget(d=2, f=6, target=7) == 6
    assert Solution().numRollsToTarget(d=2, f=5, target=10) == 1
    assert Solution().numRollsToTarget(d=1, f=2, target=3) == 0
    assert Solution().numRollsToTarget(d=30, f=30, target=500) == 222616187
