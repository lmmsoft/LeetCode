### [551\. Student Attendance Record I](https://leetcode.com/problems/student-attendance-record-i/)

Difficulty: **Easy**

You are given a string representing an attendance record for a student. The record only contains the following three characters:

1.  **'A'** : Absent.
2.  **'L'** : Late.
3.  **'P'** : Present.

A student could be rewarded if his attendance record doesn't contain **more than one 'A' (absent)** or **more than two continuous 'L' (late)**.

You need to return whether the student could be rewarded according to his attendance record.

**Example 1:**  

```
Input: "PPALLP"
Output: True
```

**Example 2:**  

```
Input: "PPALLL"
Output: False
```


#### Solution
- 水题，别着急，难度在于读懂题意

Language: **Python3**

```python3
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and s.count('LLL') < 1
```