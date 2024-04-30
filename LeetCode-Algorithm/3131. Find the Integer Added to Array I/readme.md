# [3131\. Find the Integer Added to Array I](https://leetcode.com/problems/find-the-integer-added-to-array-i/)

- https://leetcode.com/problems/find-the-integer-added-to-array-i/description/
- https://leetcode.com/contest/weekly-contest-395/problems/find-the-integer-added-to-array-i/

## Description

Difficulty: **Easy**

You are given two arrays of equal length, nums1 and nums2.

Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.

As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

Return the integer x.

 

Example 1:

Input: nums1 = [2,6,4], nums2 = [9,7,5]

Output: 3

Explanation:

The integer added to each element of nums1 is 3.

Example 2:

Input: nums1 = [10], nums2 = [5]

Output: -5

Explanation:

The integer added to each element of nums1 is -5.

Example 3:

Input: nums1 = [1,1,1,1], nums2 = [1,1,1,1]

Output: 0

Explanation:

The integer added to each element of nums1 is 0.

 

Constraints:

1 <= nums1.length == nums2.length <= 100
0 <= nums1[i], nums2[i] <= 1000
The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by adding x to each element of nums1.

## Solution

- 比较两个数组的距离，返回差值
- 我比较保守，先排序，再用首字母相减 O(nlogn)
- 高手直接 max(nums1) - max(nums2)，或者 min 也行，或者直接求和相减除以个数，都是 O(N)

```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        return n2[0] - n1[0]


class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        return -(sum(nums1) - sum(nums2)) // n
    
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        return max(nums2) - max(nums1)

```


Language: python

```python
class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = sorted(nums1)
        n2 = sorted(nums2)
        return n2[0] - n1[0]
[2,6,4]
```



