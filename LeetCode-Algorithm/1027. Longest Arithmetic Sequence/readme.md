### [1027\. Longest Arithmetic Sequence](https://leetcode.com/contest/weekly-contest-132/problems/longest-arithmetic-sequence/)

Difficulty: **Medium**

Given an array `A` of integers, return the **length** of the longest arithmetic subsequence in `A`.

Recall that a _subsequence_ of `A` is a list `A[i_1], A[i_2], ..., A[i_k]` with `0 <= i_1 < i_2 < ... < i_k <= A.length - 1`, and that a sequence `B` is _arithmetic_ if `B[i+1] - B[i]` are all the same value (for `0 <= i < B.length - 1`).

**Example 1:**

```
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
```


**Example 2:**

```
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
```


**Example 3:**

```
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```


**Note:**

1.  `2 <= A.length <= 2000`
2.  `0 <= A[i] <= 10000`


#### Solution
- https://leetcode.com/contest/weekly-contest-132/ranking/
- 比赛时候一直WA没做出来
- 赛后看了一下，很可惜
- 求子数列里 项数最多 的等差数列

- 我的思路：暴力 O(N^3)
    - 枚举 前两项，然后用dict辅助判断后面的项是否在数列里，且下标递增
- 比赛代码的失误
    - 枚举i j的时候，j应该初始化为i+1，比赛是弄成1，造成下标没递增
    - 我用了self.xx 保存过程数据，没有每次都初始化，造成runtime error，怀疑judge不会没出都除湿盒class实例，下次注意

- 更好是思路 O(N^2)
    - 上面思路枚举i j的时候，继续推倒后面的下标k
    - 其实是荣誉的，后面自然会枚举到j, k (即i==j, j==k的时候)
    - 所以用记忆化的方法，枚举 j,k 的时候能代入 i,j的结果
    - 于是保存一个dict，key=(diff, j), value=项数，于是
    - 递推公式 dp(diff, j) = dp(diff, i) + 1, dp(diff,i)的默认值是1
    


Language: **Python3**

```python3
class Solution:
    def longestArithSeqLength2(self, A):
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[j, diff] = dp.get((i, diff), 1) + 1
        return max(dp.values())
        
```