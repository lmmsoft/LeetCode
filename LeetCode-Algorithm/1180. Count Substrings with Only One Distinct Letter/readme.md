### [1180\. Count Substrings with Only One Distinct Letter](https://leetcode.com/contest/biweekly-contest-8/problems/count-substrings-with-only-one-distinct-letter/)
- https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/discuss
- https://leetcode.com/contest/biweekly-contest-8/problems/count-substrings-with-only-one-distinct-letter/

Difficulty: **Easy**

Given a string `S`, return the number of substrings that have only **one distinct** letter.

**Example 1:**

```
Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.
```

**Example 2:**

```
Input: S = "aaaaaaaaaa"
Output: 55
```

**Constraints:**

*   `1 <= S.length <= 1000`
*   `S[i]` consists of only lowercase English letters.

#### Solution
- 水题，统计连续同样字母个数，每组的n同样个字母的子串个数不难发现是1+2+...+n=(1+n)*n/2，求和即可
- 使用itertool的groupby可以加快速度，排名第一的就是这么实现的，我比赛的时候没搞清用法，赛后了解了一下 

Language: **Python3**

```python3
class Solution:
    def countLetters1(self, S: str) -> int:
        g = []
        cnt = 1
        if len(S) == 1:
            return 1
        for i in range(1, len(S)):
            if S[i] == S[i - 1]:
                cnt += 1
            else:
                g.append(cnt)
                cnt = 1
        g.append(cnt)
        # print(g)
​
        res = 0
        for i in g:
            res += (i + 1) * i // 2
        return res
​
    def countLetters(self, S: str) -> int:
        from itertools import groupby
        res = 0
        for ch, g in groupby(S):
            cnt = len(list(g))
            res += cnt * (cnt + 1) // 2
        return res
​
​
if __name__ == '__main__':
    assert Solution().countLetters("aaaba") == 8
    assert Solution().countLetters("aaaaaaaaaa") == 55
​
```