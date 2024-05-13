class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        r = 0
        for i,c in enumerate(s):
            j = t.index(c)
            r += int(abs(i-j))
        return r