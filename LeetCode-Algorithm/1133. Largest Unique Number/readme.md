# 1133. Largest Unique Number Copy for Markdown

User Accepted: 887

User Tried: 900
T
otal Accepted: 906

Total Submissions: 1266

Difficulty: Easy

Given an array of integers A, return the largest integer that only occurs once.

If no integer occurs once, return -1.

 
```
Example 1:

Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.
Example 2:

Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.
 

Note:

1 <= A.length <= 2000
0 <= A[i] <= 1000
```

## Link
- https://leetcode.com/contest/biweekly-contest-5/problems/largest-unique-number/
- https://leetcode.com/contest/biweekly-contest-5
- https://leetcode.com/contest/biweekly-contest-5/ranking/

## 解法
- 这题其实没什么难度，O(1)空间就是O(N*logN)的排序算法，O(N)空间就是O(N)的遍历算法

```python
我的Counter

c = Counter()
for a in A:
    c[a] += 1

其实可以直接构造
c = Counter(A)
```