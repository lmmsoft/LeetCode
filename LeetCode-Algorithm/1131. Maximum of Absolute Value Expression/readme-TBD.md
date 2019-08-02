### [1131\. Maximum of Absolute Value Expression](https://leetcode.com/problems/maximum-of-absolute-value-expression/)

Difficulty: **Medium**


Given two arrays of integers with equal lengths, return the maximum value of:

`|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|`

where the maximum is taken over all `0 <= i, j < arr1.length`.

**Example 1:**

```
Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
```

**Example 2:**

```
Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
```

**Constraints:**

*   `2 <= arr1.length == arr2.length <= 40000`
*   `-10^6 <= arr1[i], arr2[i] <= 10^6`


#### Solution
- 解析和证明
- 把 `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|` 改写成 `|a1-a2| + |b1-b2| + |i-j|` 方便表达
- 按照索引顺序遍历数组，那么|i-j| 就是 j-1
- 

Language: **Python3**

```python3
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        
```