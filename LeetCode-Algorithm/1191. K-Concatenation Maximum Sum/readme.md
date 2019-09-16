### [1191\. K-Concatenation Maximum Sum](https://leetcode.com/contest/weekly-contest-154/problems/k-concatenation-maximum-sum/)
- https://leetcode.com/contest/weekly-contest-154/problems/k-concatenation-maximum-sum/

Difficulty: **Medium**

Given an integer array `arr` and an integer `k`, modify the array by repeating it `k` times.

For example, if `arr = [1, 2]` and `k = 3` then the modified array will be `[1, 2, 1, 2, 1, 2]`.

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be `0` and its sum in that case is `0`.

As the answer can be very large, return the answer **modulo** `10^9 + 7`.

**Example 1:**

```
Input: arr = [1,2], k = 3
Output: 9
```

**Example 2:**

```
Input: arr = [1,-2,1], k = 5
Output: 2
```

**Example 3:**

```
Input: arr = [-1,-2], k = 7
Output: 0
```

**Constraints:**

*   `1 <= arr.length <= 10^5`
*   `1 <= k <= 10^5`
*   `-10^4 <= arr[i] <= 10^4`

#### Solution
- 郁闷的题，赛后一分钟才AC
- 题意： K个连续数组的最大子段和
- 求一个数组的最大子段和，可以用Kadane算法DP
- 如果是K个呢？讨论一下不同情况
    - K=1，和一个一样
    - K=2, 把两个数组合成一个新数组计算即可
    - K=3, 有两种情况
        - sum(arr)<=0, 中间的和比较小，计算两个数组的和即可
        - sum(arr)>0, 有可能是两个数组的和，也可能是第一个数组的后缀和+再加上中间的和+最后一个数组和前缀和
    - 于是乎，转换成前缀和，后缀和，字段和 三个子问题即可
- 我的思路：
    - 我比赛时候k=3的思路略有不同, 没想到前后缀和的办法:
    - sum<=0 就两个数组的最大值
    - sum>0, 考虑所有求出最大和的情况，如果跨了前后两个数组，那就可以把中间所有重复数组的和加上去， 于是乎我又统计了组成最大值的下标，代码比较烦

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def max_sub(arr: List[int]):
            pos = []
            p_min = -1
            s = 0
            s_min = 0
            s_max = -float("inf")
            for p, a in enumerate(arr):
                s += a
                if s - s_min > s_max:
                    pos = [(p_min, p)]
                    s_max = s - s_min
                elif s - s_min == s_max:
                    pos.append((p_min, p))
​
                if s < s_min:
                    s_min = s
                    p_min = p
​
            if s - s_min > s_max:
                pos = [(p_min, len(arr) - 1)]
                s_max = s - s_min
            elif s - s_min == s_max:
                pos.append((p_min, len(arr) - 1))
​
            return s_max, pos
​
        if k == 1:
            s, pos = max_sub(arr)
        elif k == 2:
            s, pos = max_sub(arr * 2)
        else:
            s, pos = max_sub(arr * 2)
            s1 = sum(arr)
            if s1 <= 0:
                pass
            else:
                found = False
                l = len(arr)
                for a, b in pos:
                    if a < l and b >= l:
                        found = True
                if found:
                    s = s + (k - 2) * s1
                else:
                    pass
​
        return s % (10 ** 9 + 7)
​
​
if __name__ == '__main__':
    assert Solution().kConcatenationMaxSum([1, -2, 1], 1) == 1
    assert Solution().kConcatenationMaxSum([1, -2, 1], 2) == 2
    assert Solution().kConcatenationMaxSum([1, -2, 1], 3) == 2
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 1) == 100
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 2) == 102
    assert Solution().kConcatenationMaxSum([50, -99, 100, -99, 50], 3) == 104
    assert Solution().kConcatenationMaxSum([1, 2], 3) == 9
​
```