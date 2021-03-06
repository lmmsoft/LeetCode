from typing import List


class Solution:
    # dp思路，如果想去掉i==0分支的话，初始化 mx=dp[0][0]=arr[0, 然后从i=1开始遍历
    def maximumSum1(self, arr: List[int]) -> int:
        d = [-100005] * len(arr)
        dp = [d.copy(), d.copy()]
        mx = -1000005
        for i in range(len(arr)):
            if i == 0:
                dp[0][i] = arr[i]
                mx = arr[i]
            else:
                # del
                dp[1][i] = max(
                    dp[0][i - 1],  # del current arr
                    dp[1][i - 1] + arr[i]  # already deleted
                )

                # no del
                dp[0][i] = (dp[0][i - 1] + arr[i]) if dp[0][i - 1] > 0 else arr[i]

                mx = max(mx, dp[0][i], dp[1][i])

        return mx

    def maximumSum(self, arr: List[int]) -> int:
        l = len(arr)
        max_end_here = [None] * l
        max_start_here = [None] * l

        max_res = max_end_here[0] = arr[0]
        for i in range(1, l):
            max_end_here[i] = max(arr[i], max_end_here[i - 1] + arr[i])
            max_res = max(max_res, max_end_here[i])  # 这里包含了不删除数字的情况，最大连续子序列和

        max_start_here[l - 1] = arr[l - 1]
        for i in range(l - 2, -1, -1):
            max_start_here[i] = max(arr[i], max_start_here[i + 1] + arr[i])
            # max_res = max(max_res, max_start_here[i])  # 这一行不需要，不删除数字的情况上面已考虑

        # 下面这段注释里的代码是错的，a b c 都可能为0，导致不能正确处理负数的情况
        # max_end_here.append(0)
        # max_start_here.append(0)
        # for i in range(0, l):
        #     a = max(0, max_end_here[i - 1])
        #     b = max(0, arr[i])
        #     c = max(0, max_start_here[i + 1])
        #     max_res = max(max_res, a + b + c)

        # 删除首尾的情况上面已包含(同不删除数字的情况)，这里只需要严格删除中间某个数的情况
        for i in range(1, l - 1):
            max_res = max(max_res, max_end_here[i - 1] + max_start_here[i + 1])
        print(max_res)
        return max_res


if __name__ == '__main__':
    assert Solution().maximumSum([-1, -1, 1, 1, - 1, -1]) == 2

    assert Solution().maximumSum([3, -1, -1, -1]) == 3
    assert Solution().maximumSum([-2, -1, -2, -2, -2]) == -1

    assert Solution().maximumSum([1, -2, 0, 3]) == 4
    assert Solution().maximumSum(arr=[1, -2, -2, 3]) == 3
    assert Solution().maximumSum([-1, -1, -1, -1]) == -1
