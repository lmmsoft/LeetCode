### [1144\. Decrease Elements To Make Array Zigzag](https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/)
- https://leetcode.com/contest/weekly-contest-148/problems/decrease-elements-to-make-array-zigzag/
- https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/

Difficulty: **Medium**


Given an array `nums` of integers, a _move_ consists of choosing any element and **decreasing it by 1**.

An array `A` is a _zigzag array_ if either:

*   Every even-indexed element is greater than adjacent elements, ie. `A[0] > A[1] < A[2] > A[3] < A[4] > ...`
*   OR, every odd-indexed element is greater than adjacent elements, ie. `A[0] < A[1] > A[2] < A[3] > A[4] < ...`

Return the minimum number of moves to transform the given array `nums` into a zigzag array.

**Example 1:**

```
Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
```

**Example 2:**

```
Input: nums = [9,6,1,6,2]
Output: 4
```

**Constraints:**

*   `1 <= nums.length <= 1000`
*   `1 <= nums[i] <= 1000`


#### Solution

Language: **Python3**
- 比较好的方法：
    - 分成奇偶计算两个值，求最小值
    - 无论奇偶，都可以通过把需要"小于左右两边的数字"减少来满足条件，减到的数字就是左右两边的最小值减一
    - 递推计算一遍，把减小的值累加即可
- 我的方法：
    - 比较麻烦，每个与下一个比，不对减少小于号指向的
    - 会导致有的是减少左边的值，有点减少右边的值，减小右边的值的时候会影响下一个值的比较，所以需要复制数组
    - 这里我也WA了两次
    - 比较烂的方法，不推荐，实现起来也很麻烦

```python3
from typing import List
​
​
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
​
        def cal(nums, isGreater):
            s = 0
            for i in range(0, len(nums) - 1):
                a, b = nums[i], nums[i + 1]
                diff = 0
                if isGreater:
                    diff = 0 if a > b else (b - a + 1)
                    nums[i + 1] -= diff
                else:
                    diff = 0 if b > a else (a - b + 1)
​
                s += diff
                isGreater = not isGreater
            return s
​
        s1 = cal(nums[:], True)
        s2 = cal(nums[:], False)
        return min(s1, s2)
​
​
if __name__ == '__main__':
    assert Solution().movesToMakeZigzag([10, 4, 4, 10, 10, 6, 2, 3]) == 13
    assert Solution().movesToMakeZigzag([2, 7, 10, 9, 8, 9]) == 4
    assert Solution().movesToMakeZigzag([1, 2, 3]) == 2
    assert Solution().movesToMakeZigzag([9, 6, 1, 6, 2]) == 4
​
```