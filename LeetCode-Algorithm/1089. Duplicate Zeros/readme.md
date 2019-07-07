### [1089\. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)

Difficulty: **Easy**


Given a fixed length array `arr` of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array **in place**, do not return anything from your function.

**Example 1:**

```
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
```

**Example 2:**

```
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
```

**Note:**

1.  `1 <= arr.length <= 10000`
2.  `0 <= arr[i] <= 9`


#### Solution

- 水题，我用了O(N)时间和O(N)空间速拍了一个，其实不符合要求
- 如果要O(1)空间，可以用arr.count(0)先统计0的个数，然后从后往前扫描arr即可

Language: **Python3**


```python3
from typing import List
​
​
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2 = []
        for a in arr:
            if a == 0:
                arr2.append(0)
                arr2.append(0)
            else:
                arr2.append(a)
        for i in range(0, len(arr)):
            arr[i] = arr2[i]
  
```