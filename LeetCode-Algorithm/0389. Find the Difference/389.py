import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = collections.Counter(s)
        for i, char in enumerate(s):
            if c[char] == 1:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().firstUniqChar("leetcode") == 0
    assert Solution().firstUniqChar("loveleetcode") == 2
