from collections import defaultdict


class Solution:
    def lastSubstring2(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        z = max(d.keys())
        ids = d[z]
        return max(s[start:] for start in ids)

    def lastSubstring(self, s: str) -> str:
        d = defaultdict(list)
        for i, c in enumerate(s): d[c].append(i)
        return max(s[start:] for start in (d[max(d.keys())]))


if __name__ == '__main__':
    assert Solution().lastSubstring("abab") == 'bab'
    assert Solution().lastSubstring("leetcode") == 'tcode'
