### [1186\. Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)

Difficulty: **Medium**


Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be **non-empty** after deleting one element.

**Example 1:**

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.
```

**Example 2:**

```
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
```

**Example 3:**

```
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
```

**Constraints:**

*   `1 <= arr.length <= 10^5`
*   `-10^4 <= arr[i] <= 10^4`


#### Solution
- 题意：可以删除一个数的最大子序列和
- 对于不可以删除的最大子序列，dp[i] = dp[i-1]>=0? dp[i-1]+arr[i] : arr[i] , MaxSum = max(dp[0...n])
- 对于可删除的最大子序列 用dp[0][i]记录没删过的值， dp[1][i]记录删过的值
- dp[0][i] 和上面的情况一样
- dp[1][i] 可以有两种情况
    - 之前删过，当前不删  dp[1][i-1] + arr[i]
    - 之前没删，当前删 dp[0][i]
    - 不存在从头开始的情况
    - 所以 dp[1][i] = max (dp[1][i-1] + arr[i], dp[0][i])
- 思路二
    - 对于朴素的Maximum Subarray eg: https://leetcode.com/problems/maximum-subarray/
    - max_sum[i:j] = sum[0:j] - min_sum(0:i)
    - 想要子序列和最大， 因为总和是固定的，所以找到最小的前缀和即可
    - 于是O(N)遍历数组，记录并更新Sum和min_sum即可
- 基于思路二推广
    - 这一题可以这么思考 删除arr[i]之后的最大值 = max(以i-1为终点的子序列) + max(以i+1为起点的子序列)
    - 然后分别求 以某个数为起点或终点的子序列，遍历即可 O(N) 顺序，逆序，再顺序，扫描三遍
    - 详见第二部分代码

Language: **Python3**

```python3
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

```