### [387\. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)
- https://leetcode.com/problems/first-unique-character-in-a-string/
- https://leetcode.com/contest/warm-up-contest/problems/first-unique-character-in-a-string/

Difficulty: **Easy**


Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

**Examples:**

```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```

**Note:** You may assume the string contain only lowercase letters.


#### Solution
- 水题，我的做法是用Counter统计次数，顺序找到第一个个数为1的，O(N)的时间和O(26)的空间
- 看了下最快的代码，是26个字母一次搜索，每次分别从左右开始搜索，如果能搜到，并且两个下标不同，就记录下来，最后找最小的下标
    - 这种方法空间是O(1)，但是理论时间是O(26N)，但非极端数据可能效果比较好，搜的时间也可以做些剪枝，但不是很通用的方法

Language: **Python3**

```python3
import collections
​
​
class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for i, char in enumerate(s):
            if c[char] == 1:
                return i
        return -1
​
​
if __name__ == '__main__':
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
​
```