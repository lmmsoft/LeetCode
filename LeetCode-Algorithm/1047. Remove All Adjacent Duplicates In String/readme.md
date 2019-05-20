# 1047. Remove All Adjacent Duplicates In String(Easy)
- https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
- Weekly Contest 137 https://leetcode.com/contest/weekly-contest-137
- Easy, 1 AC

# Q2 删除字符串中的所有相邻重复项 1047 Easy
- https://leetcode.com/contest/weekly-contest-137/problems/remove-all-adjacent-duplicates-in-string/
- https://leetcode-cn.com/contest/weekly-contest-137/problems/remove-all-adjacent-duplicates-in-string/
- 题意：每次删除字符串里相邻且相同的字母对，求最后无法再删除的字符串
- 解法：栈

# Code
- my code
- 写得很丑，而且调试了很久
```python
def removeDuplicates(self, S: str) -> str:
    s = [ss for ss in S]
    s2 = []
    found = True

    while found:
        found = False
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                s2.append(s[i])
            elif s[i] == s[i + 1]:
                found = True
                i += 1
            else:
                s2.append(s[i])
            i += 1
        s = copy.copy(s2)
        s2 = []
    return ''.join(s)

```

- rank1 Ryuusei
```python
def removeDuplicates(self, S: str) -> str:
    q = []
    for c in S:
        q += [c]
        if len(q) > 1:
            if q[-1] == q[-2]:
                q.pop()
                q.pop()
    return "".join(q)
```

- rank3 seeean
```python
def removeDuplicates(self, S):
    stack = []
    for c in S:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)
```