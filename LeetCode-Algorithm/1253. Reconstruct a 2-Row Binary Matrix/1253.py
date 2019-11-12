from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []

        l = len(colsum)
        m = [[0 for mm in range(l)] for nn in range(2)]

        for i, c in enumerate(colsum):
            if c == 0:
                continue
            if c == 2:
                m[0][i] += 1
                m[1][i] += 1
                upper -= 1
                lower -= 1
        for i, c in enumerate(colsum):
            if c == 1:
                if upper > 0:
                    m[0][i] += 1
                    upper -= 1
                else:
                    m[1][i] += 1
                    lower -= 1

            if upper < 0 or lower < 0:
                return []

        return m


if __name__ == '__main__':
    assert Solution().reconstructMatrix(upper=2, lower=1, colsum=[1, 1, 1]) == [[1, 1, 0], [0, 0, 1]]
    assert Solution().reconstructMatrix(upper=2, lower=3, colsum=[2, 2, 1, 1]) == []
    assert Solution().reconstructMatrix(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]) == [
        [1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]]
