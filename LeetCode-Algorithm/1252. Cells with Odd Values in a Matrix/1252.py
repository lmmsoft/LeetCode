from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        l = [[0 for mm in range(m)] for nn in range(n)]
        for a, b in indices:
            for mm in range(m):
                l[a][mm] += 1
            for nn in range(n):
                l[nn][b] += 1
        return sum([l[nn][mm] % 2 == 1 for nn in range(n) for mm in range(m)])


if __name__ == '__main__':
    assert Solution().oddCells(n=2, m=3, indices=[[0, 1], [1, 1]]) == 6
    assert Solution().oddCells(n=2, m=2, indices=[[1, 1], [0, 0]]) == 0
