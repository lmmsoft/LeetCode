# [136\. Single Number](https://leetcode.com/problems/single-number/submissions/)

## Description

Difficulty: **Easy**  

Related Topics: [Array](https://leetcode.com/tag/array/), [Bit Manipulation](https://leetcode.com/tag/bit-manipulation/)


Given a **non-empty** array of integers `nums`, every element appears _twice_ except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

**Example 1:**

```
Input: nums = [2,2,1]
Output: 1
```

**Example 2:**

```
Input: nums = [4,1,2,1,2]
Output: 4
```

**Example 3:**

```
Input: nums = [1]
Output: 1
```

**Constraints:**

*   1 <= nums.length <= 3 * 10<sup>4</sup>
*   -3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup>
*   Each element in the array appears twice except for one element which appears only once.


## Solution

题目不是不难，用异或即可，可以学习各种python 一行的写法，很有意思

Language: **Python3**

```python3
import collections
from functools import reduce
from operator import xor
​
from typing import List
​
​
class Solution:
    def singleNumber1(self, nums: List[int]) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a
​
    def singleNumber2(self, nums: List[int]) -> int:
        return reduce(lambda total, el: total ^ el, nums)
​
    def singleNumber3(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
​
    def singleNumber4(self, nums: List[int]) -> int:
        # This can be simpler: reduce(xor, nums) (LeetCode imports operator.xor as xor).
        return reduce(xor, nums)
​
    def singleNumber5(self, nums: List[int]) -> int:
        # Nice! Here's another one-liner for Python 3, using the walrus operator :=:
        # 解释
        # [x := x ^ v for v in nums] 枚举nums，每个数字和x做xor, 结果放到了[]里，[]的最后一个就是所有数字异或的值
        # (x:=0, ) 上面的x没有初始化，所以用 x:=0 先初始化一下
        # 最后的返回是个元组，结果在元组[1]的最后一个，所以[-1][-1] 或者 [1][-1] 也行
        return (x := 0, [x := x ^ v for v in nums])[-1][-1]
​
    def singleNumber6(self, nums: List[int]) -> int:
        # 这个不是最优的方法，找到最少的值，输出值(而不是个数)
        return collections.Counter(nums).most_common()[-1][0]
​
​
if __name__ == '__main__':
    assert 1 == Solution().singleNumber([2,2,1])
```