## Link
- https://leetcode.com/problems/first-missing-positive/submissions/
- https://leetcode-cn.com/problems/first-missing-positive/submissions/

## Description
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
```
Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:
```
Your algorithm should run in O(n) time and uses constant extra space.

## Solution
- Time is limited to O(n) and space is limited to constant, so we can't use some easy implemented methods:
    - sort: time nlogn, constant extra space
    - hashmap: O(n) time and O(n) space
- we can only move numbers in the array
    - Since the number range is limited to [1 to n], we can use bucket sort(桶排序) to solve
    - nums[index] must be index+1 , if not, we can swap it with nums[nums[index]] 
    - for each number, do above swap
    - the loop the array, find out number[index] != index + 1
    - What's more:
        - If all numbers are valid after moves, return len(nums) + 1
        - nums can be duplicated
        
## My Solution
- I finish O(n) time and O(1) space, but my code is not good, if use recurrence to swap numbers