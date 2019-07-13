### [1121\. Divide Array Into Increasing Sequences](https://leetcode.com/problems/divide-array-into-increasing-sequences/)
- https://leetcode.com/problems/divide-array-into-increasing-sequences/
- https://leetcode.com/contest/biweekly-contest-4/problems/divide-array-into-increasing-sequences/

Difficulty: **Hard**


Given a **non-decreasing** array of positive integers `nums` and an integer `K`, find out if this array can be divided into one or more **disjoint increasing subsequences of length at least** `K`.

**Example 1:**

```
Input: nums = [1,2,2,3,3,4,4], K = 3
Output: true
Explanation: 
The array can be divided into the two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
```

**Example 2:**

```
Input: nums = [5,6,6,7,8], K = 3
Output: false
Explanation: 
There is no way to divide the array using the conditions required.
```

**Note:**

1.  `1 <= nums.length <= 10^5`
2.  `1 <= K <= nums.length`
3.  `1 <= nums[i] <= 10^5`


#### Solution
- 被表面的Hard欺骗，其实是道水题，代码没写周全错了一次 1WA 1A
- 数据按要求分组，比较好的思路是，如果有同样的数字，必须分到不同的组内，因为同组必须绝对递增，所以可以求的最少要多少组M（同样数字最大的个数）
- 然后每组最少K个，K*M就是最少的元素个数，判断nums是否满足即可
Language: **Python3**

```python3
class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        # 相同的值有N个，那么至少要分成n组，那么总数最少KN个才行
        pre = -1
        cnt_max = 0
        cnt_cur = 0
        for n in nums:
            if pre == -1:
                pre = n
                cnt_cur = 1
                continue
            if n == pre:
                cnt_cur += 1
            else:
                pre = n
                cnt_max = max(cnt_max, cnt_cur)
                cnt_cur = 1
        cnt_max = max(cnt_max, cnt_cur)
​
        if cnt_max * K > len(nums):
            return False
        return True
```

- 利用Python的counter可以实现一行的解法
```python3

    def canDivideIntoSubsequences2(self, nums, K: int) -> bool:
        return max(collections.Counter(nums).values()) * K <= len(nums)

    def canDivideIntoSubsequences3(self, nums: List[int], K: int) -> bool:
        return collections.Counter(nums).most_common(1)[0][1] <= (len(nums) // K)
```