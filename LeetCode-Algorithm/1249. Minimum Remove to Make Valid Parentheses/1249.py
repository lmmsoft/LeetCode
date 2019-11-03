class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = []
        for i, ch in enumerate(s):
            if ch in ['(', ')']:
                l.append((i, ch))
        stack = []
        for i, ch in l:
            if not stack:
                stack.append((i, ch))
            elif stack[len(stack) - 1][1] == '(' and ch == ')':
                stack.pop()
            else:
                stack.append((i, ch))
        # print(stack)
        d = {i for i, ch in stack}
        s2 = []
        for i, ch in enumerate(s):
            if i not in d:
                s2.append(ch)
        res = ''.join(s2)
        # print(res)
        return res


if __name__ == '__main__':
    assert Solution().minRemoveToMakeValid(s="lee(t(c)o)de)") in ["lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"]
    assert Solution().minRemoveToMakeValid(s="a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid(s="))((") == ""
    assert Solution().minRemoveToMakeValid(s="(a(b(c)d)") == "a(b(c)d)"
