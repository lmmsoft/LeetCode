from typing import List


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        Li, Lj = len(A), len(A[0])

        def dfs(i, j):
            A[i][j] = 0
            for ii, jj in [i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]:
                if 0 <= ii < Li and 0 <= jj < Lj and A[ii][jj] == 1:
                    dfs(ii, jj)

        for j in range(0, Lj):
            if A[0][j]:
                dfs(0, j)
            if A[Li - 1][j]:
                dfs(Li - 1, j)

        for i in range(0, Li):
            if A[i][0]:
                dfs(i, 0)
            if A[i][Lj - 1]:
                dfs(i, Lj - 1)

        res = sum(sum(row) for row in A)
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().numEnclaves([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]) == 3
    assert Solution().numEnclaves([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == 0
