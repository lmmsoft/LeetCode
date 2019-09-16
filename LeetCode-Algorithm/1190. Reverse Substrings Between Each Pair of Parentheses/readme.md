### [1190\. Reverse Substrings Between Each Pair of Parentheses](https://leetcode.com/contest/weekly-contest-154/problems/reverse-substrings-between-each-pair-of-parentheses/)

Difficulty: **Medium**

Given a string `s` that consists of lower case English letters and brackets. 

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should **not** contain any bracket.

**Example 1:**

```
Input: s = "(abcd)"
Output: "dcba"
```

**Example 2:**

```
Input: s = "(u(love)i)"
Output: "iloveu"
```

**Example 3:**

```
Input: s = "(ed(et(oc))el)"
Output: "leetcode"
```

**Example 4:**

```
Input: s = "a(bcdefghijkl(mno)p)q"
Output: "apmnolkjihgfedcbq"
```

**Constraints:**

*   `0 <= s.length <= 2000`
*   `s` only contains lower case English characters and parentheses.
*   It's guaranteed that all parentheses are balanced.

#### Solution
-  好题
- 第二题很不顺，一开始想多了，卡了很久，草稿纸写了两张，才朴素写出 53min 1AC
- 这题很显然是用堆栈做，但是一开始我想直接吧字母拼接起来，失败了，后来用栈保存过程的字母，才通过

Language: **Python3**

```python3
class Solution:
    def reverseParentheses1(self, s: str) -> str:
        stack = []
        tmp = ""
        for c in s:
            if c == '(':
                if tmp:
                    stack.append(tmp)
                    tmp = ""
                stack.append('(')
            elif c == ')':
                while True:
                    top = stack.pop()
                    if top == "(":
                        break
                    tmp = top + tmp
                stack.append(tmp[::-1])
                tmp = ""
            else:
                tmp += c
​
        res = ''.join(stack) + tmp
        print(res)
        return res
​
    def reverseParentheses(self, s: str) -> str:
        stack = ['']  # 默认空串，保证第一个字母可以直接添加
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]  # 顶部元素取出，并倒序， 【即把左右括号里的都取出，倒序】
                stack[-1] += add  # 添加到前一个元素尾部，即和前一层左括号的元素合并
            else:
                stack[-1] += c  # 把c添加到stack顶部元素末尾
        return stack.pop()  # 此时所以对应括号里的元素都合并到最后一个字母里了
​
​
if __name__ == '__main__':
    assert Solution().reverseParentheses('a(bc)d') == 'acbd'
    assert Solution().reverseParentheses("(abcd)") == "dcba"
    assert Solution().reverseParentheses("(u(love)i)") == "iloveu"
    assert Solution().reverseParentheses("(ed(et(oc))el)") == "leetcode"
    assert Solution().reverseParentheses("a(bcdefghijkl(mno)p)q") == "apmnolkjihgfedcbq"
​
```