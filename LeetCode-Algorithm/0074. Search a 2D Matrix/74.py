from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        row, col = len(matrix), len(matrix[0])
        l, r = 0, row * col - 1
        while l <= r:
            mid = (l + r) // 2
            i, j = mid // col, mid % col
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


def test_solution():
    assert Solution().searchMatrix(matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target=3)
    assert not Solution().searchMatrix(matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], target=13)
    assert not Solution().searchMatrix([], 0)
    assert not Solution().searchMatrix([[]], 1)
    assert not Solution().searchMatrix([[1, 1]], 2)


if __name__ == '__main__':
    test_solution()
