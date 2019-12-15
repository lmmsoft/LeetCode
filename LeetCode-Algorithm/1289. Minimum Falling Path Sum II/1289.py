from typing import List


class A:
    def __init__(self, v, p):
        self.v = v
        self.p = p


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr) == 1:
            return arr[0][0]

        def find2(row):
            l = [(n, i) for i, n in enumerate(row)]
            l = sorted(l)
            return A(l[0][0], l[0][1]), A(l[1][0], l[1][1])

        ma = 100 * 200

        dp = [[ma for _ in range(l)] for _ in range(l)]
        for i in range(l):
            if i != 0:
                t0, t1 = find2(dp[i - 1])
            for j in range(l):
                if i == 0:
                    dp[i][j] = arr[0][j]
                else:
                    if j != t0.p:
                        dp[i][j] = arr[i][j] + dp[i - 1][t0.p]
                    else:
                        dp[i][j] = arr[i][j] + dp[i - 1][t1.p]
        return min(dp[l - 1])


if __name__ == '__main__':
    assert Solution().minFallingPathSum(arr=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 13
    assert Solution().minFallingPathSum(
        [[-37, 51, -36, 34, -22], [82, 4, 30, 14, 38], [-68, -52, -92, 65, -85], [-49, -3, -77, 8, -19],
         [-60, -71, -21, -62, -73]]) == -268
