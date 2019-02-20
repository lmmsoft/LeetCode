class Solution:
    def rotate1(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(0, n):
            for j in range(0, n - i - 1):
                matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

        # a[j][j] <-> a [n-1-i][j]
        # for i in range(0, n // 2):
        #     for j in range(0, n):
        #         matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        matrix.reverse()

    def rotate2(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        # 按照 i=j这条斜线对称 (转置)
        for i in range(0, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 按照 n/2 左右对称
        for i in range(0, n):
            for j in range(0, n // 2):
                matrix[i][j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], matrix[i][j]
        # matrix[:] = [row[::-1] for row in matrix]

    def rotate3(self, matrix: 'List[List[int]]') -> 'None':
        n = len(matrix)
        matrix[:] = [[matrix[n - i - 1][j] for i in range(n)] for j in range(n)]

    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        # zip(*matrix) 是把矩阵转置
        # x[::-1] 是把每一行倒序
        matrix[:] = [x[::-1] for x in zip(*matrix)]


def test(a, b):
    Solution().rotate2(a)
    assert a == b


if __name__ == '__main__':
    test([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ], [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ])

    test([
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ], [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ])
