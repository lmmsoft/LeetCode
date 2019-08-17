### [1151\. Minimum Swaps to Group All 1's Together](https://leetcode.com/contest/biweekly-contest-6/problems/minimum-swaps-to-group-all-1s-together/)
- https://leetcode.com/contest/biweekly-contest-6/ranking/

Difficulty: **Medium**

Given a binary array `data`, return the minimum number of swaps required to group all `1`’s present in the array together in **any place** in the array.

**Example 1:**

```
Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
```

**Example 2:**

```
Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
```

**Example 3:**

```
Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
```

<span style="display: inline;">**Note****:**</span>

1.  `1 <= data.length <= 10^5`
2.  `0 <= data[i] <= 1`

#### Solution
- 题意，每次可以任意交换两个数，求把1都连续在一起，最少交换多少数
- 解法，找到1的个数，比如是x个，再求连续x个数里面最多有y个1，x-y就是最少交换的个数

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        cnt = sum(data)
        l = len(data)
        m = sum(data[0:cnt])
        maxx = m
        for i in range(cnt, l):
            m = m + data[i] - data[i - cnt]
            maxx = max(maxx, m)
        return cnt - maxx
​
​
if __name__ == '__main__':
    assert Solution().minSwaps([1, 0, 1, 0, 1]) == 1
    assert Solution().minSwaps([0, 0, 0, 1, 0]) == 0
    assert Solution().minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]) == 3
​
```