from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        L = len(grid)

        s = sum(sum(r) for r in grid)
        if s == 0 or s == L * L:
            return -1

        def add(i, j, cnt, next):
            if 0 <= i < L and 0 <= j < L and grid[i][j] == 0:
                grid[i][j] = 1
                cnt += 1
                next.append((i, j))
            return cnt

        q = []
        cnt = 0
        for i in range(L):
            for j in range(L):
                if grid[i][j] == 1:
                    q.append((i, j))
                    cnt += 1
        mx = 0
        while cnt < L * L:
            mx += 1
            next = []
            while q:
                i, j = q.pop()
                cnt = add(i + 1, j, cnt, next)
                cnt = add(i - 1, j, cnt, next)
                cnt = add(i, j + 1, cnt, next)
                cnt = add(i, j - 1, cnt, next)
            q = next
        return mx


if __name__ == '__main__':
    assert Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]) == 2
    assert Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == 4
