### [1283\. Find the Smallest Divisor Given a Threshold](https://leetcode.com/contest/weekly-contest-166/problems/find-the-smallest-divisor-given-a-threshold/)

Difficulty: **Medium**

Given an array of integers `nums` and an integer `threshold`, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the **smallest** divisor such that the result mentioned above is less than or equal to `threshold`.

Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

It is guaranteed that there will be an answer.

**Example 1:**

```
Input: nums = [1,2,5,9], threshold = 6
Output: 5
Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1\.
If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
```

**Example 2:**

```
Input: nums = [2,3,5,7,11], threshold = 11
Output: 3
```

**Example 3:**

```
Input: nums = [19], threshold = 5
Output: 4
```

**Constraints:**

*   `1 <= nums.length <= 5 * 10^4`
*   `1 <= nums[i] <= 10^6`
*   `nums.length <= threshold <= 10^6`

#### Solution
- 二分题，注意考虑出口情况

Language: **Python3**

```python3
from math import ceil
from typing import List
​
​
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        s = sum(nums)
        mi = s // threshold
        if mi == 0:
            mi = 1
​
        def lessOrEaualToThreshold(dividor):
            if dividor==0:
                return False
            th = sum(ceil((n / dividor)) for n in nums)
            return th <= threshold
​
        # 求 smallest dividor满足 和 小于等于 threshold
        # divider太小， 和大于thres
        # divider太大，不满足最小
        # divider 满足
        # divider+1 不满足, 和> thre
        l = mi
        r = 1000001
        while l < r:
            mid = (l + r) // 2
            m1 = lessOrEaualToThreshold(mid - 1) # should be false
            m2 = lessOrEaualToThreshold(mid) # should be true
            if not m1 and m2:
                return mid
            if m1:
                r = mid
            elif not m2:
                l = mid
```