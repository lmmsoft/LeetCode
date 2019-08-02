from collections import defaultdict
from typing import List


class Solution:
    ll = 0
    d = defaultdict(list)  # val, list:index

    def longestArithSeqLength(self, A: List[int]) -> int:

        self.ll = 2
        self.d = defaultdict(list)  # val, list:index

        l = len(A)
        for i in range(0, l):
            v = A[i]
            self.d[v].append(i)

        for i in range(0, l):
            for j in range(i + 1, l):
                self.check(A, i, j)

        return self.ll

    def check(self, A, i, j):

        t_ll = 2

        while True:
            next = A[j] + A[j] - A[i]
            exi, idx = self.exist(j, next)
            if exi:
                t_ll += 1
                i = j
                j = idx
            else:
                break

        if t_ll > self.ll:
            self.ll = t_ll

    def exist(self, j, next):
        if next in self.d:
            for idx in self.d[next]:
                if idx > j:
                    return True, idx

        return False, 0


if __name__ == '__main__':
    assert Solution().longestArithSeqLength([24, 13, 1, 100, 0, 94, 3, 0, 3]) == 2

    assert Solution().longestArithSeqLength([83, 20, 17, 43, 52, 78, 68, 45]) == 2

    assert (Solution().longestArithSeqLength([3, 6, 9, 12])) == 4
    assert Solution().longestArithSeqLength([9, 4, 7, 2, 10]) == 3
    assert Solution().longestArithSeqLength([20, 1, 15, 3, 10, 5, 8]) == 4
