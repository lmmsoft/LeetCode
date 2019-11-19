from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, n in enumerate(nums):
            if i < 2:
                dp[i] = n
                continue
            if i == 2:
                dp[i] = dp[i - 2] + n
                continue
            dp[i] = max(dp[i - 2], dp[i - 3]) + n
        l = len(nums)
        if l == 0:
            return 0
        if l > 1:
            return max(dp[l - 1], dp[l - 2])
        return dp[0]


if __name__ == '__main__':
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    assert Solution().rob([8, 1, 1, 8, 1]) == 16
    assert Solution().rob([9]) == 9
    assert Solution().rob([]) == 0
