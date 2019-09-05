class Solution:
    def isValid(self, s: str) -> bool:
        d1 = {
            '(': 1,
            '{': 2,
            '[': 3,
        }
        d2 = {
            ')': 1,
            '}': 2,
            ']': 3,
        }

        stack = []
        for c in s:
            if len(stack):
                if c in list(d2.keys()):
                    if d2[c] == d1.get(stack[-1], 0):
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)

            else:
                stack.append(c)

        return not len(stack)


if __name__ == '__main__':
    assert Solution().isValid("()")
    assert Solution().isValid("()[]{}")
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("{[]}")
