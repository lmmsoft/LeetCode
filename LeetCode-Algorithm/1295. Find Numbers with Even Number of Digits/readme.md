### [1295\. Find Numbers with Even Number of Digits](https://leetcode.com/contest/weekly-contest-168/problems/find-numbers-with-even-number-of-digits/)

Difficulty: **Easy**

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

**Example 1:**

```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

**Example 2:**

```
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
```

**Constraints:**

*   `1 <= nums.length <= 500`
*   `1 <= nums[i] <= 10^5`

#### Solution

Language: **Python3**
- 题意：判断偶数位数字的个数
- 水题，难得在比赛中用网页拍了一行代码，比较惊讶的是居然有人14s就AC了，并且还是好几行的代码~
```python3
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for n in nums if len(str(n))%2==0)
            
        
```