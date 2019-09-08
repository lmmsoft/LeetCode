from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        l = len(arr)
        d = [-100005] * len(arr)
        dp = [d.copy(), d.copy()]
        mx = -1000005
        for i in range(len(arr)):
            if i == 0:
                # dp[1][i]=arr[i]
                dp[0][i] = arr[i]
                mx = arr[i]
            else:
                # del
                dp[1][i] = max(
                    #dp[1][i],
                    dp[0][i - 1],
                    dp[1][i - 1] + arr[i]
                )

                # dp[1][i] = max(dp[1][i], )

                dp[0][i] = (dp[0][i - 1] + arr[i]) if dp[0][i - 1] > 0 else arr[i]

                mx = max(mx, dp[0][i],dp[1][i])

        print(dp)
        return mx


if __name__ == '__main__':
    assert Solution().maximumSum([3, -1, -1, -1]) == 3
    assert Solution().maximumSum([-2, -1, -2, -2, -2]) == -1

    assert Solution().maximumSum([1, -2, 0, 3]) == 4
    assert Solution().maximumSum(arr=[1, -2, -2, 3]) == 3
    assert Solution().maximumSum([-1, -1, -1, -1]) == -1

