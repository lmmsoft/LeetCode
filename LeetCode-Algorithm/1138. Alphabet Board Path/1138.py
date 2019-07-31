class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = {}
        for i in range(len(board)):
            for j in range(len(board[i])):
                d[board[i][j]] = (i, j)

        def move_i(a, b):
            if a > b:
                return 'U' * (a - b)
            else:
                return 'D' * (b - a)

        def move_j(a, b):
            if a > b:
                return 'L' * (a - b)
            else:
                return 'R' * (b - a)

        i, j = (0, 0)
        res = ''

        for s in target:
            ii, jj = d[s]
            if s == 'z':
                res += move_j(j, jj)
                res += move_i(i, ii)
            else:
                res += move_i(i, ii)
                res += move_j(j, jj)
            res += '!'
            i, j = ii, jj
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().alphabetBoardPath("leet") == "DDR!UURRR!!DDD!"
    assert Solution().alphabetBoardPath("code") == "RR!DDRR!UUL!R!"
    assert Solution().alphabetBoardPath('vzv') == 'DDDDR!LD!UR!'
