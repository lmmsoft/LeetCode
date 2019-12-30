### [1299\. Replace Elements with Greatest Element on Right Side](https://leetcode.com/contest/biweekly-contest-16/problems/replace-elements-with-greatest-element-on-right-side/)

Difficulty: **Easy**

Given an array `arr`, replace every element in that array with the greatest element among the elements to its right, and replace the last element with `-1`.

After doing so, return the array.

**Example 1:**

```
Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
```

**Constraints:**

*   `1 <= arr.length <= 10^4`
*   `1 <= arr[i] <= 10^5`

#### Solution
- - 简单题，但快速写对不容易，我一开始写得不对，最后AC的代码和第一名基本结构差不多，但思路没别人清晰
Language: **Python3**

```python3
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        mx = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            t = arr[i]
            arr[i] = mx
            if t > mx:
                mx = t
        arr[0] = mx
        arr[-1] = -1
        #print(arr)
        return arr
```