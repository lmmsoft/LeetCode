### [1111\. Maximum Nesting Depth of Two Valid Parentheses Strings](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/)

Contest 144 https://leetcode.com/contest/weekly-contest-144/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

Difficulty: **Medium**


A string is a _valid parentheses string_ (denoted VPS) if and only if it consists of `"("` and `")"` characters only, and:

*   It is the empty string, or
*   It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are VPS's, or
*   It can be written as `(A)`, where `A` is a VPS.

We can similarly define the _nesting depth_ `depth(S)` of any VPS `S` as follows:

*   `depth("") = 0`
*   `depth(A + B) = max(depth(A), depth(B))`, where `A` and `B` are VPS's
*   `depth("(" + A + ")") = 1 + depth(A)`, where `A` is a VPS.

For example,  `""`, `"()()"`, and `"()(()())"` are VPS's (with nesting depths 0, 1, and 2), and `")("` and `"(()"` are not VPS's.

Given a VPS <font face="monospace" style="display: inline;">seq</font>, split it into two disjoint subsequences `A` and `B`, such that `A` and `B` are VPS's (and `A.length + B.length = seq.length`).

Now choose **any** such `A` and `B` such that `max(depth(A), depth(B))` is the minimum possible value.

Return an `answer` array (of length `seq.length`) that encodes such a choice of `A` and `B`:  `answer[i] = 0` if `seq[i]` is part of `A`, else `answer[i] = 1`.  Note that even though multiple answers may exist, you may return any of them.

**Example 1:**

```
Input: seq = "(()())"
Output: [0,1,1,1,1,0]
```

**Example 2:**

```
Input: seq = "()(())()"
Output: [0,0,0,1,1,0,1,1]
```

**Constraints:**

*   `1 <= seq.size <= 10000`


#### Solution

- 思路：
    - 首先计算每个括号发深度，遇到'('深度+1 , 遇到')'的时候深度不变，下一个深度-1
    - 然后分成两组，最大的深度的最小值: 最多变成原来最大深度的一半
    - 具体分法有很多种，一种简单的分法是：
        - 原来深度按照奇偶分成两组
        - 这样能保证每组都左右匹配，并且深度变成一半

Language: **Python3**

```python3
from typing import List
​
​
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        depth: list = []
        cur_depth = 0
        for s in seq:
            if s == '(':
                cur_depth += 1
                depth.append(cur_depth)
            else:
                depth.append(cur_depth)
                cur_depth -= 1
​
        print(seq)
        print(depth)
        res = []
        for i in depth:
            if i % 2 == 1:
                res.append(0)
            else:
                res.append(1)
        print(res)
        return res
​
​
​
```

- 比较好的解法 https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/328841/JavaC%2B%2BPython-Several-Ideas

- 神奇的一行C++ 解法
```c++
vector<int> maxDepthAfterSplit(string seq) {
    return vector<int>(seq.length(), 1);
}
```