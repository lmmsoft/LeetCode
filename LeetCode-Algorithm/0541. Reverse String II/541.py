class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0, len(s), 2 * k):
            l[i:i + k] = list(reversed(l[i:i + k]))
        return ''.join(l)


if __name__ == '__main__':
    assert Solution().reverseStr(s="abcdefg", k=2) == "bacdfeg"
    assert Solution().reverseStr('a', 2) == 'a'
    assert Solution().reverseStr("abcdefg", 8) == "gfedcba"
