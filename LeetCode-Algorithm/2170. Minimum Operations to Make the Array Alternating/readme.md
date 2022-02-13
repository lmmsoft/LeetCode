### [2170\. Minimum Operations to Make the Array Alternating](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/)

Difficulty: **Medium**


You are given a **0-indexed** array `nums` consisting of `n` positive integers.

The array `nums` is called **alternating** if:

*   `nums[i - 2] == nums[i]`, where `2 <= i <= n - 1`.
*   `nums[i - 1] != nums[i]`, where `1 <= i <= n - 1`.

In one **operation**, you can choose an index `i` and **change** `nums[i]` into **any** positive integer.

Return _the **minimum number of operations** required to make the array alternating_.

**Example 1:**

```
Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
```

**Example 2:**

```
Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.
```

**Constraints:**

*   `1 <= nums.length <= 10<sup>5</sup>`
*   `1 <= nums[i] <= 10<sup>5</sup>`


#### Solution
- 题意：把数组换成奇偶位上数字都相同的数组，要求奇偶位本身不同，求最小次数
- 解法：
    - 如果奇偶位本身不同，就各自换成各自子数组里出现次数最多的数
    - 如果奇偶位本身相同，有一个要换成子数组里出现次数第二多的数
        - 注意，如果有可能子数组数字都一样，那么第二多的次数就是0

Language: **Python3**

```python3
from collections import Counter
from typing import List
​
​
class Solution:
    def get_first_second_number_count(self, ji2):
        if len(ji2) >= 2:
            return ji2[0][1], ji2[1][1]
        # 注意，如果有可能子数组数字都一样，那么第二多的次数就是0
        return ji2[0][1], 0
​
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        # 奇偶数列
        ji_list = [n for i, n in enumerate(nums) if i % 2 == 1]
        ou_list = [n for i, n in enumerate(nums) if i % 2 == 0]
        # 使用 Counter 统计次数
        ji = Counter(ji_list)
        ou = Counter(ou_list)
​
        # 奇偶 数字,次数 元组的数列
        ji_number_count_list = [(k, v) for k, v in ji.items()]
        ou_ji_number_count_list = [(k, v) for k, v in ou.items()]
        # 排序
        ji_number_count_list = sorted(ji_number_count_list, key=lambda x: x[1], reverse=True)
        ou_number_count_list = sorted(ou_ji_number_count_list, key=lambda x: x[1], reverse=True)
​
        if ji_number_count_list[0][0] != ou_number_count_list[0][0]:
            # 如果奇偶次数最多的数字不同，就用他们俩，其他的换成他们俩
            cnt_ji = len(ji_list) - ji_number_count_list[0][1]
            cnt_ou = len(ou_list) - ou_number_count_list[0][1]
            return cnt_ji + cnt_ou
        else:
            # 如果奇偶次数最多的数字相同，就比较第二大次数的大小，换成第二大次数较多的那个
            ji_first_count, ji_second_count = self.get_first_second_number_count(ji_number_count_list)
            ou_first_count, ou_second_count = self.get_first_second_number_count(ou_number_count_list)
​
            cnt_operation_1 = len(ji_list) - ji_first_count + len(ou_list) - ou_second_count
            cnt_operation_2 = len(ji_list) - ji_second_count + len(ou_list) - ou_first_count
            return min(cnt_operation_1, cnt_operation_2)
​
​
assert Solution().minimumOperations([3]) == 0
assert Solution().minimumOperations([3, 1, 3, 2, 4, 3]) == 3
assert Solution().minimumOperations([1, 2, 2, 2, 2]) == 2
​
        ji = Counter(ji_list)
```