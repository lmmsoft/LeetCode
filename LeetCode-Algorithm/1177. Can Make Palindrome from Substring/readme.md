### [1177\. Can Make Palindrome from Substring](https://leetcode.com/problems/can-make-palindrome-from-substring/)
- https://leetcode.com/contest/weekly-contest-152/problems/can-make-palindrome-from-substring/
- https://leetcode.com/problems/can-make-palindrome-from-substring/

Difficulty: **Medium**


Given a string `s`, we make queries on substrings of `s`.

For each query `queries[i] = [left, right, k]`, we may **rearrange** the substring `s[left], ..., s[right]`, and then choose **up to** `k` of them to replace with any lowercase English letter. 

If the substring is possible to be a palindrome string after the operations above, the result of the query is `true`. Otherwise, the result is `false`.

Return an array `answer[]`, where `answer[i]` is the result of the `i`-th query `queries[i]`.

Note that: Each letter is counted **individually** for replacement so if for example `s[left..right] = "aaa"`, and `k = 2`, we can only replace two of the letters.  (Also, note that the initial string `s` is never modified by any query.)

**Example :**

```
Input: s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
Output: [true,false,false,true,true]
Explanation:
queries[0] : substring = "d", is palidrome.
queries[1] : substring = "bc", is not palidrome.
queries[2] : substring = "abcd", is not palidrome after replacing only 1 character.
queries[3] : substring = "abcd", could be changed to "abba" which is palidrome. Also this can be changed to "baab" first rearrange it "bacd" then replace "cd" with "ab".
queries[4] : substring = "abcda", could be changed to "abcba" which is palidrome.
```

**Constraints:**

*   `1 <= s.length, queries.length <= 10^5`
*   `0 <= queries[i][0] <= queries[i][1] < s.length`
*   `0 <= queries[i][2] <= s.length`
*   `s` only contains lowercase English letters.


#### Solution
- 坑爹题 for Python3
    - 用counter必然TLE，必须用普通dict优化一下统计和集合相减才能过，TLE了6次，很郁闷！
- 题意：
    - 给一个字符串，问这个字符串的某些字串能否在不超过 k次修改并重新排列组合组成回文串。
- 思路
    - 字串
    - 一开始没注意要先重新排列，再考虑回文 WA了一次，其实有个Case里面讲了，没仔细看
    - 因为可以重新排列，所以直接统计每个字母的个数，偶数直接通过，奇数记下，考虑对称  'a'回文 'ab'改一次 'abc'改一次
    - 对比diff//2与k即可
    - 子串的重排列
        - 每次统计字串会超时，可以求出s的前缀和，然后sum(r)-sum(l-1)即可

Language: **Python3**

```python3
from collections import defaultdict
​
from typing import List
​
​
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        def check(d, k):
            return sum(v % 2 for v in d.values()) // 2 <= k
​
        def minus(d1, d2):
            d3 = {}
            for k, v in d1.items():
                d3[k] = v - d2[k]
            return d3
​
        res = []
        dict_list = []
​
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
            dd = d.copy()
            dict_list.append(dd)
​
        for l, r, k in queries:
            if l == 0:
                d = dict_list[r]
            else:
                d = minus(dict_list[r], dict_list[l - 1])
            res.append(check(d, k))
        return res
​
​
if __name__ == '__main__':
    true = True
    false = False
    assert Solution().canMakePaliQueries(
        s="abcda",
        queries=[[3, 3, 0], [1, 2, 0], [0, 3, 1], [0, 3, 2], [0, 4, 1]]) == [
               true,
               false,
               false,
               true,
               true]
​
    assert Solution().canMakePaliQueries(
        "hunu",
        [[1, 1, 1], [2, 3, 0], [3, 3, 1], [0, 3, 2], [1, 3, 3], [2, 3, 1], [3, 3, 1], [0, 3, 0], [1, 1, 1], [2, 3, 0],
         [3, 3, 1], [0, 3, 1], [1, 1, 1]]) == [
               true, false, true, true, true, true, true, false, true, false, true, true, true]
​
```