### [1048\. Longest String Chain](https://leetcode.com/problems/longest-string-chain/)

Difficulty: **Medium**


Given a list of words, each word consists of English lowercase letters.

Let's say `word1` is a predecessor of `word2` if and only if we can add exactly one letter anywhere in `word1` to make it equal to `word2`.  For example, `"abc"` is a predecessor of `"abac"`.

A _word chain _is a sequence of words `[word_1, word_2, ..., word_k]` with `k >= 1`, where `word_1` is a predecessor of `word_2`, `word_2` is a predecessor of `word_3`, and so on.

Return the longest possible length of a word chain with words chosen from the given list of `words`.

**Example 1:**

```
Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".
```

**Note:**

1.  `1 <= words.length <= 1000`
2.  `1 <= words[i].length <= 16`
3.  `words[i]` only consists of English lowercase letters.

## Q3 最长字符串链 1048 Medium
- https://leetcode.com/contest/weekly-contest-137/problems/longest-string-chain/
- https://leetcode-cn.com/contest/weekly-contest-137/problems/longest-string-chain/
- 题意： 一堆小写字母单词，如果word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身;词链是一个词链条，每个都是后面的前身，求最长磁链
- 解法：
- 磁链里面单词的长度肯定是连续的，比如2 3 4 5 ...
- 先预处理数据，按照单词长度分组
- 然后暴力枚举，把每个单词的后续单词们找到（只要枚举长度相差1的单词即可）
- 单词的磁链长度 = max(前身长度) + 1
- 长度从小到大dp一下即可
- 可惜代码写得不是很顺畅，写了很久，调了很久，最后差了几十秒，没来得及提交~

# Good Solutions
- rank1 Ryuusei
- dp 的思路
- dp[word]为到word为止的磁链长度
- dp[word] = max(dp[word的前序])+1 
```python
def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        f = collections.defaultdict(int)
        ans = 0
        for w in words:
            l = len(w)
            for i in range(l):
                f[w] = max(f[w], f[w[:i] + w[i+1:]] + 1)
                ans = max(ans, f[w])
        return ans
```