### 1150\. Check If a Number Is Majority Element in a Sorted Array My Submissions Back to Contest

Difficulty: **Easy**

Given an array `nums` sorted in **non-decreasing** order, and a number `target`, return `True` if and only if `target` is a majority element.

A _majority element_ is an element that appears **more than `N/2`** times in an array of length `N`.

**Example 1:**

```
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.
```

**Example 2:**

```
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: 
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.
```

<span style="display: inline;">**Note:**</span>

1.  `1 <= nums.length <= 1000`
2.  `1 <= nums[i] <= 10^9`
3.  `1 <= target <= 10^9`

#### Solution

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        cnt = sum(1 for i in nums if target == i)
        return cnt > len(nums) / 2
​
​
if __name__ == '__main__':
    assert Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5)
    assert not Solution().isMajorityElement([10, 100, 101, 101], target=101)
​
```