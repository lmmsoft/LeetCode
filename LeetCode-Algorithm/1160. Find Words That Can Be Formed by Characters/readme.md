### [1160\. Find Words That Can Be Formed by Characters](https://leetcode.com/contest/weekly-contest-150/problems/find-words-that-can-be-formed-by-characters/)
- https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
- https://leetcode.com/contest/weekly-contest-150/problems/find-words-that-can-be-formed-by-characters/

Difficulty: **Easy**

You are given an array of strings `words` and a string `chars`.

A string is _good_ if it can be formed by characters from `chars` (each character can only be used once).

Return the sum of lengths of all good strings in `words`.

**Example 1:**

```
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```

**Example 2:**

```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```

<span style="display: inline;">**Note:**</span>

1.  `1 <= words.length <= 1000`
2.  `1 <= words[i].length, chars.length <= 100`
3.  All strings contain lowercase English letters only.

#### Solution
- 水题，判断每个字母的数量是否满足要求即可
- 收集了好几种Counter()的用法，用得越溜，代码越短

Language: **Python3**

```python3
from collections import Counter
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def check(c, cw) -> bool:
            for k, v in cw.items():
                if c[k] < v:
                    return False
            return True

        c = Counter(chars)
        res = 0
        for w in words:
            cw = Counter(w)
            if check(c, cw):
                res += len(w)
        return res

    def countCharacters3(self, words: List[str], chars: str) -> int:
        return sum(len(w) for w in words if sum(1 for k, v in Counter(w).items() if Counter(chars)[k] < v) == 0)  # 我的思路，比较差

    def countCharacters4(self, words: List[str], chars: str) -> int:
        return len(''.join(filter(lambda w: len(Counter(w) - Counter(chars)) == 0, words)))

    def countCharacters5(self, words, chars):
        return sum(len(w) for w in words if not (Counter(w) - Counter(chars)))  # cw - c 为做差集，如果减去c==0, 说明被chars包含，符合条件


if __name__ == '__main__':
    assert Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach") == 6
    assert Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr") == 10

​
```