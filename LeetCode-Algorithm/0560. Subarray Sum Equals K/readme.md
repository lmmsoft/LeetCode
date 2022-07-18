# [560\. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/submissions/)

## Description

Difficulty: **Medium**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Hash Table](https://leetcode.com/tag/hash-table/), [Prefix Sum](https://leetcode.com/tag/prefix-sum/)


Given an array of integers `nums` and an integer `k`, return _the total number of subarrays whose sum equals to_ `k`.

A subarray is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

```
Input: nums = [1,1,1], k = 2
Output: 2
```

**Example 2:**

```
Input: nums = [1,2,3], k = 3
Output: 2
```

**Constraints:**

*   1 <= nums.length <= 2 * 10<sup>4</sup>
*   `-1000 <= nums[i] <= 1000`
*   -10<sup>7</sup> <= k <= 10<sup>7</sup>


## Solution

解法：

1. 最暴力的解法是枚举 start 和 end 两个点，然后中间的和，时间复杂度 O(N^3)， start/end循环N^2, 求和再N
2. 上述可以在求和部分优化，sum(start, end) = sum(0, end) - sum(0, start)， 即求出前缀和，然后详见可得区间和， 时间复杂度降到 O(N + N^2) = O(N)
3. 再一个优化，以上是求出 sum(start, end) 并和target对比，即 sum(0, end) - sum(0, start) == target 其实可以换个思路：
   1. 求 sum(0, start) - target ==sum(0, start), 即 当前前缀和-target 是否在之前的前缀和 里出现过，如果之前出现过x次，那么那x个到当前位置的和都是 target
   2. 这样复杂度就降到 O(N) 了，求前缀和是O(N) ，查询部分是用hash，可以做到 O(1)

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefsum = 0
        d = {0: 1}
​
        for num in nums:
            prefsum += num
​
            if prefsum - k in d:
                cnt += d[prefsum - k]
​
            d[prefsum] = d.get(prefsum, 0) + 1
        return cnt
​
​
if __name__ == '__main__':
    assert 2 == Solution().subarraySum(nums=[1, 1, 1], k=2)
    assert 2 == Solution().subarraySum(nums=[1, 2, 3], k=3)
    assert 3 == Solution().subarraySum(nums=[1, 1, 1, 1], k = 2)
​
```