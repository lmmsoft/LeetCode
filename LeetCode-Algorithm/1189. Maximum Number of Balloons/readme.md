### [1189\. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)

Difficulty: **Easy**


Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

**Example 1:**

**![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex1_upd.JPG)**

```
Input: text = "nlaebolko"
Output: 1
```

**Example 2:**

**![](https://assets.leetcode.com/uploads/2019/09/05/1536_ex2_upd.JPG)**

```
Input: text = "loonbalxballpoon"
Output: 2
```

**Example 3:**

```
Input: text = "leetcode"
Output: 0
```

**Constraints:**

*   `1 <= text.length <= 10^4`
*   `text` consists of lower case English letters only.


#### Solution
- 水题，统计字母出现次数即可，可以用Counter() 也可以用count()

Language: **Python3**

```python3
from collections import Counter
​
​
class Solution:
    def maxNumberOfBalloons1(self, text: str) -> int:
        c = Counter(text)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])
​
    def maxNumberOfBalloons2(self, t: str) -> int:
        return min(t.count('b'), t.count('a'), t.count('l') // 2, t.count('o') // 2, t.count('n'))
​
    def maxNumberOfBalloons(self, t: str) -> int:
        return min(t.count(c) // int(cnt) for c, cnt in zip('balon', '11221'))
​
if __name__ == '__main__':
    assert Solution().maxNumberOfBalloons("nlaebolko") == 1
    assert Solution().maxNumberOfBalloons("loonbalxballpoon") == 2
    assert Solution().maxNumberOfBalloons("leetcode") == 0
​
```