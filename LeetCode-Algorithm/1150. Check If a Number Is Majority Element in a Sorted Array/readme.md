### [1150\. Check If a Number Is Majority Element in a Sorted Array](https://leetcode.com/contest/biweekly-contest-6/problems/check-if-a-number-is-majority-element-in-a-sorted-array/)
- https://leetcode.com/contest/biweekly-contest-6/ranking/
- https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
- https://leetcode.com/contest/biweekly-contest-6/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

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
- 题意：求target数在数组里出现次数是否超过总数的一半
- 题目比较水，一行写也有很多方法，最短的是用Counter
- [最快]的的方法是直接count target，和总个数比较
- [最好]有个log N的方法值得一看

Language: **Python3**

```python3
from collections import Counter
from typing import List
​
​
class Solution:
    def isMajorityElement2(self, nums: List[int], target: int) -> bool:
        cnt = sum(1 for i in nums if target == i)
        return cnt > len(nums) / 2
​
    def isMajorityElement3(self, nums: List[int], target: int) -> bool:
        return sum(target == i for i in nums) > len(nums) / 2
        # return sum(1 for i in nums if target == i) > len(nums) / 2
​
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return Counter(nums)[target] > len(nums) / 2
​
​
if __name__ == '__main__':
    assert Solution().isMajorityElement(nums=[2, 4, 5, 5, 5, 5, 5, 6, 6], target=5)
    assert not Solution().isMajorityElement([10, 100, 101, 101], target=101)
​
```