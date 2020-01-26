class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a2 = sorted(arr)
        a3 = []
        d = {}
        rank = 1
        for i, a in enumerate(a2):
            if a not in d:
                d[a] = rank
                rank += 1
        for a in arr:
            a3.append(d[a])
        return a3

