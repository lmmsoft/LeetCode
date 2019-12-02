from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        r = [[0 for _ in range(3)] for _ in range(3)]

        def check():
            for i in range(3):
                s = sum(r[i])
                if s == 3:
                    return 'A'
                elif s == -3:
                    return 'B'
            for i in range(3):
                s = 0
                for j in range(3):
                    s += r[j][i]
                if s == 3:
                    return 'A'
                elif s == -3:
                    return 'B'

            s = r[0][0] + r[1][1] + r[2][2]
            if s == 3:
                return 'A'
            elif s == -3:
                return 'B'

            s = r[0][2] + r[1][1] + r[2][0]
            if s == 3:
                return 'A'
            elif s == -3:
                return 'B'
            return ''

        for id, m in enumerate(moves):
            a, b = m
            r[a][b] = -1 if id % 2 else 1
            c = check()
            if c:
                return c
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'


if __name__ == '__main__':
    assert Solution().tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]) == 'A'
    assert Solution().tictactoe(moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]) == 'B'
    assert Solution().tictactoe(
        moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]) == 'Draw'
    assert Solution().tictactoe(moves=[[0, 0], [1, 1]]) == 'Pending'
