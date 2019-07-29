from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:

        # check all zero
        ss = 0
        for i in grid:
            ss += sum(i)
        if ss == 0:
            return 0
        if ss < 4:
            return 1

        len_i = len(grid)
        len_j = len(grid[0])
        size = min(len_i, len_j)
        for s in range(size, 1, -1):  # size to 2
            # from 0 to len_i - s
            for i in range(0, len_i - s + 1):
                for j in range(0, len_j - s + 1):
                    # check
                    failed = False
                    ii, jj = i + s - 1, j + s - 1
                    for ss in range(s):
                        if grid[i + ss][j] == 0:
                            failed = True
                            break
                        if grid[i][j + ss] == 0:
                            failed = True
                            break

                        if grid[i + ss][jj] == 0:
                            failed = True
                            break
                        if grid[ii][j + ss] == 0:
                            failed = True
                            break
                    if not failed:
                        print(s * s)

                        return s * s
        return 1


if __name__ == '__main__':
    assert Solution().largest1BorderedSquare([[1, 1, 1], [1, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 1]]) == 4
    assert Solution().largest1BorderedSquare([[0, 0], [0, 0]]) == 0
    assert Solution().largest1BorderedSquare([[1, 1, 0, 0]]) == 1
    assert Solution().largest1BorderedSquare([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == 9
