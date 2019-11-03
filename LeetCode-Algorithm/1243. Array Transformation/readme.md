### [1243\. Array Transformation](https://leetcode.com/contest/biweekly-contest-12/problems/array-transformation/)
- https://leetcode.com/contest/biweekly-contest-12/problems/array-transformation/
- https://leetcode.com/problems/array-transformation/
- https://leetcode.com/problems/array-transformation/discuss/

Difficulty: **Easy**

Given an initial array `arr`, every day you produce a new array using the array of the previous day.

On the `i`-th day, you do the following operations on the array of day `i-1` to produce the array of day `i`:

1.  If an element is smaller than both its left neighbor and its right neighbor, then this element is incremented.
2.  If an element is bigger than both its left neighbor and its right neighbor, then this element is decremented.
3.  The first and last elements never change.

After some days, the array does not change. Return that final array.

**Example 1:**

```
Input: arr = [6,2,3,4]
Output: [6,3,3,4]
Explanation: 
On the first day, the array is changed from [6,2,3,4] to [6,3,3,4].
No more operations can be done to this array.
```

**Example 2:**

```
Input: arr = [1,6,3,4,3,5]
Output: [1,4,4,4,4,5]
Explanation: 
On the first day, the array is changed from [1,6,3,4,3,5] to [1,5,4,3,4,5].
On the second day, the array is changed from [1,5,4,3,4,5] to [1,4,4,4,4,5].
No more operations can be done to this array.
```

**Constraints:**

*   `1 <= arr.length <= 100`
*   `1 <= arr[i] <= 100`

#### Solution
- 题意：一个数组，每次操作： 比两边都大的数减一，比两边都小的数加一，求最后的数组
- 模拟即可，水题

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        while True:
            arr2 = [a for a in arr]
            changed = 0
            for id in range(1, len(arr) - 1):
                l = arr[id - 1]
                r = arr[id + 1]
                m = arr[id]
                if l > m and r > m:
                    m += 1
                    changed += 1
                elif l < m and r < m:
                    m -= 1
                    changed += 1
                arr2[id] = m
            arr = arr2
            if changed == 0:
                break
        return arr
    
    def transformArray(self, A):
        for _ in range(100):
            A = A[:1] + [b + (a > b < c) - (a < b > c) for a, b, c in zip(A, A[1:], A[2:])] + A[-1:]
        return A
 
 
```