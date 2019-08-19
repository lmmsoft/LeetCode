### [1156\. Swap For Longest Repeated Character Substring](https://leetcode.com/problems/swap-for-longest-repeated-character-substring/)
- https://leetcode.com/problems/swap-for-longest-repeated-character-substring/
- https://leetcode.com/contest/weekly-contest-149/problems/swap-for-longest-repeated-character-substring/

Difficulty: **Medium**


Given a string `text`, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.

**Example 1:**

```
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
```

**Example 2:**

```
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
```

**Example 3:**

```
Input: text = "aaabbaaa"
Output: 4
```

**Example 4:**

```
Input: text = "aaaaa"
Output: 5
Explanation: No need to swap, longest repeated character substring is "aaaaa", length is 5.
```

**Example 5:**

```
Input: text = "abcdef"
Output: 1
```

**Constraints:**

*   `1 <= text.length <= 20000`
*   `text` consist of lowercase English characters only.


#### Solution
- 比赛时乱搞一气，没做出来
- 赛后看了lee的解答，豁然开朗
    - https://leetcode.com/problems/swap-for-longest-repeated-character-substring/discuss/355852/Python-Groupby
- 其实只要两种可能
- Case1 某连续的组多一个
- Case2 某两个组字母一样，中间隔一个，中间换一个，让两边连起来
- 依次枚举上面两种情况就行
- 使用python groupby可以帮助简化代码


Language: **Python3**

```python3
import collections
import itertools
​
​
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        counter = collections.Counter(text)
        group = [(char, len(list(g))) for char, g in itertools.groupby(text)]
​
        # Case1, extend 1 more for longest group
        mx = max(min(length + 1, counter[char]) for char, length in group)
​
        # Case2, merge 2 groups together, distance between 2 groups is 1
        for mid in range(1, len(group) - 1):  # from 1 to len-1
            if group[mid - 1][0] == group[mid + 1][0] and group[mid][1] == 1:
                mx = max(
                    mx,
                    min(
                        1 + group[mid - 1][1] + group[mid + 1][1],
                        counter[group[mid - 1][0]],
                    )
                )
        return mx
​
​
if __name__ == '__main__':
    assert Solution().maxRepOpt1("ababa") == 3
​
    assert Solution().maxRepOpt1("aaabaaa") == 6
​
    assert Solution().maxRepOpt1("aaabbaaa") == 4
​
    assert Solution().maxRepOpt1("aaaaa") == 5
​
    assert Solution().maxRepOpt1("abcdef") == 1
​
    assert Solution().maxRepOpt1("aaabaa") == 5
​
```