### [1186\. Maximum Subarray Sum with One Deletion](https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/)

Difficulty: **Medium**


Given an array of integers, return the maximum sum for a **non-empty** subarray (contiguous elements) with at most one element deletion. In other words, you want to choose a subarray and optionally delete one element from it so that there is still at least one element left and the sum of the remaining elements is maximum possible.

Note that the subarray needs to be **non-empty** after deleting one element.

**Example 1:**

```
Input: arr = [1,-2,0,3]
Output: 4
Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the subarray [1, 0, 3] becomes the maximum value.```

**Example 2:**

```
Input: arr = [1,-2,-2,3]
Output: 3
Explanation: We just choose [3] and it's the maximum sum.
```

**Example 3:**

```
Input: arr = [-1,-1,-1,-1]
Output: -1
Explanation: The final subarray needs to be non-empty. You can't choose [-1] and delete -1 from it, then get an empty subarray to make the sum equals to 0.
```

**Constraints:**

*   `1 <= arr.length <= 10^5`
*   `-10^4 <= arr[i] <= 10^4`


#### Solution

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        l = len(arr)
        d = [-100005] * len(arr)
        dp = [d.copy(), d.copy()]
        mx = -1000005
        for i in range(len(arr)):
            if i == 0:
                # dp[1][i]=arr[i]
                dp[0][i] = arr[i]
                mx = arr[i]
            else:
                # del
                dp[1][i] = max(
                    #dp[1][i],
                    dp[0][i - 1],
                    dp[1][i - 1] + arr[i]
                )
​
                # dp[1][i] = max(dp[1][i], )
​
                dp[0][i] = (dp[0][i - 1] + arr[i]) if dp[0][i - 1] > 0 else arr[i]
​
                mx = max(mx, dp[0][i],dp[1][i])
​
        print(dp)
        return mx
```