class Solution:
    def strStr1(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    assert Solution().strStr(haystack="hello", needle="ll") == 2
    assert Solution().strStr(haystack="aaaaa", needle="bba") == -1
