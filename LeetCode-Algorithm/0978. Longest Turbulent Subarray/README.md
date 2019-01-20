# link
- problem
    - https://leetcode.com/problems/squares-of-a-sorted-array/
    - https://leetcode-cn.com/problems/squares-of-a-sorted-array/
- Contest link
    - https://leetcode.com/contest/weekly-contest-120/problems/longest-turbulent-subarray/
    - https://leetcode-cn.com/contest/weekly-contest-120/problems/longest-turbulent-subarray/
- Official Solution
    - https://leetcode.com/articles/longest-turbulent-subarray/
    - https://leetcode-cn.com/articles/longest-turbulent-subarray/
    
# Description
A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only if:

For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is even;
OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.
That is, the subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Return the length of a maximum size turbulent subarray of A.
 
```
Example 1:

Input: [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
Example 2:

Input: [4,8,12,16]
Output: 2
Example 3:

Input: [100]
Output: 1
 

Note:

1 <= A.length <= 40000
0 <= A[i] <= 10^9
```

# Solution
- 先预处理一下数列，变成 -1, 0, 1 这样的数组，然后顺序扫描，找到 -1 与 1 连续出现的的最大长度
- 比赛时候写得很急躁，边界情况怎么都没处理好，因为晚开始半个多小时，后面时间越来越紧张，没能静下心来慢慢写完，也没来得及想清楚重写，最后赛后过了十几分钟才AC
- 赛后看了一下官方解题报告，预处理为 -1 0 1的思路和我一样
    - 在求长度的时候思路比较好，用end-start+1来处理，思路很清晰
    - 而我是扫描的过程中不断+1，越写越乱，代码也又臭又长
```python
class Solution(object):
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(A[i-1], A[i])
            if i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
```