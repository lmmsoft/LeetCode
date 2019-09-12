### [1187\. Make Array Strictly Increasing](https://leetcode.com/problems/make-array-strictly-increasing/)
- https://leetcode.com/contest/weekly-contest-153/problems/make-array-strictly-increasing/
- https://leetcode.com/problems/make-array-strictly-increasing/

Difficulty: **Hard**

Given two integer arrays `arr1` and `arr2`, return the minimum number of operations (possibly zero) needed to make `arr1` strictly increasing.

In one operation, you can choose two indices `0 <= i < arr1.length` and `0 <= j < arr2.length` and do the assignment `arr1[i] = arr2[j]`.

If there is no way to make `arr1` strictly increasing, return `-1`.

**Example 1:**

```
Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
Output: 1
Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
```

**Example 2:**

```
Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
Output: 2
Explanation: Replace 5 with 3 and then replace 3 with 4\. arr1 = [1, 3, 4, 6, 7].
```

**Example 3:**

```
Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
Output: -1
Explanation: You can't make arr1 strictly increasing.
```

**Constraints:**

*   `1 <= arr1.length, arr2.length <= 2000`
*   `0 <= arr1[i], arr2[i] <= 10^9`


#### Solution
- 比赛时候没做出来，压根没想到是dp
- 赛后看了好几种方案，花花酱的dp思路特别麻烦
- dp这个思路比较巧妙，代码也简单
    - https://leetcode.com/problems/make-array-strictly-increasing/discuss/377403/Python-DP-solution-with-explanation.
    - 我的代码基本是借鉴这个的
- 暴力
    - 这题暴力也可以做， dfs + backtracking
    - https://leetcode.com/problems/make-array-strictly-increasing/discuss/377531/O(n2-log(n))-solutionStarting-from-brute-force-improve-by-memoization
    - https://leetcode.com/problems/make-array-strictly-increasing/discuss/377402/C%2B%2B-DFS-%2B-memo-based-on-Longest-Increasing-subsequence-solution-with-explanation
    - 思路：
    - 从左往右搜索，保证前面的阶段性数组满足递增
    - 对于一个新的数
        - case1: 如果 left_num < new_num， 这时候有两种操作
            - way1: 直接把new_num添加到最后，替换次数不变
            - way2: 把心的数替换成arr2里最小的num, 且满足 left_num < arr2_num
        - case2: 如果 left_num >= new_num
            - 把new_num 替换成arr2里面大于left_num的数字
    
- LIS思路升级
    - https://leetcode.com/problems/make-array-strictly-increasing/discuss/377495/Java-dp-solution-%3A-A-simple-change-from-Longest-Increasing-Subsequence

Language: **Python3**

```python3
from collections import defaultdict
​
import bisect
from typing import List
​
​
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(set(arr2))
        pre_dp = {-1: 0}  # pre_dp[i] 表示当前元素为i时所需替换的最小次数
        for cur_num in arr1:
            cur_dp = defaultdict(lambda: float('inf'))
            for pre_num, min_operations in pre_dp.items():
                # 当上一个数小于当前数的时候，当前数不用改变，替换的次数也不用增加
                if pre_num < cur_num:
                    cur_dp[cur_num] = min(cur_dp[cur_num], min_operations)
​
                # 在arr2里二分查找大于pre_num上一个数的数，对应的数的替换的次数加一，看是否更小
                pos = bisect.bisect_right(arr2, pre_num)
                if pos < len(arr2):
                    cur_dp[arr2[pos]] = min(cur_dp[arr2[pos]], min_operations + 1)
            pre_dp = cur_dp  # 把dp压缩到一维
        return min(pre_dp.values()) if pre_dp else -1
​
​
if __name__ == '__main__':
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]) == 1
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]) == 2
    assert Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]) == -1
​
```