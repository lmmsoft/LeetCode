## Link
- https://leetcode.com/problems/two-sum/
- https://leetcode-cn.com/problems/two-sum/

## Description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

## Solution
- Brute Force O(N^2)
    - 2 Loops to calculate sum of two numbers
- Sort nlogn
    - Sort first (nlogn), then find from two side by 2 point from start and end O(2n)
- Hash O(n)
    - add numbsers to hash map, check if (traget-n) existed in hash map