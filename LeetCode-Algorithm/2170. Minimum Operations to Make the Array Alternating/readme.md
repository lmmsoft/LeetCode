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

Language: **Python3**

```python3
class Solution:
    def get_first_second_number_and_count(self, ji2):
        if len(ji2) >= 2:
            return ji2[0][0], ji2[0][1], ji2[1][0], ji2[1][1]
        return ji2[0][0], ji2[0][1], 0, 0
​
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ji_list = [n for i, n in enumerate(nums) if i % 2 == 1]
        ou_list = [n for i, n in enumerate(nums) if i % 2 == 0]
        ji = Counter(ji_list)
        ou = Counter(ou_list)
        ji1 = [(k, v) for k, v in ji.items()]
        ou1 = [(k, v) for k, v in ou.items()]
        ji2 = sorted(ji1, key=lambda x: x[1], reverse=True)
        ou2 = sorted(ou1, key=lambda x: x[1], reverse=True)
​
        if ji2[0][0] != ou2[0][0]:
            cnt1 = len(ji_list) - ji2[0][1]
            cnt2 = len(ou_list) - ou2[0][1]
            return cnt1 + cnt2
        else:
            ji00, ji01, ji10, ji11 = self.get_first_second_number_and_count(ji2)
            ou00, ou01, ou10, ou11 = self.get_first_second_number_and_count(ou2)
​
            cnt1 = len(ji_list) - ji01 + len(ou_list) - ou11
            cnt2 = len(ji_list) - ji11 + len(ou_list) - ou01
            return min(cnt1, cnt2)
```