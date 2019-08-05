### [1147\. Longest Chunked Palindrome Decomposition](https://leetcode.com/problems/longest-chunked-palindrome-decomposition/)
- https://leetcode.com/problems/longest-chunked-palindrome-decomposition/
- https://leetcode.com/contest/weekly-contest-148/problems/longest-chunked-palindrome-decomposition/
- https://leetcode.com/submissions/detail/249147756/

Difficulty: **Hard**


Return the largest possible `k` such that there exists `a_1, a_2, ..., a_k` such that:

*   Each `a_i` is a non-empty string;
*   Their concatenation `a_1 + a_2 + ... + a_k` is equal to `text`;
*   For all `1 <= i <= k`,  `a_i = a_{k+1 - i}`.

**Example 1:**

```
Input: text = "ghiabcdefhelloadamhelloabcdefghi"
Output: 7
Explanation: We can split the string on "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".
```

**Example 2:**

```
Input: text = "merchant"
Output: 1
Explanation: We can split the string on "(merchant)".
```

**Example 3:**

```
Input: text = "antaprezatepzapreanta"
Output: 11
Explanation: We can split the string on "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".
```

**Example 4:**

```
Input: text = "aaa"
Output: 3
Explanation: We can split the string on "(a)(a)(a)".
```

**Constraints:**

*   `text` consists only of lowercase English characters.
*   `1 <= text.length <= 1000`


#### Solution

Language: **Python3**
- 这题可以贪心做，因为如果一个长的
- left_str和right_str应该是完全逆序，可以把right_str反转后直接比较
- 我的代码有点问题，把代码映射到hashmap里再比较字母个数(言外之意是字母可以乱序，只要字符个数匹配即可)，可惜测试数据没测出来
- Discuss里介绍了Rabin Karp Algorithm，比较高效的字符串匹配比较算法，学习了
    - https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
    - https://www.cnblogs.com/golove/p/3234673.html


```python3
from collections import defaultdict
​
​
class Solution:
    def longestDecomposition(self, text: str) -> int:
        num = 0
        L = len(text)
        l, r = 0, L - 1
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        while l < r:
            mp1[text[l]] += 1
            mp2[text[r]] += 1
            if mp1 == mp2:
                num += 2
                mp1 = defaultdict(int)
                mp2 = defaultdict(int)
            l += 1
            r -= 1
        if not mp1 and not mp2 and l>r:
            pass
        else:
            num+=1
        return num
​
​
if __name__ == '__main__':
    assert Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi") == 7
    assert Solution().longestDecomposition("merchant") == 1
    assert Solution().longestDecomposition("antaprezatepzapreanta") == 11
    assert Solution().longestDecomposition("aaa") == 3
​
```