### [33\. Search in Rotated Sorted ArrayCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Difficulty: **Medium**


Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).

You are given a target value to search. If found in the array return its index, otherwise return `-1`.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of _O_(log _n_).

**Example 1:**

```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

**Example 2:**

```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```


#### Solution
- 二分没写出来，下次再来

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
​
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1
​
​
if __name__ == '__main__':
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
    assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
​
```