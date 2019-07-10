from typing import List


class Solution:
    # 这种按照题意，求排列数个数
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp: List = [1] + [0] * target

        for s in range(0, target + 1):  # 完全背包，从小到大
            for n in nums:  # 对于每个数
                if s - n >= 0:
                    dp[s] += dp[s - n]
        return dp[target]

    # 这种前两行交换，求组合数个数
    def combinationSum4_1(self, nums: List[int], target: int) -> int:
        dp: List = [1] + [0] * target

        for s in range(0, target + 1):  # 完全背包，从小到大
            for n in nums:  # 对于每个数
                if s - n >= 0:
                    dp[s] += dp[s - n]
        return dp[target]


if __name__ == '__main__':
    assert Solution().combinationSum4([1, 2, 3], 4) == 7
    assert Solution().combinationSum4([4, 2, 1], 32) == 39882198
