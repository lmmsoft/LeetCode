# link
- problem
    - https://leetcode.com/problems/squares-of-a-sorted-array/
    - https://leetcode-cn.com/problems/squares-of-a-sorted-array/
- contest
    - https://leetcode.com/contest/weekly-contest-120/problems/squares-of-a-sorted-array/
    - https://leetcode-cn.com/contest/weekly-contest-120/problems/squares-of-a-sorted-array/
- Official Solution
    - https://leetcode.com/articles/squares-of-a-sorted-array/
    - https://leetcode-cn.com/articles/squares-of-a-sorted-array/
# Description
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.


Example 1:
```
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 ```

Note:
```
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
```

# Solution
 - My Solution
     - In contest, since it is a esay question, I use O(nlogn) sort method to solve it in a fast way
     - After contest, I use two point to finish it within O(n)    