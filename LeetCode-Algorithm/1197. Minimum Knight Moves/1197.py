class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        x = abs(x)
        y = abs(y)

        d = {(0, 0): 0}

        l = [(0, 0)]
        ab = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]

        while True:
            l2 = []
            while l:
                xx, yy = l.pop()
                s = d[(xx, yy)]
                for a, b in ab:
                    aa, bb = xx + a, yy + b
                    if aa == x and bb == y:
                        return s + 1
                    if (aa, bb) not in d:
                        d[(aa, bb)] = s + 1
                        if aa < -20 or bb < -20:
                            continue
                        l2.append((aa, bb))
            l = l2


if __name__ == '__main__':
    assert Solution().minKnightMoves(x=0, y=0) == 0
    assert Solution().minKnightMoves(x=5, y=5) == 4
    assert Solution().minKnightMoves(68, -157) == 79
