### [1071\. Greatest Common Divisor of StringsCopy for MarkdownCopy for Markdown](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

Difficulty: **Easy**


For strings `S` and `T`, we say "`T` divides `S`" if and only if `S = T + ... + T`  (`T` concatenated with itself 1 or more times)

Return the largest string `X` such that `X` divides <font face="monospace" style="display: inline;">str1</font> and `X` divides <font face="monospace" style="display: inline;">str2</font>.

**Example 1:**

```
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
```

**Example 2:**

```
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
```

**Example 3:**

```
Input: str1 = "LEET", str2 = "CODE"
Output: ""
```

**Note:**

1.  `1 <= str1.length <= 1000`
2.  `1 <= str2.length <= 1000`
3.  `str1[i]` and `str2[i]` are English uppercase letters.

### Link
- https://leetcode.com/problems/greatest-common-divisor-of-strings/
- https://leetcode.com/submissions/detail/247840176/

#### Solution

- 我的解法，不算漂亮，漂亮的代码直接用math.gcd
- 这题测试数据也有问题， 比如 输入 "abcd"， "ab"，输出应该是"", 很多discuss黎明贴的代码会输出'ab'，居然系统一百多组测试数据都测不出来。。。

Language: **Python3**

- 
```python3
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1,str2 = str2, str1
        for i in range(len(str1),0,-1):
            
                
            
            sub = str1[0:i]
            
            
            if len(str2) % len(sub) !=0 or len(str1) % len(sub)!=0: 
                continue
            
            l= len(sub)
            x1 = len(str1)//l
            x2 = len(str2)//l
            if x1 * sub == str1 and x2 * sub == str2:
                return sub
        return ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n = math.gcd(len(str1), len(str2))
        t = str1[:n]
        if t * (len(str1)//n) == str1 and t * (len(str2)//n) == str2:
            return t
        return ''
```