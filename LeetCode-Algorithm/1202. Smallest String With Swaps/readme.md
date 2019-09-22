### [1202\. Smallest String With Swaps](https://leetcode.com/contest/weekly-contest-155/problems/smallest-string-with-swaps/)

Difficulty: **Medium**

You are given a string `s`, and an array of pairs of indices in the string `pairs` where `pairs[i] = [a, b]` indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given `pairs` **any number of times**.

Return the lexicographically smallest string that `s` can be changed to after using the swaps.

**Example 1:**

```
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
```

**Example 2:**

```
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
```

**Example 3:**

```
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"

```

**Constraints:**

*   `1 <= s.length <= 10^5`
*   `0 <= pairs.length <= 10^5`
*   `0 <= pairs[i][0], pairs[i][1] < s.length`
*   `s` only contains lower case English letters.

#### Solution
- 读完题，很快相处并查集的贪心思路
- 写的时候还算顺利，代码可能有点冗余，但基本算是一次通过
- 思路，并查集：
    - 把可以相互交换的位置放到一个集合里（用并查集）
    - 同一个集合里的字母按照字典序重新排序
    
Language: **Python3**

```python3
from collections import defaultdict
from typing import List
​
​
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
​
        parents = [x for x in range(0, n + 1)]
        members = [1] * (n + 1)
​
        def find(x: int) -> int:
            while parents[x] != x:
                x = parents[x]
            return x
​
        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if members[px] < members[py]:
                px, py = py, px
            members[px] += members[py]
            parents[py] = px
            return True
​
        for fa_id, b in pairs:
            union(fa_id, b)
​
        d_id = defaultdict(list)
        d_ch = defaultdict(list)
        for i, ch in enumerate(s):
            fa_id = find(i)
            d_id[fa_id].append(i)
            d_ch[fa_id].append(ch)
​
        res = ['' for _ in range(len(s))]  # 初始化res,保证长度
        for fa_id in d_id.keys():
            ids = sorted(d_id[fa_id])
            chs = sorted(d_ch[fa_id])
            for i, fa_id in enumerate(ids):
                res[fa_id] = chs[i]
​
        res2 = ''.join(res)
        print(res2)
        return res2
​
​
if __name__ == '__main__':
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2]]) == 'bacd'
    assert Solution().smallestStringWithSwaps(s="dcab", pairs=[[0, 3], [1, 2], [0, 2]]) == 'abcd'
    assert Solution().smallestStringWithSwaps(s="cba", pairs=[[0, 1], [1, 2]]) == 'abc'
​
```