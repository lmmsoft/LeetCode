### [1170\. Compare Strings by Frequency of the Smallest Character](https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/)
- https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
- https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

Difficulty: **Easy**


Let's define a function `f(s)` over a non-empty string `s`, which calculates the frequency of the smallest character in `s`. For example, if `s = "dcce"` then `f(s) = 2` because the smallest character is `"c"` and its frequency is 2.

Now, given string arrays `queries` and `words`, return an integer array `answer`, where each `answer[i]` is the number of words such that `f(queries[i])` < `f(W)`, where `W` is a word in `words`.

**Example 1:**

```
Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
```

**Example 2:**

```
Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
```

**Constraints:**

*   `1 <= queries.length <= 2000`
*   `1 <= words.length <= 2000`
*   `1 <= queries[i].length, words[i].length <= 10`
*   `queries[i][j]`, `words[i][j]` are English lowercase letters.


#### Solution
- 简单题，N^2暴力过了，其实最好能用二分，nlogn
- 可以练习一下bisect写法

Language: **Python3**

```python3
from collections import Counter
​
from typing import List
​
​
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def fun(w):
            c = Counter(w)
            m = min(c.keys())
            return c[m]
​
        fq = [fun(f) for f in queries]
        fw = [fun(f) for f in words]
        fw = sorted(fw)
​
        res = []
        for q in fq:
            found = False
            for id, w in enumerate(fw):
                if w > q:
                    res.append(len(fw) - id)
                    found = True
                    break
            if not found:
                res.append(0)
        print(res)
        return res
​
​
if __name__ == '__main__':
    assert Solution().numSmallerByFrequency(queries=["cbd"], words=["zaaaz"]) == [1]
    assert Solution().numSmallerByFrequency(queries=["bbb", "cc"], words=["a", "aa", "aaa", "aaaa"]) == [1, 2]
​
```