from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = len(s)
        d = defaultdict(int)
        for size in range(minSize, maxSize + 1):
            for i in range(0, l - size + 1):
                ss = s[i:i + size]
                if len(set(ss)) <= maxLetters:
                    d[ss] += 1
        if not d:
            return 0
        return max(d.values())

    # sliding window
    def maxFreq2(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = defaultdict(int)
        n = len(s)
        st = ed = 0
        while st < n:
            temp = set()
            while len(temp) <= maxLetters and ed - st <= maxSize and ed <= n:
                if ed - st >= minSize:
                    cnt[s[st:ed]] += 1
                if ed < n:
                    temp.add(s[ed])
                ed += 1
            st += 1
            ed = st
        return max(cnt.values()) if cnt else 0


if __name__ == '__main__':
    assert Solution().maxFreq(s="aababcaab", maxLetters=2, minSize=3, maxSize=4) == 2
    assert Solution().maxFreq(s="aaaa", maxLetters=1, minSize=3, maxSize=3) == 2
    assert Solution().maxFreq(s="aabcabcab", maxLetters=2, minSize=2, maxSize=3) == 3
    assert Solution().maxFreq(s="abcde", maxLetters=2, minSize=3, maxSize=3) == 0
