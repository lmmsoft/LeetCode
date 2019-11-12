from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        x, y = len(grid), len(grid[0])
        n = x * y

        def getnum(i, j):
            return i * y + j

        def isFailed(i, j):
            return i == 0 or i == x - 1 or j == 0 or j == y - 1

        parents = [x for x in range(0, n + 1)]
        members = [1] * (n + 1)
        failed = [0 for x in range(n + 1)]

        def find(x: int) -> int:
            while parents[x] != x:
                x = parents[x]
            return x

        def union(x: int, y: int) -> bool:
            px, py = find(x), find(y)
            if px == py:
                return False
            if members[px] < members[py]:
                px, py = py, px
            members[px] += members[py]
            parents[py] = px
            return True

        dir = [[0, 1], [0, -1], [1, 0], [-1], 0]
        for i in range(x):
            for j in range(y):
                # i,j
                num = getnum(i, j)

                if grid[i][j] == 0:
                    failed[num] = isFailed(i, j)
                    for a, b in dir:
                        xx, yy = i + a, j + b
                        if grid[xx][yy]==0 and 0 <= xx < x and 0 <= yy < y:
                            num2 = getnum(xx,yy)
                            union(num,num2)

        for i in range(x):
            for j in range(y):
                # i,j
                num = getnum(i, j)
                if grid[i][j] == 0:
                    failed[num] = isFailed(i, j)
                    if failed[num]:
                        fa = find(num)
                        failed[fa]=1
        d = {}
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 0:
                    num = getnum(i, j)
                    fa = find(num)
                    if failed[fa]==0:
                        d[fa]=1
        return len(d)


if __name__ == '__main__':
    assert Solution().closedIsland(
        grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 0]]) == 2
    assert Solution().closedIsland(grid=[[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]]) == 1
    assert Solution().closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1],
                                         [1, 0, 0, 0, 0, 0, 1],
                                         [1, 0, 1, 1, 1, 0, 1],
                                         [1, 0, 1, 0, 1, 0, 1],
                                         [1, 0, 1, 1, 1, 0, 1],
                                         [1, 0, 0, 0, 0, 0, 1],
                                         [1, 1, 1, 1, 1, 1, 1]]) == 2
