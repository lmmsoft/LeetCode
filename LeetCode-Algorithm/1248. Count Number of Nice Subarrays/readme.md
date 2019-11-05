### [1248\. Count Number of Nice Subarrays](https://leetcode.com/contest/weekly-contest-161/problems/count-number-of-nice-subarrays/)
- https://leetcode.com/contest/weekly-contest-161/problems/count-number-of-nice-subarrays/
- https://leetcode.com/problems/count-number-of-nice-subarrays

Difficulty: **Medium**

Given an array of integers `nums` and an integer `k`. Asubarray is called **nice** if there are `k` odd numbers on it.

Return the number of **nice** sub-arrays.

**Example 1:**

```
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
```

**Example 2:**

```
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
```

**Example 3:**

```
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
```

**Constraints:**

*   `1 <= nums.length <= 50000`
*   `1 <= nums[i] <= 10^5`
*   `1 <= k <= nums.length`

#### Solution
- 题意：求nice子数列的个数，nice定义是连续的子数列里有k个奇数
- 解法，思路不难，但难在实现，使用滑动窗口，指向包含k个奇数的最左最右的奇数，观察他们左右有几个偶数，然后个数加一相乘
- 我的写法预处理两次，统计个数，比较啰嗦
- 比较好的写法是直接统计奇数的下标，左右添加[-1]和[总个数]
    - 然后 奇数对应的下标减去前一个下标 恰好就是 [偶数个数+1]
    - 滑动统计一下就好

Language: **Python3**

```python3
from itertools import groupby
from typing import List
​
​
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = [i % 2 for i in nums]
        # print(l)
        g = [(char, len(list(g))) for char, g in groupby(l)]
        # print(g)
​
        g2 = []
​
        for isOdd, size in g:
            if isOdd:
                for _ in range(size):
                    g2.append((1, 1))
            else:
                g2.append((isOdd, size))
        # print(g2)
​
        oddPos = []
        for id, p in enumerate(g2):
            isOdd, size = p
            if isOdd:
                oddPos.append(id)
        # print(oddPos)
​
        def getNum(g2, l, r):
            base = 1
            if l - 1 >= 0:
                isOdd, size = g2[l - 1]
                if not isOdd:
                    base *= size + 1
            if r + 1 < len(g2):
                isOdd, size = g2[r + 1]
                if not isOdd:
                    base *= size + 1
            return base
​
        cnt = 0
        for i in range(0, len(oddPos) - k + 1):
            cnt += getNum(g2, oddPos[i], oddPos[i + k - 1])
        return cnt
```