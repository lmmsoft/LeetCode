### [416\. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)

Difficulty: **Medium**


Given a **non-empty** array containing **only positive integers**, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

**Note:**

1.  Each of the array element will not exceed 100.
2.  The array size will not exceed 200.

**Example 1:**

```
Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
```

**Example 2:**

```
Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
```


#### Solution

- 01背包入门题
- 针对题目的特殊性，几个可以考虑的优化
    - 总和是奇数->不可能
    - 阶段和到sum/2 已经满足
    - 阶段和超过sum/2的也可以排除了

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
​
        s1 = set([0])
​
        for n in nums:
            s2 = set()
            for item in s1:
                s2.add(item + n)
            s1 = s1.union(s2)
        if (s / 2) in s1:
            return True
        return False
​
​
if __name__ == '__main__':
    assert Solution().canPartition([1, 5, 11, 5])
    assert not Solution().canPartition([1, 2, 3, 5])
​
```