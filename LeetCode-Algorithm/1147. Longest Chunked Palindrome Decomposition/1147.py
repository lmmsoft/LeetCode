from collections import defaultdict


class Solution:
    def longestDecomposition(self, text: str) -> int:
        num = 0
        L = len(text)
        l, r = 0, L - 1
        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        while l < r:
            mp1[text[l]] += 1
            mp2[text[r]] += 1
            if mp1 == mp2:
                num += 2
                mp1 = defaultdict(int)
                mp2 = defaultdict(int)
            l += 1
            r -= 1
        if not mp1 and not mp2 and l > r:
            pass
        else:
            num += 1
        return num


if __name__ == '__main__':
    assert Solution().longestDecomposition("ghiabcdefhelloadamhelloabcdefghi") == 7
    assert Solution().longestDecomposition("merchant") == 1
    assert Solution().longestDecomposition("antaprezatepzapreanta") == 11
    assert Solution().longestDecomposition("aaa") == 3
