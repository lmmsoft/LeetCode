# links
https://leetcode.com/problems/merge-sorted-array/
https://leetcode-cn.com/problems/merge-sorted-array/

# Description

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:
```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

# Solution
- Connect 2 list together then sort it
    - simple to write but n*logn
```python
nums1[0: m + n] = sorted(nums1[0:m] + nums2[0:n])
```

- O(n)
    - write number from back to front to protect nums1 
```python
index = m + n - 1
m -= 1
n -= 1
while index >= 0:
    if m < 0:
        nums1[index] = nums2[n]
        n -= 1
    elif n < 0:
        nums1[index] = nums1[m]
        m -= 1
    elif nums1[m] < nums2[n]:
        nums1[index] = nums2[n]
        n -= 1
    else:
        nums1[index] = nums1[m]
        m -= 1
    index -= 1
```