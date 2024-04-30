# [](https://leetcode.com/problems/find-the-integer-added-to-array-ii/description/)

## Description

Difficulty: **Medium**

3132. Find the Integer Added to Array II

ou are given two integer arrays nums1 and nums2.

From nums1 two elements have been removed, and all other elements have been increased (or decreased in the case of negative) by an integer, represented by the variable x.

As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.

Return the minimum possible integer x that achieves this equivalence.

 

Example 1:

Input: nums1 = [4,20,16,12,8], nums2 = [14,18,10]

Output: -2

Explanation:

After removing elements at indices [0,4] and adding -2, nums1 becomes [18,14,10].

Example 2:

Input: nums1 = [3,5,5,3], nums2 = [7,7]

Output: 2

Explanation:

After removing elements at indices [0,3] and adding 2, nums1 becomes [7,7].

 

Constraints:

3 <= nums1.length <= 200
nums2.length == nums1.length - 2
0 <= nums1[i], nums2[i] <= 1000
The test cases are generated in a way that there is an integer x such that nums1 can become equal to nums2 by removing two elements and adding x to each element of nums1.

## Solution

- https://leetcode.com/problems/find-the-integer-added-to-array-ii/
- https://leetcode.com/contest/weekly-contest-395/problems/find-the-integer-added-to-array-ii/
- 类似于第一题，多两个数字，要去掉两个，找出差最少的
- 我的解法是暴力，枚举两个数字的位置ij，然后判断是否相等，有点剪枝，O(n^3)
  - 和我写法一样的解法（可读性更好） https://leetcode.com/problems/find-the-integer-added-to-array-ii/solutions/5082013/easy-solution-bruteforce-28-04-2024-contest/
- 好的算法：
- O(NlogN):
  - https://leetcode.com/problems/find-the-integer-added-to-array-ii/solutions/5082086/3-pass/ 
  - 先排序，因为一定有正确解，所以最后的结果一定是 n2[0] - n1[2] or n2[1] - n1[1] or n2[2] - n1[0] 三个中的一个(第一个最小，所以先尝试)
  - 那就用这三个值分别去尝试匹配， 即  n1[x] + diff = n2[y], 不匹配就让 skip 次数加一，
  - 满足 skip的次数小于3就返回，如果前两个都不满足，直接返回第三个 n2[2] - n1[0]
- 英文解释 O(NlogN):
  - There are only 3 possibilities: min(nums2) - x for the 3 smallest elements x of nums1. 
  - Sort nums1 and nums2. For a difference d, use two pointers to match elements t of nums1 to t+d of nums2. 
  - If you have to skip more than 2 elements of nums1, the difference is invalid.


Language: Python

```python
import math
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        current_min = math.inf
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for i in range(0, len(nums1)):
            for j in range(i+1, len(nums1)):
                # remove i, j
                nn = [nums1[k]   for k in range(len(nums1)) if k!=i and k!=j ]
                
                ok, new_min = self.check_equals(nn, nums2, current_min)
                if ok:
                    current_min = new_min
        return current_min
                
                
    def check_equals(self, n1, n2, current_min):
        new_min = n2[0] - n1[0]
        if new_min > current_min:
            return False, None
        for p in range(1, len(n1)):
            if n2[p] - n1[p] != new_min:
                return False, None
[4,20,16,12,8]
```


有趣代码学习
```python
from collections import Counter

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        
        # 统计每个数的个数
        ctr1, ctr2 = Counter(nums1), Counter(nums2)
        
        # 从小到大，枚举 差值
        for x in range(-1005, 1005):
            is_valid = True
            for y in nums2:
                # ctr[y - x] 个数一定是  >= ctr2[y] 的, 只有两个大，其他都一样
                if ctr1[y - x] < ctr2[y]:
                    is_valid = False
                    break
                    
            if is_valid:
                return x
```


```python
# 同样的暴力，判断写得太好了，简洁！
class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        ans = math.inf
        n = len(nums1)
        for i in range(n):
            for j in range(i + 1, n):
                l = nums1[:i] + nums1[i + 1:j] + nums1[j + 1:]
                
                # 到上面都和我一样
                # 下面的判断写得太好了
                # 用了 all 和 zip，简洁明了
                
                diff = nums2[0] - l[0]
                if all(x - y == diff for x, y in zip(nums2, l)):
                    # print(diff, nums2, l)
                    ans = min(ans, diff)
        return ans
```