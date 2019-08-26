### [1165\. Single-Row Keyboard](https://leetcode.com/contest/biweekly-contest-7/problems/single-row-keyboard/)
- https://leetcode.com/problems/single-row-keyboard/
- https://leetcode.com/contest/biweekly-contest-7/problems/single-row-keyboard/

Difficulty: **Easy**

There is a special keyboard with **all keys in a single row**.

Given a string `keyboard` of length 26 indicating the layout of the keyboard (indexed from 0 to 25), initially your finger is at index 0\. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index `i` to index `j` is `|i - j|`.

You want to type a string `word`. Write a function to calculate how much time it takes to type it with one finger.

**Example 1:**

```
Input: keyboard = "abcdefghijklmnopqrstuvwxyz", word = "cba"
Output: 4
Explanation: The index moves from 0 to 2 to write 'c' then to 1 to write 'b' then to 0 again to write 'a'.
Total time = 2 + 1 + 1 = 4\. 
```

**Example 2:**

```
Input: keyboard = "pqrstuvwxyzabcdefghijklmno", word = "leetcode"
Output: 73
```

**Constraints:**

*   `keyboard.length == 26`
*   `<font face="monospace" style="display: inline;">keyboard</font>` contains each English lowercase letter exactly once in some order.
*   `1 <= word.length <= 10^4`
*   `word[i]` is an English lowercase letter.

#### Solution
- 下标统计，水题

Language: **Python3**

```python3
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        s = 0
        p = 0
        for w in word:
            pp = keyboard.index(w)
            s += abs(pp - p)
            p = pp
        return s
​
​
if __name__ == '__main__':
    assert Solution().calculateTime(keyboard="abcdefghijklmnopqrstuvwxyz", word="cba") == 4
    assert Solution().calculateTime(keyboard="pqrstuvwxyzabcdefghijklmno", word="leetcode") == 73
​
```